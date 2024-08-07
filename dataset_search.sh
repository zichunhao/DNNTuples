# dataset=$1
dataset="/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v15-v3/MINIAODSIM"
dasgoclient --query="file dataset=$dataset" | tee dataset.txt
echo "Dataset $dataset has `wc -l dataset.txt` files"