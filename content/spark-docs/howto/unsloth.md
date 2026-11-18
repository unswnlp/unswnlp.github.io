---
title: "Fine-tune with Unsloth"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="fine-tune-with-unsloth">Fine-tune with Unsloth<a class="headerlink" href="#fine-tune-with-unsloth" title="Permanent link">¶</a></h1>
<p><a href="https://unsloth.ai">Unsloth</a> speeds up LoRA and QLoRA fine-tuning. On the Spark machines it comes as the
<code>unsloth/26.11</code> module: Unsloth 2026.11.6 in a container built on NVIDIA's PyTorch 25.11, with
its own transformers 5.17, TRL 1.15, PEFT, xformers and bitsandbytes. You run your script with
<code>unsloth-python</code> instead of <code>python</code>, inside a Slurm job.</p>
<p>For plain PEFT/TRL without Unsloth, the <code>train/26.11</code> module is simpler.</p>
<h2 id="a-training-job">A training job<a class="headerlink" href="#a-training-job" title="Permanent link">¶</a></h2>
<div class="highlight"><span class="filename">finetune.py</span><pre><span></span><code><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">torch</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">unsloth</span><span class="w"> </span><span class="kn">import</span> <span class="n">FastLanguageModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">datasets</span><span class="w"> </span><span class="kn">import</span> <span class="n">Dataset</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">trl</span><span class="w"> </span><span class="kn">import</span> <span class="n">SFTConfig</span><span class="p">,</span> <span class="n">SFTTrainer</span>

<span class="n">model</span><span class="p">,</span> <span class="n">tok</span> <span class="o">=</span> <span class="n">FastLanguageModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
    <span class="s2">"/models/Qwen/Qwen3-1.7B"</span><span class="p">,</span> <span class="n">max_seq_length</span><span class="o">=</span><span class="mi">2048</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">torch</span><span class="o">.</span><span class="n">bfloat16</span><span class="p">,</span> <span class="n">load_in_4bit</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">FastLanguageModel</span><span class="o">.</span><span class="n">get_peft_model</span><span class="p">(</span>
    <span class="n">model</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="mi">16</span><span class="p">,</span> <span class="n">lora_alpha</span><span class="o">=</span><span class="mi">16</span><span class="p">,</span> <span class="n">target_modules</span><span class="o">=</span><span class="p">[</span><span class="s2">"q_proj"</span><span class="p">,</span> <span class="s2">"k_proj"</span><span class="p">,</span> <span class="s2">"v_proj"</span><span class="p">,</span> <span class="s2">"o_proj"</span><span class="p">])</span>

<span class="n">data</span> <span class="o">=</span> <span class="n">Dataset</span><span class="o">.</span><span class="n">from_dict</span><span class="p">({</span><span class="s2">"text"</span><span class="p">:</span> <span class="p">[</span><span class="s2">"Q: what is 2 plus 2? A: 4."</span><span class="p">]</span> <span class="o">*</span> <span class="mi">64</span><span class="p">})</span>   <span class="c1"># your data here</span>
<span class="n">out</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"/scratch/</span><span class="si">{</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'USER'</span><span class="p">]</span><span class="si">}</span><span class="s2">/runs/qwen3-lora"</span>
<span class="n">trainer</span> <span class="o">=</span> <span class="n">SFTTrainer</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span> <span class="n">processing_class</span><span class="o">=</span><span class="n">tok</span><span class="p">,</span> <span class="n">train_dataset</span><span class="o">=</span><span class="n">data</span><span class="p">,</span>
                     <span class="n">args</span><span class="o">=</span><span class="n">SFTConfig</span><span class="p">(</span><span class="n">output_dir</span><span class="o">=</span><span class="n">out</span><span class="p">,</span> <span class="n">max_steps</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">per_device_train_batch_size</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
                                    <span class="n">logging_steps</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">report_to</span><span class="o">=</span><span class="s2">"none"</span><span class="p">))</span>
<span class="n">trainer</span><span class="o">.</span><span class="n">train</span><span class="p">()</span>
</code></pre></div>
<div class="highlight"><span class="filename">finetune.sbatch</span><pre><span></span><code><span class="ch">#!/bin/bash -l</span>
<span class="c1">#SBATCH -J finetune</span>
<span class="c1">#SBATCH -p batch</span>
<span class="c1">#SBATCH --gres=shard:2</span>
<span class="c1">#SBATCH -c 8</span>
<span class="c1">#SBATCH --mem=48G</span>
<span class="c1">#SBATCH -t 08:00:00</span>
<span class="c1">#SBATCH -o /scratch/%u/finetune.%j.log</span>

module<span class="w"> </span>load<span class="w"> </span>unsloth/26.11
<span class="nb">cd</span><span class="w"> </span>/scratch/<span class="nv">$USER</span><span class="w">        </span><span class="c1"># Unsloth writes a compiled cache in the current folder</span>
unsloth-python<span class="w"> </span>finetune.py
</code></pre></div>
<p>For a quick try, an interactive job works too:</p>
<div class="highlight"><pre><span></span><code>module<span class="w"> </span>load<span class="w"> </span>unsloth/26.11
<span class="nb">cd</span><span class="w"> </span>/scratch/<span class="nv">$USER</span>
srun<span class="w"> </span>-p<span class="w"> </span>interactive<span class="w"> </span>-c<span class="w"> </span><span class="m">4</span><span class="w"> </span>--mem<span class="o">=</span>24G<span class="w"> </span>--gres<span class="o">=</span>shard:1<span class="w"> </span>-t<span class="w"> </span><span class="m">30</span><span class="w"> </span>unsloth-python<span class="w"> </span>finetune.py
</code></pre></div>
<h2 id="sizing">Sizing<a class="headerlink" href="#sizing" title="Permanent link">¶</a></h2>
<ul>
<li><strong>LoRA in BF16</strong> needs the model's weights (2 GB per billion parameters) plus activations and
  optimizer state for the adapters. A 1.7B model fits easily in <code>--mem=24G</code>; a 27–31B model needs
  most of the machine (<code>--gres=gpu:1 --mem=105G</code>).</li>
<li><strong>QLoRA</strong> (<code>load_in_4bit=True</code>) cuts the weights to about a quarter, for models that don't fit
  in BF16. bitsandbytes works on the GB10.</li>
</ul>
<h2 id="extra-packages">Extra packages<a class="headerlink" href="#extra-packages" title="Permanent link">¶</a></h2>
<p><code>unsloth-python</code> runs the container's Python, so the <code>core</code>/<code>hf</code> modules and your own virtual
environments don't apply inside it. If your script needs a package the container doesn't have,
ask the maintainer. To see what's included:</p>
<div class="highlight"><pre><span></span><code>apptainer<span class="w"> </span><span class="nb">exec</span><span class="w"> </span>/apps/containers/unsloth/26.11/unsloth.sif<span class="w"> </span>pip<span class="w"> </span>list
</code></pre></div>
<h2 id="messages-you-can-ignore">Messages you can ignore<a class="headerlink" href="#messages-you-can-ignore" title="Permanent link">¶</a></h2>
<ul>
<li><code>Not an error, but Unsloth cannot patch MLP layers…</code>: normal when your LoRA doesn't cover the
  MLP layers (as in the example above), or the model has bias terms.</li>
<li><code>Ignoring an unusable torchao…</code>: only matters for torchao quantization, which LoRA and QLoRA
  don't use.</li>
</ul>
