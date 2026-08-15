---
title: "Run artifacts"
---

<h1 id="run-artifacts">Run artifacts<a class="headerlink" href="#run-artifacts" title="Permanent link">¶</a></h1>
<p><code>TriageRunner.run()</code> returns a single dictionary containing everything that
happened. It is plain JSON-serialisable data — no live objects — so it can be
written to disk, shipped elsewhere, and analysed long after the run finished.</p>
<h2 id="top-level-keys">Top-level keys<a class="headerlink" href="#top-level-keys" title="Permanent link">¶</a></h2>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>run_id</code></td>
<td><code>str</code></td>
<td>UUID4 identifying the run. Also the namespace used in the state store.</td>
</tr>
<tr>
<td><code>ground_truth</code></td>
<td><code>dict</code></td>
<td>The vignette the run was built from, echoed back unchanged.</td>
</tr>
<tr>
<td><code>state</code></td>
<td><code>dict</code></td>
<td>Final simulation state: <code>ground_truth</code>, <code>turn</code>, <code>done</code>.</td>
</tr>
<tr>
<td><code>history</code></td>
<td><code>list[dict]</code></td>
<td>The transcript: nurse and patient utterances plus system events.</td>
</tr>
<tr>
<td><code>trace</code></td>
<td><code>list[dict]</code></td>
<td>Per-action nurse cognition record.</td>
</tr>
<tr>
<td><code>belief</code></td>
<td><code>dict</code></td>
<td>Flattened final belief state.</td>
</tr>
<tr>
<td><code>red_flags</code></td>
<td><code>list[str]</code></td>
<td>Red flags accepted by the environment, in logging order.</td>
</tr>
</tbody>
</table>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="n">artifact</span> <span class="o">=</span> <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="nb">print</span><span class="p">(</span><span class="n">artifact</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="c1"># dict_keys(['run_id', 'ground_truth', 'state', 'history', 'trace', 'belief', 'red_flags'])</span>
</span></code></pre></div>
<h2 id="state"><code>state</code><a class="headerlink" href="#state" title="Permanent link">¶</a></h2>
<div class="language-json highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="p">{</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a><span class="w">  </span><span class="nt">"ground_truth"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nt">"chiefcomplaint"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Syncope"</span><span class="p">,</span><span class="w"> </span><span class="nt">"acuity"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="nt">"pain"</span><span class="p">:</span><span class="w"> </span><span class="mi">7</span><span class="p">,</span><span class="w"> </span><span class="nt">"vitals"</span><span class="p">:</span><span class="w"> </span><span class="p">{}</span><span class="w"> </span><span class="p">},</span>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="w">  </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">12</span><span class="p">,</span>
</span><span id="__span-1-4"><a href="#__codelineno-1-4" id="__codelineno-1-4" name="__codelineno-1-4"></a><span class="w">  </span><span class="nt">"done"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
</span><span id="__span-1-5"><a href="#__codelineno-1-5" id="__codelineno-1-5" name="__codelineno-1-5"></a><span class="p">}</span>
</span></code></pre></div>
<p><code>turn</code> counts <strong>patient</strong> turns. Comparing it against <code>max_turns</code> tells you
whether the run ended naturally or was cut short: if <code>turn</code> is well below
<code>max_turns</code> and <code>done</code> is <code>true</code>, the nurse chose to end — or the step safety
cap tripped.</p>
<h2 id="history"><code>history</code><a class="headerlink" href="#history" title="Permanent link">¶</a></h2>
<p>The transcript, in order. Three entry shapes appear, distinguished by <code>actor</code>.</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:3"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><input id="__tabbed_1_3" name="__tabbed_1" type="radio"><div class="tabbed-labels"><label for="__tabbed_1_1">Nurse utterance</label><label for="__tabbed_1_2">Patient utterance</label><label for="__tabbed_1_3">System event</label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-json highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a><span class="p">{</span>
</span><span id="__span-2-2"><a href="#__codelineno-2-2" id="__codelineno-2-2" name="__codelineno-2-2"></a><span class="w">  </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
</span><span id="__span-2-3"><a href="#__codelineno-2-3" id="__codelineno-2-3" name="__codelineno-2-3"></a><span class="w">  </span><span class="nt">"actor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"nurse"</span><span class="p">,</span>
</span><span id="__span-2-4"><a href="#__codelineno-2-4" id="__codelineno-2-4" name="__codelineno-2-4"></a><span class="w">  </span><span class="nt">"utterance"</span><span class="p">:</span><span class="w"> </span><span class="s2">"What brings you in today?"</span><span class="p">,</span>
</span><span id="__span-2-5"><a href="#__codelineno-2-5" id="__codelineno-2-5" name="__codelineno-2-5"></a><span class="w">  </span><span class="nt">"triage"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span>
</span><span id="__span-2-6"><a href="#__codelineno-2-6" id="__codelineno-2-6" name="__codelineno-2-6"></a><span class="p">}</span>
</span></code></pre></div>
<p>Nurse lines carry the triage level believed at the moment of speaking.</p>
</div>
<div class="tabbed-block">
<div class="language-json highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a><span class="p">{</span>
</span><span id="__span-3-2"><a href="#__codelineno-3-2" id="__codelineno-3-2" name="__codelineno-3-2"></a><span class="w">  </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
</span><span id="__span-3-3"><a href="#__codelineno-3-3" id="__codelineno-3-3" name="__codelineno-3-3"></a><span class="w">  </span><span class="nt">"actor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-3-4"><a href="#__codelineno-3-4" id="__codelineno-3-4" name="__codelineno-3-4"></a><span class="w">  </span><span class="nt">"utterance"</span><span class="p">:</span><span class="w"> </span><span class="s2">"I passed out at the shops this morning."</span>
</span><span id="__span-3-5"><a href="#__codelineno-3-5" id="__codelineno-3-5" name="__codelineno-3-5"></a><span class="p">}</span>
</span></code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-json highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a><span class="p">{</span>
</span><span id="__span-4-2"><a href="#__codelineno-4-2" id="__codelineno-4-2" name="__codelineno-4-2"></a><span class="w">  </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
</span><span id="__span-4-3"><a href="#__codelineno-4-3" id="__codelineno-4-3" name="__codelineno-4-3"></a><span class="w">  </span><span class="nt">"actor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"system"</span><span class="p">,</span>
</span><span id="__span-4-4"><a href="#__codelineno-4-4" id="__codelineno-4-4" name="__codelineno-4-4"></a><span class="w">  </span><span class="nt">"event"</span><span class="p">:</span><span class="w"> </span><span class="s2">"vital"</span><span class="p">,</span>
</span><span id="__span-4-5"><a href="#__codelineno-4-5" id="__codelineno-4-5" name="__codelineno-4-5"></a><span class="w">  </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"heartrate"</span><span class="p">,</span>
</span><span id="__span-4-6"><a href="#__codelineno-4-6" id="__codelineno-4-6" name="__codelineno-4-6"></a><span class="w">  </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">112</span>
</span><span id="__span-4-7"><a href="#__codelineno-4-7" id="__codelineno-4-7" name="__codelineno-4-7"></a><span class="p">}</span>
</span></code></pre></div>
<p>A released vital. The terminating event is
<code>{"turn": n, "actor": "system", "event": "triage_end"}</code>.</p>
</div>
</div>
</input></input></input></div>
<p>Rendering it as a readable transcript:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a><span class="k">for</span> <span class="n">h</span> <span class="ow">in</span> <span class="n">artifact</span><span class="p">[</span><span class="s2">"history"</span><span class="p">]:</span>
</span><span id="__span-5-2"><a href="#__codelineno-5-2" id="__codelineno-5-2" name="__codelineno-5-2"></a>    <span class="k">if</span> <span class="n">h</span><span class="p">[</span><span class="s2">"actor"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"nurse"</span><span class="p">:</span>
</span><span id="__span-5-3"><a href="#__codelineno-5-3" id="__codelineno-5-3" name="__codelineno-5-3"></a>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Nurse: </span><span class="si">{</span><span class="n">h</span><span class="p">[</span><span class="s1">'utterance'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-5-4"><a href="#__codelineno-5-4" id="__codelineno-5-4" name="__codelineno-5-4"></a>    <span class="k">elif</span> <span class="n">h</span><span class="p">[</span><span class="s2">"actor"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"patient"</span><span class="p">:</span>
</span><span id="__span-5-5"><a href="#__codelineno-5-5" id="__codelineno-5-5" name="__codelineno-5-5"></a>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Patient: </span><span class="si">{</span><span class="n">h</span><span class="p">[</span><span class="s1">'utterance'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-5-6"><a href="#__codelineno-5-6" id="__codelineno-5-6" name="__codelineno-5-6"></a>    <span class="k">elif</span> <span class="n">h</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"event"</span><span class="p">)</span> <span class="o">==</span> <span class="s2">"vital"</span><span class="p">:</span>
</span><span id="__span-5-7"><a href="#__codelineno-5-7" id="__codelineno-5-7" name="__codelineno-5-7"></a>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"[Vital] </span><span class="si">{</span><span class="n">h</span><span class="p">[</span><span class="s1">'name'</span><span class="p">]</span><span class="si">}</span><span class="s2"> = </span><span class="si">{</span><span class="n">h</span><span class="p">[</span><span class="s1">'value'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-5-8"><a href="#__codelineno-5-8" id="__codelineno-5-8" name="__codelineno-5-8"></a>    <span class="k">elif</span> <span class="n">h</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"event"</span><span class="p">)</span> <span class="o">==</span> <span class="s2">"triage_end"</span><span class="p">:</span>
</span><span id="__span-5-9"><a href="#__codelineno-5-9" id="__codelineno-5-9" name="__codelineno-5-9"></a>        <span class="nb">print</span><span class="p">(</span><span class="s2">"[Triage ended]"</span><span class="p">)</span>
</span></code></pre></div>
<h2 id="trace"><code>trace</code><a class="headerlink" href="#trace" title="Permanent link">¶</a></h2>
<p>One entry per <strong>nurse action</strong> — including micro-turns that produced no speech.
This is the cognition record, and it is where most analysis happens.</p>
<div class="language-json highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a><span class="p">{</span>
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a><span class="w">  </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
</span><span id="__span-6-3"><a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a><span class="w">  </span><span class="nt">"actor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"nurse"</span><span class="p">,</span>
</span><span id="__span-6-4"><a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a><span class="w">  </span><span class="nt">"action"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
</span><span id="__span-6-5"><a href="#__codelineno-6-5" id="__codelineno-6-5" name="__codelineno-6-5"></a><span class="w">    </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"check_vital"</span><span class="p">,</span>
</span><span id="__span-6-6"><a href="#__codelineno-6-6" id="__codelineno-6-6" name="__codelineno-6-6"></a><span class="w">    </span><span class="nt">"vital"</span><span class="p">:</span><span class="w"> </span><span class="s2">"heartrate"</span>
</span><span id="__span-6-7"><a href="#__codelineno-6-7" id="__codelineno-6-7" name="__codelineno-6-7"></a><span class="w">  </span><span class="p">},</span>
</span><span id="__span-6-8"><a href="#__codelineno-6-8" id="__codelineno-6-8" name="__codelineno-6-8"></a><span class="w">  </span><span class="nt">"triage"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span>
</span><span id="__span-6-9"><a href="#__codelineno-6-9" id="__codelineno-6-9" name="__codelineno-6-9"></a><span class="w">  </span><span class="nt">"confidence"</span><span class="p">:</span><span class="w"> </span><span class="s2">"low"</span><span class="p">,</span>
</span><span id="__span-6-10"><a href="#__codelineno-6-10" id="__codelineno-6-10" name="__codelineno-6-10"></a><span class="w">  </span><span class="nt">"explanation"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Syncope with no witnessed head strike. Need heart rate to assess for arrhythmia before assigning acuity."</span><span class="p">,</span>
</span><span id="__span-6-11"><a href="#__codelineno-6-11" id="__codelineno-6-11" name="__codelineno-6-11"></a><span class="w">  </span><span class="nt">"red_flags_proposed"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"syncope"</span><span class="p">]</span>
</span><span id="__span-6-12"><a href="#__codelineno-6-12" id="__codelineno-6-12" name="__codelineno-6-12"></a><span class="p">}</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>turn</code></td>
<td>Patient-turn index the action occurred within.</td>
</tr>
<tr>
<td><code>actor</code></td>
<td>Always <code>"nurse"</code>.</td>
</tr>
<tr>
<td><code>action</code></td>
<td>The executable action, as a dict. <code>type</code> is one of <code>utterance</code>, <code>check_vital</code>, <code>log_red_flag</code>, <code>end</code>; remaining keys depend on the type.</td>
</tr>
<tr>
<td><code>triage</code></td>
<td>Triage level at this step.</td>
</tr>
<tr>
<td><code>confidence</code></td>
<td><code>low</code>, <code>medium</code>, or <code>high</code>.</td>
</tr>
<tr>
<td><code>explanation</code></td>
<td>The nurse's stated reasoning at this step.</td>
</tr>
<tr>
<td><code>red_flags_proposed</code></td>
<td>Flags the model proposed — <strong>before</strong> environment deduplication.</td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">Proposed versus accepted flags</p>
<p><code>red_flags_proposed</code> is what the model claimed; the top-level <code>red_flags</code>
list is what the environment actually accepted after normalising case and
whitespace, dropping repeats, and capping at five new flags per turn. The
two will usually differ, and the gap is itself informative.</p>
</div>
<p>Because <code>triage</code>, <code>confidence</code> and <code>explanation</code> are recorded at <em>every</em> step,
the trace shows the decision trajectory rather than just its endpoint:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-7-1"><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="k">for</span> <span class="n">step</span> <span class="ow">in</span> <span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">]:</span>
</span><span id="__span-7-2"><a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>    <span class="n">action</span> <span class="o">=</span> <span class="n">step</span><span class="p">[</span><span class="s2">"action"</span><span class="p">]</span>
</span><span id="__span-7-3"><a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"turn </span><span class="si">{</span><span class="n">step</span><span class="p">[</span><span class="s1">'turn'</span><span class="p">]</span><span class="si">:</span><span class="s2">&gt;2</span><span class="si">}</span><span class="s2">  </span><span class="si">{</span><span class="n">action</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">:</span><span class="s2">&lt;13</span><span class="si">}</span><span class="s2"> "</span>
</span><span id="__span-7-4"><a href="#__codelineno-7-4" id="__codelineno-7-4" name="__codelineno-7-4"></a>          <span class="sa">f</span><span class="s2">"triage=</span><span class="si">{</span><span class="n">step</span><span class="p">[</span><span class="s1">'triage'</span><span class="p">]</span><span class="si">}</span><span class="s2"> (</span><span class="si">{</span><span class="n">step</span><span class="p">[</span><span class="s1">'confidence'</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
</span></code></pre></div>
<div class="language-text highlight"><pre><span></span><code><span id="__span-8-1"><a href="#__codelineno-8-1" id="__codelineno-8-1" name="__codelineno-8-1"></a>turn  0  utterance     triage=3 (low)
</span><span id="__span-8-2"><a href="#__codelineno-8-2" id="__codelineno-8-2" name="__codelineno-8-2"></a>turn  1  check_vital   triage=3 (low)
</span><span id="__span-8-3"><a href="#__codelineno-8-3" id="__codelineno-8-3" name="__codelineno-8-3"></a>turn  1  log_red_flag  triage=2 (medium)
</span><span id="__span-8-4"><a href="#__codelineno-8-4" id="__codelineno-8-4" name="__codelineno-8-4"></a>turn  1  utterance     triage=2 (medium)
</span><span id="__span-8-5"><a href="#__codelineno-8-5" id="__codelineno-8-5" name="__codelineno-8-5"></a>turn  2  end           triage=2 (high)
</span></code></pre></div>
<h2 id="belief"><code>belief</code><a class="headerlink" href="#belief" title="Permanent link">¶</a></h2>
<p>The final belief state, flattened from the provenance graph into a
consumer-friendly view. Each slot maps to a <strong>list</strong> of belief items, because
the graph deliberately preserves competing values rather than resolving them.</p>
<div class="language-json highlight"><pre><span></span><code><span id="__span-9-1"><a href="#__codelineno-9-1" id="__codelineno-9-1" name="__codelineno-9-1"></a><span class="p">{</span>
</span><span id="__span-9-2"><a href="#__codelineno-9-2" id="__codelineno-9-2" name="__codelineno-9-2"></a><span class="w">  </span><span class="nt">"chief_complaint"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
</span><span id="__span-9-3"><a href="#__codelineno-9-3" id="__codelineno-9-3" name="__codelineno-9-3"></a><span class="w">    </span><span class="p">{</span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"syncope"</span><span class="p">,</span><span class="w"> </span><span class="nt">"source"</span><span class="p">:</span><span class="w"> </span><span class="s2">"patient"</span><span class="p">,</span><span class="w"> </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nt">"certainty"</span><span class="p">:</span><span class="w"> </span><span class="s2">"explicit"</span><span class="p">}</span>
</span><span id="__span-9-4"><a href="#__codelineno-9-4" id="__codelineno-9-4" name="__codelineno-9-4"></a><span class="w">  </span><span class="p">],</span>
</span><span id="__span-9-5"><a href="#__codelineno-9-5" id="__codelineno-9-5" name="__codelineno-9-5"></a><span class="w">  </span><span class="nt">"associated_symptoms"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
</span><span id="__span-9-6"><a href="#__codelineno-9-6" id="__codelineno-9-6" name="__codelineno-9-6"></a><span class="w">    </span><span class="p">{</span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"dizziness"</span><span class="p">,</span><span class="w"> </span><span class="nt">"source"</span><span class="p">:</span><span class="w"> </span><span class="s2">"patient"</span><span class="p">,</span><span class="w"> </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="nt">"certainty"</span><span class="p">:</span><span class="w"> </span><span class="s2">"explicit"</span><span class="p">},</span>
</span><span id="__span-9-7"><a href="#__codelineno-9-7" id="__codelineno-9-7" name="__codelineno-9-7"></a><span class="w">    </span><span class="p">{</span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"palpitations"</span><span class="p">,</span><span class="w"> </span><span class="nt">"source"</span><span class="p">:</span><span class="w"> </span><span class="s2">"patient"</span><span class="p">,</span><span class="w"> </span><span class="nt">"turn"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="nt">"certainty"</span><span class="p">:</span><span class="w"> </span><span class="s2">"inferred"</span><span class="p">}</span>
</span><span id="__span-9-8"><a href="#__codelineno-9-8" id="__codelineno-9-8" name="__codelineno-9-8"></a><span class="w">  </span><span class="p">],</span>
</span><span id="__span-9-9"><a href="#__codelineno-9-9" id="__codelineno-9-9" name="__codelineno-9-9"></a><span class="w">  </span><span class="nt">"vitals_known"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"heartrate"</span><span class="p">,</span><span class="w"> </span><span class="s2">"o2sat"</span><span class="p">],</span>
</span><span id="__span-9-10"><a href="#__codelineno-9-10" id="__codelineno-9-10" name="__codelineno-9-10"></a><span class="w">  </span><span class="nt">"red_flags_logged"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"syncope"</span><span class="p">,</span><span class="w"> </span><span class="s2">"tachycardia"</span><span class="p">]</span>
</span><span id="__span-9-11"><a href="#__codelineno-9-11" id="__codelineno-9-11" name="__codelineno-9-11"></a><span class="p">}</span>
</span></code></pre></div>
<table>
<thead>
<tr>
<th>Item field</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>value</code></td>
<td>The extracted value.</td>
</tr>
<tr>
<td><code>source</code></td>
<td><code>patient</code>, <code>nurse</code>, <code>system_vital</code>, or <code>system_other</code>.</td>
</tr>
<tr>
<td><code>turn</code></td>
<td>Turn the value was acquired on.</td>
</tr>
<tr>
<td><code>certainty</code></td>
<td><code>explicit</code>, <code>inferred</code>, or <code>suspected</code>.</td>
</tr>
</tbody>
</table>
<p>Two keys are always present and are <strong>not</strong> lists of belief items:</p>
<ul>
<li><code>vitals_known</code> — sorted list of released vital names</li>
<li><code>red_flags_logged</code> — sorted list of accepted red flags</li>
</ul>
<p>Slot names are whatever the belief detectors produced, with two renames applied
on the way out: <code>associated_symptom</code> becomes <code>associated_symptoms</code>, and
<code>red_flag</code> becomes <code>red_flags</code>. Treat every other slot key as optional and use
<code>.get()</code>.</p>
<div class="admonition warning">
<p class="admonition-title">The observation view is lossy</p>
<p><code>belief</code> drops the evidence graph — the quotes supporting each value and the
slot-to-evidence edges. That provenance exists in the environment's
<code>BeliefGraph</code> but is not included in the artifact.</p>
</div>
<h2 id="saving-and-reloading">Saving and reloading<a class="headerlink" href="#saving-and-reloading" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-10-1"><a href="#__codelineno-10-1" id="__codelineno-10-1" name="__codelineno-10-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
</span><span id="__span-10-2"><a href="#__codelineno-10-2" id="__codelineno-10-2" name="__codelineno-10-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>
</span><span id="__span-10-3"><a href="#__codelineno-10-3" id="__codelineno-10-3" name="__codelineno-10-3"></a>
</span><span id="__span-10-4"><a href="#__codelineno-10-4" id="__codelineno-10-4" name="__codelineno-10-4"></a><span class="n">out</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="s2">"runs"</span><span class="p">)</span> <span class="o">/</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">artifact</span><span class="p">[</span><span class="s1">'run_id'</span><span class="p">]</span><span class="si">}</span><span class="s2">.json"</span>
</span><span id="__span-10-5"><a href="#__codelineno-10-5" id="__codelineno-10-5" name="__codelineno-10-5"></a><span class="n">out</span><span class="o">.</span><span class="n">parent</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">parents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">exist_ok</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="__span-10-6"><a href="#__codelineno-10-6" id="__codelineno-10-6" name="__codelineno-10-6"></a><span class="n">out</span><span class="o">.</span><span class="n">write_text</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">artifact</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">2</span><span class="p">))</span>
</span></code></pre></div>
<p>Everything is JSON-native, so no custom encoder is needed. Reloading:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-11-1"><a href="#__codelineno-11-1" id="__codelineno-11-1" name="__codelineno-11-1"></a><span class="n">artifact</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">out</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
</span></code></pre></div>
<p>A saved artifact is all <a href="/triagesim/guide/metrics/">the metrics</a> require — you can score a
batch of runs offline without touching a model:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-12-1"><a href="#__codelineno-12-1" id="__codelineno-12-1" name="__codelineno-12-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
</span><span id="__span-12-2"><a href="#__codelineno-12-2" id="__codelineno-12-2" name="__codelineno-12-2"></a><span class="kn">from</span><span class="w"> </span><span class="nn">pathlib</span><span class="w"> </span><span class="kn">import</span> <span class="n">Path</span>
</span><span id="__span-12-3"><a href="#__codelineno-12-3" id="__codelineno-12-3" name="__codelineno-12-3"></a>
</span><span id="__span-12-4"><a href="#__codelineno-12-4" id="__codelineno-12-4" name="__codelineno-12-4"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span><span id="__span-12-5"><a href="#__codelineno-12-5" id="__codelineno-12-5" name="__codelineno-12-5"></a>
</span><span id="__span-12-6"><a href="#__codelineno-12-6" id="__codelineno-12-6" name="__codelineno-12-6"></a><span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="s2">"runs"</span><span class="p">)</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="s2">"*.json"</span><span class="p">)):</span>
</span><span id="__span-12-7"><a href="#__codelineno-12-7" id="__codelineno-12-7" name="__codelineno-12-7"></a>    <span class="n">artifact</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">path</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
</span><span id="__span-12-8"><a href="#__codelineno-12-8" id="__codelineno-12-8" name="__codelineno-12-8"></a>    <span class="n">metrics</span> <span class="o">=</span> <span class="n">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-12-9"><a href="#__codelineno-12-9" id="__codelineno-12-9" name="__codelineno-12-9"></a>        <span class="n">trace</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"trace"</span><span class="p">],</span>
</span><span id="__span-12-10"><a href="#__codelineno-12-10" id="__codelineno-12-10" name="__codelineno-12-10"></a>        <span class="n">belief</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"belief"</span><span class="p">],</span>
</span><span id="__span-12-11"><a href="#__codelineno-12-11" id="__codelineno-12-11" name="__codelineno-12-11"></a>        <span class="n">ground_truth</span><span class="o">=</span><span class="n">artifact</span><span class="p">[</span><span class="s2">"ground_truth"</span><span class="p">],</span>
</span><span id="__span-12-12"><a href="#__codelineno-12-12" id="__codelineno-12-12" name="__codelineno-12-12"></a>    <span class="p">)</span>
</span><span id="__span-12-13"><a href="#__codelineno-12-13" id="__codelineno-12-13" name="__codelineno-12-13"></a>    <span class="nb">print</span><span class="p">(</span><span class="n">path</span><span class="o">.</span><span class="n">stem</span><span class="p">,</span> <span class="n">metrics</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"correct"</span><span class="p">])</span>
</span></code></pre></div>
<p>Storing <code>ground_truth</code> inside the artifact is what makes this work: a run file
is self-describing and needs no external key to be scored.</p>
<p>Next: <a href="/triagesim/guide/metrics/">Evaluation metrics</a>.</p>
