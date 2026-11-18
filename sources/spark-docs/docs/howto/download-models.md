# Download a model

First check `/models`: the model may already be there (`ls /models/*/`).

## Log in to Hugging Face (once)

Gated models (Gemma, Llama, Cohere, …) need your Hugging Face token, and you need to accept the
model's licence on its Hugging Face page first.

```bash
module load hf/26.11
hf auth login
```

The token is saved in your scratch (`/scratch/<username>/.cache/huggingface`), which only you can
read.

## Download as a job

Run big downloads as a batch job: they don't need you to stay logged in, and they aren't held back
by the login limits.

```bash
module load hf/26.11
sbatch -J dl -c 4 --mem=8G -t 12:00:00 -o /scratch/$USER/dl.%j.log \
  --wrap 'hf download Qwen/Qwen3-4B --local-dir /scratch/$USER/models/Qwen/Qwen3-4B'
```

Downloads run at about 110 MB/s, so a 50 GB model takes around 8 minutes.

??? example "Several models in one job"
    ```bash title="get-models.sbatch"
    #!/bin/bash -l
    #SBATCH -J get-models -c 4 --mem=8G -t 12:00:00
    #SBATCH -o /scratch/%u/get-models.%j.log

    MODELS=(Qwen/Qwen3-1.7B Qwen/Qwen3-4B)

    module load hf/26.11
    for m in "${MODELS[@]}"; do
      echo "=== $(date +%T)  $m"
      hf download "$m" --local-dir "/scratch/$USER/models/$m" >/dev/null || echo "!!! failed: $m"
    done
    echo "=== $(date +%T)  done"
    ```

## Checking progress

In a job's log, hf only shows a "Fetching N files" bar, which moves when a whole file finishes. To
see the real speed, watch the folder grow:

```bash
d=/scratch/$USER/models/Qwen/Qwen3-4B; p=$(du -sb "$d" | cut -f1)
while sleep 10; do n=$(du -sb "$d" | cut -f1); awk -v n="$n" -v p="$p" -v t="$(date +%T)" 'BEGIN { printf "%s  %6.1f GB  %6.1f MB/s\n", t, n/1e9, (n-p)/1e7 }'; p=$n; done
```

Press Ctrl+C to stop watching (the download carries on). It's finished when the job has gone from
`squeue`.

## If downloads crawl

The machines download over plain HTTPS (`HF_HUB_DISABLE_XET=1` is set for you), because Hugging Face's
newer "xet" downloader stalls on the long link to Australia. If you change that setting and a
download crawls, set it back, delete the half-finished files and start again:

```bash
rm -f /scratch/$USER/models/<org>/<name>/.cache/huggingface/download/*.incomplete
```

## Sharing it

If others will use the model too, ask the maintainer to publish it to `/models` on that machine. Once it's
published, delete your copy.
