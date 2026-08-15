---
title: "Personas"
type: "docsite"
docSite: "triagesim"
---

<h1 id="personas">Personas<a class="headerlink" href="#personas" title="Permanent link">¶</a></h1>
<p>Personas are how you control <em>who</em> is in the room. Both agents are conditioned
on a persona object that shapes how they speak, what they remember, and how
they reason. Because personas are data rather than code, you can build a pool
once and slice it into experimental conditions.</p>
<h2 id="patient-personas">Patient personas<a class="headerlink" href="#patient-personas" title="Permanent link">¶</a></h2>
<p><code>PatientPersona</code> is a Pydantic model with fourteen required string fields and
one optional free-text field.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>age_group</code></td>
<td>Broad age band, e.g. <code>child</code>, <code>adult</code>, <code>elderly</code>.</td>
</tr>
<tr>
<td><code>gender</code></td>
<td>Patient gender.</td>
</tr>
<tr>
<td><code>ethnicity</code></td>
<td>Cultural and linguistic background.</td>
</tr>
<tr>
<td><code>socioeconomic_status</code></td>
<td>e.g. <code>low</code>, <code>middle</code>, <code>high</code>.</td>
</tr>
<tr>
<td><code>language_proficiency</code></td>
<td>Fluency in the language of the consultation.</td>
</tr>
<tr>
<td><code>recall_accuracy</code></td>
<td>How reliably the patient remembers onset, timing and history.</td>
</tr>
<tr>
<td><code>cognitive_state</code></td>
<td>e.g. <code>clear</code>, <code>confused</code>, <code>drowsy</code>.</td>
</tr>
<tr>
<td><code>trust_in_healthcare</code></td>
<td>Willingness to disclose fully to a clinician.</td>
</tr>
<tr>
<td><code>pain_expression</code></td>
<td>How strongly pain is verbalised — <code>stoic</code> through <code>dramatic</code>.</td>
</tr>
<tr>
<td><code>reactivity_to_clinician_emotion</code></td>
<td>How much the nurse's tone shifts the patient's behaviour.</td>
</tr>
<tr>
<td><code>emotion_regulation</code></td>
<td>e.g. <code>stable</code>, <code>labile</code>.</td>
</tr>
<tr>
<td><code>disfluency_rate</code></td>
<td>Frequency of hesitations, restarts and fillers.</td>
</tr>
<tr>
<td><code>topic_drift</code></td>
<td>Tendency to wander off the clinical question.</td>
</tr>
<tr>
<td><code>verbosity</code></td>
<td>Typical response length.</td>
</tr>
<tr>
<td><code>instruction</code></td>
<td><em>Optional.</em> Free-text instruction describing how the patient should speak.</td>
</tr>
</tbody>
</table>
<div class="admonition warning">
<p class="admonition-title"><code>verbosity</code>, not <code>response_length</code></p>
<p>Some older examples show a <code>response_length</code> field for patients. The schema
field is <code>verbosity</code>. A file using <code>response_length</code> will not populate the
field you expect.</p>
</div>
<div class="language-yaml highlight"><span class="filename">patient.yaml</span><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">age_group</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">elderly</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="w">  </span><span class="nt">gender</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">male</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="w">  </span><span class="nt">ethnicity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">Vietnamese-Australian</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="w">  </span><span class="nt">socioeconomic_status</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="w">  </span><span class="nt">language_proficiency</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">limited</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a><span class="w">  </span><span class="nt">recall_accuracy</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a><span class="w">  </span><span class="nt">cognitive_state</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">mildly confused</span>
</span><span id="__span-0-8"><a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a><span class="w">  </span><span class="nt">trust_in_healthcare</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-9"><a href="#__codelineno-0-9" id="__codelineno-0-9" name="__codelineno-0-9"></a><span class="w">  </span><span class="nt">pain_expression</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">stoic</span>
</span><span id="__span-0-10"><a href="#__codelineno-0-10" id="__codelineno-0-10" name="__codelineno-0-10"></a><span class="w">  </span><span class="nt">reactivity_to_clinician_emotion</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-11"><a href="#__codelineno-0-11" id="__codelineno-0-11" name="__codelineno-0-11"></a><span class="w">  </span><span class="nt">emotion_regulation</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">stable</span>
</span><span id="__span-0-12"><a href="#__codelineno-0-12" id="__codelineno-0-12" name="__codelineno-0-12"></a><span class="w">  </span><span class="nt">disfluency_rate</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-13"><a href="#__codelineno-0-13" id="__codelineno-0-13" name="__codelineno-0-13"></a><span class="w">  </span><span class="nt">topic_drift</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-14"><a href="#__codelineno-0-14" id="__codelineno-0-14" name="__codelineno-0-14"></a><span class="w">  </span><span class="nt">verbosity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">short</span>
</span><span id="__span-0-15"><a href="#__codelineno-0-15" id="__codelineno-0-15" name="__codelineno-0-15"></a><span class="w">  </span><span class="nt">instruction</span><span class="p">:</span><span class="w"> </span><span class="p p-Indicator">&gt;-</span>
</span><span id="__span-0-16"><a href="#__codelineno-0-16" id="__codelineno-0-16" name="__codelineno-0-16"></a><span class="w">    </span><span class="no">Speaks in short sentences with frequent pauses. Occasionally substitutes a</span>
</span><span id="__span-0-17"><a href="#__codelineno-0-17" id="__codelineno-0-17" name="__codelineno-0-17"></a><span class="w">    </span><span class="no">Vietnamese word when the English one does not come to mind. Downplays pain.</span>
</span><span id="__span-0-18"><a href="#__codelineno-0-18" id="__codelineno-0-18" name="__codelineno-0-18"></a>
</span><span id="__span-0-19"><a href="#__codelineno-0-19" id="__codelineno-0-19" name="__codelineno-0-19"></a><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">age_group</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">adult</span>
</span><span id="__span-0-20"><a href="#__codelineno-0-20" id="__codelineno-0-20" name="__codelineno-0-20"></a><span class="w">  </span><span class="nt">gender</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">female</span>
</span><span id="__span-0-21"><a href="#__codelineno-0-21" id="__codelineno-0-21" name="__codelineno-0-21"></a><span class="w">  </span><span class="nt">ethnicity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">Australian</span>
</span><span id="__span-0-22"><a href="#__codelineno-0-22" id="__codelineno-0-22" name="__codelineno-0-22"></a><span class="w">  </span><span class="nt">socioeconomic_status</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">middle</span>
</span><span id="__span-0-23"><a href="#__codelineno-0-23" id="__codelineno-0-23" name="__codelineno-0-23"></a><span class="w">  </span><span class="nt">language_proficiency</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-24"><a href="#__codelineno-0-24" id="__codelineno-0-24" name="__codelineno-0-24"></a><span class="w">  </span><span class="nt">recall_accuracy</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-25"><a href="#__codelineno-0-25" id="__codelineno-0-25" name="__codelineno-0-25"></a><span class="w">  </span><span class="nt">cognitive_state</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">clear</span>
</span><span id="__span-0-26"><a href="#__codelineno-0-26" id="__codelineno-0-26" name="__codelineno-0-26"></a><span class="w">  </span><span class="nt">trust_in_healthcare</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-0-27"><a href="#__codelineno-0-27" id="__codelineno-0-27" name="__codelineno-0-27"></a><span class="w">  </span><span class="nt">pain_expression</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">moderate</span>
</span><span id="__span-0-28"><a href="#__codelineno-0-28" id="__codelineno-0-28" name="__codelineno-0-28"></a><span class="w">  </span><span class="nt">reactivity_to_clinician_emotion</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-29"><a href="#__codelineno-0-29" id="__codelineno-0-29" name="__codelineno-0-29"></a><span class="w">  </span><span class="nt">emotion_regulation</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">stable</span>
</span><span id="__span-0-30"><a href="#__codelineno-0-30" id="__codelineno-0-30" name="__codelineno-0-30"></a><span class="w">  </span><span class="nt">disfluency_rate</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-31"><a href="#__codelineno-0-31" id="__codelineno-0-31" name="__codelineno-0-31"></a><span class="w">  </span><span class="nt">topic_drift</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-0-32"><a href="#__codelineno-0-32" id="__codelineno-0-32" name="__codelineno-0-32"></a><span class="w">  </span><span class="nt">verbosity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">medium</span>
</span></code></pre></div>
<h2 id="nurse-personas">Nurse personas<a class="headerlink" href="#nurse-personas" title="Permanent link">¶</a></h2>
<p><code>NursePersona</code> has eight required string fields plus the same optional
<code>instruction</code>.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gender</code></td>
<td>Nurse gender.</td>
</tr>
<tr>
<td><code>ethnicity</code></td>
<td>Cultural and linguistic background.</td>
</tr>
<tr>
<td><code>experience_level</code></td>
<td>e.g. <code>graduate</code>, <code>mid-level</code>, <code>senior</code>.</td>
</tr>
<tr>
<td><code>risk_tolerance</code></td>
<td>Willingness to accept diagnostic uncertainty before deciding.</td>
</tr>
<tr>
<td><code>guideline_adherence</code></td>
<td>How strictly the triage protocol is followed.</td>
</tr>
<tr>
<td><code>communication_style</code></td>
<td>e.g. <code>direct</code>, <code>warm</code>, <code>clipped</code>.</td>
</tr>
<tr>
<td><code>verbosity</code></td>
<td>Typical utterance length.</td>
</tr>
<tr>
<td><code>emotional_expression</code></td>
<td>e.g. <code>neutral</code>, <code>reassuring</code>, <code>brusque</code>.</td>
</tr>
<tr>
<td><code>instruction</code></td>
<td><em>Optional.</em> Free-text instruction describing how the nurse should speak.</td>
</tr>
</tbody>
</table>
<div class="language-yaml highlight"><span class="filename">nurse.yaml</span><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">gender</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">female</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="w">  </span><span class="nt">ethnicity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">Australian</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="w">  </span><span class="nt">experience_level</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">senior</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="w">  </span><span class="nt">risk_tolerance</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">low</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a><span class="w">  </span><span class="nt">guideline_adherence</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-1-6"><a href="#__codelineno-1-6" id="__codelineno-1-6" name="__codelineno-1-6"></a><span class="w">  </span><span class="nt">communication_style</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">direct</span>
</span><span id="__span-1-7"><a href="#__codelineno-1-7" id="__codelineno-1-7" name="__codelineno-1-7"></a><span class="w">  </span><span class="nt">verbosity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">medium</span>
</span><span id="__span-1-8"><a href="#__codelineno-1-8" id="__codelineno-1-8" name="__codelineno-1-8"></a><span class="w">  </span><span class="nt">emotional_expression</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">neutral</span>
</span><span id="__span-1-9"><a href="#__codelineno-1-9" id="__codelineno-1-9" name="__codelineno-1-9"></a>
</span><span id="__span-1-10"><a href="#__codelineno-1-10" id="__codelineno-1-10" name="__codelineno-1-10"></a><span class="p p-Indicator">-</span><span class="w"> </span><span class="nt">gender</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">male</span>
</span><span id="__span-1-11"><a href="#__codelineno-1-11" id="__codelineno-1-11" name="__codelineno-1-11"></a><span class="w">  </span><span class="nt">ethnicity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">Indian-Australian</span>
</span><span id="__span-1-12"><a href="#__codelineno-1-12" id="__codelineno-1-12" name="__codelineno-1-12"></a><span class="w">  </span><span class="nt">experience_level</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">graduate</span>
</span><span id="__span-1-13"><a href="#__codelineno-1-13" id="__codelineno-1-13" name="__codelineno-1-13"></a><span class="w">  </span><span class="nt">risk_tolerance</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-1-14"><a href="#__codelineno-1-14" id="__codelineno-1-14" name="__codelineno-1-14"></a><span class="w">  </span><span class="nt">guideline_adherence</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">medium</span>
</span><span id="__span-1-15"><a href="#__codelineno-1-15" id="__codelineno-1-15" name="__codelineno-1-15"></a><span class="w">  </span><span class="nt">communication_style</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">warm</span>
</span><span id="__span-1-16"><a href="#__codelineno-1-16" id="__codelineno-1-16" name="__codelineno-1-16"></a><span class="w">  </span><span class="nt">verbosity</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">high</span>
</span><span id="__span-1-17"><a href="#__codelineno-1-17" id="__codelineno-1-17" name="__codelineno-1-17"></a><span class="w">  </span><span class="nt">emotional_expression</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">reassuring</span>
</span><span id="__span-1-18"><a href="#__codelineno-1-18" id="__codelineno-1-18" name="__codelineno-1-18"></a><span class="w">  </span><span class="nt">instruction</span><span class="p">:</span><span class="w"> </span><span class="p p-Indicator">&gt;-</span>
</span><span id="__span-1-19"><a href="#__codelineno-1-19" id="__codelineno-1-19" name="__codelineno-1-19"></a><span class="w">    </span><span class="no">Checks understanding often and apologises for repeating questions.</span>
</span></code></pre></div>
<div class="admonition tip">
<p class="admonition-title">Fields are free-form strings</p>
<p>None of these fields is an enum. <code>experience_level: "12 years in a rural ED"</code>
is as valid as <code>"senior"</code> — it is interpolated into the prompt as written.
That flexibility is deliberate, but it also means typos pass validation
silently.</p>
</div>
<h2 id="loading">Loading<a class="headerlink" href="#loading" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="n">load_patient_personas</span><span class="p">,</span> <span class="n">load_nurse_personas</span>
</span><span id="__span-2-2"><a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a>
</span><span id="__span-2-3"><a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a><span class="n">patients</span> <span class="o">=</span> <span class="n">load_patient_personas</span><span class="p">(</span><span class="s2">"patient.yaml"</span><span class="p">)</span>
</span><span id="__span-2-4"><a href="#__codelineno-2-4" id="__codelineno-2-4" name="__codelineno-2-4"></a><span class="n">nurses</span> <span class="o">=</span> <span class="n">load_nurse_personas</span><span class="p">(</span><span class="s2">"nurse.yaml"</span><span class="p">)</span>
</span></code></pre></div>
<p>Each function reads a YAML file containing a <strong>list</strong> of mappings and returns a
list of validated persona objects.</p>
<p>Missing required fields do not raise. The loader fills any absent required field
with a default before validation, so a partial persona still constructs — with
the unspecified traits taking a neutral value rather than the one you meant.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Because absent fields are silently defaulted, a misspelled key (say
<code>verbosty</code>) will not error. It will be dropped and the real <code>verbosity</code>
field will be defaulted. Validate your persona files if they are
machine-generated.</p>
</div>
<h2 id="sampling">Sampling<a class="headerlink" href="#sampling" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="n">sample_patient_personas</span><span class="p">,</span> <span class="n">sample_nurse_personas</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a><span class="n">chosen</span> <span class="o">=</span> <span class="n">sample_patient_personas</span><span class="p">(</span><span class="n">patients</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</span></code></pre></div>
<p>Sampling is <strong>without replacement</strong> and uses a local <code>random.Random(seed)</code>
instance, so it does not disturb the global RNG. The same <code>seed</code> and the same
input list always yield the same selection.</p>
<p>Requesting more personas than exist raises <code>ValueError</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="n">sample_patient_personas</span><span class="p">(</span><span class="n">patients</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a><span class="c1"># ValueError: Cannot sample k=100 personas from population of size 2</span>
</span></code></pre></div>
<h2 id="filtering">Filtering<a class="headerlink" href="#filtering" title="Permanent link">¶</a></h2>
<p><code>filter_patient_personas</code> and <code>filter_nurse_personas</code> take a criteria dict and
keep only personas where <strong>every</strong> field matches exactly:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="n">filter_patient_personas</span>
</span><span id="__span-5-2"><a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>
</span><span id="__span-5-3"><a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a><span class="n">low_proficiency</span> <span class="o">=</span> <span class="n">filter_patient_personas</span><span class="p">(</span>
</span><span id="__span-5-4"><a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a>    <span class="n">patients</span><span class="p">,</span>
</span><span id="__span-5-5"><a href="#__codelineno-5-5" id="__codelineno-5-5" name="__codelineno-5-5"></a>    <span class="p">{</span><span class="s2">"language_proficiency"</span><span class="p">:</span> <span class="s2">"limited"</span><span class="p">,</span> <span class="s2">"trust_in_healthcare"</span><span class="p">:</span> <span class="s2">"low"</span><span class="p">},</span>
</span><span id="__span-5-6"><a href="#__codelineno-5-6" id="__codelineno-5-6" name="__codelineno-5-6"></a><span class="p">)</span>
</span></code></pre></div>
<p>Matching is exact string equality — <code>"Limited"</code> will not match <code>"limited"</code>.
Passing a field name that does not exist on the model raises <code>AttributeError</code>,
which is a useful early failure when building experimental conditions.</p>
<h2 id="a-worked-example">A worked example<a class="headerlink" href="#a-worked-example" title="Permanent link">¶</a></h2>
<p>Filtering and sampling compose naturally into experimental arms:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a>    <span class="n">load_patient_personas</span><span class="p">,</span>
</span><span id="__span-6-3"><a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>    <span class="n">filter_patient_personas</span><span class="p">,</span>
</span><span id="__span-6-4"><a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a>    <span class="n">sample_patient_personas</span><span class="p">,</span>
</span><span id="__span-6-5"><a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a><span class="p">)</span>
</span><span id="__span-6-6"><a href="#__codelineno-6-6" id="__codelineno-6-6" name="__codelineno-6-6"></a>
</span><span id="__span-6-7"><a href="#__codelineno-6-7" id="__codelineno-6-7" name="__codelineno-6-7"></a><span class="n">patients</span> <span class="o">=</span> <span class="n">load_patient_personas</span><span class="p">(</span><span class="s2">"patients.yaml"</span><span class="p">)</span>
</span><span id="__span-6-8"><a href="#__codelineno-6-8" id="__codelineno-6-8" name="__codelineno-6-8"></a>
</span><span id="__span-6-9"><a href="#__codelineno-6-9" id="__codelineno-6-9" name="__codelineno-6-9"></a><span class="n">conditions</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-6-10"><a href="#__codelineno-6-10" id="__codelineno-6-10" name="__codelineno-6-10"></a>    <span class="s2">"high_proficiency"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"language_proficiency"</span><span class="p">:</span> <span class="s2">"high"</span><span class="p">},</span>
</span><span id="__span-6-11"><a href="#__codelineno-6-11" id="__codelineno-6-11" name="__codelineno-6-11"></a>    <span class="s2">"limited_proficiency"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"language_proficiency"</span><span class="p">:</span> <span class="s2">"limited"</span><span class="p">},</span>
</span><span id="__span-6-12"><a href="#__codelineno-6-12" id="__codelineno-6-12" name="__codelineno-6-12"></a><span class="p">}</span>
</span><span id="__span-6-13"><a href="#__codelineno-6-13" id="__codelineno-6-13" name="__codelineno-6-13"></a>
</span><span id="__span-6-14"><a href="#__codelineno-6-14" id="__codelineno-6-14" name="__codelineno-6-14"></a><span class="n">arms</span> <span class="o">=</span> <span class="p">{}</span>
</span><span id="__span-6-15"><a href="#__codelineno-6-15" id="__codelineno-6-15" name="__codelineno-6-15"></a><span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">criteria</span> <span class="ow">in</span> <span class="n">conditions</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="__span-6-16"><a href="#__codelineno-6-16" id="__codelineno-6-16" name="__codelineno-6-16"></a>    <span class="n">pool</span> <span class="o">=</span> <span class="n">filter_patient_personas</span><span class="p">(</span><span class="n">patients</span><span class="p">,</span> <span class="n">criteria</span><span class="p">)</span>
</span><span id="__span-6-17"><a href="#__codelineno-6-17" id="__codelineno-6-17" name="__codelineno-6-17"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">pool</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">10</span><span class="p">:</span>
</span><span id="__span-6-18"><a href="#__codelineno-6-18" id="__codelineno-6-18" name="__codelineno-6-18"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Condition </span><span class="si">{</span><span class="n">name</span><span class="si">!r}</span><span class="s2"> has only </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">pool</span><span class="p">)</span><span class="si">}</span><span class="s2"> personas"</span><span class="p">)</span>
</span><span id="__span-6-19"><a href="#__codelineno-6-19" id="__codelineno-6-19" name="__codelineno-6-19"></a>    <span class="n">arms</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">sample_patient_personas</span><span class="p">(</span><span class="n">pool</span><span class="p">,</span> <span class="n">k</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">seed</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</span></code></pre></div>
<p>Holding the seed fixed across arms keeps sampling noise from confounding the
comparison, so any difference in outcomes is attributable to the condition
rather than to which personas happened to be drawn.</p>
<h2 id="generating-persona-pools">Generating persona pools<a class="headerlink" href="#generating-persona-pools" title="Permanent link">¶</a></h2>
<p>Writing hundreds of personas by hand is impractical. The
<a href="https://github.com/dipankarsrirag/triage-sim">repository</a> includes
<code>scripts/generate_personas.py</code>, which produces persona YAML files
programmatically — a useful starting point for building a pool large enough to
filter meaningfully.</p>
<p>Next: <a href="/triagesim/guide/agents/">Agents and LLM backends</a> covers how a persona is turned into
a prompt.</p>
