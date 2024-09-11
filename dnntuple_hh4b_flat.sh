#!/bin/bash -xe
DATASETS=(
    "XtoHH_MX-1000to4000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v6-v2"
    "XtoHH_MX-1000to4000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v2"
    "XtoHH_MX-500to1000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v6-v2"
    "XtoHH_MX-500to1000_MH-20to250_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v2"
)
for DATASET in "${DATASETS[@]}"; do
    python3 create.py --dataset /${DATASET}/"MINIAODSIM" \
    --eos-path "root://redirector.t2.ucsd.edu:1095//store/user/zichun/Hbb-tagger/samples/${DATASET}/dnntuples" \
    --job-tag ${DATASET} \
    --max-retries 10;
    
    condor_submit condor_jobs/${DATASET}/dnntuple.jdl
done
