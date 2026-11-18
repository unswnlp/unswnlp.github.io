---
title: "Running jobs"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="running-jobs">Running jobs<a class="headerlink" href="#running-jobs" title="Permanent link">¶</a></h1>
<p>Anything that needs the GPU, more than 2 cores or more than 8 GB of memory runs as a <strong>Slurm job</strong>.
Slurm queues jobs and starts them when the resources they asked for are free.</p>
<h2 id="partitions">Partitions<a class="headerlink" href="#partitions" title="Permanent link">¶</a></h2>
<table>
<thead>
<tr>
<th>Partition</th>
<th>Use it for</th>
<th>Time: default / max</th>
<th>Memory</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>batch</code> (default)</td>
<td>Scripts you submit with <code>sbatch</code></td>
<td>1 h / 24 h</td>
<td>up to ~105 GB per node</td>
</tr>
<tr>
<td><code>interactive</code></td>
<td>Shells and quick tests with <code>srun</code></td>
<td>1 h / 4 h</td>
<td>up to 32 GB</td>
</tr>
</tbody>
</table>
<p>Each node has 20 cores, about 105 GB of memory for jobs, and one GPU. spark-2 is one node;
spark-1 has two. If you don't ask for memory, you get 4 GB per core.</p>
<p>If your work needs more than 24 hours, or the whole GPU for days, it's past proof of concept:
run it on <a href="https://docs.restech.unsw.edu.au/">Katana</a>.</p>
<h2 id="a-batch-job">A batch job<a class="headerlink" href="#a-batch-job" title="Permanent link">¶</a></h2>
<div class="highlight"><span class="filename">train.sbatch</span><pre><span></span><code><span class="ch">#!/bin/bash -l</span>
<span class="c1">#SBATCH -J my-training</span>
<span class="c1">#SBATCH -p batch</span>
<span class="c1">#SBATCH -c 8</span>
<span class="c1">#SBATCH --mem=48G</span>
<span class="c1">#SBATCH --gres=shard:2</span>
<span class="c1">#SBATCH -t 12:00:00</span>
<span class="c1">#SBATCH -o /scratch/%u/logs/%x.%j.log</span>

module<span class="w"> </span>load<span class="w"> </span>train/26.11
<span class="nb">source</span><span class="w"> </span>/scratch/<span class="nv">$USER</span>/envs/myproject/bin/activate<span class="w">     </span><span class="c1"># if you use one</span>
<span class="nb">cd</span><span class="w"> </span>/scratch/<span class="nv">$USER</span>/myproject
python<span class="w"> </span>train.py
</code></pre></div>
<div class="highlight"><pre><span></span><code>mkdir<span class="w"> </span>-p<span class="w"> </span>/scratch/<span class="nv">$USER</span>/logs
sbatch<span class="w"> </span>train.sbatch
</code></pre></div>
<ul>
<li>Start scripts with <code>#!/bin/bash -l</code> and load modules <strong>inside</strong> the script. A job otherwise
  inherits whatever happened to be loaded when you submitted it.</li>
<li>Write logs and outputs to scratch.</li>
</ul>
<h2 id="an-interactive-job">An interactive job<a class="headerlink" href="#an-interactive-job" title="Permanent link">¶</a></h2>
<div class="highlight"><pre><span></span><code>srun<span class="w"> </span>-p<span class="w"> </span>interactive<span class="w"> </span>-c<span class="w"> </span><span class="m">4</span><span class="w"> </span>--mem<span class="o">=</span>16G<span class="w"> </span>--gres<span class="o">=</span>shard:1<span class="w"> </span>-t<span class="w"> </span><span class="m">2</span>:00:00<span class="w"> </span>--pty<span class="w"> </span>bash
</code></pre></div>
<p>You get a shell inside the job, with its GPU share; <code>exit</code> ends it.</p>
<div class="admonition warning">
<p class="admonition-title"><code>srun</code> reads your keyboard</p>
<p>While <code>srun</code> runs, anything you paste goes to the job, not to your shell. Run <code>srun</code> commands
one at a time, and add <code>&lt; /dev/null</code> when you use <code>srun</code> in a script.</p>
</div>
<h2 id="gpu-jobs-and-memory">GPU jobs and memory<a class="headerlink" href="#gpu-jobs-and-memory" title="Permanent link">¶</a></h2>
<p>The GB10 has <strong>no separate GPU memory</strong>: the CPU and GPU share the same 128 GB. So:</p>
<ul>
<li><strong>Every GPU job must set <code>--mem</code></strong> (or <code>--mem-per-cpu</code>). Jobs that ask for the GPU without it
  are refused.</li>
<li><strong><code>--mem</code> must cover your GPU memory plus your normal RAM.</strong> A job that uses more than its
  <code>--mem</code> (plus 5%) is cancelled within about a minute.</li>
<li>As a rule of thumb: model weights in BF16 take 2 GB per billion parameters. Add working memory
  on top (activations, KV cache, optimizer state).</li>
</ul>
<p>Ask for the GPU in one of two ways:</p>
<table>
<thead>
<tr>
<th>Request</th>
<th>You get</th>
<th>Use it when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>--gres=shard:1</code> to <code>shard:4</code></td>
<td>A share of the GPU, run alongside other jobs</td>
<td>Most work: experiments, small models, notebooks</td>
</tr>
<tr>
<td><code>--gres=gpu:1</code></td>
<td>The whole GPU, no one else on it</td>
<td>Big training runs, benchmarking, large models</td>
</tr>
</tbody>
</table>
<p>Shards share the GPU's compute; they don't divide its memory (that's what <code>--mem</code> does). A
whole-GPU job waits until no shard jobs are running, and vice versa.</p>
<p>The GPU is available <strong>only inside jobs</strong>. In a login session, <code>nvidia-smi</code> fails and PyTorch
sees no GPU.</p>
<h2 id="watching-your-jobs">Watching your jobs<a class="headerlink" href="#watching-your-jobs" title="Permanent link">¶</a></h2>
<div class="highlight"><pre><span></span><code>squeue<span class="w">                 </span><span class="c1"># your jobs, waiting (PD) and running (R)</span>
sacct<span class="w"> </span>-X<span class="w"> </span>-S<span class="w"> </span>today<span class="w">      </span><span class="c1"># your jobs today, including finished ones</span>
scancel<span class="w"> </span><span class="m">1234</span><span class="w">           </span><span class="c1"># cancel job 1234</span>
scancel<span class="w"> </span>-n<span class="w"> </span>my-training<span class="w"> </span><span class="c1"># cancel by name</span>
nodestat<span class="w">               </span><span class="c1"># how busy the machine is</span>
</code></pre></div>
<p>On spark-2, <code>nodestat</code> looks like this (on spark-1 it shows each node):</p>
<div class="highlight"><pre><span></span><code>  ------------------------------------------------------------
  unswnlp-spark2            In use    Total
  ------------------------------------------------------------
  CPU cores                      8       20
  Memory                       48G     105G
  GPU shards                     2        4
  ------------------------------------------------------------
  GPU                     shared, 2 of 4 shards in use
  Your jobs               1 running, 0 waiting
  ------------------------------------------------------------
</code></pre></div>
<p><strong>Privacy:</strong> you see only your own jobs and processes. Others can't see what you run, and you
can't see theirs. <code>nodestat</code> shows how busy the machine is, without names.</p>
<h2 id="who-runs-first">Who runs first<a class="headerlink" href="#who-runs-first" title="Permanent link">¶</a></h2>
<p>When jobs are waiting, Slurm orders them by:</p>
<ul>
<li><strong>Fair share:</strong> people who've used less recently go first. Past use counts for half as much
  after a week. Each machine keeps its own history.</li>
<li><strong>Waiting time:</strong> jobs that have waited longer move up.</li>
<li><strong>Backfill:</strong> a short job can start early if it fits in a gap without delaying anyone.</li>
</ul>
<p>Running jobs are never interrupted to make room for others.</p>
<p>The maintainer's account has a higher priority and no time limit, for maintenance and long runs
on the machine's behalf. That's set openly in Slurm; it's the only exception.</p>
<h2 id="using-both-nodes-spark-1">Using both nodes (spark-1)<a class="headerlink" href="#using-both-nodes-spark-1" title="Permanent link">¶</a></h2>
<div class="admonition info">
<p class="admonition-title">Being set up</p>
<p>Multi-node jobs will work on spark-1 once it's running; a how-to will follow.</p>
</div>
<p>A job can ask for both of spark-1's nodes with <code>-N 2</code>, with <code>--gres</code> and <code>--mem</code> counting <strong>per
node</strong>. For example, <code>-N 2 --gres=gpu:1 --mem=100G</code> gets both GPUs and 100 GB on each node.
Single-node jobs (the usual case) need nothing extra: Slurm picks a free node.</p>
<h2 id="ports-for-servers">Ports for servers<a class="headerlink" href="#ports-for-servers" title="Permanent link">¶</a></h2>
<p>If your job starts a server (vLLM, Jupyter, TensorBoard), don't use a fixed port like 8000:
another job may already have it. Pick one from your job ID:</p>
<div class="highlight"><pre><span></span><code><span class="nv">port</span><span class="o">=</span><span class="k">$((</span><span class="m">20000</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="nv">SLURM_JOB_ID</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="m">10000</span><span class="k">))</span>
</code></pre></div>
<h2 id="coming-from-gadi-pbs">Coming from Gadi (PBS)?<a class="headerlink" href="#coming-from-gadi-pbs" title="Permanent link">¶</a></h2>
<p><code>qsub</code> and <code>qstat</code> work for simple cases, but the rest of this guide uses Slurm commands.</p>
<table>
<thead>
<tr>
<th>PBS</th>
<th>Slurm</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>qsub job.sh</code></td>
<td><code>sbatch job.sh</code></td>
</tr>
<tr>
<td><code>qstat -u $USER</code></td>
<td><code>squeue</code></td>
</tr>
<tr>
<td><code>qdel 1234</code></td>
<td><code>scancel 1234</code></td>
</tr>
<tr>
<td><code>#PBS -l walltime=12:00:00</code></td>
<td><code>#SBATCH -t 12:00:00</code></td>
</tr>
<tr>
<td><code>#PBS -l ncpus=8,mem=48GB</code></td>
<td><code>#SBATCH -c 8 --mem=48G</code></td>
</tr>
<tr>
<td><code>#PBS -l ngpus=1</code></td>
<td><code>#SBATCH --gres=gpu:1</code></td>
</tr>
</tbody>
</table>
