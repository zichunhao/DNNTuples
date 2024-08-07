DATA_NUM=$1
EOS_PATH=$2
WORKDIR=`pwd`

# Setup CMSSW
export SCRAM_ARCH=el8_amd64_gcc11
export RELEASE_DNN=CMSSW_13_0_13
if [ -r $RELEASE_DNN/src ] ; then
  echo release $RELEASE_DNN already exists
else
  scram p CMSSW $RELEASE_DNN
fi

cd $RELEASE_DNN/src
eval `scram runtime -sh`

# Install the DeepNTuples package
git cms-addpkg PhysicsTools/ONNXRuntime
# clone this repo into "DeepNTuples" directory
if ! [ -d DeepNTuples ]; then
  git clone https://github.com/zichunhao/DNNTuples.git DeepNTuples -b hh4b
fi
# Use a faster version of ONNXRuntime
curl -s --retry 10 https://coli.web.cern.ch/coli/tmp/.230626-003937_partv2_model/ak8/V02-HidLayer/model_embed.onnx -o $CMSSW_BASE/src/DeepNTuples/Ntupler/data/InclParticleTransformer-MD/ak8/V02-HidLayer/model_embed.onnx
scram b -j $NTHREAD

# Must run inside the test folder..
cd DeepNTuples/Ntupler/test/;
# read line number $DATA_NUM from the file
inputfile=`sed "${DATA_NUM}q;d" dataset.txt`
filename=`basename $inputfile`
cmsRun DeepNtuplizerAK8.py inputFiles="${inputfile}" outputFile="${WORKDIR}"/${filename}.root

echo "xrdcp -f ${filename}.root ${EOS_PATH}/${filename}.root"
xrdcp -f ${filename}.root ${EOS_PATH}/${filename}.root

touch dummy.cc
echo "Done"