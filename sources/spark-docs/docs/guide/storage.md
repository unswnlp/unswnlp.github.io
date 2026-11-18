# Storage

You have two places to keep files on each machine. Neither is backed up, and the two machines
don't share storage ([Machines](../getting-started/machines.md)).

| | Home | Scratch |
|---|---|---|
| Path | `/home/<username>` | `/scratch/<username>` (also `/scratch/$USER`) |
| For | Config files, small scripts | Code, data, models, environments, outputs: everything else |
| Space: quota / limit | 10 GB / 11 GB | 100 GB / 105 GB |
| Files: quota / limit | 100,000 / 110,000 | 200,000 / 220,000 |
| Backed up | No | No |
| Cleaned up | No | Files unused for 100 days are deleted |

**Keep anything you can't lose somewhere else**: code in git, results and papers on OneDrive or
your own machine.

## Checking your usage

```bash
lquota
```

```
  --------------------------------------------------------------------------
  Filesystem            Used   Quota   Limit  Use%     Files   Quota   Limit  Use%
  --------------------------------------------------------------------------
  /home/alice           645M     10G     11G    6%        3k    100k    110k    2%
  /scratch/alice         26G    100G    105G   26%        5k    200k    220k    2%
  --------------------------------------------------------------------------
```

The same table appears when you log in.

## Quota and limit

- The **quota** is what you're meant to stay under. You can go over it for up to 7 days.
- The **limit** is a hard stop. Past it (or 7 days over the quota), writes fail with
  `Disk quota exceeded` until you delete something.

The file count matters as much as the space: a Python environment or a dataset of many small
files can hit the file quota long before the space quota. That's one reason to use the shared
[software modules](software.md) rather than installing your own PyTorch.

!!! note "Home counts everything you own on the system disk"
    The home quota covers every file you own on the machine's main disk, not only files in your
    home folder. If `lquota` shows more than `du -sh ~` does, the rest is elsewhere (for example
    in `/tmp`). Ask the maintainer if you can't find it.

If you need more scratch for a project, ask the maintainer.

## Caches go to scratch automatically

Tools that download or compile things keep caches. On the Spark machines these already point into
`/scratch/<username>/.cache`, so they don't fill your home:

| Tool | Setting |
|---|---|
| Hugging Face (models, datasets, your token) | `HF_HOME` |
| uv (pip keeps no cache here) | `UV_CACHE_DIR` |
| Triton, PyTorch compile | `TRITON_CACHE_DIR`, `TORCHINDUCTOR_CACHE_DIR` |
| CUDA compile cache | `CUDA_CACHE_PATH` |
| Apptainer | `APPTAINER_CACHEDIR` |

Don't override these in your `.bashrc` unless you mean to.

## Scratch clean-up

Like Gadi, the Spark machines delete scratch files that nobody has **read or changed for 100 days**.

!!! info "Trial period"
    The clean-up starts after a trial period, which is when the warnings described below begin.
    Until then nothing is deleted.

- A week before any of your files are due, your login screen shows a warning with the number of
  files, and the full list is in `/scratch/<username>/.purge-soon.txt`.
- Files you use (read or write) are safe. Deliberately touching files just to keep them isn't in
  the spirit of it: move what you want to keep somewhere else.
- Empty folders unused for 100 days go too.

## Shared models: `/models`

Models that several people use live in `/models` on each machine, readable by everyone and
changeable by no one:

```bash
ls /models/*/
```

Load them by path, for example `AutoModel.from_pretrained("/models/Qwen/Qwen3-4B")` or
`vllm serve /models/google/gemma-4-26B-A4B-it`. This saves everyone a copy in their own scratch.

To add a model, download it to your scratch (see [Download a model](../howto/download-models.md))
and ask the maintainer to publish it.

## Job temporary files

Inside a Slurm job, `/tmp` is private to that job, and it's deleted when the job ends. Copy
anything you need out of it before your job finishes.
