---
title: "Quick start"
---

<h1 id="quick-start">Quick start<a class="headerlink" href="#quick-start" title="Permanent link">¶</a></h1>
<p>This page walks through a complete simulation, one piece at a time. By the end
you will have run a nurse ↔ patient dialogue and inspected the triage decision
the nurse arrived at.</p>
<p>Before starting, make sure you have <a href="/triagesim/getting-started/installation/">installed</a> TriageSim and
<a href="/triagesim/getting-started/configuration/">set your API key</a>.</p>
<h2 id="1-define-persona-files">1. Define persona files<a class="headerlink" href="#1-define-persona-files" title="Permanent link">¶</a></h2>
<p>Personas are plain YAML lists. Create two small files to start with:</p>
<div class="language-yaml highlight"><span class="filename">patient.yaml</span><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">age_group</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">adult</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="w">  </span><span class="nt">gender</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">female</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="w">  </span><span class="nt">ethnicity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">Australian</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="w">  </span><span class="nt">socioeconomic_status</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">middle</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="w">  </span><span class="nt">language_proficiency</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a><span class="w">  </span><span class="nt">recall_accuracy</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a><span class="w">  </span><span class="nt">cognitive_state</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">clear</span>
</span><span id="__span-0-8"><a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a><span class="w">  </span><span class="nt">trust_in_healthcare</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-9"><a href="#__codelineno-0-9" id="__codelineno-0-9" name="__codelineno-0-9"></a><span class="w">  </span><span class="nt">pain_expression</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">moderate</span>
</span><span id="__span-0-10"><a href="#__codelineno-0-10" id="__codelineno-0-10" name="__codelineno-0-10"></a><span class="w">  </span><span class="nt">reactivity_to_clinician_emotion</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-11"><a href="#__codelineno-0-11" id="__codelineno-0-11" name="__codelineno-0-11"></a><span class="w">  </span><span class="nt">emotion_regulation</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">stable</span>
</span><span id="__span-0-12"><a href="#__codelineno-0-12" id="__codelineno-0-12" name="__codelineno-0-12"></a><span class="w">  </span><span class="nt">disfluency_rate</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-13"><a href="#__codelineno-0-13" id="__codelineno-0-13" name="__codelineno-0-13"></a><span class="w">  </span><span class="nt">topic_drift</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-14"><a href="#__codelineno-0-14" id="__codelineno-0-14" name="__codelineno-0-14"></a><span class="w">  </span><span class="nt">verbosity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">medium</span>
</span></code></pre></div>
<div class="language-yaml highlight"><span class="filename">nurse.yaml</span><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">gender</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">female</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="w">  </span><span class="nt">ethnicity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">Australian</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="w">  </span><span class="nt">experience_level</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">senior</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="w">  </span><span class="nt">risk_tolerance</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a><span class="w">  </span><span class="nt">guideline_adherence</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-1-6"><a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a><span class="w">  </span><span class="nt">communication_style</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">direct</span>
</span><span id="__span-1-7"><a href="#__codelineno-1-7" id="__codelineno-1-7" name="__codelineno-1-7"></a><span class="w">  </span><span class="nt">verbosity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">medium</span>
</span><span id="__span-1-8"><a href="#__codelineno-1-8" id="__codelineno-1-8" name="__codelineno-1-8"></a><span class="w">  </span><span class="nt">emotional_expression</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">neutral</span>
</span></code></pre></div>
<p>Every field is a free-form string, which is what lets you introduce new
categories without changing the schema. See <a href="/triagesim/guide/personas/">Personas</a>
for the full field reference.</p>
<h2 id="2-load-and-sample-personas">2. Load and sample personas<a class="headerlink" href="#2-load-and-sample-personas" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
</span><span id="__span-2-2"><a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a>    <span class="n">load_patient_personas</span><span class="p">,</span>
</span><span id="__span-2-3"><a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a>    <span class="n">load_nurse_personas</span><span class="p">,</span>
</span><span id="__span-2-4"><a href="#__codelineno-2-4" id="__codelineno-2-4" name="__codelineno-2-4"></a>    <span class="n">sample_patient_personas</span><span class="p">,</span>
</span><span id="__span-2-5"><a href="#__codelineno-2-5" id="__codelineno-2-5" name="__codelineno-2-5"></a>    <span class="n">sample_nurse_personas</span><span class="p">,</span>
</span><span id="__span-2-6"><a href="#__codelineno-2-6" id="__codelineno-2-6" name="__codelineno-2-6"></a><span class="p">)</span>
</span><span id="__span-2-7"><a href="#__codelineno-2-7" id="__codelineno-2-7" name="__codelineno-2-7"></a>
</span><span id="__span-2-8"><a href="#__codelineno-2-8" id="__codelineno-2-8" name="__codelineno-2-8"></a><span class="n">patients</span> <span class="o">=</span> <span class="n">load_patient_personas</span><span class="p">(</span><span class="s2">"patient.yaml"</span><span class="p">)</span>
</span><span id="__span-2-9"><a href="#__codelineno-2-9" id="__codelineno-2-9" name="__codelineno-2-9"></a><span class="n">nurses</span> <span class="o">=</span> <span class="n">load_nurse_personas</span><span class="p">(</span><span class="s2">"nurse.yaml"</span><span class="p">)</span>
</span><span id="__span-2-10"><a href="#__codelineno-2-10" id="__codelineno-2-10" name="__codelineno-2-10"></a>
</span><span id="__span-2-11"><a href="#__codelineno-2-11" id="__codelineno-2-11" name="__codelineno-2-11"></a><span class="n">patient_persona</span> <span class="o">=</span> <span class="n">sample_patient_personas</span><span class="p">(</span><span class="n">patients</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="__span-2-12"><a href="#__codelineno-2-12" id="__codelineno-2-12" name="__codelineno-2-12"></a><span class="n">nurse_persona</span> <span class="o">=</span> <span class="n">sample_nurse_personas</span><span class="p">(</span><span class="n">nurses</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span></code></pre></div>
<p>Passing a <code>seed</code> fixes which personas are drawn, so the same seed always
selects the same pair from a larger pool.</p>
<h2 id="3-define-the-ground-truth">3. Define the ground truth<a class="headerlink" href="#3-define-the-ground-truth" title="Permanent link">¶</a></h2>
<p>This is the structured record the simulation is grounded in. <strong>Neither agent
can see it.</strong> The patient agent is told only its chief complaint and pain
score; the nurse agent starts with nothing and must elicit everything.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">ground_truth</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>    <span class="s2">"chiefcomplaint"</span><span class="p">:</span> <span class="s2">"Syncope"</span><span class="p">,</span>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a>    <span class="s2">"vitals"</span><span class="p">:</span> <span class="p">{</span>
</span><span id="__span-3-4"><a href="#__codelineno-3-4" id="__codelineno-3-4" name="__codelineno-3-4"></a>        <span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">99.1</span><span class="p">,</span>
</span><span id="__span-3-5"><a href="#__codelineno-3-5" id="__codelineno-3-5" name="__codelineno-3-5"></a>        <span class="s2">"heartrate"</span><span class="p">:</span> <span class="mi">112</span><span class="p">,</span>
</span><span id="__span-3-6"><a href="#__codelineno-3-6" id="__codelineno-3-6" name="__codelineno-3-6"></a>        <span class="s2">"resprate"</span><span class="p">:</span> <span class="mi">26</span><span class="p">,</span>
</span><span id="__span-3-7"><a href="#__codelineno-3-7" id="__codelineno-3-7" name="__codelineno-3-7"></a>        <span class="s2">"o2sat"</span><span class="p">:</span> <span class="mi">91</span><span class="p">,</span>
</span><span id="__span-3-8"><a href="#__codelineno-3-8" id="__codelineno-3-8" name="__codelineno-3-8"></a>        <span class="s2">"sbp"</span><span class="p">:</span> <span class="mi">98</span><span class="p">,</span>
</span><span id="__span-3-9"><a href="#__codelineno-3-9" id="__codelineno-3-9" name="__codelineno-3-9"></a>    <span class="p">},</span>
</span><span id="__span-3-10"><a href="#__codelineno-3-10" id="__codelineno-3-10" name="__codelineno-3-10"></a>    <span class="s2">"acuity"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
</span><span id="__span-3-11"><a href="#__codelineno-3-11" id="__codelineno-3-11" name="__codelineno-3-11"></a>    <span class="s2">"pain"</span><span class="p">:</span> <span class="mi">7</span><span class="p">,</span>
</span><span id="__span-3-12"><a href="#__codelineno-3-12" id="__codelineno-3-12" name="__codelineno-3-12"></a><span class="p">}</span>
</span></code></pre></div>
<p>The <code>acuity</code> field is the reference triage level used for scoring. The five
keys under <code>vitals</code> are the only vitals the nurse can check.</p>
<h2 id="4-create-the-llm-backends">4. Create the LLM backends<a class="headerlink" href="#4-create-the-llm-backends" title="Permanent link">¶</a></h2>
<p>Each backend is bound to a single output schema, so the nurse and patient need
one each:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenRouterLLM</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span><span id="__span-4-3"><a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a>
</span><span id="__span-4-4"><a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a><span class="n">model</span> <span class="o">=</span> <span class="s2">"anthropic/claude-sonnet-4-5"</span>
</span><span id="__span-4-5"><a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a>
</span><span id="__span-4-6"><a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a><span class="n">patient_llm</span> <span class="o">=</span> <span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">model</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">PatientOutput</span><span class="p">)</span>
</span><span id="__span-4-7"><a href="#__codelineno-4-7" id="__codelineno-4-7" name="__codelineno-4-7"></a><span class="n">nurse_llm</span> <span class="o">=</span> <span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">model</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">NurseOutput</span><span class="p">)</span>
</span></code></pre></div>
<p>The two backends can use different models if you want to study asymmetric
pairings.</p>
<h2 id="5-create-the-agents">5. Create the agents<a class="headerlink" href="#5-create-the-agents" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseAgent</span><span class="p">,</span> <span class="n">PatientAgent</span>
</span><span id="__span-5-2"><a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>
</span><span id="__span-5-3"><a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="n">patient</span> <span class="o">=</span> <span class="n">PatientAgent</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">patient_llm</span><span class="p">,</span> <span class="n">persona</span><span class="o">=</span><span class="n">patient_persona</span><span class="p">)</span>
</span><span id="__span-5-4"><a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a><span class="n">nurse</span> <span class="o">=</span> <span class="n">NurseAgent</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">nurse_llm</span><span class="p">,</span> <span class="n">persona</span><span class="o">=</span><span class="n">nurse_persona</span><span class="p">,</span> <span class="n">algorithm</span><span class="o">=</span><span class="s2">"esi"</span><span class="p">)</span>
</span></code></pre></div>
<p><code>algorithm</code> selects the triage protocol the nurse reasons with — <code>"esi"</code> for
the Emergency Severity Index or <code>"ats"</code> for the Australasian Triage Scale.
Both produce a level from 1 to 5, but the reasoning prompt differs.</p>
<h2 id="6-run">6. Run<a class="headerlink" href="#6-run" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">TriageRunner</span><span class="p">,</span> <span class="n">RunnerConfig</span>
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a>
</span><span id="__span-6-3"><a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a><span class="n">config</span> <span class="o">=</span> <span class="n">RunnerConfig</span><span class="p">(</span><span class="n">max_turns</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">store_backend</span><span class="o">=</span><span class="s2">"memory"</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</span><span id="__span-6-4"><a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a>
</span><span id="__span-6-5"><a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a><span class="n">runner</span> <span class="o">=</span> <span class="n">TriageRunner</span><span class="p">(</span>
</span><span id="__span-6-6"><a href="#__codelineno-6-6" id="__codelineno-6-6" name="__codelineno-6-6"></a>    <span class="n">nurse_agent</span><span class="o">=</span><span class="n">nurse</span><span class="p">,</span>
</span><span id="__span-6-7"><a href="#__codelineno-6-7" id="__codelineno-6-7" name="__codelineno-6-7"></a>    <span class="n">patient_agent</span><span class="o">=</span><span class="n">patient</span><span class="p">,</span>
</span><span id="__span-6-8"><a href="#__codelineno-6-8" id="__codelineno-6-8" name="__codelineno-6-8"></a>    <span class="n">ground_truth</span><span class="o">=</span><span class="n">ground_truth</span><span class="p">,</span>
</span><span id="__span-6-9"><a href="#__codelineno-6-9" id="__codelineno-6-9" name="__codelineno-6-9"></a>    <span class="n">config</span><span class="o">=</span><span class="n">config</span><span class="p">,</span>
</span><span id="__span-6-10"><a href="#__codelineno-6-10" id="__codelineno-6-10" name="__codelineno-6-10"></a><span class="p">)</span>
</span><span id="__span-6-11"><a href="#__codelineno-6-11" id="__codelineno-6-11" name="__codelineno-6-11"></a>
</span><span id="__span-6-12"><a href="#__codelineno-6-12" id="__codelineno-6-12" name="__codelineno-6-12"></a><span class="n">artifact</span> <span class="o">=</span> <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span></code></pre></div>
<div class="admonition tip">
<p class="admonition-title">Start small</p>
<p><code>max_turns</code> defaults to <code>6</code>. Each turn is at least two model calls, so
raise it deliberately — a 20-turn run costs roughly three times a 6-turn
one.</p>
</div>
<h2 id="7-inspect-the-result">7. Inspect the result<a class="headerlink" href="#7-inspect-the-result" title="Permanent link">¶</a></h2>
<p><code>run()</code> returns a dictionary describing everything that happened:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-7-1"><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="nb">print</span><span class="p">(</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"run_id"</span><span class="p">])</span>
</span><span id="__span-7-2"><a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>
</span><span id="__span-7-3"><a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="k">for</span> <span class="n">turn</span> <span class="ow">in</span> <span class="n">artifact</span><span class="p">[</span><span class="s2">"history"</span><span class="p">]:</span>
</span><span id="__span-7-4"><a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a>    <span class="nb">print</span><span class="p">(</span><span class="n">turn</span><span class="p">)</span>
</span><span id="__span-7-5"><a href="#__codelineno-7-5" id="__codelineno-7-5" name="__codelineno-7-5"></a>
</span><span id="__span-7-6"><a href="#__codelineno-7-6" id="__codelineno-7-6" name="__codelineno-7-6"></a><span class="n">final</span> <span class="o">=</span> <span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">][</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="__span-7-7"><a href="#__codelineno-7-7" id="__codelineno-7-7" name="__codelineno-7-7"></a><span class="nb">print</span><span class="p">(</span><span class="n">final</span><span class="p">[</span><span class="s2">"action"</span><span class="p">][</span><span class="s2">"triage"</span><span class="p">],</span> <span class="n">final</span><span class="p">[</span><span class="s2">"action"</span><span class="p">][</span><span class="s2">"explanation"</span><span class="p">])</span>
</span></code></pre></div>
<p>See <a href="/triagesim/guide/artifacts/">Run artifacts</a> for the complete structure.</p>
<h2 id="8-score-it">8. Score it<a class="headerlink" href="#8-score-it" title="Permanent link">¶</a></h2>
<p>Because the ground truth is known, the run is scorable straight away:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-8-1"><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span><span id="__span-8-2"><a href="#__codelineno-8-2" id="__codelineno-8-2" name="__codelineno-8-2"></a>
</span><span id="__span-8-3"><a href="#__codelineno-8-3" id="__codelineno-8-3" name="__codelineno-8-3"></a><span class="n">metrics</span> <span class="o">=</span> <span class="n">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-8-4"><a href="#__codelineno-8-4" id="__codelineno-8-4" name="__codelineno-8-4"></a>    <span class="n">trace</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">],</span>
</span><span id="__span-8-5"><a href="#__codelineno-8-5" id="__codelineno-8-5" name="__codelineno-8-5"></a>    <span class="n">belief</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"belief"</span><span class="p">],</span>
</span><span id="__span-8-6"><a href="#__codelineno-8-6" id="__codelineno-8-6" name="__codelineno-8-6"></a>    <span class="n">ground_truth</span><span class="o">=</span><span class="n">ground_truth</span><span class="p">,</span>
</span><span id="__span-8-7"><a href="#__codelineno-8-7" id="__codelineno-8-7" name="__codelineno-8-7"></a><span class="p">)</span>
</span><span id="__span-8-8"><a href="#__codelineno-8-8" id="__codelineno-8-8" name="__codelineno-8-8"></a>
</span><span id="__span-8-9"><a href="#__codelineno-8-9" id="__codelineno-8-9" name="__codelineno-8-9"></a><span class="nb">print</span><span class="p">(</span><span class="n">metrics</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"correct"</span><span class="p">])</span>
</span><span id="__span-8-10"><a href="#__codelineno-8-10" id="__codelineno-8-10" name="__codelineno-8-10"></a><span class="nb">print</span><span class="p">(</span><span class="n">metrics</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"absolute_error"</span><span class="p">])</span>
</span></code></pre></div>
<p><a href="/triagesim/guide/metrics/">Evaluation metrics</a> documents every value returned.</p>
<h2 id="next-steps">Next steps<a class="headerlink" href="#next-steps" title="Permanent link">¶</a></h2>
<div class="grid cards">
<ul>
<li>
<p><strong>Understand the loop</strong> — how the environment, belief state and nurse
    micro-turns fit together.</p>
<p><a href="/triagesim/guide/concepts/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Core concepts</a></p>
</li>
<li>
<p><strong>Vary the population</strong> — build larger persona pools and filter them into
    experimental conditions.</p>
<p><a href="/triagesim/guide/personas/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Personas</a></p>
</li>
<li>
<p><strong>Scale up</strong> — persist runs to Redis instead of process memory.</p>
<p><a href="/triagesim/guide/runner/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Running a simulation</a></p>
</li>
</ul>
</div>
