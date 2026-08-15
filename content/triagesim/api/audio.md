---
title: "triagesim.audio"
---

<h1 id="triagesimaudio"><code>triagesim.audio</code><a class="headerlink" href="#triagesimaudio" title="Permanent link">¶</a></h1>
<p>Optional speech synthesis via XTTS-v2. Requires the <code>audio</code> extra:</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[audio]"</span>
</span></code></pre></div>
<div class="admonition note">
<p class="admonition-title">Documented by hand</p>
<p>This page is written manually rather than generated, because importing the
module requires <code>torch</code> and <code>TTS</code> — heavy dependencies that the
documentation build does not install.</p>
</div>
<p>See <a href="/triagesim/guide/audio/">Audio rendering</a> for worked examples.</p>
<h2 id="speechrenderer"><code>SpeechRenderer</code><a class="headerlink" href="#speechrenderer" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.audio.renderer</span><span class="w"> </span><span class="kn">import</span> <span class="n">SpeechRenderer</span>
</span></code></pre></div>
<p>Local neural TTS renderer using XTTS-v2. Supports voice cloning from a reference
WAV, and selects CUDA, MPS or CPU automatically.</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p><code>triagesim/audio/__init__.py</code> is empty, so
<code>from triagesim.audio import SpeechRenderer</code> raises <code>ImportError</code>. Import
from <code>triagesim.audio.renderer</code> as shown above.</p>
</div>
<h3 id="__init__"><code>__init__</code><a class="headerlink" href="#__init__" title="Permanent link">¶</a></h3>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="n">SpeechRenderer</span><span class="p">(</span><span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"tts_models/multilingual/multi-dataset/xtts_v2"</span><span class="p">)</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>model_name</code></td>
<td><code>str</code></td>
<td><code>"tts_models/multilingual/multi-dataset/xtts_v2"</code></td>
<td>Coqui TTS model identifier.</td>
</tr>
</tbody>
</table>
<p>Selects a device and loads the model. On Apple Silicon it also sets
<code>torch.set_float32_matmul_precision("high")</code>. GPU acceleration is passed to the
underlying <code>TTS</code> object only when the device is CUDA.</p>
<p>Model loading is expensive — construct one renderer and reuse it.</p>
<p><strong>Attributes</strong></p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>device</code></td>
<td><code>str</code></td>
<td>The selected device: <code>"cuda"</code>, <code>"mps"</code> or <code>"cpu"</code>.</td>
</tr>
<tr>
<td><code>tts</code></td>
<td><code>TTS</code></td>
<td>The underlying Coqui TTS model.</td>
</tr>
</tbody>
</table>
<h3 id="render"><code>render</code><a class="headerlink" href="#render" title="Permanent link">¶</a></h3>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">render</span><span class="p">(</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a>    <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-3-4"><a href="#__codelineno-3-4" id="__codelineno-3-4" name="__codelineno-3-4"></a>    <span class="n">speaker_wav</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Path</span><span class="p">,</span>
</span><span id="__span-3-5"><a href="#__codelineno-3-5" id="__codelineno-3-5" name="__codelineno-3-5"></a>    <span class="n">out_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Path</span><span class="p">,</span>
</span><span id="__span-3-6"><a href="#__codelineno-3-6" id="__codelineno-3-6" name="__codelineno-3-6"></a>    <span class="n">language</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"en"</span><span class="p">,</span>
</span><span id="__span-3-7"><a href="#__codelineno-3-7" id="__codelineno-3-7" name="__codelineno-3-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Path</span>
</span></code></pre></div>
<p>Synthesise <code>text</code> in the voice of <code>speaker_wav</code> and write it to <code>out_path</code>. All
arguments are keyword-only.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>text</code></td>
<td><code>str</code></td>
<td>—</td>
<td>Text to synthesise.</td>
</tr>
<tr>
<td><code>speaker_wav</code></td>
<td><code>str \| Path</code></td>
<td>—</td>
<td>Reference recording to clone.</td>
</tr>
<tr>
<td><code>out_path</code></td>
<td><code>str \| Path</code></td>
<td>—</td>
<td>Destination WAV path. Parent directories are created.</td>
</tr>
<tr>
<td><code>language</code></td>
<td><code>str</code></td>
<td><code>"en"</code></td>
<td>Language code for XTTS-v2.</td>
</tr>
</tbody>
</table>
<p><strong>Returns</strong> the <code>Path</code> that was written.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="n">renderer</span> <span class="o">=</span> <span class="n">SpeechRenderer</span><span class="p">()</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>
</span><span id="__span-4-3"><a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a><span class="n">renderer</span><span class="o">.</span><span class="n">render</span><span class="p">(</span>
</span><span id="__span-4-4"><a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a>    <span class="n">text</span><span class="o">=</span><span class="s2">"Can you tell me what happened this morning?"</span><span class="p">,</span>
</span><span id="__span-4-5"><a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a>    <span class="n">speaker_wav</span><span class="o">=</span><span class="s2">"voices/nurse.wav"</span><span class="p">,</span>
</span><span id="__span-4-6"><a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a>    <span class="n">out_path</span><span class="o">=</span><span class="s2">"audio/000_nurse.wav"</span><span class="p">,</span>
</span><span id="__span-4-7"><a href="#__codelineno-4-7" id="__codelineno-4-7" name="__codelineno-4-7"></a><span class="p">)</span>
</span></code></pre></div>
<div class="admonition danger">
<p class="admonition-title">Licence and consent</p>
<p>XTTS-v2 carries its own model licence, separate from TriageSim's. Review its
terms before publishing synthesised output, and only clone voices with the
speaker's consent. See <a href="/triagesim/guide/audio/">Audio rendering</a>.</p>
</div>
