---
title: "Agents and LLM backends"
type: "docsite"
docSite: "triagesim"
---

<h1 id="agents-and-llm-backends">Agents and LLM backends<a class="headerlink" href="#agents-and-llm-backends" title="Permanent link">¶</a></h1>
<p>TriageSim separates <em>who is speaking</em> (the agent, which owns a persona and a
prompt) from <em>what generates the text</em> (the LLM backend). This page covers both
layers and the schemas that connect them.</p>
<h2 id="the-two-layer-design">The two-layer design<a class="headerlink" href="#the-two-layer-design" title="Permanent link">¶</a></h2>
<pre class="mermaid"><code>flowchart LR
    P[Persona] --&gt; A[NurseAgent / PatientAgent]
    H[Transcript] --&gt; A
    A --&gt;|prompt| B[BaseLLM]
    B --&gt;|validated Pydantic model| A
    A --&gt;|NurseOutput / PatientOutput| E[TriageEnv]</code></pre>
<p>An agent builds a prompt from its persona, the transcript, and the triage
protocol. The backend turns that prompt into a <strong>schema-validated object</strong> — not
a string. Nothing downstream ever parses free text.</p>
<h2 id="output-schemas">Output schemas<a class="headerlink" href="#output-schemas" title="Permanent link">¶</a></h2>
<p>Both schemas inherit from <code>BaseAgentOutput</code>, which forbids extra fields. If the
model invents a key, validation fails rather than the key being quietly
accepted — the comment in the source calls this out as critical, and it is the
main defence against a model smuggling unsanctioned state into the run.</p>
<h3 id="patientoutput"><code>PatientOutput</code><a class="headerlink" href="#patientoutput" title="Permanent link">¶</a></h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>utterance</code></td>
<td><code>str</code></td>
<td>What the patient says this turn.</td>
</tr>
</tbody>
</table>
<p>The patient has exactly one thing it can do: speak.</p>
<h3 id="nurseoutput"><code>NurseOutput</code><a class="headerlink" href="#nurseoutput" title="Permanent link">¶</a></h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>action</code></td>
<td><code>"utterance" \| "check_vital" \| "log_red_flag" \| "end"</code></td>
<td>The next action the nurse chooses.</td>
</tr>
<tr>
<td><code>utterance</code></td>
<td><code>str \| None</code></td>
<td>The nurse's line, or the request naming a vital. Null for <code>end</code> and <code>log_red_flag</code>.</td>
</tr>
<tr>
<td><code>triage</code></td>
<td><code>int</code>, 1–5</td>
<td>Current predicted triage level. Required on <strong>every</strong> output, not just at the end.</td>
</tr>
<tr>
<td><code>confidence</code></td>
<td><code>"low" \| "medium" \| "high"</code></td>
<td>Confidence in that triage level.</td>
</tr>
<tr>
<td><code>red_flags</code></td>
<td><code>list[str]</code></td>
<td>All red flags identified so far. Defaults to empty.</td>
</tr>
<tr>
<td><code>explanation</code></td>
<td><code>str</code></td>
<td>Clinical reasoning grounded in the selected triage algorithm.</td>
</tr>
</tbody>
</table>
<p>Because <code>triage</code>, <code>confidence</code> and <code>explanation</code> are emitted at every step, the
<a href="/triagesim/guide/artifacts/">trace</a> records how the decision evolved — including the
turn at which the nurse first arrived at the correct level.</p>
<div class="admonition note">
<p class="admonition-title"><code>utterance</code> carries the vital request</p>
<p>There is no separate "which vital" field. For a <code>check_vital</code> action, the
environment infers the vital from the wording of <code>utterance</code> — so
<code>"Let me take your blood pressure"</code> resolves to <code>sbp</code>. See
<a href="/triagesim/guide/concepts/">Vitals</a>.</p>
</div>
<h2 id="basellm"><code>BaseLLM</code><a class="headerlink" href="#basellm" title="Permanent link">¶</a></h2>
<p>The backend interface is a single abstract method:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">abc</span><span class="w"> </span><span class="kn">import</span> <span class="n">ABC</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">List</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="k">class</span><span class="w"> </span><span class="nc">BaseLLM</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="k">def</span><span class="w"> </span><span class="nf">generate</span><span class="p">(</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>        <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a>        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-0-8"><a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a>        <span class="n">max_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-9"><a href="#__codelineno-0-9" id="__codelineno-0-9" name="__codelineno-0-9"></a>        <span class="n">stop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-10"><a href="#__codelineno-0-10" id="__codelineno-0-10" name="__codelineno-0-10"></a>        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
</span><span id="__span-0-11"><a href="#__codelineno-0-11" id="__codelineno-0-11" name="__codelineno-0-11"></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseAgentOutput</span><span class="p">]:</span>
</span><span id="__span-0-12"><a href="#__codelineno-0-12" id="__codelineno-0-12" name="__codelineno-0-12"></a>        <span class="o">...</span>
</span></code></pre></div>
<p>Anything implementing <code>generate</code> can drive an agent.</p>
<h2 id="openrouterllm"><code>OpenRouterLLM</code><a class="headerlink" href="#openrouterllm" title="Permanent link">¶</a></h2>
<p>The bundled backend routes through <a href="https://openrouter.ai/">OpenRouter</a> using
<code>pydantic-ai</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenRouterLLM</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="n">nurse_llm</span> <span class="o">=</span> <span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="s2">"anthropic/claude-sonnet-4-5"</span><span class="p">,</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a>                          <span class="n">output_type</span><span class="o">=</span><span class="n">NurseOutput</span><span class="p">)</span>
</span><span id="__span-1-6"><a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a><span class="n">patient_llm</span> <span class="o">=</span> <span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="s2">"google/gemini-3-pro-preview"</span><span class="p">,</span>
</span><span id="__span-1-7"><a href="#__codelineno-1-7" id="__codelineno-1-7" name="__codelineno-1-7"></a>                            <span class="n">output_type</span><span class="o">=</span><span class="n">PatientOutput</span><span class="p">)</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>model_name</code></td>
<td><code>str</code></td>
<td>OpenRouter model identifier.</td>
</tr>
<tr>
<td><code>output_type</code></td>
<td><code>type[BaseAgentOutput]</code></td>
<td>Pydantic model the agent is forced to produce.</td>
</tr>
<tr>
<td><code>**agent_kwargs</code></td>
<td></td>
<td>Forwarded to the underlying <code>pydantic_ai.Agent</code>.</td>
</tr>
</tbody>
</table>
<p>The API key is read from <code>triagesim.config.OPENROUTER_API_KEY</code>, not passed in.
See <a href="/triagesim/getting-started/configuration/">Configuration</a>.</p>
<p><strong>One backend per agent.</strong> The output schema is bound at construction, so a
nurse backend physically cannot serve a patient agent. This turns a whole class
of wiring mistakes into an obvious two-line setup instead of a confusing
validation error twenty turns into a run.</p>
<div class="admonition warning">
<p class="admonition-title">Structured output is required</p>
<p><code>OpenRouterLLM</code> requests a low reasoning effort and constrains generation to
the given schema. Models without tool-calling or JSON-mode support will fail
validation. Check the model's OpenRouter listing before using it.</p>
</div>
<h2 id="patientagent"><code>PatientAgent</code><a class="headerlink" href="#patientagent" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">PatientAgent</span>
</span><span id="__span-2-2"><a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a>
</span><span id="__span-2-3"><a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a><span class="n">patient</span> <span class="o">=</span> <span class="n">PatientAgent</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">patient_llm</span><span class="p">,</span> <span class="n">persona</span><span class="o">=</span><span class="n">patient_persona</span><span class="p">)</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>llm</code></td>
<td><code>BaseLLM</code> bound to <code>PatientOutput</code></td>
</tr>
<tr>
<td><code>persona</code></td>
<td><code>PatientPersona</code></td>
</tr>
</tbody>
</table>
<p>Its single method is:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">output</span> <span class="o">=</span> <span class="n">patient</span><span class="o">.</span><span class="n">act</span><span class="p">(</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>    <span class="n">history</span><span class="o">=</span><span class="s2">"Nurse: What brings you in today?"</span><span class="p">,</span>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a>    <span class="n">chief_complaint</span><span class="o">=</span><span class="s2">"Syncope"</span><span class="p">,</span>
</span><span id="__span-3-4"><a href="#__codelineno-3-4" id="__codelineno-3-4" name="__codelineno-3-4"></a>    <span class="n">pain</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
</span><span id="__span-3-5"><a href="#__codelineno-3-5" id="__codelineno-3-5" name="__codelineno-3-5"></a><span class="p">)</span>
</span><span id="__span-3-6"><a href="#__codelineno-3-6" id="__codelineno-3-6" name="__codelineno-3-6"></a><span class="nb">print</span><span class="p">(</span><span class="n">output</span><span class="o">.</span><span class="n">utterance</span><span class="p">)</span>
</span></code></pre></div>
<p>The patient sees only the transcript, its chief complaint, and its pain score.
It never sees vitals or the true acuity — it can only report what a person in
that situation would plausibly know and choose to say.</p>
<h2 id="nurseagent"><code>NurseAgent</code><a class="headerlink" href="#nurseagent" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseAgent</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>
</span><span id="__span-4-3"><a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a><span class="n">nurse</span> <span class="o">=</span> <span class="n">NurseAgent</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">nurse_llm</span><span class="p">,</span> <span class="n">persona</span><span class="o">=</span><span class="n">nurse_persona</span><span class="p">,</span> <span class="n">algorithm</span><span class="o">=</span><span class="s2">"esi"</span><span class="p">)</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>llm</code></td>
<td><code>BaseLLM</code> bound to <code>NurseOutput</code></td>
<td>Generation backend.</td>
</tr>
<tr>
<td><code>persona</code></td>
<td><code>NursePersona</code></td>
<td>Conditioning traits.</td>
</tr>
<tr>
<td><code>algorithm</code></td>
<td><code>str</code></td>
<td><code>"esi"</code> or <code>"ats"</code>. Selects the protocol text embedded in the prompt.</td>
</tr>
</tbody>
</table>
<h3 id="act"><code>act</code><a class="headerlink" href="#act" title="Permanent link">¶</a></h3>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="n">output</span> <span class="o">=</span> <span class="n">nurse</span><span class="o">.</span><span class="n">act</span><span class="p">(</span><span class="n">history</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">known_vitals</span><span class="o">=</span><span class="p">{</span><span class="s2">"heartrate"</span><span class="p">,</span> <span class="s2">"o2sat"</span><span class="p">})</span>
</span></code></pre></div>
<p><code>known_vitals</code> is the set of vitals already released. The agent uses it to build
the list of actions still available, so the nurse is not offered a vital it has
already seen.</p>
<h3 id="infer_belief_updates"><code>infer_belief_updates</code><a class="headerlink" href="#infer_belief_updates" title="Permanent link">¶</a></h3>
<p>After each patient utterance the runner asks the nurse to extract structured
belief updates from what was just said:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="n">updates</span> <span class="o">=</span> <span class="n">nurse</span><span class="o">.</span><span class="n">infer_belief_updates</span><span class="p">(</span>
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a>    <span class="n">history</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span>
</span><span id="__span-6-3"><a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>    <span class="n">last_utterance</span><span class="o">=</span><span class="s2">"I went dizzy and the next thing I knew I was on the floor."</span><span class="p">,</span>
</span><span id="__span-6-4"><a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a>    <span class="n">turn</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
</span><span id="__span-6-5"><a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a><span class="p">)</span>
</span></code></pre></div>
<p>These are merged into the environment's belief graph. This is a <em>separate</em> call
from <code>act</code> — reasoning about what was learned is deliberately not entangled with
deciding what to do next.</p>
<h2 id="custom-backends">Custom backends<a class="headerlink" href="#custom-backends" title="Permanent link">¶</a></h2>
<p>To use a provider other than OpenRouter, subclass <code>BaseLLM</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-7-1"><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">List</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span>
</span><span id="__span-7-2"><a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>
</span><span id="__span-7-3"><a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseLLM</span>
</span><span id="__span-7-4"><a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseAgentOutput</span><span class="p">,</span> <span class="n">NurseOutput</span>
</span><span id="__span-7-5"><a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a>
</span><span id="__span-7-6"><a href="#__codelineno-7-6" id="__codelineno-7-6" name="__codelineno-7-6"></a>
</span><span id="__span-7-7"><a href="#__codelineno-7-7" id="__codelineno-7-7" name="__codelineno-7-7"></a><span class="k">class</span><span class="w"> </span><span class="nc">MyLLM</span><span class="p">(</span><span class="n">BaseLLM</span><span class="p">):</span>
</span><span id="__span-7-8"><a href="#__codelineno-7-8" id="__codelineno-7-8" name="__codelineno-7-8"></a>    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">output_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">BaseAgentOutput</span><span class="p">]):</span>
</span><span id="__span-7-9"><a href="#__codelineno-7-9" id="__codelineno-7-9" name="__codelineno-7-9"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_type</span> <span class="o">=</span> <span class="n">output_type</span>
</span><span id="__span-7-10"><a href="#__codelineno-7-10" id="__codelineno-7-10" name="__codelineno-7-10"></a>
</span><span id="__span-7-11"><a href="#__codelineno-7-11" id="__codelineno-7-11" name="__codelineno-7-11"></a>    <span class="k">def</span><span class="w"> </span><span class="nf">generate</span><span class="p">(</span>
</span><span id="__span-7-12"><a href="#__codelineno-7-12" id="__codelineno-7-12" name="__codelineno-7-12"></a>        <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-7-13"><a href="#__codelineno-7-13" id="__codelineno-7-13" name="__codelineno-7-13"></a>        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-7-14"><a href="#__codelineno-7-14" id="__codelineno-7-14" name="__codelineno-7-14"></a>        <span class="n">max_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-7-15"><a href="#__codelineno-7-15" id="__codelineno-7-15" name="__codelineno-7-15"></a>        <span class="n">stop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-7-16"><a href="#__codelineno-7-16" id="__codelineno-7-16" name="__codelineno-7-16"></a>        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
</span><span id="__span-7-17"><a href="#__codelineno-7-17" id="__codelineno-7-17" name="__codelineno-7-17"></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseAgentOutput</span><span class="p">]:</span>
</span><span id="__span-7-18"><a href="#__codelineno-7-18" id="__codelineno-7-18" name="__codelineno-7-18"></a>        <span class="n">raw</span> <span class="o">=</span> <span class="n">my_provider_call</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">max_tokens</span><span class="o">=</span><span class="n">max_tokens</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="n">stop</span><span class="p">)</span>
</span><span id="__span-7-19"><a href="#__codelineno-7-19" id="__codelineno-7-19" name="__codelineno-7-19"></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_type</span><span class="o">.</span><span class="n">model_validate_json</span><span class="p">(</span><span class="n">raw</span><span class="p">)</span>
</span><span id="__span-7-20"><a href="#__codelineno-7-20" id="__codelineno-7-20" name="__codelineno-7-20"></a>
</span><span id="__span-7-21"><a href="#__codelineno-7-21" id="__codelineno-7-21" name="__codelineno-7-21"></a>
</span><span id="__span-7-22"><a href="#__codelineno-7-22" id="__codelineno-7-22" name="__codelineno-7-22"></a><span class="n">nurse_llm</span> <span class="o">=</span> <span class="n">MyLLM</span><span class="p">(</span><span class="n">output_type</span><span class="o">=</span><span class="n">NurseOutput</span><span class="p">)</span>
</span></code></pre></div>
<p>Two requirements:</p>
<ol>
<li><code>generate</code> must return an <strong>instance of the bound output type</strong>, not a
   string, or the environment will reject it with a <code>TypeError</code>.</li>
<li>Your provider must be able to honour the schema. Prompting for JSON and
   validating with <code>model_validate_json</code> works, but budget for retries — an
   unconstrained model will occasionally emit prose.</li>
</ol>
<p>Next: <a href="/triagesim/guide/runner/">Running a simulation</a>.</p>
