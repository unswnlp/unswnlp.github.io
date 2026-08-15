---
title: "Core concepts"
---

<h1 id="core-concepts">Core concepts<a class="headerlink" href="#core-concepts" title="Permanent link">¶</a></h1>
<p>A TriageSim run is a small, auditable simulation loop. This page explains the
pieces and how control flows between them, which makes the rest of the
documentation much easier to read.</p>
<h2 id="the-hidden-ground-truth">The hidden ground truth<a class="headerlink" href="#the-hidden-ground-truth" title="Permanent link">¶</a></h2>
<p>Every run starts from a structured clinical vignette:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="n">ground_truth</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="s2">"chiefcomplaint"</span><span class="p">:</span> <span class="s2">"Syncope"</span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="s2">"vitals"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">99.1</span><span class="p">,</span> <span class="s2">"heartrate"</span><span class="p">:</span> <span class="mi">112</span><span class="p">,</span> <span class="s2">"resprate"</span><span class="p">:</span> <span class="mi">26</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>               <span class="s2">"o2sat"</span><span class="p">:</span> <span class="mi">91</span><span class="p">,</span> <span class="s2">"sbp"</span><span class="p">:</span> <span class="mi">98</span><span class="p">},</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="s2">"acuity"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="s2">"pain"</span><span class="p">:</span> <span class="mi">7</span><span class="p">,</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a><span class="p">}</span>
</span></code></pre></div>
<p>Neither agent receives this dictionary. The patient agent is given only
<code>chiefcomplaint</code> and <code>pain</code>, and must express them in character. The nurse
agent is given nothing at all — it starts from an empty transcript.</p>
<p>Vitals are <strong>released by the environment</strong>, not spoken by the patient: when the
nurse takes a <code>check_vital</code> action, the environment reads the true value out of
<code>ground_truth["vitals"]</code> and appends it to the transcript as a system event.
<code>acuity</code> is never released; it exists purely so the run can be scored
afterwards.</p>
<p>This separation is what makes the data useful. The dialogue is generated, but
the label it should have produced is known exactly.</p>
<h2 id="the-environment">The environment<a class="headerlink" href="#the-environment" title="Permanent link">¶</a></h2>
<p><code>TriageEnv</code> (in <code>triagesim.core.environment</code>) is the single source of truth. It
owns the belief graph, applies nurse actions, releases vitals, tracks red flags,
and persists everything through a <code>StateStore</code>. Its three methods are
<code>reset(ground_truth) -&gt; run_id</code>, <code>observe(run_id)</code>, and
<code>step(run_id, actor, action)</code>.</p>
<p><code>TriageRunner</code> deliberately contains <strong>no clinical logic</strong>. It only decides
whose turn it is. Everything that could affect a triage outcome lives in the
environment, where it is schema-validated and recorded.</p>
<h2 id="structured-actions-not-free-text">Structured actions, not free text<a class="headerlink" href="#structured-actions-not-free-text" title="Permanent link">¶</a></h2>
<p>The nurse model does not act directly. It emits a <code>NurseOutput</code> — a Pydantic
model — which <code>map_nurse_output_to_action</code> converts into exactly one executable
action:</p>
<table>
<thead>
<tr>
<th>Nurse action</th>
<th>Executable action</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>utterance</code></td>
<td><code>NurseUtteranceAction</code></td>
<td>Appends the nurse's line to the transcript and hands control to the patient.</td>
</tr>
<tr>
<td><code>check_vital</code></td>
<td><code>NurseCheckVitalAction</code></td>
<td>Releases one vital from the ground truth as a system event.</td>
</tr>
<tr>
<td><code>log_red_flag</code></td>
<td><code>NurseLogRedFlagAction</code></td>
<td>Records clinical red flags.</td>
</tr>
<tr>
<td><code>end</code></td>
<td><code>NurseEndAction</code></td>
<td>Terminates the run with a final triage level.</td>
</tr>
</tbody>
</table>
<p>Invalid combinations are rejected rather than guessed at: an <code>utterance</code> with
no text, or a <code>log_red_flag</code> with no flags, raises <code>ActionMappingError</code>. This
mapping layer is what prevents a model from taking an action the environment
never sanctioned.</p>
<div class="admonition note">
<p class="admonition-title">Why an intermediate representation</p>
<p><code>NurseOutput</code> is what the <em>model</em> is good at producing; the action classes
are what the <em>environment</em> can safely execute. Keeping them separate means a
malformed generation fails loudly at the boundary instead of corrupting the
run state.</p>
</div>
<h2 id="vitals">Vitals<a class="headerlink" href="#vitals" title="Permanent link">¶</a></h2>
<p>Only five vitals exist, defined as <code>ALLOWED_VITALS</code>:</p>
<p><code>temperature</code>, <code>heartrate</code>, <code>resprate</code>, <code>o2sat</code>, <code>sbp</code></p>
<p>Which one the nurse asked for is inferred from its utterance by keyword
matching — <code>"pulse"</code> and <code>"heart rate"</code> both resolve to <code>heartrate</code>, <code>"bp"</code> and
<code>"blood pressure"</code> to <code>sbp</code>, <code>"oxygen"</code> and <code>"saturation"</code> to <code>o2sat</code>, and so
on. If several are mentioned, the <strong>first</strong> match wins; if none match, the
vital resolves to <code>None</code>.</p>
<p>Setting <code>ENABLE_LLM_DETECTORS = True</code> in <code>triagesim.config</code> adds a model-based
fallback when the keyword rules find nothing. See
<a href="/triagesim/getting-started/configuration/">Configuration</a>.</p>
<h2 id="the-belief-graph">The belief graph<a class="headerlink" href="#the-belief-graph" title="Permanent link">¶</a></h2>
<p><code>BeliefGraph</code> is the environment's record of what the nurse has actually
learned. It is provenance-aware: each slot value carries the turn it was
acquired on, whether it came from the patient, the nurse or a system vital, and
whether it was <code>explicit</code>, <code>inferred</code>, or <code>suspected</code>.</p>
<p>Updates are merged deterministically even though extraction is probabilistic:
<code>None</code> values are dropped, exact <code>(slot, value)</code> duplicates are ignored, and
genuinely different values for the same slot are both kept so ambiguity
survives rather than being silently resolved.</p>
<p>Two things are tracked as special sets: <code>vitals_known</code> (which vitals have been
released) and <code>red_flags_logged</code> (flags the nurse explicitly logged).</p>
<p><code>to_observation()</code> flattens the graph into the lossy, provenance-free view that
agents and metrics consume — this is what appears under the <code>belief</code> key of a
run artifact.</p>
<h2 id="turn-structure">Turn structure<a class="headerlink" href="#turn-structure" title="Permanent link">¶</a></h2>
<p>The loop is asymmetric, and this catches people out:</p>
<p><strong>The nurse may act several times before the patient responds.</strong> Checking a
vital or logging a red flag is a <em>micro-turn</em> — it does not advance the turn
counter or hand over control. Only a nurse <code>utterance</code> does that.</p>
<div class="language-text highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a>turn 0  nurse: check_vital  -&gt; system releases heartrate = 112   (micro-turn)
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a>turn 0  nurse: log_red_flag -&gt; "tachycardia" recorded            (micro-turn)
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a>turn 0  nurse: utterance    -&gt; "Did you hit your head?"          (yields)
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a>turn 0  patient: utterance  -&gt; "No, my partner caught me."       (turn -&gt; 1)
</span></code></pre></div>
<p>The turn counter advances <strong>only on a patient action</strong>, so <code>max_turns</code> counts
patient responses, not model calls. After each patient utterance the nurse
infers belief updates from what was said, and the environment merges them.</p>
<p>A run ends when the turn counter reaches <code>max_turns</code>, or when the nurse takes
the <code>end</code> action. A hard safety cap of <code>max_turns * 4</code> total steps guarantees
termination even if an agent misbehaves.</p>
<p>Red-flag logging is deduplicated: flags are normalised to lowercase,
whitespace-collapsed strings, repeats within a turn and across earlier turns are
discarded, and at most five new flags are accepted per turn.</p>
<h2 id="triage-algorithms">Triage algorithms<a class="headerlink" href="#triage-algorithms" title="Permanent link">¶</a></h2>
<p>The nurse agent reasons with one of two protocols, selected at construction:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels"><label for="__tabbed_1_1">ESI</label><label for="__tabbed_1_2">ATS</label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="n">nurse</span> <span class="o">=</span> <span class="n">NurseAgent</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">nurse_llm</span><span class="p">,</span> <span class="n">persona</span><span class="o">=</span><span class="n">persona</span><span class="p">,</span> <span class="n">algorithm</span><span class="o">=</span><span class="s2">"esi"</span><span class="p">)</span>
</span></code></pre></div>
<p>The Emergency Severity Index, used widely in the United States. Level 1 is
the most acute.</p>
</div>
<div class="tabbed-block">
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">nurse</span> <span class="o">=</span> <span class="n">NurseAgent</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">nurse_llm</span><span class="p">,</span> <span class="n">persona</span><span class="o">=</span><span class="n">persona</span><span class="p">,</span> <span class="n">algorithm</span><span class="o">=</span><span class="s2">"ats"</span><span class="p">)</span>
</span></code></pre></div>
<p>The Australasian Triage Scale, used in Australia and New Zealand. Level 1
is the most acute.</p>
</div>
</div>
</input></input></div>
<p>Both scales run from 1 to 5 and <code>NurseOutput.triage</code> is constrained to that
range, but the reasoning prompt differs substantially. Because <strong>lower means
more urgent</strong> on both, predicting a number below the true acuity is
<em>over</em>-triage — a convention that matters when reading
<a href="/triagesim/guide/metrics/">the metrics</a>.</p>
<h2 id="persistence">Persistence<a class="headerlink" href="#persistence" title="Permanent link">¶</a></h2>
<p>All state lives behind the <code>StateStore</code> interface, under keys namespaced by run:</p>
<div class="language-text highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a>triage:{run_id}:state
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>triage:{run_id}:belief_graph
</span><span id="__span-4-3"><a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a>triage:{run_id}:history
</span><span id="__span-4-4"><a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a>triage:{run_id}:trace
</span><span id="__span-4-5"><a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a>triage:{run_id}:red_flags
</span></code></pre></div>
<p><code>InMemoryStateStore</code> keeps these in a dictionary; <code>RedisStateStore</code> keeps them
in Redis so runs outlive the Python process. Both implement the same five
operations, so switching is a one-line config change. See
<a href="/triagesim/guide/runner/">Running a simulation</a>.</p>
<h2 id="putting-it-together">Putting it together<a class="headerlink" href="#putting-it-together" title="Permanent link">¶</a></h2>
<pre class="mermaid"><code>flowchart TD
    GT[Ground truth vignette] --&gt;|hidden| ENV[TriageEnv]
    ENV --&gt;|transcript| NA[NurseAgent]
    NA --&gt;|NurseOutput| MAP[map_nurse_output_to_action]
    MAP --&gt;|executable action| ENV
    ENV --&gt;|vital released| ENV
    ENV --&gt;|transcript| PA[PatientAgent]
    PA --&gt;|PatientOutput| ENV
    ENV --&gt; BG[(BeliefGraph)]
    ENV --&gt; SS[(StateStore)]
    SS --&gt; ART[Run artifact]</code></pre>
<p>Next: <a href="/triagesim/guide/personas/">Personas</a> covers how the two agents are conditioned, and
<a href="/triagesim/guide/artifacts/">Run artifacts</a> covers what comes out the other end.</p>
