#!/bin/bash -xe
# GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v3/MINIAODSIM
DATASETS=(
    "GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8"
)
for DATASET in "${DATASETS[@]}"; do
    python3 create.py --dataset "/"${DATASET}/"Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v3/MINIAODSIM" \
    --eos-path "root://redirector.t2.ucsd.edu:1095//store/user/zichun/Hbb-tagger/samples/${DATASET}/dnntuples" \
    --job-tag ${DATASET} \
    --max-retries 10;
    
    condor_submit ${DATASET}/dnntuple.jdl
done
