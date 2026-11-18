---
title: "Troubleshooting"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="troubleshooting">Troubleshooting<a class="headerlink" href="#troubleshooting" title="Permanent link">¶</a></h1>
<h2 id="logging-in">Logging in<a class="headerlink" href="#logging-in" title="Permanent link">¶</a></h2>
<h3 id="too-many-authentication-failures"><code>Too many authentication failures</code><a class="headerlink" href="#too-many-authentication-failures" title="Permanent link">¶</a></h3>
<p>Your SSH client is offering every key it has. Add <code>IdentitiesOnly yes</code> and an <code>IdentityFile</code> line
under <code>Host cse</code> and each <code>Host spark-…</code> entry in <code>~/.ssh/config</code>.</p>
<h3 id="permission-denied-after-a-few-password-tries"><code>Permission denied</code> after a few password tries<a class="headerlink" href="#permission-denied-after-a-few-password-tries" title="Permanent link">¶</a></h3>
<p>The machines allow three attempts per connection. Check you're typing your password for that
machine (not your zPass) at the second prompt. If you've forgotten it, ask the maintainer to reset it.</p>
<h3 id="it-hangs-when-i-connect">It hangs when I connect<a class="headerlink" href="#it-hangs-when-i-connect" title="Permanent link">¶</a></h3>
<p>You're probably connecting to the machine directly. Make sure your config has <code>ProxyJump cse</code> (see
<a href="/spark-docs/getting-started/connecting/">Connecting</a>).</p>
<h2 id="storage">Storage<a class="headerlink" href="#storage" title="Permanent link">¶</a></h2>
<h3 id="disk-quota-exceeded"><code>Disk quota exceeded</code><a class="headerlink" href="#disk-quota-exceeded" title="Permanent link">¶</a></h3>
<p>Run <code>lquota</code>. If your home is full but <code>du -sh ~</code> shows much less, the rest is files you own
elsewhere on the system disk; ask the maintainer. Otherwise, delete or move files to scratch. A
<code>.cache</code> folder in your home usually means a tool ignored the cache settings: delete it.</p>
<h3 id="a-warning-about-files-being-deleted">A warning about files being deleted<a class="headerlink" href="#a-warning-about-files-being-deleted" title="Permanent link">¶</a></h3>
<p>Files in your scratch that haven't been used for over 93 days are listed in
<code>/scratch/&lt;username&gt;/.purge-soon.txt</code>, and will be deleted within a week. Copy anything you need
somewhere else. See <a href="/spark-docs/guide/storage/">Scratch clean-up</a>.</p>
<h2 id="jobs">Jobs<a class="headerlink" href="#jobs" title="Permanent link">¶</a></h2>
<h3 id="gpu-jobs-must-set-mem"><code>GPU jobs must set --mem …</code><a class="headerlink" href="#gpu-jobs-must-set-mem" title="Permanent link">¶</a></h3>
<p>Add <code>--mem=…</code> to your job. See <a href="/spark-docs/guide/jobs/">GPU jobs and memory</a>.</p>
<h3 id="my-job-was-cancelled-after-a-minute-or-so">My job was cancelled after a minute or so<a class="headerlink" href="#my-job-was-cancelled-after-a-minute-or-so" title="Permanent link">¶</a></h3>
<p>Most likely it used more memory (GPU plus RAM) than its <code>--mem</code>. Check <code>sacct -j &lt;jobid&gt;</code>, then
raise <code>--mem</code> or make the job smaller.</p>
<h3 id="my-job-wont-start-pd-in-squeue">My job won't start (<code>PD</code> in <code>squeue</code>)<a class="headerlink" href="#my-job-wont-start-pd-in-squeue" title="Permanent link">¶</a></h3>
<p>The last column of <code>squeue</code> says why:</p>
<ul>
<li><code>Resources</code>: what you asked for isn't free yet. <code>nodestat</code> shows what's in use.</li>
<li><code>Priority</code>: other jobs are ahead of you. See <a href="/spark-docs/guide/jobs/">Who runs first</a>.</li>
</ul>
<h3 id="requested-time-limit-is-invalid-or-another-limit-when-submitting"><code>Requested time limit is invalid</code> (or another limit) when submitting<a class="headerlink" href="#requested-time-limit-is-invalid-or-another-limit-when-submitting" title="Permanent link">¶</a></h3>
<p>Jobs that ask for more than a partition allows are refused straight away: at most 24 h on
<code>batch</code> and 4 h on <code>interactive</code>, and 32 GB of memory on <code>interactive</code>.</p>
<h3 id="modulenotfounderror-inside-a-job-but-it-works-in-my-shell"><code>ModuleNotFoundError</code> inside a job, but it works in my shell<a class="headerlink" href="#modulenotfounderror-inside-a-job-but-it-works-in-my-shell" title="Permanent link">¶</a></h3>
<p>Your job script doesn't load its modules. Start it with <code>#!/bin/bash -l</code> and put the
<code>module load</code> (and <code>source …/activate</code>) lines inside the script.</p>
<h3 id="commands-i-pasted-after-srun-disappeared">Commands I pasted after <code>srun</code> disappeared<a class="headerlink" href="#commands-i-pasted-after-srun-disappeared" title="Permanent link">¶</a></h3>
<p><code>srun</code> passes your keyboard to the job. Run <code>srun</code> commands one at a time.</p>
<h3 id="two-servers-fight-over-a-port">Two servers fight over a port<a class="headerlink" href="#two-servers-fight-over-a-port" title="Permanent link">¶</a></h3>
<p>Pick the port from your job ID: <code>port=$((20000 + SLURM_JOB_ID % 10000))</code>.</p>
<h2 id="gpu-and-software">GPU and software<a class="headerlink" href="#gpu-and-software" title="Permanent link">¶</a></h2>
<h3 id="nvidia-smi-says-failed-to-initialize-nvml"><code>nvidia-smi</code> says <code>Failed to initialize NVML</code><a class="headerlink" href="#nvidia-smi-says-failed-to-initialize-nvml" title="Permanent link">¶</a></h3>
<p>You're in a login session, which has no GPU. That's expected: run it inside a job, e.g.
<code>srun -p interactive --mem=4G --gres=shard:1 -t 5 nvidia-smi</code>.</p>
<h3 id="torchcudais_available-is-false"><code>torch.cuda.is_available()</code> is <code>False</code><a class="headerlink" href="#torchcudais_available-is-false" title="Permanent link">¶</a></h3>
<p>Same cause: you're not inside a job that asked for the GPU (<code>--gres=shard:…</code> or <code>--gres=gpu:1</code>).</p>
<h3 id="pip-install-says-it-needs-a-virtual-environment"><code>pip install</code> says it needs a virtual environment<a class="headerlink" href="#pip-install-says-it-needs-a-virtual-environment" title="Permanent link">¶</a></h3>
<p>That's on purpose. Make one on top of the modules: see
<a href="/spark-docs/guide/software/">Adding your own packages</a>.</p>
<h3 id="uv-pip-install-downloads-pytorch-again"><code>uv pip install</code> downloads PyTorch again<a class="headerlink" href="#uv-pip-install-downloads-pytorch-again" title="Permanent link">¶</a></h3>
<p>uv can't see the bundle packages. Use <code>python -m pip</code> instead.</p>
<h3 id="flash-attn-wont-install">flash-attn won't install<a class="headerlink" href="#flash-attn-wont-install" title="Permanent link">¶</a></h3>
<p>It doesn't build for this GPU. Use <code>attn_implementation="sdpa"</code>.</p>
<h3 id="warnings-about-register_constant-and-enum-subclasses-when-importing-torchao">Warnings about <code>register_constant()</code> and Enum subclasses when importing torchao<a class="headerlink" href="#warnings-about-register_constant-and-enum-subclasses-when-importing-torchao" title="Permanent link">¶</a></h3>
<p>Harmless; they come from the torchao version in the 26.11 release.</p>
<h3 id="hf-download-seems-stuck"><code>hf download</code> seems stuck<a class="headerlink" href="#hf-download-seems-stuck" title="Permanent link">¶</a></h3>
<p>Its progress bar only moves when a whole file finishes. Watch the folder grow instead: see
<a href="/spark-docs/howto/download-models/">Checking progress</a>.</p>
