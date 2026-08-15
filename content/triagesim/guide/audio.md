---
title: "Audio rendering"
---

<h1 id="audio-rendering">Audio rendering<a class="headerlink" href="#audio-rendering" title="Permanent link">¶</a></h1>
<p>TriageSim can turn a finished dialogue into multi-speaker speech using
<a href="https://github.com/coqui-ai/TTS">XTTS-v2</a>, giving nurse and patient distinct
cloned voices. This closes the loop from structured EHR to spoken data.</p>
<p>Audio is entirely optional — the simulation and metrics work without it.</p>
<h2 id="installation">Installation<a class="headerlink" href="#installation" title="Permanent link">¶</a></h2>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[audio]"</span>
</span></code></pre></div>
<p>This pulls in <code>torch</code> and <code>TTS</code>, which are large. Install the extra only if you
need speech output.</p>
<h2 id="import-path">Import path<a class="headerlink" href="#import-path" title="Permanent link">¶</a></h2>
<p><code>triagesim/audio/__init__.py</code> is empty, so <code>SpeechRenderer</code> must be imported
from the module itself:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.audio.renderer</span><span class="w"> </span><span class="kn">import</span> <span class="n">SpeechRenderer</span>
</span></code></pre></div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p><code>from triagesim.audio import SpeechRenderer</code> will raise <code>ImportError</code>. Use
the full module path above.</p>
</div>
<h2 id="speechrenderer"><code>SpeechRenderer</code><a class="headerlink" href="#speechrenderer" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="n">renderer</span> <span class="o">=</span> <span class="n">SpeechRenderer</span><span class="p">()</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Default</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>model_name</code></td>
<td><code>"tts_models/multilingual/multi-dataset/xtts_v2"</code></td>
<td>Any Coqui TTS model identifier.</td>
</tr>
</tbody>
</table>
<p>Construction downloads the model on first use and loads it into memory, so
build <strong>one</strong> renderer and reuse it. Instantiating a renderer per utterance will
reload the model every time.</p>
<h3 id="device-selection">Device selection<a class="headerlink" href="#device-selection" title="Permanent link">¶</a></h3>
<p>The device is chosen automatically at construction, in order of preference:</p>
<ol>
<li><code>cuda</code> — if <code>torch.cuda.is_available()</code></li>
<li><code>mps</code> — Apple Silicon; also sets <code>torch.set_float32_matmul_precision("high")</code></li>
<li><code>cpu</code> — the fallback</li>
</ol>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">renderer</span> <span class="o">=</span> <span class="n">SpeechRenderer</span><span class="p">()</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a><span class="nb">print</span><span class="p">(</span><span class="n">renderer</span><span class="o">.</span><span class="n">device</span><span class="p">)</span>  <span class="c1"># 'cuda', 'mps', or 'cpu'</span>
</span></code></pre></div>
<p>GPU acceleration is only enabled for CUDA. On MPS the model runs but is not
passed the <code>gpu=True</code> flag, and on CPU expect synthesis to be several times
slower than real time.</p>
<h3 id="render"><code>render</code><a class="headerlink" href="#render" title="Permanent link">¶</a></h3>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="n">path</span> <span class="o">=</span> <span class="n">renderer</span><span class="o">.</span><span class="n">render</span><span class="p">(</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>    <span class="n">text</span><span class="o">=</span><span class="s2">"Can you tell me what happened this morning?"</span><span class="p">,</span>
</span><span id="__span-4-3"><a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a>    <span class="n">speaker_wav</span><span class="o">=</span><span class="s2">"voices/nurse.wav"</span><span class="p">,</span>
</span><span id="__span-4-4"><a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a>    <span class="n">out_path</span><span class="o">=</span><span class="s2">"audio/turn_000_nurse.wav"</span><span class="p">,</span>
</span><span id="__span-4-5"><a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a>    <span class="n">language</span><span class="o">=</span><span class="s2">"en"</span><span class="p">,</span>
</span><span id="__span-4-6"><a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a><span class="p">)</span>
</span></code></pre></div>
<p>All arguments are <strong>keyword-only</strong>.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Default</th>
<th>Meaning</th>
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
<td>Reference recording to clone the voice from.</td>
</tr>
<tr>
<td><code>out_path</code></td>
<td><code>str \| Path</code></td>
<td>—</td>
<td>Destination WAV file.</td>
</tr>
<tr>
<td><code>language</code></td>
<td><code>str</code></td>
<td><code>"en"</code></td>
<td>Language code passed to XTTS-v2.</td>
</tr>
</tbody>
</table>
<p>Returns the output <code>Path</code>. Parent directories are created automatically, so you
do not need to <code>mkdir</code> first.</p>
<p>Reference clips should be clean speech of roughly 6–20 seconds. Background
noise in the reference is reproduced in the clone.</p>
<h2 id="rendering-a-full-dialogue">Rendering a full dialogue<a class="headerlink" href="#rendering-a-full-dialogue" title="Permanent link">¶</a></h2>
<p>Walk the artifact's <code>history</code>, giving each speaker its own reference voice:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>
</span><span id="__span-5-2"><a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>
</span><span id="__span-5-3"><a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.audio.renderer</span><span class="w"> </span><span class="kn">import</span> <span class="n">SpeechRenderer</span>
</span><span id="__span-5-4"><a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a>
</span><span id="__span-5-5"><a href="#__codelineno-5-5" id="__codelineno-5-5" name="__codelineno-5-5"></a><span class="n">VOICES</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-5-6"><a href="#__codelineno-5-6" id="__codelineno-5-6" name="__codelineno-5-6"></a>    <span class="s2">"nurse"</span><span class="p">:</span> <span class="s2">"voices/nurse.wav"</span><span class="p">,</span>
</span><span id="__span-5-7"><a href="#__codelineno-5-7" id="__codelineno-5-7" name="__codelineno-5-7"></a>    <span class="s2">"patient"</span><span class="p">:</span> <span class="s2">"voices/patient.wav"</span><span class="p">,</span>
</span><span id="__span-5-8"><a href="#__codelineno-5-8" id="__codelineno-5-8" name="__codelineno-5-8"></a><span class="p">}</span>
</span><span id="__span-5-9"><a href="#__codelineno-5-9" id="__codelineno-5-9" name="__codelineno-5-9"></a>
</span><span id="__span-5-10"><a href="#__codelineno-5-10" id="__codelineno-5-10" name="__codelineno-5-10"></a><span class="n">renderer</span> <span class="o">=</span> <span class="n">SpeechRenderer</span><span class="p">()</span>
</span><span id="__span-5-11"><a href="#__codelineno-5-11" id="__codelineno-5-11" name="__codelineno-5-11"></a><span class="n">out_dir</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="s2">"audio"</span><span class="p">)</span> <span class="o">/</span> <span class="n">artifact</span><span class="p">[</span><span class="s2">"run_id"</span><span class="p">]</span>
</span><span id="__span-5-12"><a href="#__codelineno-5-12" id="__codelineno-5-12" name="__codelineno-5-12"></a>
</span><span id="__span-5-13"><a href="#__codelineno-5-13" id="__codelineno-5-13" name="__codelineno-5-13"></a><span class="n">rendered</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-5-14"><a href="#__codelineno-5-14" id="__codelineno-5-14" name="__codelineno-5-14"></a><span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">entry</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"history"</span><span class="p">]):</span>
</span><span id="__span-5-15"><a href="#__codelineno-5-15" id="__codelineno-5-15" name="__codelineno-5-15"></a>    <span class="n">actor</span> <span class="o">=</span> <span class="n">entry</span><span class="p">[</span><span class="s2">"actor"</span><span class="p">]</span>
</span><span id="__span-5-16"><a href="#__codelineno-5-16" id="__codelineno-5-16" name="__codelineno-5-16"></a>    <span class="k">if</span> <span class="n">actor</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">VOICES</span><span class="p">:</span>
</span><span id="__span-5-17"><a href="#__codelineno-5-17" id="__codelineno-5-17" name="__codelineno-5-17"></a>        <span class="k">continue</span>  <span class="c1"># skip system events: released vitals, triage_end</span>
</span><span id="__span-5-18"><a href="#__codelineno-5-18" id="__codelineno-5-18" name="__codelineno-5-18"></a>
</span><span id="__span-5-19"><a href="#__codelineno-5-19" id="__codelineno-5-19" name="__codelineno-5-19"></a>    <span class="n">rendered</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-5-20"><a href="#__codelineno-5-20" id="__codelineno-5-20" name="__codelineno-5-20"></a>        <span class="n">renderer</span><span class="o">.</span><span class="n">render</span><span class="p">(</span>
</span><span id="__span-5-21"><a href="#__codelineno-5-21" id="__codelineno-5-21" name="__codelineno-5-21"></a>            <span class="n">text</span><span class="o">=</span><span class="n">entry</span><span class="p">[</span><span class="s2">"utterance"</span><span class="p">],</span>
</span><span id="__span-5-22"><a href="#__codelineno-5-22" id="__codelineno-5-22" name="__codelineno-5-22"></a>            <span class="n">speaker_wav</span><span class="o">=</span><span class="n">VOICES</span><span class="p">[</span><span class="n">actor</span><span class="p">],</span>
</span><span id="__span-5-23"><a href="#__codelineno-5-23" id="__codelineno-5-23" name="__codelineno-5-23"></a>            <span class="n">out_path</span><span class="o">=</span><span class="n">out_dir</span> <span class="o">/</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">i</span><span class="si">:</span><span class="s2">03d</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">actor</span><span class="si">}</span><span class="s2">.wav"</span><span class="p">,</span>
</span><span id="__span-5-24"><a href="#__codelineno-5-24" id="__codelineno-5-24" name="__codelineno-5-24"></a>            <span class="n">language</span><span class="o">=</span><span class="s2">"en"</span><span class="p">,</span>
</span><span id="__span-5-25"><a href="#__codelineno-5-25" id="__codelineno-5-25" name="__codelineno-5-25"></a>        <span class="p">)</span>
</span><span id="__span-5-26"><a href="#__codelineno-5-26" id="__codelineno-5-26" name="__codelineno-5-26"></a>    <span class="p">)</span>
</span><span id="__span-5-27"><a href="#__codelineno-5-27" id="__codelineno-5-27" name="__codelineno-5-27"></a>
</span><span id="__span-5-28"><a href="#__codelineno-5-28" id="__codelineno-5-28" name="__codelineno-5-28"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"rendered </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">rendered</span><span class="p">)</span><span class="si">}</span><span class="s2"> utterances to </span><span class="si">{</span><span class="n">out_dir</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span></code></pre></div>
<p>Skipping entries whose <code>actor</code> is not in <code>VOICES</code> filters out system events —
released vitals and the <code>triage_end</code> marker have no <code>utterance</code> key and would
raise <code>KeyError</code>.</p>
<p>Numbering files by their index in <code>history</code> preserves turn order, which matters
when concatenating them into a single conversation.</p>
<h3 id="varying-voices-across-runs">Varying voices across runs<a class="headerlink" href="#varying-voices-across-runs" title="Permanent link">¶</a></h3>
<p>Persona attributes such as <code>gender</code> and <code>ethnicity</code> are a natural key into a
library of reference clips:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="k">def</span><span class="w"> </span><span class="nf">voice_for</span><span class="p">(</span><span class="n">persona</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a>    <span class="k">return</span> <span class="sa">f</span><span class="s2">"voices/</span><span class="si">{</span><span class="n">persona</span><span class="o">.</span><span class="n">gender</span><span class="si">}</span><span class="s2">_</span><span class="si">{</span><span class="n">persona</span><span class="o">.</span><span class="n">ethnicity</span><span class="si">}</span><span class="s2">.wav"</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">" "</span><span class="p">,</span> <span class="s2">"_"</span><span class="p">)</span>
</span></code></pre></div>
<p>This keeps the acoustic identity consistent with the persona that generated the
text, which is the point of persona-conditioned generation in the first place.</p>
<h2 id="preparing-text-for-synthesis">Preparing text for synthesis<a class="headerlink" href="#preparing-text-for-synthesis" title="Permanent link">¶</a></h2>
<p><code>triagesim.utils.text_control</code> provides <code>enforce_response_budget(text,
response_length)</code>, which trims an utterance to a target length band. It is a
text-shaping helper rather than an audio one, but it is useful before synthesis
when you need utterance durations to stay within a budget.</p>
<h2 id="licensing-and-consent">Licensing and consent<a class="headerlink" href="#licensing-and-consent" title="Permanent link">¶</a></h2>
<div class="admonition danger">
<p class="admonition-title">Review the model licence and obtain voice consent</p>
<p>XTTS-v2 is distributed under the Coqui Public Model License, which carries
its own restrictions — including on commercial use. TriageSim's Apache-2.0
licence does not extend to it. Review the model's terms before using
synthesised output in a publication or product.</p>
<p>Voice cloning also raises consent questions independent of licensing. Use
reference recordings only where the speaker has agreed to voice cloning for
this purpose, prefer clips from datasets released for synthesis research,
and never clone a real clinician's or patient's voice without explicit
permission.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Synthetic data stays synthetic</p>
<p>Rendered dialogues are generated artefacts, not recordings of real
encounters. Label them as such in any dataset you release so downstream
users cannot mistake them for clinical recordings.</p>
</div>
