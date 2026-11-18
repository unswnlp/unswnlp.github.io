# Running jobs

Anything that needs the GPU, more than 2 cores or more than 8 GB of memory runs as a **Slurm job**.
Slurm queues jobs and starts them when the resources they asked for are free.

## Partitions

| Partition | Use it for | Time: default / max | Memory |
|---|---|---|---|
| `batch` (default) | Scripts you submit with `sbatch` | 1 h / 24 h | up to ~105 GB per node |
| `interactive` | Shells and quick tests with `srun` | 1 h / 4 h | up to 32 GB |

Each node has 20 cores, about 105 GB of memory for jobs, and one GPU. spark-2 is one node;
spark-1 has two. If you don't ask for memory, you get 4 GB per core.

If your work needs more than 24 hours, or the whole GPU for days, it's past proof of concept:
run it on [Katana](https://docs.restech.unsw.edu.au/).

## A batch job

```bash title="train.sbatch"
#!/bin/bash -l
#SBATCH -J my-training
#SBATCH -p batch
#SBATCH -c 8
#SBATCH --mem=48G
#SBATCH --gres=shard:2
#SBATCH -t 12:00:00
#SBATCH -o /scratch/%u/logs/%x.%j.log

module load train/26.11
source /scratch/$USER/envs/myproject/bin/activate     # if you use one
cd /scratch/$USER/myproject
python train.py
```

```bash
mkdir -p /scratch/$USER/logs
sbatch train.sbatch
```

- Start scripts with `#!/bin/bash -l` and load modules **inside** the script. A job otherwise
  inherits whatever happened to be loaded when you submitted it.
- Write logs and outputs to scratch.

## An interactive job

```bash
srun -p interactive -c 4 --mem=16G --gres=shard:1 -t 2:00:00 --pty bash
```

You get a shell inside the job, with its GPU share; `exit` ends it.

!!! warning "`srun` reads your keyboard"
    While `srun` runs, anything you paste goes to the job, not to your shell. Run `srun` commands
    one at a time, and add `< /dev/null` when you use `srun` in a script.

## GPU jobs and memory

The GB10 has **no separate GPU memory**: the CPU and GPU share the same 128 GB. So:

- **Every GPU job must set `--mem`** (or `--mem-per-cpu`). Jobs that ask for the GPU without it
  are refused.
- **`--mem` must cover your GPU memory plus your normal RAM.** A job that uses more than its
  `--mem` (plus 5%) is cancelled within about a minute.
- As a rule of thumb: model weights in BF16 take 2 GB per billion parameters. Add working memory
  on top (activations, KV cache, optimizer state).

Ask for the GPU in one of two ways:

| Request | You get | Use it when |
|---|---|---|
| `--gres=shard:1` to `shard:4` | A share of the GPU, run alongside other jobs | Most work: experiments, small models, notebooks |
| `--gres=gpu:1` | The whole GPU, no one else on it | Big training runs, benchmarking, large models |

Shards share the GPU's compute; they don't divide its memory (that's what `--mem` does). A
whole-GPU job waits until no shard jobs are running, and vice versa.

The GPU is available **only inside jobs**. In a login session, `nvidia-smi` fails and PyTorch
sees no GPU.

## Watching your jobs

```bash
squeue                 # your jobs, waiting (PD) and running (R)
sacct -X -S today      # your jobs today, including finished ones
scancel 1234           # cancel job 1234
scancel -n my-training # cancel by name
nodestat               # how busy the machine is
```

On spark-2, `nodestat` looks like this (on spark-1 it shows each node):

```
  ------------------------------------------------------------
  unswnlp-spark2            In use    Total
  ------------------------------------------------------------
  CPU cores                      8       20
  Memory                       48G     105G
  GPU shards                     2        4
  ------------------------------------------------------------
  GPU                     shared, 2 of 4 shards in use
  Your jobs               1 running, 0 waiting
  ------------------------------------------------------------
```

**Privacy:** you see only your own jobs and processes. Others can't see what you run, and you
can't see theirs. `nodestat` shows how busy the machine is, without names.

## Who runs first

When jobs are waiting, Slurm orders them by:

- **Fair share:** people who've used less recently go first. Past use counts for half as much
  after a week. Each machine keeps its own history.
- **Waiting time:** jobs that have waited longer move up.
- **Backfill:** a short job can start early if it fits in a gap without delaying anyone.

Running jobs are never interrupted to make room for others.

The maintainer's account has a higher priority and no time limit, for maintenance and long runs
on the machine's behalf. That's set openly in Slurm; it's the only exception.

## Using both nodes (spark-1)

!!! info "Being set up"
    Multi-node jobs will work on spark-1 once it's running; a how-to will follow.

A job can ask for both of spark-1's nodes with `-N 2`, with `--gres` and `--mem` counting **per
node**. For example, `-N 2 --gres=gpu:1 --mem=100G` gets both GPUs and 100 GB on each node.
Single-node jobs (the usual case) need nothing extra: Slurm picks a free node.

## Ports for servers

If your job starts a server (vLLM, Jupyter, TensorBoard), don't use a fixed port like 8000:
another job may already have it. Pick one from your job ID:

```bash
port=$((20000 + SLURM_JOB_ID % 10000))
```

## Coming from Gadi (PBS)?

`qsub` and `qstat` work for simple cases, but the rest of this guide uses Slurm commands.

| PBS | Slurm |
|---|---|
| `qsub job.sh` | `sbatch job.sh` |
| `qstat -u $USER` | `squeue` |
| `qdel 1234` | `scancel 1234` |
| `#PBS -l walltime=12:00:00` | `#SBATCH -t 12:00:00` |
| `#PBS -l ncpus=8,mem=48GB` | `#SBATCH -c 8 --mem=48G` |
| `#PBS -l ngpus=1` | `#SBATCH --gres=gpu:1` |
