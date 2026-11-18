# Policies

The Spark machines are shared by a small group, so a few rules keep them fair and safe.

## What the machines are for

The Spark machines are for **proof of concept**: trying ideas, debugging, and small experiments.
When work is ready to run at scale (long training runs, sweeps, large evaluations), move it to
[Katana](https://docs.restech.unsw.edu.au/). That keeps the Sparks free for the next person's quick experiment.

## Accounts

- Accounts are personal. Don't share your password or let others use your account.
- Every account has an expiry date. When it passes, you can't log in; your files stay until the
  maintainer cleans up after a grace period. Ask for an extension before it runs out.
- Use the machines for UNSW-NLP research and teaching only.

## Fair use

- Run heavy work as Slurm jobs, never in your login session.
- Ask for what you need: memory and GPU you request but don't use are kept from others.
- Cancel jobs (servers, notebooks) when you're done with them.
- Use shards for most work; take the whole GPU (`--gres=gpu:1`) only when you need it.
- For a long run on a whole GPU (or both of spark-1's nodes), give the group a heads-up first.

## Data

- **Nothing on the machines is backed up.** Keep code in git and results elsewhere.
- Don't keep sensitive or identifiable data (for example health records) on the machines unless your
  project's ethics approval allows it, and talk to the maintainer first.
- Scratch files unused for 100 days are deleted, with a week's warning at login.

## Privacy

- Other users can't see your jobs, your processes or your files. You can't see theirs.
- `nodestat` shows how busy the machine is, without names.
- The maintainer can see everything, for running the machine, and doesn't look at your files
  otherwise.

## Maintenance

The machines need occasional updates and reboots. They're announced ahead of time where possible;
a reboot ends running jobs, so save checkpoints in long runs.

## Scheduling

Waiting jobs are ordered by fair share and waiting time. The one exception is the maintainer's
account, which has a higher priority and no time limit, for maintenance and long runs on the
machine's behalf.
