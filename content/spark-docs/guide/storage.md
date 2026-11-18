---
title: "Storage"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="storage">Storage<a class="headerlink" href="#storage" title="Permanent link">¶</a></h1>
<p>You have two places to keep files on each machine. Neither is backed up, and the two machines
don't share storage (<a href="/spark-docs/getting-started/machines/">Machines</a>).</p>
<table>
<thead>
<tr>
<th></th>
<th>Home</th>
<th>Scratch</th>
</tr>
</thead>
<tbody>
<tr>
<td>Path</td>
<td><code>/home/&lt;username&gt;</code></td>
<td><code>/scratch/&lt;username&gt;</code> (also <code>/scratch/$USER</code>)</td>
</tr>
<tr>
<td>For</td>
<td>Config files, small scripts</td>
<td>Code, data, models, environments, outputs: everything else</td>
</tr>
<tr>
<td>Space: quota / limit</td>
<td>10 GB / 11 GB</td>
<td>100 GB / 105 GB</td>
</tr>
<tr>
<td>Files: quota / limit</td>
<td>100,000 / 110,000</td>
<td>200,000 / 220,000</td>
</tr>
<tr>
<td>Backed up</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td>Cleaned up</td>
<td>No</td>
<td>Files unused for 100 days are deleted</td>
</tr>
</tbody>
</table>
<p><strong>Keep anything you can't lose somewhere else</strong>: code in git, results and papers on OneDrive or
your own machine.</p>
<h2 id="checking-your-usage">Checking your usage<a class="headerlink" href="#checking-your-usage" title="Permanent link">¶</a></h2>
<div class="highlight"><pre><span></span><code>lquota
</code></pre></div>
<div class="highlight"><pre><span></span><code>  --------------------------------------------------------------------------
  Filesystem            Used   Quota   Limit  Use%     Files   Quota   Limit  Use%
  --------------------------------------------------------------------------
  /home/alice           645M     10G     11G    6%        3k    100k    110k    2%
  /scratch/alice         26G    100G    105G   26%        5k    200k    220k    2%
  --------------------------------------------------------------------------
</code></pre></div>
<p>The same table appears when you log in.</p>
<h2 id="quota-and-limit">Quota and limit<a class="headerlink" href="#quota-and-limit" title="Permanent link">¶</a></h2>
<ul>
<li>The <strong>quota</strong> is what you're meant to stay under. You can go over it for up to 7 days.</li>
<li>The <strong>limit</strong> is a hard stop. Past it (or 7 days over the quota), writes fail with
  <code>Disk quota exceeded</code> until you delete something.</li>
</ul>
<p>The file count matters as much as the space: a Python environment or a dataset of many small
files can hit the file quota long before the space quota. That's one reason to use the shared
<a href="/spark-docs/guide/software/">software modules</a> rather than installing your own PyTorch.</p>
<div class="admonition note">
<p class="admonition-title">Home counts everything you own on the system disk</p>
<p>The home quota covers every file you own on the machine's main disk, not only files in your
home folder. If <code>lquota</code> shows more than <code>du -sh ~</code> does, the rest is elsewhere (for example
in <code>/tmp</code>). Ask the maintainer if you can't find it.</p>
</div>
<p>If you need more scratch for a project, ask the maintainer.</p>
<h2 id="caches-go-to-scratch-automatically">Caches go to scratch automatically<a class="headerlink" href="#caches-go-to-scratch-automatically" title="Permanent link">¶</a></h2>
<p>Tools that download or compile things keep caches. On the Spark machines these already point into
<code>/scratch/&lt;username&gt;/.cache</code>, so they don't fill your home:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Setting</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hugging Face (models, datasets, your token)</td>
<td><code>HF_HOME</code></td>
</tr>
<tr>
<td>uv (pip keeps no cache here)</td>
<td><code>UV_CACHE_DIR</code></td>
</tr>
<tr>
<td>Triton, PyTorch compile</td>
<td><code>TRITON_CACHE_DIR</code>, <code>TORCHINDUCTOR_CACHE_DIR</code></td>
</tr>
<tr>
<td>CUDA compile cache</td>
<td><code>CUDA_CACHE_PATH</code></td>
</tr>
<tr>
<td>Apptainer</td>
<td><code>APPTAINER_CACHEDIR</code></td>
</tr>
</tbody>
</table>
<p>Don't override these in your <code>.bashrc</code> unless you mean to.</p>
<h2 id="scratch-clean-up">Scratch clean-up<a class="headerlink" href="#scratch-clean-up" title="Permanent link">¶</a></h2>
<p>Like Gadi, the Spark machines delete scratch files that nobody has <strong>read or changed for 100 days</strong>.</p>
<div class="admonition info">
<p class="admonition-title">Trial period</p>
<p>The clean-up starts after a trial period, which is when the warnings described below begin.
Until then nothing is deleted.</p>
</div>
<ul>
<li>A week before any of your files are due, your login screen shows a warning with the number of
  files, and the full list is in <code>/scratch/&lt;username&gt;/.purge-soon.txt</code>.</li>
<li>Files you use (read or write) are safe. Deliberately touching files just to keep them isn't in
  the spirit of it: move what you want to keep somewhere else.</li>
<li>Empty folders unused for 100 days go too.</li>
</ul>
<h2 id="shared-models-models">Shared models: <code>/models</code><a class="headerlink" href="#shared-models-models" title="Permanent link">¶</a></h2>
<p>Models that several people use live in <code>/models</code> on each machine, readable by everyone and
changeable by no one:</p>
<div class="highlight"><pre><span></span><code>ls<span class="w"> </span>/models/*/
</code></pre></div>
<p>Load them by path, for example <code>AutoModel.from_pretrained("/models/Qwen/Qwen3-4B")</code> or
<code>vllm serve /models/google/gemma-4-26B-A4B-it</code>. This saves everyone a copy in their own scratch.</p>
<p>To add a model, download it to your scratch (see <a href="/spark-docs/howto/download-models/">Download a model</a>)
and ask the maintainer to publish it.</p>
<h2 id="job-temporary-files">Job temporary files<a class="headerlink" href="#job-temporary-files" title="Permanent link">¶</a></h2>
<p>Inside a Slurm job, <code>/tmp</code> is private to that job, and it's deleted when the job ends. Copy
anything you need out of it before your job finishes.</p>
