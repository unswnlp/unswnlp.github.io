---
title: "Serve a model with vLLM"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="serve-a-model-with-vllm">Serve a model with vLLM<a class="headerlink" href="#serve-a-model-with-vllm" title="Permanent link">¶</a></h1>
<p>vLLM serves a model behind an OpenAI-compatible API. On the Spark machines it comes as the <code>vllm/26.09</code> module
(vLLM 0.29, NVIDIA's NGC build) and runs only inside Slurm jobs.</p>
<h2 id="a-serving-job">A serving job<a class="headerlink" href="#a-serving-job" title="Permanent link">¶</a></h2>
<div class="highlight"><span class="filename">serve.sbatch</span><pre><span></span><code><span class="ch">#!/bin/bash -l</span>
<span class="c1">#SBATCH -J serve</span>
<span class="c1">#SBATCH -p batch</span>
<span class="c1">#SBATCH --gres=gpu:1</span>
<span class="c1">#SBATCH -c 8</span>
<span class="c1">#SBATCH --mem=105G</span>
<span class="c1">#SBATCH -t 04:00:00</span>
<span class="c1">#SBATCH -o /scratch/%u/serve.%j.log</span>

module<span class="w"> </span>load<span class="w"> </span>vllm/26.09
<span class="nv">port</span><span class="o">=</span><span class="k">$((</span><span class="m">20000</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="nv">SLURM_JOB_ID</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="m">10000</span><span class="k">))</span>
<span class="nb">echo</span><span class="w"> </span><span class="s2">"serving on port </span><span class="nv">$port</span><span class="s2">"</span>
vllm<span class="w"> </span>serve<span class="w"> </span>/models/google/gemma-4-26B-A4B-it<span class="w"> </span>--served-model-name<span class="w"> </span>gemma-4-26b<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>--port<span class="w"> </span><span class="s2">"</span><span class="nv">$port</span><span class="s2">"</span><span class="w"> </span>--max-model-len<span class="w"> </span><span class="m">8192</span>
</code></pre></div>
<div class="highlight"><pre><span></span><code>sbatch<span class="w"> </span>serve.sbatch
grep<span class="w"> </span><span class="s1">'serving on port'</span><span class="w"> </span>/scratch/<span class="nv">$USER</span>/serve.*.log<span class="w">     </span><span class="c1"># which port it picked</span>
</code></pre></div>
<p>The server is ready when the log shows <code>Application startup complete</code>. Loading a 50 GB model
takes a few minutes.</p>
<h2 id="memory">Memory<a class="headerlink" href="#memory" title="Permanent link">¶</a></h2>
<p>You don't need to set <code>--gpu-memory-utilization</code>: the <code>vllm</code> command works it out from your job's
<code>--mem</code>, leaving room for vLLM's own RAM. What you do need is a <code>--mem</code> big enough for the model:</p>
<table>
<thead>
<tr>
<th>Model (BF16)</th>
<th>Weights</th>
<th>Suggested <code>--mem</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>4B</td>
<td>8 GB</td>
<td>24G</td>
</tr>
<tr>
<td>7–12B</td>
<td>16–24 GB</td>
<td>48G</td>
</tr>
<tr>
<td>26–31B</td>
<td>52–62 GB</td>
<td>105G (all of it)</td>
</tr>
</tbody>
</table>
<p>If the log says there's no room for the KV cache, raise <code>--mem</code> or lower <code>--max-model-len</code>.</p>
<h2 id="querying-it">Querying it<a class="headerlink" href="#querying-it" title="Permanent link">¶</a></h2>
<p>From the same machine (a login shell or another job):</p>
<div class="highlight"><pre><span></span><code>curl<span class="w"> </span>-s<span class="w"> </span>localhost:&lt;port&gt;/v1/chat/completions<span class="w"> </span>-H<span class="w"> </span><span class="s1">'Content-Type: application/json'</span><span class="w"> </span><span class="se">\</span>
<span class="w">  </span>-d<span class="w"> </span><span class="s1">'{"model": "gemma-4-26b", "messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 50}'</span>
</code></pre></div>
<p>From your laptop, forward the port through your SSH connection first:</p>
<div class="highlight"><pre><span></span><code>ssh<span class="w"> </span>-N<span class="w"> </span>-L<span class="w"> </span><span class="m">8000</span>:localhost:&lt;port&gt;<span class="w"> </span>spark-2
</code></pre></div>
<p>Then use <code>http://localhost:8000/v1</code> as the base URL in your client (for example the <code>openai</code>
Python package, with any API key).</p>
<div class="admonition note">
<p class="admonition-title">On spark-1</p>
<p>Your job may run on the node you're not logged in to. <code>squeue</code> shows which (<code>NODELIST</code>); use
that node's name instead of <code>localhost</code>, e.g. <code>ssh -N -L 8000:&lt;node&gt;:&lt;port&gt; spark-1</code>.</p>
</div>
<h2 id="tips">Tips<a class="headerlink" href="#tips" title="Permanent link">¶</a></h2>
<ul>
<li><strong>Speed:</strong> dense models are slow on the GB10, because every generated token reads all the
  weights. Gemma 4 31B gives about 3.5 tokens/s in BF16. Mixture-of-experts models such as
  <code>gemma-4-26B-A4B-it</code> are several times faster, and <code>--quantization fp8</code> can roughly double the speed.</li>
<li><strong>Smaller models share well:</strong> for 4B-class models, <code>--gres=shard:1 --mem=24G</code> is enough.</li>
<li><strong>Anyone on the machine can reach your port.</strong> Add <code>--api-key &lt;some-secret&gt;</code> to <code>vllm serve</code> (and
  send it as the API key) if that matters.</li>
<li><strong>Stop the server</strong> when you're done (<code>scancel -n serve</code>); it holds its memory the whole time.</li>
<li>Warnings when the job ends, about force-killing <code>EngineCore</code> or a leaked semaphore, are harmless.</li>
</ul>
