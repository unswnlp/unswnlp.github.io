# Troubleshooting

## Logging in

### `Too many authentication failures`

Your SSH client is offering every key it has. Add `IdentitiesOnly yes` and an `IdentityFile` line
under `Host cse` and each `Host spark-…` entry in `~/.ssh/config`.

### `Permission denied` after a few password tries

The machines allow three attempts per connection. Check you're typing your password for that
machine (not your zPass) at the second prompt. If you've forgotten it, ask the maintainer to reset it.

### It hangs when I connect

You're probably connecting to the machine directly. Make sure your config has `ProxyJump cse` (see
[Connecting](../getting-started/connecting.md)).

## Storage

### `Disk quota exceeded`

Run `lquota`. If your home is full but `du -sh ~` shows much less, the rest is files you own
elsewhere on the system disk; ask the maintainer. Otherwise, delete or move files to scratch. A
`.cache` folder in your home usually means a tool ignored the cache settings: delete it.

### A warning about files being deleted

Files in your scratch that haven't been used for over 93 days are listed in
`/scratch/<username>/.purge-soon.txt`, and will be deleted within a week. Copy anything you need
somewhere else. See [Scratch clean-up](../guide/storage.md#scratch-clean-up).

## Jobs

### `GPU jobs must set --mem …`

Add `--mem=…` to your job. See [GPU jobs and memory](../guide/jobs.md#gpu-jobs-and-memory).

### My job was cancelled after a minute or so

Most likely it used more memory (GPU plus RAM) than its `--mem`. Check `sacct -j <jobid>`, then
raise `--mem` or make the job smaller.

### My job won't start (`PD` in `squeue`)

The last column of `squeue` says why:

- `Resources`: what you asked for isn't free yet. `nodestat` shows what's in use.
- `Priority`: other jobs are ahead of you. See [Who runs first](../guide/jobs.md#who-runs-first).

### `Requested time limit is invalid` (or another limit) when submitting

Jobs that ask for more than a partition allows are refused straight away: at most 24 h on
`batch` and 4 h on `interactive`, and 32 GB of memory on `interactive`.

### `ModuleNotFoundError` inside a job, but it works in my shell

Your job script doesn't load its modules. Start it with `#!/bin/bash -l` and put the
`module load` (and `source …/activate`) lines inside the script.

### Commands I pasted after `srun` disappeared

`srun` passes your keyboard to the job. Run `srun` commands one at a time.

### Two servers fight over a port

Pick the port from your job ID: `port=$((20000 + SLURM_JOB_ID % 10000))`.

## GPU and software

### `nvidia-smi` says `Failed to initialize NVML`

You're in a login session, which has no GPU. That's expected: run it inside a job, e.g.
`srun -p interactive --mem=4G --gres=shard:1 -t 5 nvidia-smi`.

### `torch.cuda.is_available()` is `False`

Same cause: you're not inside a job that asked for the GPU (`--gres=shard:…` or `--gres=gpu:1`).

### `pip install` says it needs a virtual environment

That's on purpose. Make one on top of the modules: see
[Adding your own packages](../guide/software.md#adding-your-own-packages).

### `uv pip install` downloads PyTorch again

uv can't see the bundle packages. Use `python -m pip` instead.

### flash-attn won't install

It doesn't build for this GPU. Use `attn_implementation="sdpa"`.

### Warnings about `register_constant()` and Enum subclasses when importing torchao

Harmless; they come from the torchao version in the 26.11 release.

### `hf download` seems stuck

Its progress bar only moves when a whole file finishes. Watch the folder grow instead: see
[Checking progress](../howto/download-models.md#checking-progress).
