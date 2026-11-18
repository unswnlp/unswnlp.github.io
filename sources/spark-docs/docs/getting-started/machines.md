# Machines

There are two Spark machines. Each is a separate system with its own Slurm queue, storage and
accounts, set up the same way.

| | spark-1 | spark-2 |
|---|---|---|
| Nodes | 2 | 1 |
| GPUs | 2 × GB10 (one per node) | 1 × GB10 |
| CPU cores | 40 (20 per node) | 20 |
| Memory for jobs | about 210 GB (105 GB per node) | about 105 GB |
| Multi-node jobs | Yes | No |
| Status | Being set up | Available |

## Which one to use

Both machines are for **proof of concept**: getting an idea working on a small scale before
running it for real. Larger jobs belong on [Katana](https://docs.restech.unsw.edu.au/).

- **spark-2** for most proof-of-concept work on one GPU: trying a method, debugging a training
  script, short fine-tuning runs, and serving a model to test against (up to roughly 30B
  parameters in BF16).
- **spark-1** for proving out things that need two GPUs or more than one node's memory, such as
  checking that a model or training run splits across nodes before you scale it up on Katana.
  Single-node jobs run there too, on either node.
- **Katana** once it works and needs to scale: long training runs, hyperparameter sweeps,
  large evaluations, or more GPUs than a Spark machine has.

## What's separate

- **Accounts:** an account on one machine doesn't give you the other. Ask for the one(s) you need.
- **Storage:** each machine has its own home, scratch and `/models`. Files don't move between them
  on their own; copy them with `rsync` if you need to (see [Copying files](connecting.md#copying-files)).
- **Queues and priority:** each machine has its own Slurm queue and its own fair-share history.

## spark-1 specifics

!!! info "Being set up"
    spark-1 isn't open yet. This section describes the plan and will be filled in once it's
    running.

- spark-1's two nodes share the same home, scratch and `/models`, so a job sees the same files on
  either node.
- You log in to spark-1 as one machine; Slurm places your job on a free node.
- A job can ask for both nodes (`-N 2`), for example to split a large model across both GPUs. A
  how-to for multi-node jobs will follow.
- `nodestat` on spark-1 shows each node separately.
