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