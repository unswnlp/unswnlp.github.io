---
title: "TriageSim"
---

<h1 id="triagesim">TriageSim<a class="headerlink" href="#triagesim" title="Permanent link">¶</a></h1>
<p><strong>A Python framework for generating synthetic, multi-speaker spoken dialogues
for emergency department triage.</strong></p>
<p>TriageSim turns structured clinical vignettes into realistic nurse ↔ patient
conversations. A ground-truth electronic health record — chief complaint,
vitals, pain score, true acuity — is hidden from both agents. The nurse agent
must <em>elicit</em> that information through dialogue, decide which vitals to check,
log red flags, and commit to a triage level. The result is paired
<strong>structured EHR → dialogue</strong> data with a full record of how the decision was
reached.</p>
<p><a class="md-button md-button--primary" href="/triagesim/getting-started/installation/">Get started</a>
<a class="md-button" href="https://github.com/dipankarsrirag/triage-sim">View on GitHub</a></p>
<hr/>
<h2 id="why-it-exists">Why it exists<a class="headerlink" href="#why-it-exists" title="Permanent link">¶</a></h2>
<p>Evaluating speech and language systems in clinical settings is hard: real
triage recordings are scarce, sensitive, and almost never paired with reliable
ground truth. TriageSim generates that pairing under controlled conditions, so
you can vary one factor at a time — the patient's language proficiency, the
nurse's risk tolerance, the underlying model — and measure what changes.</p>
<p>Because the ground truth is known by construction, every run is scorable. The
framework ships metrics for triage accuracy, red-flag detection, belief
coverage, and how well the nurse's stated reasoning is supported by what was
actually elicited.</p>
<hr/>
<h2 id="what-you-get">What you get<a class="headerlink" href="#what-you-get" title="Permanent link">¶</a></h2>
<div class="grid cards">
<ul>
<li>
<p><span class="twemoji lg middle"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9 5a4 4 0 0 1 4 4 4 4 0 0 1-4 4 4 4 0 0 1-4-4 4 4 0 0 1 4-4m0 10c2.67 0 8 1.34 8 4v2H1v-2c0-2.66 5.33-4 8-4m7.76-9.64c2.02 2.2 2.02 5.25 0 7.27l-1.68-1.69c.84-1.18.84-2.71 0-3.89zM20.07 2c3.93 4.05 3.9 10.11 0 14l-1.63-1.63c2.77-3.18 2.77-7.72 0-10.74z"></path></svg></span> <strong>Agent dialogue</strong></p>
<hr/>
<p>Nurse and patient agents backed by any OpenRouter-compatible model, each
emitting schema-validated structured output rather than free text.</p>
<p><a href="/triagesim/guide/agents/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Agents</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1s-2.4.84-2.82 2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2m-7 0a1 1 0 0 1 1 1 1 1 0 0 1-1 1 1 1 0 0 1-1-1 1 1 0 0 1 1-1M5 13.46h2.17l3.33-6.38.94 6.97 2.49-3.19 2.6 2.6H19V15h-3.11l-1.82-1.79-3.69 4.71-.76-5.77L8.11 15H5z"></path></svg></span> <strong>Two triage algorithms</strong></p>
<hr/>
<p>The Emergency Severity Index (ESI) and the Australasian Triage Scale (ATS),
selected per nurse agent and reflected in its reasoning prompt.</p>
<p><a href="/triagesim/guide/concepts/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Concepts</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 5.5A3.5 3.5 0 0 1 15.5 9a3.5 3.5 0 0 1-3.5 3.5A3.5 3.5 0 0 1 8.5 9 3.5 3.5 0 0 1 12 5.5M5 8c.56 0 1.08.15 1.53.42-.15 1.43.27 2.85 1.13 3.96C7.16 13.34 6.16 14 5 14a3 3 0 0 1-3-3 3 3 0 0 1 3-3m14 0a3 3 0 0 1 3 3 3 3 0 0 1-3 3c-1.16 0-2.16-.66-2.66-1.62a5.54 5.54 0 0 0 1.13-3.96c.45-.27.97-.42 1.53-.42M5.5 18.25c0-2.07 2.91-3.75 6.5-3.75s6.5 1.68 6.5 3.75V20h-13zM0 20v-1.5c0-1.39 1.89-2.56 4.45-2.9-.59.68-.95 1.62-.95 2.65V20zm24 0h-3.5v-1.75c0-1.03-.36-1.97-.95-2.65 2.56.34 4.45 1.51 4.45 2.9z"></path></svg></span> <strong>Persona conditioning</strong></p>
<hr/>
<p>Patient and nurse personas defined in YAML — ethnicity, recall accuracy,
pain expression, guideline adherence, verbosity, and more.</p>
<p><a href="/triagesim/guide/personas/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Personas</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 3h6v4H3zm12 7h6v4h-6zm0 7h6v4h-6zm-2-4H7v5h6v2H5V9h2v2h6z"></path></svg></span> <strong>Replayable artifacts</strong></p>
<hr/>
<p>Every run returns dialogue history, a per-turn cognition trace, the final
belief state, and logged red flags — persisted in memory or Redis.</p>
<p><a href="/triagesim/guide/artifacts/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Run artifacts</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2M9 17H7v-7h2zm4 0h-2V7h2zm4 0h-2v-4h2z"></path></svg></span> <strong>Built-in metrics</strong></p>
<hr/>
<p>Triage correctness and over/under-triage, time-to-first-correct, red-flag
precision/recall/F1, and explanation support statistics.</p>
<p><a href="/triagesim/guide/metrics/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Metrics</a></p>
</li>
<li>
<p><span class="twemoji lg middle"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m22 12-2 1-1 1-1-1-1 3-1-3-1 8-1-8-1 2-1-2-1 4-1-4-1 9-1-9-1 6-1-6-1 1-1-1-2-1 2-1 1-1 1 1 1-6 1 6 1-9 1 9 1-4 1 4 1-2 1 2 1-8 1 8 1-3 1 3 1-1 1 1z"></path></svg></span> <strong>Optional speech synthesis</strong></p>
<hr/>
<p>Render finished dialogues to multi-speaker audio with XTTS-v2 voice
cloning, on CUDA, MPS, or CPU.</p>
<p><a href="/triagesim/guide/audio/"><span class="twemoji"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"></path></svg></span> Audio</a></p>
</li>
</ul>
</div>
<hr/>
<h2 id="install">Install<a class="headerlink" href="#install" title="Permanent link">¶</a></h2>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>pip<span class="w"> </span>install<span class="w"> </span>triagesim
</span></code></pre></div>
<p>Requires Python 3.11 or newer. See <a href="/triagesim/getting-started/installation/">Installation</a>
for the <code>redis</code> and <code>audio</code> extras.</p>
<h2 id="a-minimal-run">A minimal run<a class="headerlink" href="#a-minimal-run" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">TriageRunner</span><span class="p">,</span> <span class="n">RunnerConfig</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenRouterLLM</span><span class="p">,</span> <span class="n">NurseAgent</span><span class="p">,</span> <span class="n">PatientAgent</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="n">load_patient_personas</span><span class="p">,</span> <span class="n">load_nurse_personas</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a>
</span><span id="__span-1-6"><a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a><span class="n">patient_persona</span> <span class="o">=</span> <span class="n">load_patient_personas</span><span class="p">(</span><span class="s2">"patient.yaml"</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="__span-1-7"><a href="#__codelineno-1-7" id="__codelineno-1-7" name="__codelineno-1-7"></a><span class="n">nurse_persona</span> <span class="o">=</span> <span class="n">load_nurse_personas</span><span class="p">(</span><span class="s2">"nurse.yaml"</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="__span-1-8"><a href="#__codelineno-1-8" id="__codelineno-1-8" name="__codelineno-1-8"></a>
</span><span id="__span-1-9"><a href="#__codelineno-1-9" id="__codelineno-1-9" name="__codelineno-1-9"></a><span class="n">ground_truth</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-1-10"><a href="#__codelineno-1-10" id="__codelineno-1-10" name="__codelineno-1-10"></a>    <span class="s2">"chiefcomplaint"</span><span class="p">:</span> <span class="s2">"Syncope"</span><span class="p">,</span>
</span><span id="__span-1-11"><a href="#__codelineno-1-11" id="__codelineno-1-11" name="__codelineno-1-11"></a>    <span class="s2">"vitals"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"temperature"</span><span class="p">:</span> <span class="mf">99.1</span><span class="p">,</span> <span class="s2">"heartrate"</span><span class="p">:</span> <span class="mi">112</span><span class="p">,</span> <span class="s2">"resprate"</span><span class="p">:</span> <span class="mi">26</span><span class="p">,</span>
</span><span id="__span-1-12"><a href="#__codelineno-1-12" id="__codelineno-1-12" name="__codelineno-1-12"></a>               <span class="s2">"o2sat"</span><span class="p">:</span> <span class="mi">91</span><span class="p">,</span> <span class="s2">"sbp"</span><span class="p">:</span> <span class="mi">98</span><span class="p">},</span>
</span><span id="__span-1-13"><a href="#__codelineno-1-13" id="__codelineno-1-13" name="__codelineno-1-13"></a>    <span class="s2">"acuity"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
</span><span id="__span-1-14"><a href="#__codelineno-1-14" id="__codelineno-1-14" name="__codelineno-1-14"></a>    <span class="s2">"pain"</span><span class="p">:</span> <span class="mi">7</span><span class="p">,</span>
</span><span id="__span-1-15"><a href="#__codelineno-1-15" id="__codelineno-1-15" name="__codelineno-1-15"></a><span class="p">}</span>
</span><span id="__span-1-16"><a href="#__codelineno-1-16" id="__codelineno-1-16" name="__codelineno-1-16"></a>
</span><span id="__span-1-17"><a href="#__codelineno-1-17" id="__codelineno-1-17" name="__codelineno-1-17"></a><span class="n">model</span> <span class="o">=</span> <span class="s2">"anthropic/claude-sonnet-4-5"</span>
</span><span id="__span-1-18"><a href="#__codelineno-1-18" id="__codelineno-1-18" name="__codelineno-1-18"></a><span class="n">patient</span> <span class="o">=</span> <span class="n">PatientAgent</span><span class="p">(</span>
</span><span id="__span-1-19"><a href="#__codelineno-1-19" id="__codelineno-1-19" name="__codelineno-1-19"></a>    <span class="n">llm</span><span class="o">=</span><span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">model</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">PatientOutput</span><span class="p">),</span>
</span><span id="__span-1-20"><a href="#__codelineno-1-20" id="__codelineno-1-20" name="__codelineno-1-20"></a>    <span class="n">persona</span><span class="o">=</span><span class="n">patient_persona</span><span class="p">,</span>
</span><span id="__span-1-21"><a href="#__codelineno-1-21" id="__codelineno-1-21" name="__codelineno-1-21"></a><span class="p">)</span>
</span><span id="__span-1-22"><a href="#__codelineno-1-22" id="__codelineno-1-22" name="__codelineno-1-22"></a><span class="n">nurse</span> <span class="o">=</span> <span class="n">NurseAgent</span><span class="p">(</span>
</span><span id="__span-1-23"><a href="#__codelineno-1-23" id="__codelineno-1-23" name="__codelineno-1-23"></a>    <span class="n">llm</span><span class="o">=</span><span class="n">OpenRouterLLM</span><span class="p">(</span><span class="n">model_name</span><span class="o">=</span><span class="n">model</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">NurseOutput</span><span class="p">),</span>
</span><span id="__span-1-24"><a href="#__codelineno-1-24" id="__codelineno-1-24" name="__codelineno-1-24"></a>    <span class="n">persona</span><span class="o">=</span><span class="n">nurse_persona</span><span class="p">,</span>
</span><span id="__span-1-25"><a href="#__codelineno-1-25" id="__codelineno-1-25" name="__codelineno-1-25"></a>    <span class="n">algorithm</span><span class="o">=</span><span class="s2">"esi"</span><span class="p">,</span>
</span><span id="__span-1-26"><a href="#__codelineno-1-26" id="__codelineno-1-26" name="__codelineno-1-26"></a><span class="p">)</span>
</span><span id="__span-1-27"><a href="#__codelineno-1-27" id="__codelineno-1-27" name="__codelineno-1-27"></a>
</span><span id="__span-1-28"><a href="#__codelineno-1-28" id="__codelineno-1-28" name="__codelineno-1-28"></a><span class="n">artifact</span> <span class="o">=</span> <span class="n">TriageRunner</span><span class="p">(</span>
</span><span id="__span-1-29"><a href="#__codelineno-1-29" id="__codelineno-1-29" name="__codelineno-1-29"></a>    <span class="n">nurse_agent</span><span class="o">=</span><span class="n">nurse</span><span class="p">,</span>
</span><span id="__span-1-30"><a href="#__codelineno-1-30" id="__codelineno-1-30" name="__codelineno-1-30"></a>    <span class="n">patient_agent</span><span class="o">=</span><span class="n">patient</span><span class="p">,</span>
</span><span id="__span-1-31"><a href="#__codelineno-1-31" id="__codelineno-1-31" name="__codelineno-1-31"></a>    <span class="n">ground_truth</span><span class="o">=</span><span class="n">ground_truth</span><span class="p">,</span>
</span><span id="__span-1-32"><a href="#__codelineno-1-32" id="__codelineno-1-32" name="__codelineno-1-32"></a>    <span class="n">config</span><span class="o">=</span><span class="n">RunnerConfig</span><span class="p">(</span><span class="n">max_turns</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">),</span>
</span><span id="__span-1-33"><a href="#__codelineno-1-33" id="__codelineno-1-33" name="__codelineno-1-33"></a><span class="p">)</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span><span id="__span-1-34"><a href="#__codelineno-1-34" id="__codelineno-1-34" name="__codelineno-1-34"></a>
</span><span id="__span-1-35"><a href="#__codelineno-1-35" id="__codelineno-1-35" name="__codelineno-1-35"></a><span class="nb">print</span><span class="p">(</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">][</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</span></code></pre></div>
<p>Walk through this line by line in the <a href="/triagesim/getting-started/quickstart/">Quick start</a>.</p>
<hr/>
<h2 id="citing">Citing<a class="headerlink" href="#citing" title="Permanent link">¶</a></h2>
<p>TriageSim accompanies a research paper. If you use it, please
<a href="/triagesim/citation/">cite the work</a>.</p>
<div class="admonition warning">
<p class="admonition-title">Research software</p>
<p>TriageSim generates <strong>synthetic</strong> data for research on speech and language
systems. It is not a clinical decision support tool and must not be used to
triage real patients.</p>
</div>
