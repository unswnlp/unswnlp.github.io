---
title: "Evaluation metrics"
---

<h1 id="evaluation-metrics">Evaluation metrics<a class="headerlink" href="#evaluation-metrics" title="Permanent link">¶</a></h1>
<p><code>triagesim.utils</code> scores a finished run against its ground truth. Every
function consumes only environment output — the artifact's <code>trace</code>, <code>belief</code>
and <code>ground_truth</code> — so metrics can be recomputed offline from a saved JSON
file, with no model calls and no agent internals.</p>
<p>The functions degrade gracefully: when something needed is missing they return
<code>None</code> rather than raising, so a batch job does not die on one malformed run.</p>
<h2 id="compute_all_metrics"><code>compute_all_metrics</code><a class="headerlink" href="#compute_all_metrics" title="Permanent link">¶</a></h2>
<p>The orchestrator. It is <strong>keyword-only</strong>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="n">metrics</span> <span class="o">=</span> <span class="n">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">trace</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">],</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">belief</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"belief"</span><span class="p">],</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="n">ground_truth</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"ground_truth"</span><span class="p">],</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a>    <span class="n">expert_red_flags</span><span class="o">=</span><span class="p">{</span><span class="s2">"syncope"</span><span class="p">,</span> <span class="s2">"hypoxia"</span><span class="p">,</span> <span class="s2">"tachycardia"</span><span class="p">},</span>  <span class="c1"># optional</span>
</span><span id="__span-0-8"><a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a><span class="p">)</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>trace</code></td>
<td><code>list[dict]</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>belief</code></td>
<td><code>dict</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>ground_truth</code></td>
<td><code>dict</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>expert_red_flags</code></td>
<td><code>set[str] \| None</code></td>
<td>No</td>
</tr>
</tbody>
</table>
<p>It returns a four-key nested dict:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="p">{</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a>    <span class="s2">"triage"</span><span class="p">:</span> <span class="p">{</span><span class="o">...</span><span class="p">},</span>           <span class="c1"># triage_decision_metrics + first_correct_turn</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a>    <span class="s2">"belief_coverage"</span><span class="p">:</span> <span class="p">{</span><span class="o">...</span><span class="p">},</span>  <span class="c1"># belief_coverage_metrics</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a>    <span class="s2">"red_flags"</span><span class="p">:</span> <span class="p">{</span><span class="o">...</span><span class="p">},</span>        <span class="c1"># red_flag_metrics</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a>    <span class="s2">"explanation"</span><span class="p">:</span> <span class="p">{</span><span class="o">...</span><span class="p">},</span>      <span class="c1"># explanation_support_metrics</span>
</span><span id="__span-1-6"><a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a><span class="p">}</span>
</span></code></pre></div>
<p>Note that <code>time_to_first_correct_triage</code> is not a separate top-level key — its
value is merged into <code>metrics["triage"]["first_correct_turn"]</code>.</p>
<h2 id="triage_decision_metrics"><code>triage_decision_metrics</code><a class="headerlink" href="#triage_decision_metrics" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="n">triage_decision_metrics</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">ground_truth</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span>
</span></code></pre></div>
<p>Compares the final predicted triage level against <code>ground_truth["acuity"]</code>.</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ground_truth</code></td>
<td><code>int \| None</code></td>
<td>The reference acuity.</td>
</tr>
<tr>
<td><code>final_prediction</code></td>
<td><code>int \| None</code></td>
<td>Last triage level in the trace.</td>
</tr>
<tr>
<td><code>correct</code></td>
<td><code>bool \| None</code></td>
<td>Exact match.</td>
</tr>
<tr>
<td><code>absolute_error</code></td>
<td><code>int \| None</code></td>
<td><code>abs(pred - gt)</code> — how many levels off.</td>
</tr>
<tr>
<td><code>over_triage</code></td>
<td><code>bool \| None</code></td>
<td>Treated as more urgent than truth.</td>
</tr>
<tr>
<td><code>under_triage</code></td>
<td><code>bool \| None</code></td>
<td>Treated as less urgent than truth.</td>
</tr>
</tbody>
</table>
<h3 id="the-sign-convention">The sign convention<a class="headerlink" href="#the-sign-convention" title="Permanent link">¶</a></h3>
<p>Both ESI and ATS run 1 (most urgent) to 5 (least urgent), so the arithmetic
inverts the intuition:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="n">error</span> <span class="o">=</span> <span class="n">pred</span> <span class="o">-</span> <span class="n">gt</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a><span class="n">over_triage</span>  <span class="o">=</span> <span class="n">error</span> <span class="o">&lt;</span> <span class="mi">0</span>   <span class="c1"># predicted a LOWER number = MORE urgent</span>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a><span class="n">under_triage</span> <span class="o">=</span> <span class="n">error</span> <span class="o">&gt;</span> <span class="mi">0</span>   <span class="c1"># predicted a HIGHER number = LESS urgent</span>
</span></code></pre></div>
<p>A prediction of 1 against a true acuity of 3 gives <code>error = -2</code>, which is
<strong>over</strong>-triage: the nurse escalated a patient who did not need it. The reverse
— predicting 4 for a true acuity of 2 — is under-triage, the clinically
dangerous direction.</p>
<div class="admonition warning">
<p class="admonition-title">Under-triage is the failure mode that matters</p>
<p>Over- and under-triage are not symmetric harms. Over-triage wastes
resources; under-triage delays care for someone who is deteriorating. Report
them separately rather than collapsing both into <code>absolute_error</code>.</p>
</div>
<p>If either <code>acuity</code> is absent from the ground truth or no triage level appears in
the trace, every field except the first two is <code>None</code>.</p>
<h3 id="how-the-final-prediction-is-found">How the final prediction is found<a class="headerlink" href="#how-the-final-prediction-is-found" title="Permanent link">¶</a></h3>
<p>The trace is scanned in reverse. The first entry whose <code>action.type</code> is <code>"end"</code>
supplies its triage level; otherwise the most recent action carrying a <code>triage</code>
key wins. Since <code>utterance</code> and <code>end</code> actions record a triage level but
<code>check_vital</code> and <code>log_red_flag</code> actions do not, this resolves to the last
<em>spoken or final</em> decision.</p>
<h2 id="time_to_first_correct_triage"><code>time_to_first_correct_triage</code><a class="headerlink" href="#time_to_first_correct_triage" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="n">time_to_first_correct_triage</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">ground_truth</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span>
</span></code></pre></div>
<p>Returns the turn index at which the nurse <strong>first</strong> stated the correct level, or
<code>None</code> if it never did — or if <code>acuity</code> is missing.</p>
<p>This measures efficiency separately from accuracy. Two runs can both finish
correct while one took twelve turns and the other took three.</p>
<div class="admonition note">
<p class="admonition-title">First, not final</p>
<p>The nurse may state the right level early, revise away from it, and land
somewhere else. A run can therefore have <code>first_correct_turn == 2</code> and
<code>correct == False</code>. Read the two together.</p>
</div>
<h2 id="belief_coverage_metrics"><code>belief_coverage_metrics</code><a class="headerlink" href="#belief_coverage_metrics" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="n">belief_coverage_metrics</span><span class="p">(</span><span class="n">belief</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span>
</span></code></pre></div>
<p>Structural measures of how much was elicited. No ground truth is needed.</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>num_associated_symptoms</code></td>
<td><code>int</code></td>
<td>Distinct associated symptoms in the belief state.</td>
</tr>
<tr>
<td><code>num_red_flags_inferred</code></td>
<td><code>int</code></td>
<td>Values under the <code>red_flags</code> belief slot.</td>
</tr>
<tr>
<td><code>has_chief_complaint</code></td>
<td><code>bool</code></td>
<td>Chief complaint was established.</td>
</tr>
<tr>
<td><code>has_pain_location</code></td>
<td><code>bool</code></td>
<td>Pain location was established.</td>
</tr>
<tr>
<td><code>has_pain_severity</code></td>
<td><code>bool</code></td>
<td>Pain severity was established.</td>
</tr>
<tr>
<td><code>has_duration</code></td>
<td><code>bool</code></td>
<td>Symptom duration was established.</td>
</tr>
<tr>
<td><code>vitals_known</code></td>
<td><code>list[str]</code></td>
<td>Which vitals were released.</td>
</tr>
<tr>
<td><code>num_vitals_known</code></td>
<td><code>int</code></td>
<td>How many, of the five available.</td>
</tr>
</tbody>
</table>
<p>Useful for asking whether a correct decision was actually <em>earned</em>: a nurse that
guesses the right acuity with <code>num_vitals_known == 0</code> and no pain severity got
lucky.</p>
<h2 id="red_flag_metrics"><code>red_flag_metrics</code><a class="headerlink" href="#red_flag_metrics" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="n">red_flag_metrics</span><span class="p">(</span><span class="n">belief</span><span class="p">,</span> <span class="n">expert_red_flags</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span>
</span></code></pre></div>
<p>Scores the flags the nurse explicitly logged, read from
<code>belief["red_flags_logged"]</code>.</p>
<p>Without expert annotations you get three descriptive keys:</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>num_red_flags_logged</code></td>
<td><code>int</code></td>
</tr>
<tr>
<td><code>logged_any</code></td>
<td><code>bool</code></td>
</tr>
<tr>
<td><code>logged_flags</code></td>
<td><code>list[str]</code>, sorted</td>
</tr>
</tbody>
</table>
<p>Passing <code>expert_red_flags</code> adds set-comparison keys:</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>expert_red_flags</code></td>
<td><code>list[str]</code></td>
<td>The reference set, sorted.</td>
</tr>
<tr>
<td><code>true_positives</code></td>
<td><code>list[str]</code></td>
<td>Logged and expected.</td>
</tr>
<tr>
<td><code>false_positives</code></td>
<td><code>list[str]</code></td>
<td>Logged but not expected.</td>
</tr>
<tr>
<td><code>false_negatives</code></td>
<td><code>list[str]</code></td>
<td>Expected but missed.</td>
</tr>
<tr>
<td><code>precision</code></td>
<td><code>float \| None</code></td>
<td><code>None</code> when nothing was logged.</td>
</tr>
<tr>
<td><code>recall</code></td>
<td><code>float \| None</code></td>
<td><code>None</code> when the expert set is empty.</td>
</tr>
</tbody>
</table>
<div class="admonition warning">
<p class="admonition-title">Matching is exact string equality</p>
<p><code>"tachycardia"</code> and <code>"Tachycardia"</code> are different flags to this function, as
are <code>"hypoxia"</code> and <code>"low oxygen saturation"</code>. The environment normalises
case and whitespace when accepting flags, but it does not map synonyms.
Normalise your expert set to lowercase, and expect free-text paraphrases to
depress precision and recall in ways that reflect vocabulary rather than
clinical judgement.</p>
</div>
<p>F1 is not computed. Derive it if you need it:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-7-1"><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="n">p</span><span class="p">,</span> <span class="n">r</span> <span class="o">=</span> <span class="n">metrics</span><span class="p">[</span><span class="s2">"red_flags"</span><span class="p">][</span><span class="s2">"precision"</span><span class="p">],</span> <span class="n">metrics</span><span class="p">[</span><span class="s2">"red_flags"</span><span class="p">][</span><span class="s2">"recall"</span><span class="p">]</span>
</span><span id="__span-7-2"><a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a><span class="n">f1</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">p</span> <span class="o">*</span> <span class="n">r</span> <span class="o">/</span> <span class="p">(</span><span class="n">p</span> <span class="o">+</span> <span class="n">r</span><span class="p">)</span> <span class="k">if</span> <span class="n">p</span> <span class="ow">and</span> <span class="n">r</span> <span class="k">else</span> <span class="kc">None</span>
</span></code></pre></div>
<h2 id="explanation_support_metrics"><code>explanation_support_metrics</code><a class="headerlink" href="#explanation_support_metrics" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-8-1"><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a><span class="n">explanation_support_metrics</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">belief</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>has_explanation</code></td>
<td><code>bool</code></td>
<td>An explanation was found on the final nurse action.</td>
</tr>
<tr>
<td><code>explanation_length</code></td>
<td><code>int</code></td>
<td>Word count, or <code>0</code>.</td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">This is a placeholder</p>
<p>The source marks this function as hooks-only, with faithfulness checks —
citation overlap, evidence hallucination — listed as future work. It reads
the explanation from the final nurse action's <code>action</code> dict, where
explanations are not stored, so in practice <code>has_explanation</code> will typically
be <code>False</code> even when the trace contains rich reasoning.</p>
<p>To analyse explanations today, read them from the trace entries directly:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-9-1"><a href="#__codelineno-9-1" id="__codelineno-9-1" name="__codelineno-9-1"></a><span class="n">explanations</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="__span-9-2"><a href="#__codelineno-9-2" id="__codelineno-9-2" name="__codelineno-9-2"></a>    <span class="n">step</span><span class="p">[</span><span class="s2">"explanation"</span><span class="p">]</span> <span class="k">for</span> <span class="n">step</span> <span class="ow">in</span> <span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">]</span>
</span><span id="__span-9-3"><a href="#__codelineno-9-3" id="__codelineno-9-3" name="__codelineno-9-3"></a>    <span class="k">if</span> <span class="n">step</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"explanation"</span><span class="p">)</span>
</span><span id="__span-9-4"><a href="#__codelineno-9-4" id="__codelineno-9-4" name="__codelineno-9-4"></a><span class="p">]</span>
</span></code></pre></div>
</div>
<h2 id="aggregating-across-runs">Aggregating across runs<a class="headerlink" href="#aggregating-across-runs" title="Permanent link">¶</a></h2>
<p>Single runs are noisy — the models sample, so the same configuration produces
different dialogues. Aggregate before drawing conclusions:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-10-1"><a href="#__codelineno-10-1" id="__codelineno-10-1" name="__codelineno-10-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
</span><span id="__span-10-2"><a href="#__codelineno-10-2" id="__codelineno-10-2" name="__codelineno-10-2"></a><span class="kn">import</span><span class="w"> </span><span class="nn">statistics</span>
</span><span id="__span-10-3"><a href="#__codelineno-10-3" id="__codelineno-10-3" name="__codelineno-10-3"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>
</span><span id="__span-10-4"><a href="#__codelineno-10-4" id="__codelineno-10-4" name="__codelineno-10-4"></a>
</span><span id="__span-10-5"><a href="#__codelineno-10-5" id="__codelineno-10-5" name="__codelineno-10-5"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span><span id="__span-10-6"><a href="#__codelineno-10-6" id="__codelineno-10-6" name="__codelineno-10-6"></a>
</span><span id="__span-10-7"><a href="#__codelineno-10-7" id="__codelineno-10-7" name="__codelineno-10-7"></a><span class="n">EXPERT_FLAGS</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"syncope"</span><span class="p">,</span> <span class="s2">"tachycardia"</span><span class="p">,</span> <span class="s2">"hypoxia"</span><span class="p">}</span>
</span><span id="__span-10-8"><a href="#__codelineno-10-8" id="__codelineno-10-8" name="__codelineno-10-8"></a>
</span><span id="__span-10-9"><a href="#__codelineno-10-9" id="__codelineno-10-9" name="__codelineno-10-9"></a><span class="n">rows</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-10-10"><a href="#__codelineno-10-10" id="__codelineno-10-10" name="__codelineno-10-10"></a><span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="s2">"runs"</span><span class="p">)</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="s2">"*.json"</span><span class="p">)):</span>
</span><span id="__span-10-11"><a href="#__codelineno-10-11" id="__codelineno-10-11" name="__codelineno-10-11"></a>    <span class="n">artifact</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">path</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
</span><span id="__span-10-12"><a href="#__codelineno-10-12" id="__codelineno-10-12" name="__codelineno-10-12"></a>    <span class="n">rows</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-10-13"><a href="#__codelineno-10-13" id="__codelineno-10-13" name="__codelineno-10-13"></a>        <span class="n">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-10-14"><a href="#__codelineno-10-14" id="__codelineno-10-14" name="__codelineno-10-14"></a>            <span class="n">trace</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">],</span>
</span><span id="__span-10-15"><a href="#__codelineno-10-15" id="__codelineno-10-15" name="__codelineno-10-15"></a>            <span class="n">belief</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"belief"</span><span class="p">],</span>
</span><span id="__span-10-16"><a href="#__codelineno-10-16" id="__codelineno-10-16" name="__codelineno-10-16"></a>            <span class="n">ground_truth</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"ground_truth"</span><span class="p">],</span>
</span><span id="__span-10-17"><a href="#__codelineno-10-17" id="__codelineno-10-17" name="__codelineno-10-17"></a>            <span class="n">expert_red_flags</span><span class="o">=</span><span class="n">EXPERT_FLAGS</span><span class="p">,</span>
</span><span id="__span-10-18"><a href="#__codelineno-10-18" id="__codelineno-10-18" name="__codelineno-10-18"></a>        <span class="p">)</span>
</span><span id="__span-10-19"><a href="#__codelineno-10-19" id="__codelineno-10-19" name="__codelineno-10-19"></a>    <span class="p">)</span>
</span><span id="__span-10-20"><a href="#__codelineno-10-20" id="__codelineno-10-20" name="__codelineno-10-20"></a>
</span><span id="__span-10-21"><a href="#__codelineno-10-21" id="__codelineno-10-21" name="__codelineno-10-21"></a><span class="n">scored</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">rows</span> <span class="k">if</span> <span class="n">r</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"correct"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="__span-10-22"><a href="#__codelineno-10-22" id="__codelineno-10-22" name="__codelineno-10-22"></a><span class="n">errors</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"absolute_error"</span><span class="p">]</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">scored</span><span class="p">]</span>
</span><span id="__span-10-23"><a href="#__codelineno-10-23" id="__codelineno-10-23" name="__codelineno-10-23"></a>
</span><span id="__span-10-24"><a href="#__codelineno-10-24" id="__codelineno-10-24" name="__codelineno-10-24"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"runs scored:   </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">scored</span><span class="p">)</span><span class="si">}</span><span class="s2">/</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">rows</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-10-25"><a href="#__codelineno-10-25" id="__codelineno-10-25" name="__codelineno-10-25"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"accuracy:      </span><span class="si">{</span><span class="nb">sum</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="s1">'triage'</span><span class="p">][</span><span class="s1">'correct'</span><span class="p">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">r</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">scored</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="nb">len</span><span class="p">(</span><span class="n">scored</span><span class="p">)</span><span class="si">:</span><span class="s2">.2%</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-10-26"><a href="#__codelineno-10-26" id="__codelineno-10-26" name="__codelineno-10-26"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"under-triage:  </span><span class="si">{</span><span class="nb">sum</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="s1">'triage'</span><span class="p">][</span><span class="s1">'under_triage'</span><span class="p">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">r</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">scored</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="nb">len</span><span class="p">(</span><span class="n">scored</span><span class="p">)</span><span class="si">:</span><span class="s2">.2%</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-10-27"><a href="#__codelineno-10-27" id="__codelineno-10-27" name="__codelineno-10-27"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"over-triage:   </span><span class="si">{</span><span class="nb">sum</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="s1">'triage'</span><span class="p">][</span><span class="s1">'over_triage'</span><span class="p">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">r</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">scored</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="nb">len</span><span class="p">(</span><span class="n">scored</span><span class="p">)</span><span class="si">:</span><span class="s2">.2%</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-10-28"><a href="#__codelineno-10-28" id="__codelineno-10-28" name="__codelineno-10-28"></a><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"mean abs err:  </span><span class="si">{</span><span class="n">statistics</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">errors</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-10-29"><a href="#__codelineno-10-29" id="__codelineno-10-29" name="__codelineno-10-29"></a>
</span><span id="__span-10-30"><a href="#__codelineno-10-30" id="__codelineno-10-30" name="__codelineno-10-30"></a><span class="n">turns</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"first_correct_turn"</span><span class="p">]</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">scored</span>
</span><span id="__span-10-31"><a href="#__codelineno-10-31" id="__codelineno-10-31" name="__codelineno-10-31"></a>         <span class="k">if</span> <span class="n">r</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"first_correct_turn"</span><span class="p">]</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="__span-10-32"><a href="#__codelineno-10-32" id="__codelineno-10-32" name="__codelineno-10-32"></a><span class="k">if</span> <span class="n">turns</span><span class="p">:</span>
</span><span id="__span-10-33"><a href="#__codelineno-10-33" id="__codelineno-10-33" name="__codelineno-10-33"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"median turns to first correct: </span><span class="si">{</span><span class="n">statistics</span><span class="o">.</span><span class="n">median</span><span class="p">(</span><span class="n">turns</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span></code></pre></div>
<p>Filtering on <code>correct is not None</code> matters: unscorable runs would otherwise be
counted as failures and quietly bias the accuracy downward.</p>
