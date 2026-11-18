---
title: "Spark"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="spark-machines">Spark machines<a class="headerlink" href="#spark-machines" title="Permanent link">¶</a></h1>
<p>UNSW-NLP has its own GPU machines, built on NVIDIA's GB10 (Grace Blackwell) chip. They're set up
like small HPC clusters, the way Gadi and Katana are: you log in, keep your work on scratch, and
run anything heavy as a Slurm job.</p>
<table>
<thead>
<tr>
<th>Machine</th>
<th>What it is</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>spark-1</strong></td>
<td>Two GB10 nodes linked together: jobs can use both GPUs</td>
<td>Being set up</td>
</tr>
<tr>
<td><strong>spark-2</strong></td>
<td>One GB10 node</td>
<td>Available</td>
</tr>
</tbody>
</table>
<p>Both are set up the same way, so everything in this guide applies to both unless it says
otherwise. See <a href="/spark-docs/getting-started/machines/">Machines</a> for the differences and which to use.</p>
<div class="admonition tip">
<p class="admonition-title">For proof of concept; scale up on Katana</p>
<p>The Spark machines are for trying ideas, debugging and small experiments close to hand. Once
something works and needs to run at scale (long training runs, big sweeps, many GPUs), move it
to <a href="https://docs.restech.unsw.edu.au/">Katana</a>, UNSW's research cluster.</p>
</div>
<p>Accounts are by invitation. If you've been given one, start with
<a href="/spark-docs/getting-started/accounts/">Accounts and first login</a>.</p>
<h2 id="each-node-at-a-glance">Each node at a glance<a class="headerlink" href="#each-node-at-a-glance" title="Permanent link">¶</a></h2>
<table>
<thead>
<tr>
<th>Item</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td>20 Arm cores (<code>aarch64</code>)</td>
</tr>
<tr>
<td>Memory</td>
<td>128 GB, <strong>shared by the CPU and the GPU</strong>; about 105 GB can go to jobs</td>
</tr>
<tr>
<td>GPU</td>
<td>1 × NVIDIA GB10 (compute capability 12.1), CUDA 13.0</td>
</tr>
<tr>
<td>Operating system</td>
<td>DGX OS 7 (Ubuntu 24.04)</td>
</tr>
<tr>
<td>Scheduler</td>
<td>Slurm: <code>batch</code> (up to 24 h) and <code>interactive</code> (up to 4 h) partitions</td>
</tr>
<tr>
<td>Your storage</td>
<td>Home 10 GB, scratch 100 GB. <strong>Nothing is backed up</strong></td>
</tr>
<tr>
<td>Software</td>
<td>Modules with PyTorch and Hugging Face, plus vLLM and Unsloth containers</td>
</tr>
<tr>
<td>Shared models</td>
<td>Read-only in <code>/models</code></td>
</tr>
</tbody>
</table>
<p>Two things work differently from a typical GPU server:</p>
<ul>
<li><strong>The GPU and the CPU share one pool of memory.</strong> GPU memory comes out of your job's
  <code>--mem</code>, so a GPU job must ask for enough memory to cover both. See
  <a href="/spark-docs/guide/jobs/">GPU jobs and memory</a>.</li>
<li><strong>There is no GPU outside jobs.</strong> Your login session (SSH, VS Code, Jupyter you start yourself)
  can't use the GPU at all; <code>nvidia-smi</code> fails there. Use a Slurm job.</li>
</ul>
<h2 id="quick-start">Quick start<a class="headerlink" href="#quick-start" title="Permanent link">¶</a></h2>
<ol>
<li><a href="/spark-docs/getting-started/connecting/">Log in</a> through CSE's login server (<code>ssh spark-2</code>, or
   <code>ssh spark-1</code>) and change your temporary password.</li>
<li>Work in your scratch folder: <code>cd /scratch/$USER</code>.</li>
<li>Load software: <code>module load hf/26.11</code> (this also loads PyTorch).</li>
<li>
<p>Run on the GPU through Slurm:</p>
<div class="highlight"><pre><span></span><code>srun<span class="w"> </span>-p<span class="w"> </span>interactive<span class="w"> </span>-c<span class="w"> </span><span class="m">4</span><span class="w"> </span>--mem<span class="o">=</span>16G<span class="w"> </span>--gres<span class="o">=</span>shard:1<span class="w"> </span>-t<span class="w"> </span><span class="m">1</span>:00:00<span class="w"> </span>--pty<span class="w"> </span>bash
</code></pre></div>
</li>
<li>
<p>Check your storage with <code>lquota</code>, and how busy the machine is with <code>nodestat</code>.</p>
</li>
</ol>
<h2 id="getting-help">Getting help<a class="headerlink" href="#getting-help" title="Permanent link">¶</a></h2>
<p>Ask the maintainer, Dipankar Srirag. When something fails, say which machine, and send the command
you ran, the job ID (from <code>sbatch</code> or <code>squeue</code>), and the end of the error output.</p>
