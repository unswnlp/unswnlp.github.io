---
title: "Software"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="software">Software<a class="headerlink" href="#software" title="Permanent link">¶</a></h1>
<p>Software is provided as <strong>modules</strong>, as on Gadi and Katana. The big Python packages (PyTorch,
transformers, …) are installed once, centrally, so they don't use up your file quota, and every
module in a release has been tested together.</p>
<h2 id="modules">Modules<a class="headerlink" href="#modules" title="Permanent link">¶</a></h2>
<div class="highlight"><pre><span></span><code>module<span class="w"> </span>avail<span class="w">                 </span><span class="c1"># what's available</span>
module<span class="w"> </span>load<span class="w"> </span>hf/26.11<span class="w">         </span><span class="c1"># load one (it loads what it needs too)</span>
module<span class="w"> </span>list<span class="w">                  </span><span class="c1"># what you have loaded</span>
module<span class="w"> </span>unload<span class="w"> </span>hf<span class="w">             </span><span class="c1"># unload</span>
module<span class="w"> </span>spider<span class="w"> </span>vllm<span class="w">           </span><span class="c1"># details about a module</span>
</code></pre></div>
<p>A small <code>base</code> module is loaded at login and stays loaded; it sets up the cache locations and a
few safety settings. You don't need to touch it.</p>
<h2 id="python-bundles-release-2611">Python bundles (release 26.11)<a class="headerlink" href="#python-bundles-release-2611" title="Permanent link">¶</a></h2>
<p>The Python stack comes as bundles that build on each other. Each does one job:</p>
<table>
<thead>
<tr>
<th>Module</th>
<th>What's in it</th>
<th>Loads first</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>core/26.11</code></td>
<td>Python 3.12, PyTorch 2.14 (CUDA 13.0), torchvision, torchaudio, NumPy, SciPy, pandas, PyArrow, scikit-learn, Matplotlib, seaborn, tqdm, Weights &amp; Biases, TensorBoard</td>
<td></td>
</tr>
<tr>
<td><code>hf/26.11</code></td>
<td>transformers 5.23, tokenizers, safetensors, huggingface_hub, accelerate, datasets, sentence-transformers, bitsandbytes, torchao, sentencepiece, tiktoken</td>
<td><code>core</code></td>
</tr>
<tr>
<td><code>train/26.11</code></td>
<td>PEFT 0.21, TRL 1.18</td>
<td><code>hf</code></td>
</tr>
<tr>
<td><code>eval/26.11</code></td>
<td>lm-eval 0.4.13, evaluate, sacreBLEU, rouge-score</td>
<td><code>hf</code></td>
</tr>
<tr>
<td><code>jupyter/26.11</code></td>
<td>JupyterLab, ipykernel, ipywidgets</td>
<td><code>core</code></td>
</tr>
</tbody>
</table>
<p>For example, <code>module load train/26.11</code> gives you everything for LoRA fine-tuning with PEFT and
TRL. To see exact versions: <code>python -m pip list</code>.</p>
<p>The release number is the year and month (<code>26.11</code> = November 2026). A new release doesn't change
an old one, so a project can stay on <code>26.11</code> while others move on.</p>
<h2 id="adding-your-own-packages">Adding your own packages<a class="headerlink" href="#adding-your-own-packages" title="Permanent link">¶</a></h2>
<p>Make a virtual environment <strong>on top of</strong> the modules. It sees everything in the modules you have
loaded, and holds only what you add:</p>
<div class="highlight"><pre><span></span><code>module<span class="w"> </span>load<span class="w"> </span>hf/26.11
python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>--system-site-packages<span class="w"> </span>--without-pip<span class="w"> </span>/scratch/<span class="nv">$USER</span>/envs/myproject
<span class="nb">source</span><span class="w"> </span>/scratch/<span class="nv">$USER</span>/envs/myproject/bin/activate
python<span class="w"> </span>-m<span class="w"> </span>pip<span class="w"> </span>install<span class="w"> </span>some-package
</code></pre></div>
<ul>
<li>Keep environments in scratch, not home.</li>
<li>Use <strong><code>python -m pip</code></strong>, not <code>uv pip</code>: uv can't see the bundle packages and would download
  second copies of transformers and friends.</li>
<li>pip won't replace PyTorch, NumPy or the CUDA libraries: the modules pin those, so your
  environment stays compatible. Other packages you install take priority over the bundle's.</li>
<li><code>pip install</code> outside a virtual environment is refused on purpose, so nothing lands in
  <code>~/.local</code>.</li>
</ul>
<p>Next time: <code>module load hf/26.11</code> and <code>source …/activate</code> again (also inside job scripts).</p>
<h2 id="containers">Containers<a class="headerlink" href="#containers" title="Permanent link">¶</a></h2>
<p>Two tools ship as containers, because they need their own builds of PyTorch. You use them
through a command, and they only run inside Slurm jobs.</p>
<table>
<thead>
<tr>
<th>Module</th>
<th>Command</th>
<th>What it is</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>vllm/26.09</code></td>
<td><code>vllm</code></td>
<td>vLLM 0.29 for serving models, from NVIDIA's NGC build. See <a href="/spark-docs/howto/vllm/">Serve a model with vLLM</a></td>
</tr>
<tr>
<td><code>unsloth/26.11</code></td>
<td><code>unsloth-python</code></td>
<td>Unsloth 2026.11.6 for fast fine-tuning, on NVIDIA's PyTorch 25.11. See <a href="/spark-docs/howto/unsloth/">Fine-tune with Unsloth</a></td>
</tr>
</tbody>
</table>
<p>You can also run your own containers with <strong>Apptainer</strong> inside a job (<code>apptainer exec --nv
my.sif …</code>). Docker isn't available to users.</p>
<h2 id="gb10-specifics">GB10 specifics<a class="headerlink" href="#gb10-specifics" title="Permanent link">¶</a></h2>
<ul>
<li><strong>Arm, not x86.</strong> Packages need <code>aarch64</code> builds. Most of PyPI has them; if pip starts compiling
  something big from source, ask before letting it run for an hour.</li>
<li><strong>flash-attn doesn't build for this GPU.</strong> Use PyTorch's built-in attention instead:
  <code>attn_implementation="sdpa"</code> in transformers. It's the default in most models anyway.</li>
<li><strong>Precision:</strong> BF16 is the safe default for training and inference. FP8 works well for
  inference (for example <code>--quantization fp8</code> in vLLM). FP4 is still experimental.</li>
</ul>
