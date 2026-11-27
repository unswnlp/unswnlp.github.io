# Serve a model with vLLM

vLLM serves a model behind an OpenAI-compatible API. On the Spark machines it comes as the `vllm/26.09` module
(vLLM 0.29, NVIDIA's NGC build) and runs only inside Slurm jobs.

## A serving job

```bash title="serve.sbatch"
#!/bin/bash -l
#SBATCH -J serve
#SBATCH -p batch
#SBATCH --gres=gpu:1
#SBATCH -c 8
#SBATCH --mem=105G
#SBATCH -t 04:00:00
#SBATCH -o /scratch/%u/serve.%j.log

module load vllm/26.09
port=$((20000 + SLURM_JOB_ID % 10000))
echo "serving on port $port"
vllm serve /models/google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b \
  --port "$port" --max-model-len 8192
```

```bash
sbatch serve.sbatch
grep 'serving on port' /scratch/$USER/serve.*.log     # which port it picked
```

The server is ready when the log shows `Application startup complete`. Loading a 50 GB model
takes a few minutes.

## Memory

You don't need to set `--gpu-memory-utilization`: the `vllm` command works it out from your job's
`--mem`, leaving room for vLLM's own RAM. What you do need is a `--mem` big enough for the model:

| Model (BF16) | Weights | Suggested `--mem` |
|---|---|---|
| 4B | 8 GB | 24G |
| 7-12B | 16-24 GB | 48G |
| 26-31B | 52-62 GB | 105G (all of it) |

If the log says there's no room for the KV cache, raise `--mem` or lower `--max-model-len`.

## Querying it

From the same machine (a login shell or another job):

```bash
curl -s localhost:<port>/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"model": "gemma-4-26b", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 50}'
```

From your laptop, forward the port through your SSH connection first:

```bash
ssh -N -L 8000:localhost:<port> spark-2
```

Then use `http://localhost:8000/v1` as the base URL in your client (for example the `openai`
Python package, with any API key).

!!! note "On spark-1"
    Your job may run on the node you're not logged in to. `squeue` shows which (`NODELIST`); use
    that node's name instead of `localhost`, e.g. `ssh -N -L 8000:<node>:<port> spark-1`.

## Tips

- **Speed:** dense models are slow on the GB10, because every generated token reads all the
  weights. Gemma 4 31B gives about 3.5 tokens/s in BF16. Mixture-of-experts models such as
  `gemma-4-26B-A4B-it` are several times faster, and `--quantization fp8` can roughly double the speed.
- **Smaller models share well:** for 4B-class models, `--gres=shard:1 --mem=24G` is enough.
- **Anyone on the machine can reach your port.** Add `--api-key <some-secret>` to `vllm serve` (and
  send it as the API key) if that matters.
- **Stop the server** when you're done (`scancel -n serve`); it holds its memory the whole time.
- Warnings when the job ends, about force-killing `EngineCore` or a leaked semaphore, are harmless.
