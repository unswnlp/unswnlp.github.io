---
title: "Jupyter in VS Code"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="jupyter-in-vs-code">Jupyter in VS Code<a class="headerlink" href="#jupyter-in-vs-code" title="Permanent link">¶</a></h1>
<p>Notebooks need the GPU, so the Jupyter server runs inside a Slurm job, and VS Code connects to it.
(VS Code's own Python kernel runs in your login session, which has no GPU.)</p>
<h2 id="1-start-a-jupyter-server-job">1. Start a Jupyter server job<a class="headerlink" href="#1-start-a-jupyter-server-job" title="Permanent link">¶</a></h2>
<div class="highlight"><span class="filename">jupyter.sbatch</span><pre><span></span><code><span class="ch">#!/bin/bash -l</span>
<span class="c1">#SBATCH -J jupyter</span>
<span class="c1">#SBATCH -p batch</span>
<span class="c1">#SBATCH --gres=shard:1</span>
<span class="c1">#SBATCH -c 4</span>
<span class="c1">#SBATCH --mem=32G</span>
<span class="c1">#SBATCH -t 08:00:00</span>
<span class="c1">#SBATCH -o /scratch/%u/jupyter.%j.log</span>

module<span class="w"> </span>load<span class="w"> </span>jupyter/26.11<span class="w"> </span>hf/26.11<span class="w"> </span>train/26.11
<span class="nv">port</span><span class="o">=</span><span class="k">$((</span><span class="m">20000</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="nv">SLURM_JOB_ID</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="m">10000</span><span class="k">))</span>
<span class="nb">cd</span><span class="w"> </span><span class="s2">"/scratch/</span><span class="nv">$USER</span><span class="s2">"</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="nb">exit</span><span class="w"> </span><span class="m">1</span>
<span class="nb">exec</span><span class="w"> </span>jupyter<span class="w"> </span>lab<span class="w"> </span>--no-browser<span class="w"> </span>--ip<span class="o">=</span><span class="m">127</span>.0.0.1<span class="w"> </span>--port<span class="o">=</span><span class="s2">"</span><span class="nv">$port</span><span class="s2">"</span><span class="w"> </span>--ServerApp.root_dir<span class="o">=</span><span class="s2">"/scratch/</span><span class="nv">$USER</span><span class="s2">"</span>
</code></pre></div>
<p>Change the modules to what your notebooks need, and <code>--mem</code>/<code>--gres</code> to their size (GPU memory
counts towards <code>--mem</code>; see <a href="/spark-docs/guide/jobs/">GPU jobs and memory</a>).</p>
<div class="highlight"><pre><span></span><code>sbatch<span class="w"> </span>jupyter.sbatch
squeue<span class="w">                      </span><span class="c1"># wait until the jupyter job shows R</span>
grep<span class="w"> </span>-o<span class="w"> </span><span class="s1">'http://127.0.0.1:[0-9]*/lab?token=[0-9a-f]*'</span><span class="w"> </span>/scratch/<span class="nv">$USER</span>/jupyter.*.log<span class="w"> </span><span class="p">|</span><span class="w"> </span>tail<span class="w"> </span>-1
</code></pre></div>
<p>The last command prints the server's address with its token. If it prints nothing, wait a few
seconds and run it again.</p>
<h2 id="2-connect-vs-code">2. Connect VS Code<a class="headerlink" href="#2-connect-vs-code" title="Permanent link">¶</a></h2>
<ol>
<li>Open or create a <code>.ipynb</code> file in VS Code (connected to the machine with Remote - SSH).</li>
<li>Click <strong>Select Kernel</strong> (top right) → <strong>Select Another Kernel…</strong> → <strong>Existing Jupyter Server…</strong></li>
<li>Paste the address, then choose <strong>Python 3 (ipykernel)</strong>.</li>
</ol>
<p>VS Code's Jupyter extension runs on the machine, so <code>127.0.0.1</code> works as it is.</p>
<div class="admonition note">
<p class="admonition-title">On spark-1</p>
<p>Your job may run on the node you're not logged in to, where <code>127.0.0.1</code> won't reach it. In the
job script, use <code>--ip="$(hostname)"</code> instead of <code>--ip=127.0.0.1</code>, and the address printed in the
log (with the node's name) instead of <code>127.0.0.1</code>.</p>
</div>
<h2 id="from-a-browser-instead">From a browser instead<a class="headerlink" href="#from-a-browser-instead" title="Permanent link">¶</a></h2>
<p>Forward the port from your laptop, then open the printed address in your browser:</p>
<div class="highlight"><pre><span></span><code>ssh<span class="w"> </span>-N<span class="w"> </span>-L<span class="w"> </span>&lt;port&gt;:127.0.0.1:&lt;port&gt;<span class="w"> </span>spark-2
</code></pre></div>
<h2 id="when-youre-done">When you're done<a class="headerlink" href="#when-youre-done" title="Permanent link">¶</a></h2>
<div class="highlight"><pre><span></span><code>scancel<span class="w"> </span>-n<span class="w"> </span>jupyter
</code></pre></div>
<p>The job holds its GPU share and memory until you cancel it or it hits its time limit.</p>
<div class="admonition warning">
<p class="admonition-title">Keep the token</p>
<p>The server only listens on <code>127.0.0.1</code>, but everyone on the machine shares that address. The
token is what keeps others out of your notebooks, so don't turn it off.</p>
</div>
