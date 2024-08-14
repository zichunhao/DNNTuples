dataset=$1
job_dir=$2 # optional
if [ -z "$job_dir" ]; then
    job_dir="."
fi
dasgoclient --query="file dataset=$dataset" | tee ${job_dir}/dataset.txt
echo "Dataset $dataset has `wc -l dataset.txt` files"