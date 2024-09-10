#!/bin/bash -xe
# /GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM
DATASETS=(
    "GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2"
)
for DATASET in "${DATASETS[@]}"; do
    python3 create.py --dataset "/"${DATASET}/"MINIAODSIM" \
    --eos-path "root://redirector.t2.ucsd.edu:1095//store/user/zichun/Hbb-tagger/samples/${DATASET}/dnntuples" \
    --job-tag ${DATASET} \
    --max-retries 10;
    
    condor_submit ${DATASET}/dnntuple.jdl
done
