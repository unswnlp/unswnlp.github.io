# Spark machines

UNSW-NLP has its own GPU machines, built on NVIDIA's GB10 (Grace Blackwell) chip. They're set up
like small HPC clusters, the way Gadi and Katana are: you log in, keep your work on scratch, and
run anything heavy as a Slurm job.

| Machine | What it is | Status |
|---|---|---|
| **spark-1** | Two GB10 nodes linked together: jobs can use both GPUs | Being set up |
| **spark-2** | One GB10 node | Available |

Both are set up the same way, so everything in this guide applies to both unless it says
otherwise. See [Machines](getting-started/machines.md) for the differences and which to use.

!!! tip "For proof of concept; scale up on Katana"
    The Spark machines are for trying ideas, debugging and small experiments close to hand. Once
    something works and needs to run at scale (long training runs, big sweeps, many GPUs), move it
    to [Katana](https://docs.restech.unsw.edu.au/), UNSW's research cluster.

Accounts are by invitation. If you've been given one, start with
[Accounts and first login](getting-started/accounts.md).

## Each node at a glance

| Item | Details |
|---|---|
| CPU | 20 Arm cores (`aarch64`) |
| Memory | 128 GB, **shared by the CPU and the GPU**; about 105 GB can go to jobs |
| GPU | 1 × NVIDIA GB10 (compute capability 12.1), CUDA 13.0 |
| Operating system | DGX OS 7 (Ubuntu 24.04) |
| Scheduler | Slurm: `batch` (up to 24 h) and `interactive` (up to 4 h) partitions |
| Your storage | Home 10 GB, scratch 100 GB. **Nothing is backed up** |
| Software | Modules with PyTorch and Hugging Face, plus vLLM and Unsloth containers |
| Shared models | Read-only in `/models` |

Two things work differently from a typical GPU server:

- **The GPU and the CPU share one pool of memory.** GPU memory comes out of your job's
  `--mem`, so a GPU job must ask for enough memory to cover both. See
  [GPU jobs and memory](guide/jobs.md#gpu-jobs-and-memory).
- **There is no GPU outside jobs.** Your login session (SSH, VS Code, Jupyter you start yourself)
  can't use the GPU at all; `nvidia-smi` fails there. Use a Slurm job.

## Quick start

1. [Log in](getting-started/connecting.md) through CSE's login server (`ssh spark-2`, or
   `ssh spark-1`) and change your temporary password.
2. Work in your scratch folder: `cd /scratch/$USER`.
3. Load software: `module load hf/26.11` (this also loads PyTorch).
4. Run on the GPU through Slurm:

    ```bash
    srun -p interactive -c 4 --mem=16G --gres=shard:1 -t 1:00:00 --pty bash
    ```

5. Check your storage with `lquota`, and how busy the machine is with `nodestat`.

## Getting help

Ask the maintainer, Dipankar Srirag. When something fails, say which machine, and send the command
you ran, the job ID (from `sbatch` or `squeue`), and the end of the error output.
