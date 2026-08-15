---
title: "Running a simulation"
---

<h1 id="running-a-simulation">Running a simulation<a class="headerlink" href="#running-a-simulation" title="Permanent link">¶</a></h1>
<p><code>TriageRunner</code> drives one triage episode from start to finish and returns a
complete, replayable artifact.</p>
<h2 id="runnerconfig"><code>RunnerConfig</code><a class="headerlink" href="#runnerconfig" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunnerConfig</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="n">config</span> <span class="o">=</span> <span class="n">RunnerConfig</span><span class="p">(</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">max_turns</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">enable_llm</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="n">store_backend</span><span class="o">=</span><span class="s2">"memory"</span><span class="p">,</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a>    <span class="n">redis_db</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="__span-0-8"><a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a>    <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span>
</span><span id="__span-0-9"><a href="#__codelineno-0-9" id="__codelineno-0-9" name="__codelineno-0-9"></a><span class="p">)</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Default</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>max_turns</code></td>
<td><code>int</code></td>
<td><code>6</code></td>
<td>Maximum <strong>patient</strong> turns before the run is forced to end.</td>
</tr>
<tr>
<td><code>enable_llm</code></td>
<td><code>bool</code></td>
<td><code>False</code></td>
<td>Allows the belief updater to call a model in addition to its deterministic rules.</td>
</tr>
<tr>
<td><code>store_backend</code></td>
<td><code>str</code></td>
<td><code>"memory"</code></td>
<td><code>"memory"</code> or <code>"redis"</code>. Anything else raises <code>ValueError</code>.</td>
</tr>
<tr>
<td><code>redis_db</code></td>
<td><code>int</code></td>
<td><code>0</code></td>
<td>Redis database index, used only when <code>store_backend="redis"</code>.</td>
</tr>
<tr>
<td><code>seed</code></td>
<td><code>int \| None</code></td>
<td><code>None</code></td>
<td>Seeds Python's global RNG for the run.</td>
</tr>
</tbody>
</table>
<div class="admonition warning">
<p class="admonition-title"><code>max_turns</code> defaults to 6</p>
<p>Six patient turns is short for a realistic triage encounter — enough to
smoke-test a setup, rarely enough to reach a confident decision. Most real
experiments want 15–25.</p>
</div>
<h2 id="triagerunner"><code>TriageRunner</code><a class="headerlink" href="#triagerunner" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">TriageRunner</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="n">runner</span> <span class="o">=</span> <span class="n">TriageRunner</span><span class="p">(</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a>    <span class="n">nurse_agent</span><span class="o">=</span><span class="n">nurse</span><span class="p">,</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a>    <span class="n">patient_agent</span><span class="o">=</span><span class="n">patient</span><span class="p">,</span>
</span><span id="__span-1-6"><a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a>    <span class="n">ground_truth</span><span class="o">=</span><span class="n">ground_truth</span><span class="p">,</span>
</span><span id="__span-1-7"><a href="#__codelineno-1-7" id="__codelineno-1-7" name="__codelineno-1-7"></a>    <span class="n">config</span><span class="o">=</span><span class="n">config</span><span class="p">,</span>
</span><span id="__span-1-8"><a href="#__codelineno-1-8" id="__codelineno-1-8" name="__codelineno-1-8"></a><span class="p">)</span>
</span><span id="__span-1-9"><a href="#__codelineno-1-9" id="__codelineno-1-9" name="__codelineno-1-9"></a>
</span><span id="__span-1-10"><a href="#__codelineno-1-10" id="__codelineno-1-10" name="__codelineno-1-10"></a><span class="n">artifact</span> <span class="o">=</span> <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span></code></pre></div>
<p>All four arguments are required.</p>
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
<td><code>nurse_agent</code></td>
<td><code>NurseAgent</code></td>
<td>The clinician.</td>
</tr>
<tr>
<td><code>patient_agent</code></td>
<td><code>PatientAgent</code></td>
<td>The patient.</td>
</tr>
<tr>
<td><code>ground_truth</code></td>
<td><code>dict</code></td>
<td>The hidden vignette.</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>RunnerConfig</code></td>
<td>Run settings.</td>
</tr>
</tbody>
</table>
<p>Constructing the runner creates the state store, instantiates a <code>TriageEnv</code>,
applies the <code>enable_llm</code> flag to the belief updater, and seeds the RNG. Nothing
runs until you call <code>run()</code>.</p>
<h3 id="the-ground-truth-dict">The ground-truth dict<a class="headerlink" href="#the-ground-truth-dict" title="Permanent link">¶</a></h3>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="n">ground_truth</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-2-2"><a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a>    <span class="s2">"chiefcomplaint"</span><span class="p">:</span> <span class="s2">"Syncope"</span><span class="p">,</span>   <span class="c1"># read by the patient agent</span>
</span><span id="__span-2-3"><a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a>    <span class="s2">"pain"</span><span class="p">:</span> <span class="mi">7</span><span class="p">,</span>                      <span class="c1"># read by the patient agent</span>
</span><span id="__span-2-4"><a href="#__codelineno-2-4" id="__codelineno-2-4" name="__codelineno-2-4"></a>    <span class="s2">"vitals"</span><span class="p">:</span> <span class="p">{</span>                     <span class="c1"># released by the environment on request</span>
</span><span id="__span-2-5"><a href="#__codelineno-2-5" id="__codelineno-2-5" name="__codelineno-2-5"></a>        <span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">99.1</span><span class="p">,</span>
</span><span id="__span-2-6"><a href="#__codelineno-2-6" id="__codelineno-2-6" name="__codelineno-2-6"></a>        <span class="s2">"heartrate"</span><span class="p">:</span> <span class="mi">112</span><span class="p">,</span>
</span><span id="__span-2-7"><a href="#__codelineno-2-7" id="__codelineno-2-7" name="__codelineno-2-7"></a>        <span class="s2">"resprate"</span><span class="p">:</span> <span class="mi">26</span><span class="p">,</span>
</span><span id="__span-2-8"><a href="#__codelineno-2-8" id="__codelineno-2-8" name="__codelineno-2-8"></a>        <span class="s2">"o2sat"</span><span class="p">:</span> <span class="mi">91</span><span class="p">,</span>
</span><span id="__span-2-9"><a href="#__codelineno-2-9" id="__codelineno-2-9" name="__codelineno-2-9"></a>        <span class="s2">"sbp"</span><span class="p">:</span> <span class="mi">98</span><span class="p">,</span>
</span><span id="__span-2-10"><a href="#__codelineno-2-10" id="__codelineno-2-10" name="__codelineno-2-10"></a>    <span class="p">},</span>
</span><span id="__span-2-11"><a href="#__codelineno-2-11" id="__codelineno-2-11" name="__codelineno-2-11"></a>    <span class="s2">"acuity"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>                    <span class="c1"># reference label, never revealed</span>
</span><span id="__span-2-12"><a href="#__codelineno-2-12" id="__codelineno-2-12" name="__codelineno-2-12"></a><span class="p">}</span>
</span></code></pre></div>
<p><code>chiefcomplaint</code> and <code>pain</code> are read directly by the runner on every patient
turn, so both keys must be present or the run raises <code>KeyError</code>. The five
<code>vitals</code> keys are the only ones the nurse can check, and <code>acuity</code> is used only
by <a href="/triagesim/guide/metrics/">the metrics</a>.</p>
<h2 id="the-run-loop">The run loop<a class="headerlink" href="#the-run-loop" title="Permanent link">¶</a></h2>
<p><code>run()</code> alternates nurse and patient phases:</p>
<ol>
<li><code>env.reset(ground_truth)</code> mints a <code>run_id</code> and clears prior state.</li>
<li><strong>Nurse phase.</strong> The nurse acts repeatedly until it yields:<ul>
<li><code>check_vital</code> → the environment releases the value, and the nurse acts again</li>
<li><code>log_red_flag</code> → flags recorded, and the nurse acts again</li>
<li><code>utterance</code> → control passes to the patient</li>
<li><code>end</code> → the run terminates</li>
</ul>
</li>
<li><strong>Patient phase.</strong> Exactly one patient utterance. The turn counter advances,
   and the nurse infers belief updates from what was said.</li>
<li>Repeat until the turn counter reaches <code>max_turns</code>, the nurse ends, or the
   safety cap trips.</li>
<li><code>_finalize_run</code> snapshots everything and returns it.</li>
</ol>
<h3 id="the-safety-cap">The safety cap<a class="headerlink" href="#the-safety-cap" title="Permanent link">¶</a></h3>
<p>Beyond <code>max_turns</code>, the loop is bounded by <code>max_turns * 4</code> total nurse-plus-patient
steps. This guarantees termination if an agent gets stuck — for example a nurse
that requests vitals indefinitely without ever speaking. With the default
<code>max_turns=6</code> that is 24 steps.</p>
<p>If your runs consistently stop early with few patient turns, the cap is the
likely cause: a nurse that checks several vitals per turn burns steps quickly.</p>
<h2 id="cost">Cost<a class="headerlink" href="#cost" title="Permanent link">¶</a></h2>
<p>Each patient turn costs at least three model calls: one or more nurse <code>act</code>
calls, one patient <code>act</code> call, and one nurse <code>infer_belief_updates</code> call. A
nurse that checks three vitals before speaking adds three more. Budget roughly
<code>max_turns × 4</code> calls as a working estimate, and more if <code>enable_llm=True</code>.</p>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Start at <code>max_turns=6</code> while wiring things up, then raise it once the
dialogue looks sensible.</p>
</div>
<h2 id="redis-state-store">Redis state store<a class="headerlink" href="#redis-state-store" title="Permanent link">¶</a></h2>
<p>By default, state lives in a plain dictionary and disappears when the process
exits. Switching to Redis persists it:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">config</span> <span class="o">=</span> <span class="n">RunnerConfig</span><span class="p">(</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>    <span class="n">max_turns</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a>    <span class="n">store_backend</span><span class="o">=</span><span class="s2">"redis"</span><span class="p">,</span>
</span><span id="__span-3-4"><a href="#__codelineno-3-4" id="__codelineno-3-4" name="__codelineno-3-4"></a>    <span class="n">redis_db</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="__span-3-5"><a href="#__codelineno-3-5" id="__codelineno-3-5" name="__codelineno-3-5"></a>    <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span>
</span><span id="__span-3-6"><a href="#__codelineno-3-6" id="__codelineno-3-6" name="__codelineno-3-6"></a><span class="p">)</span>
</span></code></pre></div>
<p>This requires the extra and a running server:</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[redis]"</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a>redis-server
</span></code></pre></div>
<p><code>RedisStateStore</code> connects to <code>localhost:6379</code> at the configured <code>db</code> index.
<code>RunnerConfig</code> exposes only <code>redis_db</code>, so a non-default host or port means
constructing the store yourself:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core.state_store</span><span class="w"> </span><span class="kn">import</span> <span class="n">RedisStateStore</span>
</span><span id="__span-5-2"><a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>
</span><span id="__span-5-3"><a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="n">store</span> <span class="o">=</span> <span class="n">RedisStateStore</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="s2">"10.0.0.5"</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">6380</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span></code></pre></div>
<p>State is written under keys namespaced by run:</p>
<div class="language-text highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a>triage:{run_id}:state
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a>triage:{run_id}:belief_graph
</span><span id="__span-6-3"><a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>triage:{run_id}:history
</span><span id="__span-6-4"><a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a>triage:{run_id}:trace
</span><span id="__span-6-5"><a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a>triage:{run_id}:red_flags
</span></code></pre></div>
<p>Keeping the <code>run_id</code> lets you inspect a completed run later without re-running
it — useful when a batch of simulations takes hours and you want to analyse
results incrementally.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Importing <code>RedisStateStore</code> without the <code>redis</code> package installed raises
<code>ImportError</code> when it is constructed, not at import time.</p>
</div>
<h2 id="reproducibility">Reproducibility<a class="headerlink" href="#reproducibility" title="Permanent link">¶</a></h2>
<p><code>seed</code> calls <code>random.seed()</code> for the run, which fixes any internal random
choices. Combined with seeded <a href="/triagesim/guide/personas/">persona sampling</a>, that
makes the <em>setup</em> deterministic.</p>
<p>It does <strong>not</strong> make the dialogue deterministic. Sampling happens on the
provider's side and is outside TriageSim's control, so two runs with identical
seeds will differ in wording and may differ in outcome. For statistical claims,
run each condition many times rather than relying on a single seeded run.</p>
<h2 id="a-complete-example">A complete example<a class="headerlink" href="#a-complete-example" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-7-1"><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">TriageRunner</span><span class="p">,</span> <span class="n">RunnerConfig</span>
</span><span id="__span-7-2"><a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenRouterLLM</span><span class="p">,</span> <span class="n">NurseAgent</span><span class="p">,</span> <span class="n">PatientAgent</span>
</span><span id="__span-7-3"><a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span><span id="__span-7-4"><a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
</span><span id="__span-7-5"><a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a>    <span class="n">load_patient_personas</span><span class="p">,</span>
</span><span id="__span-7-6"><a href="#__codelineno-7-6" id="__codelineno-7-6" name="__codelineno-7-6"></a>    <span class="n">load_nurse_personas</span><span class="p">,</span>
</span><span id="__span-7-7"><a href="#__codelineno-7-7" id="__codelineno-7-7" name="__codelineno-7-7"></a>    <span class="n">sample_patient_personas</span><span class="p">,</span>
</span><span id="__span-7-8"><a href="#__codelineno-7-8" id="__codelineno-7-8" name="__codelineno-7-8"></a>    <span class="n">sample_nurse_personas</span><span class="p">,</span>
</span><span id="__span-7-9"><a href="#__codelineno-7-9" id="__codelineno-7-9" name="__codelineno-7-9"></a><span class="p">)</span>
</span><span id="__span-7-10"><a href="#__codelineno-7-10" id="__codelineno-7-10" name="__codelineno-7-10"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span><span id="__span-7-11"><a href="#__codelineno-7-11" id="__codelineno-7-11" name="__codelineno-7-11"></a>
</span><span id="__span-7-12"><a href="#__codelineno-7-12" id="__codelineno-7-12" name="__codelineno-7-12"></a><span class="n">MODEL</span> <span class="o">=</span> <span class="s2">"anthropic/claude-sonnet-4-5"</span>
</span><span id="__span-7-13"><a href="#__codelineno-7-13" id="__codelineno-7-13" name="__codelineno-7-13"></a>
</span><span id="__span-7-14"><a href="#__codelineno-7-14" id="__codelineno-7-14" name="__codelineno-7-14"></a><span class="n">patients</span> <span class="o">=</span> <span class="n">load_patient_personas</span><span class="p">(</span><span class="s2">"patient.yaml"</span><span class="p">)</span>
</span><span id="__span-7-15"><a href="#__codelineno-7-15" id="__codelineno-7-15" name="__codelineno-7-15"></a><span class="n">nurses</span> <span class="o">=</span> <span class="n">load_nurse_personas</span><span class="p">(</span><span class="s2">"nurse.yaml"</span><span class="p">)</span>
</span><span id="__span-7-16"><a href="#__codelineno-7-16" id="__codelineno-7-16" name="__codelineno-7-16"></a>
</span><span id="__span-7-17"><a href="#__codelineno-7-17" id="__codelineno-7-17" name="__codelineno-7-17"></a><span class="n">ground_truth</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-7-18"><a href="#__codelineno-7-18" id="__codelineno-7-18" name="__codelineno-7-18"></a>    <span class="s2">"chiefcomplaint"</span><span class="p">:</span> <span class="s2">"Syncope"</span><span class="p">,</span>
</span><span id="__span-7-19"><a href="#__codelineno-7-19" id="__codelineno-7-19" name="__codelineno-7-19"></a>    <span class="s2">"pain"</span><span class="p">:</span> <span class="mi">7</span><span class="p">,</span>
</span><span id="__span-7-20"><a href="#__codelineno-7-20" id="__codelineno-7-20" name="__codelineno-7-20"></a>    <span class="s2">"vitals"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">99.1</span><span class="p">,</span> <span class="s2">"heartrate"</span><span class="p">:</span> <span class="mi">112</span><span class="p">,</span> <span class="s2">"resprate"</span><span class="p">:</span> <span class="mi">26</span><span class="p">,</span>
</span><span id="__span-7-21"><a href="#__codelineno-7-21" id="__codelineno-7-21" name="__codelineno-7-21"></a>               <span class="s2">"o2sat"</span><span class="p">:</span> <span class="mi">91</span><span class="p">,</span> <span class="s2">"sbp"</span><span class="p">:</span> <span class="mi">98</span><span class="p">},</span>
</span><span id="__span-7-22"><a href="#__codelineno-7-22" id="__codelineno-7-22" name="__codelineno-7-22"></a>    <span class="s2">"acuity"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
</span><span id="__span-7-23"><a href="#__codelineno-7-23" id="__codelineno-7-23" name="__codelineno-7-23"></a><span class="p">}</span>
</span><span id="__span-7-24"><a href="#__codelineno-7-24" id="__codelineno-7-24" name="__codelineno-7-24"></a>
</span><span id="__span-7-25"><a href="#__codelineno-7-25" id="__codelineno-7-25" name="__codelineno-7-25"></a><span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-7-26"><a href="#__codelineno-7-26" id="__codelineno-7-26" name="__codelineno-7-26"></a>
</span><span id="__span-7-27"><a href="#__codelineno-7-27" id="__codelineno-7-27" name="__codelineno-7-27"></a><span class="k">for</span> <span class="n">seed</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
</span><span id="__span-7-28"><a href="#__codelineno-7-28" id="__codelineno-7-28" name="__codelineno-7-28"></a>    <span class="n">nurse</span> <span class="o">=</span> <span class="n">NurseAgent</span><span class="p">(</span>
</span><span id="__span-7-29"><a href="#__codelineno-7-29" id="__codelineno-7-29" name="__codelineno-7-29"></a>        <span class="n">llm</span><span class="o">=</span><span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">MODEL</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">NurseOutput</span><span class="p">),</span>
</span><span id="__span-7-30"><a href="#__codelineno-7-30" id="__codelineno-7-30" name="__codelineno-7-30"></a>        <span class="n">persona</span><span class="o">=</span><span class="n">sample_nurse_personas</span><span class="p">(</span><span class="n">nurses</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="n">seed</span><span class="p">)[</span><span class="mi">0</span><span class="p">],</span>
</span><span id="__span-7-31"><a href="#__codelineno-7-31" id="__codelineno-7-31" name="__codelineno-7-31"></a>        <span class="n">algorithm</span><span class="o">=</span><span class="s2">"esi"</span><span class="p">,</span>
</span><span id="__span-7-32"><a href="#__codelineno-7-32" id="__codelineno-7-32" name="__codelineno-7-32"></a>    <span class="p">)</span>
</span><span id="__span-7-33"><a href="#__codelineno-7-33" id="__codelineno-7-33" name="__codelineno-7-33"></a>    <span class="n">patient</span> <span class="o">=</span> <span class="n">PatientAgent</span><span class="p">(</span>
</span><span id="__span-7-34"><a href="#__codelineno-7-34" id="__codelineno-7-34" name="__codelineno-7-34"></a>        <span class="n">llm</span><span class="o">=</span><span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">MODEL</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">PatientOutput</span><span class="p">),</span>
</span><span id="__span-7-35"><a href="#__codelineno-7-35" id="__codelineno-7-35" name="__codelineno-7-35"></a>        <span class="n">persona</span><span class="o">=</span><span class="n">sample_patient_personas</span><span class="p">(</span><span class="n">patients</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="n">seed</span><span class="p">)[</span><span class="mi">0</span><span class="p">],</span>
</span><span id="__span-7-36"><a href="#__codelineno-7-36" id="__codelineno-7-36" name="__codelineno-7-36"></a>    <span class="p">)</span>
</span><span id="__span-7-37"><a href="#__codelineno-7-37" id="__codelineno-7-37" name="__codelineno-7-37"></a>
</span><span id="__span-7-38"><a href="#__codelineno-7-38" id="__codelineno-7-38" name="__codelineno-7-38"></a>    <span class="n">artifact</span> <span class="o">=</span> <span class="n">TriageRunner</span><span class="p">(</span>
</span><span id="__span-7-39"><a href="#__codelineno-7-39" id="__codelineno-7-39" name="__codelineno-7-39"></a>        <span class="n">nurse_agent</span><span class="o">=</span><span class="n">nurse</span><span class="p">,</span>
</span><span id="__span-7-40"><a href="#__codelineno-7-40" id="__codelineno-7-40" name="__codelineno-7-40"></a>        <span class="n">patient_agent</span><span class="o">=</span><span class="n">patient</span><span class="p">,</span>
</span><span id="__span-7-41"><a href="#__codelineno-7-41" id="__codelineno-7-41" name="__codelineno-7-41"></a>        <span class="n">ground_truth</span><span class="o">=</span><span class="n">ground_truth</span><span class="p">,</span>
</span><span id="__span-7-42"><a href="#__codelineno-7-42" id="__codelineno-7-42" name="__codelineno-7-42"></a>        <span class="n">config</span><span class="o">=</span><span class="n">RunnerConfig</span><span class="p">(</span><span class="n">max_turns</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="n">seed</span><span class="p">),</span>
</span><span id="__span-7-43"><a href="#__codelineno-7-43" id="__codelineno-7-43" name="__codelineno-7-43"></a>    <span class="p">)</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span><span id="__span-7-44"><a href="#__codelineno-7-44" id="__codelineno-7-44" name="__codelineno-7-44"></a>
</span><span id="__span-7-45"><a href="#__codelineno-7-45" id="__codelineno-7-45" name="__codelineno-7-45"></a>    <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-7-46"><a href="#__codelineno-7-46" id="__codelineno-7-46" name="__codelineno-7-46"></a>        <span class="n">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-7-47"><a href="#__codelineno-7-47" id="__codelineno-7-47" name="__codelineno-7-47"></a>            <span class="n">trace</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">],</span>
</span><span id="__span-7-48"><a href="#__codelineno-7-48" id="__codelineno-7-48" name="__codelineno-7-48"></a>            <span class="n">belief</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"belief"</span><span class="p">],</span>
</span><span id="__span-7-49"><a href="#__codelineno-7-49" id="__codelineno-7-49" name="__codelineno-7-49"></a>            <span class="n">ground_truth</span><span class="o">=</span><span class="n">ground_truth</span><span class="p">,</span>
</span><span id="__span-7-50"><a href="#__codelineno-7-50" id="__codelineno-7-50" name="__codelineno-7-50"></a>        <span class="p">)</span>
</span><span id="__span-7-51"><a href="#__codelineno-7-51" id="__codelineno-7-51" name="__codelineno-7-51"></a>    <span class="p">)</span>
</span><span id="__span-7-52"><a href="#__codelineno-7-52" id="__codelineno-7-52" name="__codelineno-7-52"></a>
</span><span id="__span-7-53"><a href="#__codelineno-7-53" id="__codelineno-7-53" name="__codelineno-7-53"></a><span class="n">correct</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"correct"</span><span class="p">])</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">results</span><span class="p">)</span>
</span><span id="__span-7-54"><a href="#__codelineno-7-54" id="__codelineno-7-54" name="__codelineno-7-54"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">correct</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">results</span><span class="p">)</span><span class="si">}</span><span class="s2"> runs triaged correctly"</span><span class="p">)</span>
</span></code></pre></div>
<p>Next: <a href="/triagesim/guide/artifacts/">Run artifacts</a> describes what <code>run()</code> gives you back.</p>
