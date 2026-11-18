---
title: "Machines"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="machines">Machines<a class="headerlink" href="#machines" title="Permanent link">¶</a></h1>
<p>There are two Spark machines. Each is a separate system with its own Slurm queue, storage and
accounts, set up the same way.</p>
<table>
<thead>
<tr>
<th></th>
<th>spark-1</th>
<th>spark-2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Nodes</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>GPUs</td>
<td>2 × GB10 (one per node)</td>
<td>1 × GB10</td>
</tr>
<tr>
<td>CPU cores</td>
<td>40 (20 per node)</td>
<td>20</td>
</tr>
<tr>
<td>Memory for jobs</td>
<td>about 210 GB (105 GB per node)</td>
<td>about 105 GB</td>
</tr>
<tr>
<td>Multi-node jobs</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Status</td>
<td>Being set up</td>
<td>Available</td>
</tr>
</tbody>
</table>
<h2 id="which-one-to-use">Which one to use<a class="headerlink" href="#which-one-to-use" title="Permanent link">¶</a></h2>
<p>Both machines are for <strong>proof of concept</strong>: getting an idea working on a small scale before
running it for real. Larger jobs belong on <a href="https://docs.restech.unsw.edu.au/">Katana</a>.</p>
<ul>
<li><strong>spark-2</strong> for most proof-of-concept work on one GPU: trying a method, debugging a training
  script, short fine-tuning runs, and serving a model to test against (up to roughly 30B
  parameters in BF16).</li>
<li><strong>spark-1</strong> for proving out things that need two GPUs or more than one node's memory, such as
  checking that a model or training run splits across nodes before you scale it up on Katana.
  Single-node jobs run there too, on either node.</li>
<li><strong>Katana</strong> once it works and needs to scale: long training runs, hyperparameter sweeps,
  large evaluations, or more GPUs than a Spark machine has.</li>
</ul>
<h2 id="whats-separate">What's separate<a class="headerlink" href="#whats-separate" title="Permanent link">¶</a></h2>
<ul>
<li><strong>Accounts:</strong> an account on one machine doesn't give you the other. Ask for the one(s) you need.</li>
<li><strong>Storage:</strong> each machine has its own home, scratch and <code>/models</code>. Files don't move between them
  on their own; copy them with <code>rsync</code> if you need to (see <a href="/spark-docs/getting-started/connecting/">Copying files</a>).</li>
<li><strong>Queues and priority:</strong> each machine has its own Slurm queue and its own fair-share history.</li>
</ul>
<h2 id="spark-1-specifics">spark-1 specifics<a class="headerlink" href="#spark-1-specifics" title="Permanent link">¶</a></h2>
<div class="admonition info">
<p class="admonition-title">Being set up</p>
<p>spark-1 isn't open yet. This section describes the plan and will be filled in once it's
running.</p>
</div>
<ul>
<li>spark-1's two nodes share the same home, scratch and <code>/models</code>, so a job sees the same files on
  either node.</li>
<li>You log in to spark-1 as one machine; Slurm places your job on a free node.</li>
<li>A job can ask for both nodes (<code>-N 2</code>), for example to split a large model across both GPUs. A
  how-to for multi-node jobs will follow.</li>
<li><code>nodestat</code> on spark-1 shows each node separately.</li>
</ul>
