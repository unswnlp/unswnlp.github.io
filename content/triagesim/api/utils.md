---
title: "triagesim.utils"
type: "docsite"
docSite: "triagesim"
---

<h1 id="triagesimutils"><code>triagesim.utils</code><a class="headerlink" href="#triagesimutils" title="Permanent link">¶</a></h1>
<p>Evaluation metrics computed from a run artifact.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.utils</span><span class="w"> </span><span class="kn">import</span> <span class="n">compute_all_metrics</span>
</span></code></pre></div>
<p>Every function consumes only environment output, so metrics can be recomputed
offline from a saved artifact. See <a href="/triagesim/guide/metrics/">Evaluation metrics</a> for
the meaning of each returned key and for the over/under-triage sign convention.</p>
<h2 id="orchestrator">Orchestrator<a class="headerlink" href="#orchestrator" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.metrics.compute_all_metrics">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">compute_all_metrics</span>
<a class="headerlink" href="#triagesim.utils.metrics.compute_all_metrics" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]],</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="n">expert_red_flags</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="typing.Set">Set</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Compute all metrics for a single simulation run.</p>
</div>
</div><h2 id="triage-decision">Triage decision<a class="headerlink" href="#triage-decision" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.metrics.triage_decision_metrics">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">triage_decision_metrics</span>
<a class="headerlink" href="#triagesim.utils.metrics.triage_decision_metrics" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">triage_decision_metrics</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]],</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Evaluate final triage decision.</p>
<p><span class="doc-section-title">Returns:</span></p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code><span title="typing.Dict">Dict</span>[<span title="str">str</span>, <span title="typing.Any">Any</span>]</code>
</td>
<td>
<div class="doc-md-description">
<ul>
<li>correctness</li>
</ul>
</div>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code><span title="typing.Dict">Dict</span>[<span title="str">str</span>, <span title="typing.Any">Any</span>]</code>
</td>
<td>
<div class="doc-md-description">
<ul>
<li>absolute error</li>
</ul>
</div>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code><span title="typing.Dict">Dict</span>[<span title="str">str</span>, <span title="typing.Any">Any</span>]</code>
</td>
<td>
<div class="doc-md-description">
<ul>
<li>over/under-triage flags</li>
</ul>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.metrics.time_to_first_correct_triage">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">time_to_first_correct_triage</span>
<a class="headerlink" href="#triagesim.utils.metrics.time_to_first_correct_triage" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">time_to_first_correct_triage</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]],</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="int">int</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Turn index when correct triage was first stated.</p>
</div>
</div><h2 id="belief-coverage">Belief coverage<a class="headerlink" href="#belief-coverage" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.metrics.belief_coverage_metrics">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">belief_coverage_metrics</span>
<a class="headerlink" href="#triagesim.utils.metrics.belief_coverage_metrics" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">belief_coverage_metrics</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Structural metrics of what information was elicited.</p>
</div>
</div><h2 id="red-flags">Red flags<a class="headerlink" href="#red-flags" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.metrics.red_flag_metrics">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">red_flag_metrics</span>
<a class="headerlink" href="#triagesim.utils.metrics.red_flag_metrics" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">red_flag_metrics</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">expert_red_flags</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="typing.Set">Set</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Metrics for explicitly logged red flags.</p>
<p>Works even without expert annotations.</p>
</div>
</div><h2 id="explanations">Explanations<a class="headerlink" href="#explanations" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.metrics.explanation_support_metrics">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">explanation_support_metrics</span>
<a class="headerlink" href="#triagesim.utils.metrics.explanation_support_metrics" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">explanation_support_metrics</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]],</span> <span class="n">belief</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Placeholder for explanation faithfulness metrics.</p>
<p>Future ideas:
- Citation overlap
- Evidence hallucination checks</p>
</div>
</div><h2 id="text-control">Text control<a class="headerlink" href="#text-control" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.utils.text_control.enforce_response_budget">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">enforce_response_budget</span>
<a class="headerlink" href="#triagesim.utils.text_control.enforce_response_budget" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">enforce_response_budget</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">text</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n">response_length</span><span class="p">:</span> <span class="n"><span title="str">str</span></span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="str">str</span></span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Trims patient utterance ONLY if it clearly violates
the persona response_length budget.</p>
</div>
</div>
