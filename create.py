from pathlib import Path
import argparse
import os
import textwrap
from typing import Optional


def get_condor_script(
    n_files: int,
    eos_path: str,
    job_dir: Path,
    request_cpus: int = 1,
    request_memory: int = 2000,
    n_thread: int = 1,
    max_retries: int = 5,
) -> str:
    return textwrap.dedent(
        f"""
    Universe   = vanilla
    Executable = {job_dir / 'dnntuple.sh'}

    +ProjectName = "cms.org.cern"

    # EOS path to store the output
    EOSPATH = {eos_path}
    NTHREAD = {n_thread}

    Arguments = $(JOBNUM) $(EOSPATH) $(NTHREAD)

    requirements = (OpSysAndVer =?= "AlmaLinux9")
    request_cpus = {request_cpus}
    request_memory = {request_memory}
    x509userproxy = $ENV(X509_USER_PROXY)
    use_x509userproxy = true

    +JobFlavour = "tomorrow"

    Log        = {job_dir.resolve()}/log/log-$(Cluster)-$(Process).log
    Output     = {job_dir.resolve()}/log/out-$(Cluster)-$(Process).out
    Error      = {job_dir.resolve()}/log/err-$(Cluster)-$(Process).err

    on_exit_remove   = (ExitBySignal == False) && (ExitCode == 0)
    max_retries      = {max_retries}
    requirements     = Machine =!= LastRemoteHost
    should_transfer_files   = YES
    when_to_transfer_output = ON_EXIT_OR_EVICT
    transfer_output_files   = dummy.cc
    transfer_input_files    = {job_dir}/dataset.txt

    Queue JOBNUM from seq 1 {n_files} |
    """
    ).strip()


def get_bash_script() -> str:
    return textwrap.dedent(
        """
    #!/bin/bash -xe

    DATA_NUM=$1
    EOSPATH=$2
    NTHREAD=$3
    WORKDIR=$(pwd)
    echo "DATA_NUM: $DATA_NUM"
    echo "EOSPATH: $EOSPATH"
    echo "WORKDIR: $WORKDIR"

    # Setup CMSSW
    export SCRAM_ARCH=el8_amd64_gcc11
    export RELEASE_DNN=CMSSW_13_0_13
    echo "Setting up $RELEASE_DNN"
    if [ -r $RELEASE_DNN/src ] ; then
      echo release $RELEASE_DNN already exists
    else
      scram p CMSSW $RELEASE_DNN
    fi

    cd $RELEASE_DNN/src
    eval `scram runtime -sh`

    # Install the DeepNTuples package
    echo "Installing DNNTuples"
    git cms-addpkg PhysicsTools/ONNXRuntime
    # clone this repo into "DeepNTuples" directory
    if ! [ -d DeepNTuples ]; then
      git clone https://github.com/zichunhao/DNNTuples.git DeepNTuples -b hh4b
    fi
    # Use a faster version of ONNXRuntime
    curl -s --retry 10 https://coli.web.cern.ch/coli/tmp/.230626-003937_partv2_model/ak8/V02-HidLayer/model_embed.onnx -o $CMSSW_BASE/src/DeepNTuples/Ntupler/data/InclParticleTransformer-MD/ak8/V02-HidLayer/model_embed.onnx
    scram b -j $NTHREAD

    # read line number $DATA_NUM from the file
    cd DeepNTuples
    inputfile=$(sed "${DATA_NUM}q;d" ${WORKDIR}/dataset.txt)
    # Must run inside the test folder..
    cd Ntupler/test/
    filename=$(basename ${inputfile})
    echo "Running DeepNtuplizerAK8.py on ${inputfile}"
    echo "cmsRun DeepNtuplizerAK8.py inputFiles=${inputfile} outputFile=${WORKDIR}/${filename}"
    cmsRun DeepNtuplizerAK8.py inputFiles="${inputfile}" outputFile="${WORKDIR}/${filename}"

    cd $WORKDIR
    echo "ls -lah"
    ls -lah

    echo "xrdcp -f ${WORKDIR}/${filename} ${EOSPATH}/${filename}"
    xrdcp -f ${WORKDIR}/${filename} ${EOSPATH}/${filename}

    touch dummy.cc
    echo "Done"
    """
    ).strip()


def search_dataset(dataset: str, job_dir: Path) -> int:
    os.system(f"bash dataset_search.sh {dataset} {job_dir}")
    with open(job_dir / "dataset.txt", "r") as f:
        return sum(1 for line in f if line.strip())


def write_condor_script(job_dir: Path, script_content: str) -> None:
    with open(job_dir / "dnntuple.jdl", "w") as f:
        f.write(script_content)


def write_bash_script(job_dir: Path, script_content: str) -> None:
    script_path = job_dir / "dnntuple.sh"
    with open(script_path, "w") as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)


def main():
    parser = argparse.ArgumentParser(description="Setup Condor job for DNNTuples")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset name")
    parser.add_argument(
        "--eos-path",
        type=str,
        required=True,
        help="URL to the EOS directory to store the outputs",
    )
    parser.add_argument(
        "--job-tag", type=str, required=True, help="Unique tag for the condor job"
    )
    parser.add_argument(
        "--job-dir",
        type=str,
        default=Path.cwd(),
        help="Directory to store the condor job files",
    )
    parser.add_argument(
        "--request-cpus",
        type=int,
        default=1,
        help="Number of CPUs requested for the job",
    )
    parser.add_argument(
        "--request-memory", type=int, default=2000, help="Memory requested for the job"
    )
    parser.add_argument(
        "--n-thread", type=int, default=1, help="Number of threads to run the job"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=5,
        help="Maximum number of retries for the job",
    )
    args = parser.parse_args()

    job_dir = (Path(args.job_dir) / args.job_tag).resolve()
    job_dir.mkdir(parents=True, exist_ok=True)
    log_dir = job_dir / "log"

    n_lines = search_dataset(args.dataset, job_dir)

    condor_script = get_condor_script(
        n_files=n_lines,
        eos_path=args.eos_path,
        job_dir=job_dir,
        request_cpus=args.request_cpus,
        request_memory=args.request_memory,
        n_thread=args.n_thread,
        max_retries=args.max_retries,
    )
    write_condor_script(job_dir, condor_script)

    bash_script = get_bash_script()
    write_bash_script(job_dir, bash_script)

    print(f"Condor job files created in {job_dir}")
    print(f"Log files will be stored in {log_dir}")
    print(f"Output root files will be stored in {args.eos_path}")
    print(f"To submit the job, run:\ncondor_submit {job_dir / 'dnntuple.jdl'}")


if __name__ == "__main__":
    main()
