# Accounts and first login

## Getting an account

Accounts are for invited members of UNSW-NLP and close collaborators. Each
[machine](machines.md) has its own accounts. The maintainer creates yours and sends you,
separately:

- which machine it's on, and your **username** there,
- a **temporary password**,
- the machine's **address** (addresses aren't published here).

Every account has an **expiry date**, usually the end of your project or degree. Ask the
maintainer to extend it if you need longer.

You also need to be able to log in to CSE's login server, `login.cse.unsw.edu.au`, because the
machines are reached through it. CSE students and staff can, with their zID and zPass. If you
can't, tell the maintainer.

## First login

1. Set up the connection as in [Connecting](connecting.md), then run `ssh spark-2` (or
   `ssh spark-1`).
2. Enter your **zPass** when CSE's login server asks for it.
3. Enter the **temporary password** when the machine asks for it.
4. It then asks you to change it: type the temporary password once more, then your new password
   twice. The connection closes after that.
5. Log in again with your new password.

On every login you'll see TARS (the resident calico) and a table of your storage:

```
  --------------------------------------------------------------------------
  Filesystem            Used   Quota   Limit  Use%     Files   Quota   Limit  Use%
  --------------------------------------------------------------------------
  /home/alice           645M     10G     11G    6%        3k    100k    110k    2%
  /scratch/alice         26G    100G    105G   26%        5k    200k    220k    2%
  --------------------------------------------------------------------------
```

If you go over a quota, or some of your scratch files are about to be deleted, a line starting
with `!` appears under the table. See [Storage](../guide/storage.md).

To turn TARS off, create an empty file called `.hushlogin` in your home folder
(`touch ~/.hushlogin`). The storage table still shows.

## Using an SSH key instead of a password

After your first login you can add a key, so you don't type your password each time. From your
laptop:

```bash
ssh-keygen -t ed25519      # only if you don't have a key yet
ssh-copy-id spark-2        # and/or spark-1
```

Your public key goes onto the machine; the private key never leaves your laptop. Do the same for
CSE's login server (`ssh-copy-id cse`) to skip the zPass prompt too.

## Changing your password

Run `passwd` on the machine. Passwords are separate on each machine.
