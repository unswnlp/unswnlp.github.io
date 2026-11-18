# Connecting

The Spark machines aren't reachable directly from campus Wi-Fi or from home. You connect through
CSE's login server, `login.cse.unsw.edu.au`, which passes your connection on. SSH does this in one
step if you describe both hops in your SSH config.

## SSH config

On your laptop, add this to `~/.ssh/config` (create the file if it doesn't exist). Replace
`<zID>` with your zID, and `<address>` and `<username>` with what you were sent with your account.
Keep only the machines you have an account on.

```
Host cse
    HostName login.cse.unsw.edu.au
    User <zID>

Host spark-1
    HostName <address of spark-1>
    User <username>
    ProxyJump cse

Host spark-2
    HostName <address of spark-2>
    User <username>
    ProxyJump cse
```

Then connect with:

```bash
ssh spark-2        # or: ssh spark-1
```

You'll be asked for your zPass (for CSE), then your password on the machine. Adding SSH keys
for both removes the prompts: see
[Using an SSH key](accounts.md#using-an-ssh-key-instead-of-a-password).

??? tip "Without a config file"
    The same thing as one command:

    ```bash
    ssh -J <zID>@login.cse.unsw.edu.au <username>@<address>
    ```

??? tip "Fewer zPass prompts"
    Add these lines under `Host cse` to reuse one CSE connection for 10 minutes:

    ```
        ControlMaster auto
        ControlPath ~/.ssh/cm-%r@%h:%p
        ControlPersist 10m
    ```

## Copying files

`scp` and `rsync` use the same config:

```bash
scp results.csv spark-2:/scratch/<username>/
rsync -avh --info=progress2 my-data/ spark-2:/scratch/<username>/my-data/
```

The two machines have separate storage. To move files between them, copy through your laptop
the same way, or ask the maintainer about a direct copy for large data.

To bring data over from Katana, run `rsync` **on the Spark machine** and pull from Katana's data
mover:

```bash
rsync -avh --info=progress2 <zID>@kdm.restech.unsw.edu.au:/srv/scratch/<zID>/my-data/ /scratch/<username>/my-data/
```

Run it inside `tmux`, so it keeps going if your connection drops.

## VS Code

1. Install the **Remote - SSH** extension.
2. Set up the SSH config above. VS Code reads the same file.
3. Run **Remote-SSH: Connect to Host…** and choose `spark-1` or `spark-2`.

Open folders under `/scratch/<username>`, not your home. VS Code's server files already live in
scratch (your `~/.vscode-server` points there), so they don't fill your home quota.

!!! warning "VS Code runs in your login session"
    The VS Code server, its terminals and any Python you run from them are limited like any login:
    8 GB of memory, 2 CPU cores, and no GPU. For GPU work in notebooks, see
    [Jupyter in VS Code](../howto/jupyter.md).

## Login sessions

Everything you start outside a Slurm job (SSH, VS Code, `tmux`) shares these limits:

| | Limit per user |
|---|---|
| Memory | 8 GB (a program that goes over is stopped) |
| CPU | 2 cores |
| Processes | 1,024 |
| GPU | none |

That's plenty for editing, git, small scripts and submitting jobs. Anything heavier goes in a
[job](../guide/jobs.md).
