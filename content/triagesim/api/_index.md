---
title: "API reference"
type: "docsite"
docSite: "triagesim"
---

<h1 id="api-reference">API reference<a class="headerlink" href="#api-reference" title="Permanent link">¶</a></h1>
<p>These pages are generated directly from the docstrings and type annotations in
the installed <code>triagesim</code> package, so they always reflect the released version
rather than a hand-maintained copy.</p>
<p>For task-oriented explanation, start with the <a href="/triagesim/guide/concepts/">User guide</a>.</p>
<h2 id="public-surface">Public surface<a class="headerlink" href="#public-surface" title="Permanent link">¶</a></h2>
<table>
<thead>
<tr>
<th>Module</th>
<th>Exports</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/triagesim/api/runner/"><code>triagesim</code></a></td>
<td><code>TriageRunner</code>, <code>RunnerConfig</code>, <code>__version__</code></td>
</tr>
<tr>
<td><a href="/triagesim/api/agents/"><code>triagesim.agents</code></a></td>
<td><code>BaseLLM</code>, <code>OpenRouterLLM</code>, <code>NurseAgent</code>, <code>PatientAgent</code></td>
</tr>
<tr>
<td><a href="/triagesim/api/core/"><code>triagesim.core</code></a></td>
<td><code>BaseAgentOutput</code>, <code>NurseOutput</code>, <code>PatientOutput</code></td>
</tr>
<tr>
<td><a href="/triagesim/api/personas/"><code>triagesim.personas</code></a></td>
<td><code>PatientPersona</code>, <code>NursePersona</code>, loaders, samplers, filters</td>
</tr>
<tr>
<td><a href="/triagesim/api/utils/"><code>triagesim.utils</code></a></td>
<td><code>compute_all_metrics</code> and the individual metric functions</td>
</tr>
<tr>
<td><a href="/triagesim/api/audio/"><code>triagesim.audio</code></a></td>
<td><code>SpeechRenderer</code> (requires the <code>audio</code> extra)</td>
</tr>
</tbody>
</table>
<h2 id="import-conventions">Import conventions<a class="headerlink" href="#import-conventions" title="Permanent link">¶</a></h2>
<p>The three most-used symbols come straight off the top-level package:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">TriageRunner</span><span class="p">,</span> <span class="n">RunnerConfig</span><span class="p">,</span> <span class="n">__version__</span>
</span></code></pre></div>
<p>Everything else lives in a subpackage:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenRouterLLM</span><span class="p">,</span> <span class="n">NurseAgent</span><span class="p">,</span> <span class="n">PatientAgent</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="n">load_patient_personas</span><span class="p">,</span> <span class="n">sample_patient_personas</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span></code></pre></div>
<div class="admonition note">
<p class="admonition-title">One exception</p>
<p><code>SpeechRenderer</code> is <strong>not</strong> re-exported from <code>triagesim.audio</code>. Import it
from the module directly:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.audio.renderer</span><span class="w"> </span><span class="kn">import</span> <span class="n">SpeechRenderer</span>
</span></code></pre></div>
</div>
<h2 id="internal-modules">Internal modules<a class="headerlink" href="#internal-modules" title="Permanent link">¶</a></h2>
<p><code>triagesim.core</code> contains more than it exports — <code>environment</code>, <code>belief_graph</code>,
<code>belief_updater</code>, <code>state_store</code>, <code>actions</code>, <code>action_mapper</code>, <code>vitals</code>, and
<code>llm_detectors</code>. These are documented in the <a href="/triagesim/guide/concepts/">User guide</a>
where they help explain behaviour, but they are not part of the public API and
may change between releases without notice.</p>
<p>The one you are most likely to reach for deliberately is <code>RedisStateStore</code>, when
you need a non-default Redis host or port:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core.state_store</span><span class="w"> </span><span class="kn">import</span> <span class="n">RedisStateStore</span>
</span></code></pre></div>
<h2 id="type-checking">Type checking<a class="headerlink" href="#type-checking" title="Permanent link">¶</a></h2>
<p>The package ships a <code>py.typed</code> marker, so <code>mypy</code> and <code>pyright</code> resolve its
annotations without additional stubs.</p>
