# Jupyter in VS Code

Notebooks need the GPU, so the Jupyter server runs inside a Slurm job, and VS Code connects to it.
(VS Code's own Python kernel runs in your login session, which has no GPU.)

## 1. Start a Jupyter server job

```bash title="jupyter.sbatch"
#!/bin/bash -l
#SBATCH -J jupyter
#SBATCH -p batch
#SBATCH --gres=shard:1
#SBATCH -c 4
#SBATCH --mem=32G
#SBATCH -t 08:00:00
#SBATCH -o /scratch/%u/jupyter.%j.log

module load jupyter/26.11 hf/26.11 train/26.11
port=$((20000 + SLURM_JOB_ID % 10000))
cd "/scratch/$USER" || exit 1
exec jupyter lab --no-browser --ip=127.0.0.1 --port="$port" --ServerApp.root_dir="/scratch/$USER"
```

Change the modules to what your notebooks need, and `--mem`/`--gres` to their size (GPU memory
counts towards `--mem`; see [GPU jobs and memory](../guide/jobs.md#gpu-jobs-and-memory)).

```bash
sbatch jupyter.sbatch
squeue                      # wait until the jupyter job shows R
grep -o 'http://127.0.0.1:[0-9]*/lab?token=[0-9a-f]*' /scratch/$USER/jupyter.*.log | tail -1
```

The last command prints the server's address with its token. If it prints nothing, wait a few
seconds and run it again.

## 2. Connect VS Code

1. Open or create a `.ipynb` file in VS Code (connected to the machine with Remote - SSH).
2. Click **Select Kernel** (top right) → **Select Another Kernel…** → **Existing Jupyter Server…**
3. Paste the address, then choose **Python 3 (ipykernel)**.

VS Code's Jupyter extension runs on the machine, so `127.0.0.1` works as it is.

!!! note "On spark-1"
    Your job may run on the node you're not logged in to, where `127.0.0.1` won't reach it. In the
    job script, use `--ip="$(hostname)"` instead of `--ip=127.0.0.1`, and the address printed in the
    log (with the node's name) instead of `127.0.0.1`.

## From a browser instead

Forward the port from your laptop, then open the printed address in your browser:

```bash
ssh -N -L <port>:127.0.0.1:<port> spark-2
```

## When you're done

```bash
scancel -n jupyter
```

The job holds its GPU share and memory until you cancel it or it hits its time limit.

!!! warning "Keep the token"
    The server only listens on `127.0.0.1`, but everyone on the machine shares that address. The
    token is what keeps others out of your notebooks, so don't turn it off.
