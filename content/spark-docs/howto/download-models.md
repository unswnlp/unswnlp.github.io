---
title: "Download a model"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="download-a-model">Download a model<a class="headerlink" href="#download-a-model" title="Permanent link">¶</a></h1>
<p>First check <code>/models</code>: the model may already be there (<code>ls /models/*/</code>).</p>
<h2 id="log-in-to-hugging-face-once">Log in to Hugging Face (once)<a class="headerlink" href="#log-in-to-hugging-face-once" title="Permanent link">¶</a></h2>
<p>Gated models (Gemma, Llama, Cohere, …) need your Hugging Face token, and you need to accept the
model's licence on its Hugging Face page first.</p>
<div class="highlight"><pre><span></span><code>module<span class="w"> </span>load<span class="w"> </span>hf/26.11
hf<span class="w"> </span>auth<span class="w"> </span>login
</code></pre></div>
<p>The token is saved in your scratch (<code>/scratch/&lt;username&gt;/.cache/huggingface</code>), which only you can
read.</p>
<h2 id="download-as-a-job">Download as a job<a class="headerlink" href="#download-as-a-job" title="Permanent link">¶</a></h2>
<p>Run big downloads as a batch job: they don't need you to stay logged in, and they aren't held back
by the login limits.</p>
<div class="highlight"><pre><span></span><code>module<span class="w"> </span>load<span class="w"> </span>hf/26.11
sbatch<span class="w"> </span>-J<span class="w"> </span>dl<span class="w"> </span>-c<span class="w"> </span><span class="m">4</span><span class="w"> </span>--mem<span class="o">=</span>8G<span class="w"> </span>-t<span class="w"> </span><span class="m">12</span>:00:00<span class="w"> </span>-o<span class="w"> </span>/scratch/<span class="nv">$USER</span>/dl.%j.log<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>--wrap<span class="w"> </span><span class="s1">'hf download Qwen/Qwen3-4B --local-dir /scratch/$USER/models/Qwen/Qwen3-4B'</span>
</code></pre></div>
<p>Downloads run at about 110 MB/s, so a 50 GB model takes around 8 minutes.</p>
<details class="example">
<summary>Several models in one job</summary>
<div class="highlight"><span class="filename">get-models.sbatch</span><pre><span></span><code><span class="ch">#!/bin/bash -l</span>
<span class="c1">#SBATCH -J get-models -c 4 --mem=8G -t 12:00:00</span>
<span class="c1">#SBATCH -o /scratch/%u/get-models.%j.log</span>

<span class="nv">MODELS</span><span class="o">=(</span>Qwen/Qwen3-1.7B<span class="w"> </span>Qwen/Qwen3-4B<span class="o">)</span>

module<span class="w"> </span>load<span class="w"> </span>hf/26.11
<span class="k">for</span><span class="w"> </span>m<span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="s2">"</span><span class="si">${</span><span class="nv">MODELS</span><span class="p">[@]</span><span class="si">}</span><span class="s2">"</span><span class="p">;</span><span class="w"> </span><span class="k">do</span>
<span class="w">  </span><span class="nb">echo</span><span class="w"> </span><span class="s2">"=== </span><span class="k">$(</span>date<span class="w"> </span>+%T<span class="k">)</span><span class="s2">  </span><span class="nv">$m</span><span class="s2">"</span>
<span class="w">  </span>hf<span class="w"> </span>download<span class="w"> </span><span class="s2">"</span><span class="nv">$m</span><span class="s2">"</span><span class="w"> </span>--local-dir<span class="w"> </span><span class="s2">"/scratch/</span><span class="nv">$USER</span><span class="s2">/models/</span><span class="nv">$m</span><span class="s2">"</span><span class="w"> </span>&gt;/dev/null<span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="nb">echo</span><span class="w"> </span><span class="s2">"!!! failed: </span><span class="nv">$m</span><span class="s2">"</span>
<span class="k">done</span>
<span class="nb">echo</span><span class="w"> </span><span class="s2">"=== </span><span class="k">$(</span>date<span class="w"> </span>+%T<span class="k">)</span><span class="s2">  done"</span>
</code></pre></div>
</details>
<h2 id="checking-progress">Checking progress<a class="headerlink" href="#checking-progress" title="Permanent link">¶</a></h2>
<p>In a job's log, hf only shows a "Fetching N files" bar, which moves when a whole file finishes. To
see the real speed, watch the folder grow:</p>
<div class="highlight"><pre><span></span><code><span class="nv">d</span><span class="o">=</span>/scratch/<span class="nv">$USER</span>/models/Qwen/Qwen3-4B<span class="p">;</span><span class="w"> </span><span class="nv">p</span><span class="o">=</span><span class="k">$(</span>du<span class="w"> </span>-sb<span class="w"> </span><span class="s2">"</span><span class="nv">$d</span><span class="s2">"</span><span class="w"> </span><span class="p">|</span><span class="w"> </span>cut<span class="w"> </span>-f1<span class="k">)</span>
<span class="k">while</span><span class="w"> </span>sleep<span class="w"> </span><span class="m">10</span><span class="p">;</span><span class="w"> </span><span class="k">do</span><span class="w"> </span><span class="nv">n</span><span class="o">=</span><span class="k">$(</span>du<span class="w"> </span>-sb<span class="w"> </span><span class="s2">"</span><span class="nv">$d</span><span class="s2">"</span><span class="w"> </span><span class="p">|</span><span class="w"> </span>cut<span class="w"> </span>-f1<span class="k">)</span><span class="p">;</span><span class="w"> </span>awk<span class="w"> </span>-v<span class="w"> </span><span class="nv">n</span><span class="o">=</span><span class="s2">"</span><span class="nv">$n</span><span class="s2">"</span><span class="w"> </span>-v<span class="w"> </span><span class="nv">p</span><span class="o">=</span><span class="s2">"</span><span class="nv">$p</span><span class="s2">"</span><span class="w"> </span>-v<span class="w"> </span><span class="nv">t</span><span class="o">=</span><span class="s2">"</span><span class="k">$(</span>date<span class="w"> </span>+%T<span class="k">)</span><span class="s2">"</span><span class="w"> </span><span class="s1">'BEGIN { printf "%s  %6.1f GB  %6.1f MB/s\n", t, n/1e9, (n-p)/1e7 }'</span><span class="p">;</span><span class="w"> </span><span class="nv">p</span><span class="o">=</span><span class="nv">$n</span><span class="p">;</span><span class="w"> </span><span class="k">done</span>
</code></pre></div>
<p>Press Ctrl+C to stop watching (the download carries on). It's finished when the job has gone from
<code>squeue</code>.</p>
<h2 id="if-downloads-crawl">If downloads crawl<a class="headerlink" href="#if-downloads-crawl" title="Permanent link">¶</a></h2>
<p>The machines download over plain HTTPS (<code>HF_HUB_DISABLE_XET=1</code> is set for you), because Hugging Face's
newer "xet" downloader stalls on the long link to Australia. If you change that setting and a
download crawls, set it back, delete the half-finished files and start again:</p>
<div class="highlight"><pre><span></span><code>rm<span class="w"> </span>-f<span class="w"> </span>/scratch/<span class="nv">$USER</span>/models/&lt;org&gt;/&lt;name&gt;/.cache/huggingface/download/*.incomplete
</code></pre></div>
<h2 id="sharing-it">Sharing it<a class="headerlink" href="#sharing-it" title="Permanent link">¶</a></h2>
<p>If others will use the model too, ask the maintainer to publish it to <code>/models</code> on that machine. Once it's
published, delete your copy.</p>
