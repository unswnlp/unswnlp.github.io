---
title: "Configuration"
---

<h1 id="configuration">Configuration<a class="headerlink" href="#configuration" title="Permanent link">¶</a></h1>
<h2 id="api-key">API key<a class="headerlink" href="#api-key" title="Permanent link">¶</a></h2>
<p>Both agents reach a model through <a href="https://openrouter.ai/">OpenRouter</a>, so
TriageSim needs an API key before any simulation will run. It is read once, at
import time, from the <code>OPENROUTER_API_KEY</code> environment variable.</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels"><label for="__tabbed_1_1">Environment variable</label><label for="__tabbed_1_2">.env file</label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nb">export</span><span class="w"> </span><span class="nv">OPENROUTER_API_KEY</span><span class="o">=</span>sk-or-...
</span></code></pre></div>
</div>
<div class="tabbed-block">
<p>Create a <code>.env</code> file at your project root:</p>
<div class="language-ini highlight"><span class="filename">.env</span><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="na">OPENROUTER_API_KEY</span><span class="o">=</span><span class="s">sk-or-...</span>
</span></code></pre></div>
<p>TriageSim calls <code>python-dotenv</code>'s <code>find_dotenv(usecwd=True)</code> on import, so
the file is discovered by searching upward from the current working
directory.</p>
</div>
</div>
</input></input></div>
<div class="admonition danger">
<p class="admonition-title">Do not commit your key</p>
<p>Add <code>.env</code> to your <code>.gitignore</code>. An OpenRouter key is a billing credential.</p>
</div>
<p>Because the key is resolved when <code>triagesim.config</code> is first imported, setting
<code>os.environ</code> <em>after</em> importing the package has no effect. Set it before your
first import, or use a <code>.env</code> file.</p>
<h2 id="choosing-a-model">Choosing a model<a class="headerlink" href="#choosing-a-model" title="Permanent link">¶</a></h2>
<p>Any OpenRouter model identifier works. The model is supplied per LLM backend,
which means the nurse and the patient can run on different models:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenRouterLLM</span>
</span><span id="__span-2-2"><a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span><span id="__span-2-3"><a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a>
</span><span id="__span-2-4"><a href="#__codelineno-2-4" id="__codelineno-2-4" name="__codelineno-2-4"></a><span class="n">nurse_llm</span> <span class="o">=</span> <span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="s2">"anthropic/claude-sonnet-4-5"</span><span class="p">,</span>
</span><span id="__span-2-5"><a href="#__codelineno-2-5" id="__codelineno-2-5" name="__codelineno-2-5"></a>                          <span class="n">output_type</span><span class="o">=</span><span class="n">NurseOutput</span><span class="p">)</span>
</span><span id="__span-2-6"><a href="#__codelineno-2-6" id="__codelineno-2-6" name="__codelineno-2-6"></a><span class="n">patient_llm</span> <span class="o">=</span> <span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="s2">"google/gemini-3-pro-preview"</span><span class="p">,</span>
</span><span id="__span-2-7"><a href="#__codelineno-2-7" id="__codelineno-2-7" name="__codelineno-2-7"></a>                            <span class="n">output_type</span><span class="o">=</span><span class="n">PatientOutput</span><span class="p">)</span>
</span></code></pre></div>
<p>Each backend is bound to exactly one output schema, so a nurse backend cannot
be handed to a patient agent. This is deliberate: it makes an invalid pairing a
construction-time error rather than a parsing failure mid-run.</p>
<p>Structured output is enforced by <code>pydantic-ai</code>, so the model must support
tool-calling or JSON mode. Models that only emit free text will fail
validation.</p>
<h2 id="feature-flags">Feature flags<a class="headerlink" href="#feature-flags" title="Permanent link">¶</a></h2>
<p>Two settings live in <code>triagesim.config</code>:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Default</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>OPENROUTER_API_KEY</code></td>
<td>from environment</td>
<td>Credential used by <code>OpenRouterLLM</code>.</td>
</tr>
<tr>
<td><code>ENABLE_LLM_DETECTORS</code></td>
<td><code>False</code></td>
<td>Enables LLM fallback when the rule-based detectors cannot identify a requested vital or a belief update from the nurse's text.</td>
</tr>
</tbody>
</table>
<p>By default TriageSim extracts requested vitals with keyword rules — <code>"pulse"</code>
and <code>"heart rate"</code> both map to <code>heartrate</code>, <code>"bp"</code> to <code>sbp</code>, and so on. Turning
on <code>ENABLE_LLM_DETECTORS</code> adds a model call whenever those rules find nothing,
which is more robust but slower and more expensive.</p>
<p>A separate, per-run flag controls LLM-backed belief updates:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnerConfig</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a><span class="n">config</span> <span class="o">=</span> <span class="n">RunnerConfig</span><span class="p">(</span><span class="n">enable_llm</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span></code></pre></div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code>RunnerConfig.enable_llm</code> defaults to <code>False</code>. The dialogue itself is always
model-driven; this flag only governs whether the <em>belief updater</em> may call a
model in addition to its deterministic rules.</p>
</div>
<h2 id="reproducibility">Reproducibility<a class="headerlink" href="#reproducibility" title="Permanent link">¶</a></h2>
<p>Pass a <code>seed</code> to <code>RunnerConfig</code> to seed Python's global RNG for the run, and to
<code>sample_patient_personas</code> / <code>sample_nurse_personas</code> to fix persona selection:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="n">config</span> <span class="o">=</span> <span class="n">RunnerConfig</span><span class="p">(</span><span class="n">max_turns</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</span></code></pre></div>
<p>This makes persona sampling and any internal random choices deterministic. It
does <strong>not</strong> make the language model deterministic — remote sampling is outside
TriageSim's control, so repeated runs with the same seed will still differ in
wording.</p>
