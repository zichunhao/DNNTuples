#!/bin/bash -xe
DATASETS=(
    "/XtoHH_MX-1000to4000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v6-v2/MINIAODSIM"
    "/XtoHH_MX-1000to4000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v2/MINIAODSIM"
    "/XtoHH_MX-500to1000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v6-v2/MINIAODSIM"
    "/XtoHH_MX-500to1000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v2/MINIAODSIM"
)
for DATASET in "${DATASETS[@]}"; do
    data_tag=$(echo $DATASET | cut -d'/' -f2)
    python3 create.py --dataset ${DATASET} \
    --eos-path "root://redirector.t2.ucsd.edu:1095//store/user/zichun/Hbb-tagger/samples/${data_tag}/dnntuples" \
    --job-tag ${data_tag} \
    --max-retries 10;
    
    condor_submit ${data_tag}/dnntuple.jdl
done
