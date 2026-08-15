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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/metrics.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-206">206</a></span>
<span class="normal"><a href="#__codelineno-0-207">207</a></span>
<span class="normal"><a href="#__codelineno-0-208">208</a></span>
<span class="normal"><a href="#__codelineno-0-209">209</a></span>
<span class="normal"><a href="#__codelineno-0-210">210</a></span>
<span class="normal"><a href="#__codelineno-0-211">211</a></span>
<span class="normal"><a href="#__codelineno-0-212">212</a></span>
<span class="normal"><a href="#__codelineno-0-213">213</a></span>
<span class="normal"><a href="#__codelineno-0-214">214</a></span>
<span class="normal"><a href="#__codelineno-0-215">215</a></span>
<span class="normal"><a href="#__codelineno-0-216">216</a></span>
<span class="normal"><a href="#__codelineno-0-217">217</a></span>
<span class="normal"><a href="#__codelineno-0-218">218</a></span>
<span class="normal"><a href="#__codelineno-0-219">219</a></span>
<span class="normal"><a href="#__codelineno-0-220">220</a></span>
<span class="normal"><a href="#__codelineno-0-221">221</a></span>
<span class="normal"><a href="#__codelineno-0-222">222</a></span>
<span class="normal"><a href="#__codelineno-0-223">223</a></span>
<span class="normal"><a href="#__codelineno-0-224">224</a></span>
<span class="normal"><a href="#__codelineno-0-225">225</a></span>
<span class="normal"><a href="#__codelineno-0-226">226</a></span>
<span class="normal"><a href="#__codelineno-0-227">227</a></span>
<span class="normal"><a href="#__codelineno-0-228">228</a></span>
<span class="normal"><a href="#__codelineno-0-229">229</a></span>
<span class="normal"><a href="#__codelineno-0-230">230</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-206"><a id="__codelineno-0-206" name="__codelineno-0-206"></a><span class="k">def</span><span class="w"> </span><span class="nf">compute_all_metrics</span><span class="p">(</span>
</span><span id="__span-0-207"><a id="__codelineno-0-207" name="__codelineno-0-207"></a>    <span class="o">*</span><span class="p">,</span>
</span><span id="__span-0-208"><a id="__codelineno-0-208" name="__codelineno-0-208"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
</span><span id="__span-0-209"><a id="__codelineno-0-209" name="__codelineno-0-209"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-210"><a id="__codelineno-0-210" name="__codelineno-0-210"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-211"><a id="__codelineno-0-211" name="__codelineno-0-211"></a>    <span class="n">expert_red_flags</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-212"><a id="__codelineno-0-212" name="__codelineno-0-212"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="__span-0-213"><a id="__codelineno-0-213" name="__codelineno-0-213"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-214"><a id="__codelineno-0-214" name="__codelineno-0-214"></a><span class="sd">    Compute all metrics for a single simulation run.</span>
</span><span id="__span-0-215"><a id="__codelineno-0-215" name="__codelineno-0-215"></a><span class="sd">    """</span>
</span><span id="__span-0-216"><a id="__codelineno-0-216" name="__codelineno-0-216"></a>
</span><span id="__span-0-217"><a id="__codelineno-0-217" name="__codelineno-0-217"></a>    <span class="n">metrics</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
</span><span id="__span-0-218"><a id="__codelineno-0-218" name="__codelineno-0-218"></a>
</span><span id="__span-0-219"><a id="__codelineno-0-219" name="__codelineno-0-219"></a>    <span class="n">metrics</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">]</span> <span class="o">=</span> <span class="n">triage_decision_metrics</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">ground_truth</span><span class="p">)</span>
</span><span id="__span-0-220"><a id="__codelineno-0-220" name="__codelineno-0-220"></a>    <span class="n">metrics</span><span class="p">[</span><span class="s2">"triage"</span><span class="p">][</span><span class="s2">"first_correct_turn"</span><span class="p">]</span> <span class="o">=</span> <span class="n">time_to_first_correct_triage</span><span class="p">(</span>
</span><span id="__span-0-221"><a id="__codelineno-0-221" name="__codelineno-0-221"></a>        <span class="n">trace</span><span class="p">,</span> <span class="n">ground_truth</span>
</span><span id="__span-0-222"><a id="__codelineno-0-222" name="__codelineno-0-222"></a>    <span class="p">)</span>
</span><span id="__span-0-223"><a id="__codelineno-0-223" name="__codelineno-0-223"></a>
</span><span id="__span-0-224"><a id="__codelineno-0-224" name="__codelineno-0-224"></a>    <span class="n">metrics</span><span class="p">[</span><span class="s2">"belief_coverage"</span><span class="p">]</span> <span class="o">=</span> <span class="n">belief_coverage_metrics</span><span class="p">(</span><span class="n">belief</span><span class="p">)</span>
</span><span id="__span-0-225"><a id="__codelineno-0-225" name="__codelineno-0-225"></a>
</span><span id="__span-0-226"><a id="__codelineno-0-226" name="__codelineno-0-226"></a>    <span class="n">metrics</span><span class="p">[</span><span class="s2">"red_flags"</span><span class="p">]</span> <span class="o">=</span> <span class="n">red_flag_metrics</span><span class="p">(</span><span class="n">belief</span><span class="p">,</span> <span class="n">expert_red_flags</span><span class="p">)</span>
</span><span id="__span-0-227"><a id="__codelineno-0-227" name="__codelineno-0-227"></a>
</span><span id="__span-0-228"><a id="__codelineno-0-228" name="__codelineno-0-228"></a>    <span class="n">metrics</span><span class="p">[</span><span class="s2">"explanation"</span><span class="p">]</span> <span class="o">=</span> <span class="n">explanation_support_metrics</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">belief</span><span class="p">)</span>
</span><span id="__span-0-229"><a id="__codelineno-0-229" name="__codelineno-0-229"></a>
</span><span id="__span-0-230"><a id="__codelineno-0-230" name="__codelineno-0-230"></a>    <span class="k">return</span> <span class="n">metrics</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/metrics.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-50">50</a></span>
<span class="normal"><a href="#__codelineno-0-51">51</a></span>
<span class="normal"><a href="#__codelineno-0-52">52</a></span>
<span class="normal"><a href="#__codelineno-0-53">53</a></span>
<span class="normal"><a href="#__codelineno-0-54">54</a></span>
<span class="normal"><a href="#__codelineno-0-55">55</a></span>
<span class="normal"><a href="#__codelineno-0-56">56</a></span>
<span class="normal"><a href="#__codelineno-0-57">57</a></span>
<span class="normal"><a href="#__codelineno-0-58">58</a></span>
<span class="normal"><a href="#__codelineno-0-59">59</a></span>
<span class="normal"><a href="#__codelineno-0-60">60</a></span>
<span class="normal"><a href="#__codelineno-0-61">61</a></span>
<span class="normal"><a href="#__codelineno-0-62">62</a></span>
<span class="normal"><a href="#__codelineno-0-63">63</a></span>
<span class="normal"><a href="#__codelineno-0-64">64</a></span>
<span class="normal"><a href="#__codelineno-0-65">65</a></span>
<span class="normal"><a href="#__codelineno-0-66">66</a></span>
<span class="normal"><a href="#__codelineno-0-67">67</a></span>
<span class="normal"><a href="#__codelineno-0-68">68</a></span>
<span class="normal"><a href="#__codelineno-0-69">69</a></span>
<span class="normal"><a href="#__codelineno-0-70">70</a></span>
<span class="normal"><a href="#__codelineno-0-71">71</a></span>
<span class="normal"><a href="#__codelineno-0-72">72</a></span>
<span class="normal"><a href="#__codelineno-0-73">73</a></span>
<span class="normal"><a href="#__codelineno-0-74">74</a></span>
<span class="normal"><a href="#__codelineno-0-75">75</a></span>
<span class="normal"><a href="#__codelineno-0-76">76</a></span>
<span class="normal"><a href="#__codelineno-0-77">77</a></span>
<span class="normal"><a href="#__codelineno-0-78">78</a></span>
<span class="normal"><a href="#__codelineno-0-79">79</a></span>
<span class="normal"><a href="#__codelineno-0-80">80</a></span>
<span class="normal"><a href="#__codelineno-0-81">81</a></span>
<span class="normal"><a href="#__codelineno-0-82">82</a></span>
<span class="normal"><a href="#__codelineno-0-83">83</a></span>
<span class="normal"><a href="#__codelineno-0-84">84</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-50"><a id="__codelineno-0-50" name="__codelineno-0-50"></a><span class="k">def</span><span class="w"> </span><span class="nf">triage_decision_metrics</span><span class="p">(</span>
</span><span id="__span-0-51"><a id="__codelineno-0-51" name="__codelineno-0-51"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
</span><span id="__span-0-52"><a id="__codelineno-0-52" name="__codelineno-0-52"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-53"><a id="__codelineno-0-53" name="__codelineno-0-53"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="__span-0-54"><a id="__codelineno-0-54" name="__codelineno-0-54"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-55"><a id="__codelineno-0-55" name="__codelineno-0-55"></a><span class="sd">    Evaluate final triage decision.</span>
</span><span id="__span-0-56"><a id="__codelineno-0-56" name="__codelineno-0-56"></a>
</span><span id="__span-0-57"><a id="__codelineno-0-57" name="__codelineno-0-57"></a><span class="sd">    Returns:</span>
</span><span id="__span-0-58"><a id="__codelineno-0-58" name="__codelineno-0-58"></a><span class="sd">        - correctness</span>
</span><span id="__span-0-59"><a id="__codelineno-0-59" name="__codelineno-0-59"></a><span class="sd">        - absolute error</span>
</span><span id="__span-0-60"><a id="__codelineno-0-60" name="__codelineno-0-60"></a><span class="sd">        - over/under-triage flags</span>
</span><span id="__span-0-61"><a id="__codelineno-0-61" name="__codelineno-0-61"></a><span class="sd">    """</span>
</span><span id="__span-0-62"><a id="__codelineno-0-62" name="__codelineno-0-62"></a>    <span class="n">gt</span> <span class="o">=</span> <span class="n">ground_truth</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"acuity"</span><span class="p">)</span>
</span><span id="__span-0-63"><a id="__codelineno-0-63" name="__codelineno-0-63"></a>    <span class="n">pred</span> <span class="o">=</span> <span class="n">_extract_final_triage</span><span class="p">(</span><span class="n">trace</span><span class="p">)</span>
</span><span id="__span-0-64"><a id="__codelineno-0-64" name="__codelineno-0-64"></a>
</span><span id="__span-0-65"><a id="__codelineno-0-65" name="__codelineno-0-65"></a>    <span class="k">if</span> <span class="n">gt</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">pred</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-66"><a id="__codelineno-0-66" name="__codelineno-0-66"></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="__span-0-67"><a id="__codelineno-0-67" name="__codelineno-0-67"></a>            <span class="s2">"ground_truth"</span><span class="p">:</span> <span class="n">gt</span><span class="p">,</span>
</span><span id="__span-0-68"><a id="__codelineno-0-68" name="__codelineno-0-68"></a>            <span class="s2">"final_prediction"</span><span class="p">:</span> <span class="n">pred</span><span class="p">,</span>
</span><span id="__span-0-69"><a id="__codelineno-0-69" name="__codelineno-0-69"></a>            <span class="s2">"correct"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-70"><a id="__codelineno-0-70" name="__codelineno-0-70"></a>            <span class="s2">"absolute_error"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-71"><a id="__codelineno-0-71" name="__codelineno-0-71"></a>            <span class="s2">"over_triage"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-72"><a id="__codelineno-0-72" name="__codelineno-0-72"></a>            <span class="s2">"under_triage"</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-73"><a id="__codelineno-0-73" name="__codelineno-0-73"></a>        <span class="p">}</span>
</span><span id="__span-0-74"><a id="__codelineno-0-74" name="__codelineno-0-74"></a>
</span><span id="__span-0-75"><a id="__codelineno-0-75" name="__codelineno-0-75"></a>    <span class="n">error</span> <span class="o">=</span> <span class="n">pred</span> <span class="o">-</span> <span class="n">gt</span>
</span><span id="__span-0-76"><a id="__codelineno-0-76" name="__codelineno-0-76"></a>
</span><span id="__span-0-77"><a id="__codelineno-0-77" name="__codelineno-0-77"></a>    <span class="k">return</span> <span class="p">{</span>
</span><span id="__span-0-78"><a id="__codelineno-0-78" name="__codelineno-0-78"></a>        <span class="s2">"ground_truth"</span><span class="p">:</span> <span class="n">gt</span><span class="p">,</span>
</span><span id="__span-0-79"><a id="__codelineno-0-79" name="__codelineno-0-79"></a>        <span class="s2">"final_prediction"</span><span class="p">:</span> <span class="n">pred</span><span class="p">,</span>
</span><span id="__span-0-80"><a id="__codelineno-0-80" name="__codelineno-0-80"></a>        <span class="s2">"correct"</span><span class="p">:</span> <span class="n">pred</span> <span class="o">==</span> <span class="n">gt</span><span class="p">,</span>
</span><span id="__span-0-81"><a id="__codelineno-0-81" name="__codelineno-0-81"></a>        <span class="s2">"absolute_error"</span><span class="p">:</span> <span class="nb">abs</span><span class="p">(</span><span class="n">error</span><span class="p">),</span>
</span><span id="__span-0-82"><a id="__codelineno-0-82" name="__codelineno-0-82"></a>        <span class="s2">"over_triage"</span><span class="p">:</span> <span class="n">error</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="__span-0-83"><a id="__codelineno-0-83" name="__codelineno-0-83"></a>        <span class="s2">"under_triage"</span><span class="p">:</span> <span class="n">error</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="__span-0-84"><a id="__codelineno-0-84" name="__codelineno-0-84"></a>    <span class="p">}</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/metrics.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-87"> 87</a></span>
<span class="normal"><a href="#__codelineno-0-88"> 88</a></span>
<span class="normal"><a href="#__codelineno-0-89"> 89</a></span>
<span class="normal"><a href="#__codelineno-0-90"> 90</a></span>
<span class="normal"><a href="#__codelineno-0-91"> 91</a></span>
<span class="normal"><a href="#__codelineno-0-92"> 92</a></span>
<span class="normal"><a href="#__codelineno-0-93"> 93</a></span>
<span class="normal"><a href="#__codelineno-0-94"> 94</a></span>
<span class="normal"><a href="#__codelineno-0-95"> 95</a></span>
<span class="normal"><a href="#__codelineno-0-96"> 96</a></span>
<span class="normal"><a href="#__codelineno-0-97"> 97</a></span>
<span class="normal"><a href="#__codelineno-0-98"> 98</a></span>
<span class="normal"><a href="#__codelineno-0-99"> 99</a></span>
<span class="normal"><a href="#__codelineno-0-100">100</a></span>
<span class="normal"><a href="#__codelineno-0-101">101</a></span>
<span class="normal"><a href="#__codelineno-0-102">102</a></span>
<span class="normal"><a href="#__codelineno-0-103">103</a></span>
<span class="normal"><a href="#__codelineno-0-104">104</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-87"><a id="__codelineno-0-87" name="__codelineno-0-87"></a><span class="k">def</span><span class="w"> </span><span class="nf">time_to_first_correct_triage</span><span class="p">(</span>
</span><span id="__span-0-88"><a id="__codelineno-0-88" name="__codelineno-0-88"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
</span><span id="__span-0-89"><a id="__codelineno-0-89" name="__codelineno-0-89"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-90"><a id="__codelineno-0-90" name="__codelineno-0-90"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]:</span>
</span><span id="__span-0-91"><a id="__codelineno-0-91" name="__codelineno-0-91"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-92"><a id="__codelineno-0-92" name="__codelineno-0-92"></a><span class="sd">    Turn index when correct triage was first stated.</span>
</span><span id="__span-0-93"><a id="__codelineno-0-93" name="__codelineno-0-93"></a><span class="sd">    """</span>
</span><span id="__span-0-94"><a id="__codelineno-0-94" name="__codelineno-0-94"></a>    <span class="n">gt</span> <span class="o">=</span> <span class="n">ground_truth</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"acuity"</span><span class="p">)</span>
</span><span id="__span-0-95"><a id="__codelineno-0-95" name="__codelineno-0-95"></a>    <span class="k">if</span> <span class="n">gt</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-96"><a id="__codelineno-0-96" name="__codelineno-0-96"></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="__span-0-97"><a id="__codelineno-0-97" name="__codelineno-0-97"></a>
</span><span id="__span-0-98"><a id="__codelineno-0-98" name="__codelineno-0-98"></a>    <span class="k">for</span> <span class="n">step</span> <span class="ow">in</span> <span class="n">trace</span><span class="p">:</span>
</span><span id="__span-0-99"><a id="__codelineno-0-99" name="__codelineno-0-99"></a>        <span class="n">action</span> <span class="o">=</span> <span class="n">step</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"action"</span><span class="p">,</span> <span class="p">{})</span>
</span><span id="__span-0-100"><a id="__codelineno-0-100" name="__codelineno-0-100"></a>        <span class="n">triage</span> <span class="o">=</span> <span class="n">action</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"triage"</span><span class="p">)</span>
</span><span id="__span-0-101"><a id="__codelineno-0-101" name="__codelineno-0-101"></a>        <span class="k">if</span> <span class="n">triage</span> <span class="o">==</span> <span class="n">gt</span><span class="p">:</span>
</span><span id="__span-0-102"><a id="__codelineno-0-102" name="__codelineno-0-102"></a>            <span class="k">return</span> <span class="n">step</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"turn"</span><span class="p">)</span>
</span><span id="__span-0-103"><a id="__codelineno-0-103" name="__codelineno-0-103"></a>
</span><span id="__span-0-104"><a id="__codelineno-0-104" name="__codelineno-0-104"></a>    <span class="k">return</span> <span class="kc">None</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/metrics.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-112">112</a></span>
<span class="normal"><a href="#__codelineno-0-113">113</a></span>
<span class="normal"><a href="#__codelineno-0-114">114</a></span>
<span class="normal"><a href="#__codelineno-0-115">115</a></span>
<span class="normal"><a href="#__codelineno-0-116">116</a></span>
<span class="normal"><a href="#__codelineno-0-117">117</a></span>
<span class="normal"><a href="#__codelineno-0-118">118</a></span>
<span class="normal"><a href="#__codelineno-0-119">119</a></span>
<span class="normal"><a href="#__codelineno-0-120">120</a></span>
<span class="normal"><a href="#__codelineno-0-121">121</a></span>
<span class="normal"><a href="#__codelineno-0-122">122</a></span>
<span class="normal"><a href="#__codelineno-0-123">123</a></span>
<span class="normal"><a href="#__codelineno-0-124">124</a></span>
<span class="normal"><a href="#__codelineno-0-125">125</a></span>
<span class="normal"><a href="#__codelineno-0-126">126</a></span>
<span class="normal"><a href="#__codelineno-0-127">127</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-112"><a id="__codelineno-0-112" name="__codelineno-0-112"></a><span class="k">def</span><span class="w"> </span><span class="nf">belief_coverage_metrics</span><span class="p">(</span>
</span><span id="__span-0-113"><a id="__codelineno-0-113" name="__codelineno-0-113"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-114"><a id="__codelineno-0-114" name="__codelineno-0-114"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="__span-0-115"><a id="__codelineno-0-115" name="__codelineno-0-115"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-116"><a id="__codelineno-0-116" name="__codelineno-0-116"></a><span class="sd">    Structural metrics of what information was elicited.</span>
</span><span id="__span-0-117"><a id="__codelineno-0-117" name="__codelineno-0-117"></a><span class="sd">    """</span>
</span><span id="__span-0-118"><a id="__codelineno-0-118" name="__codelineno-0-118"></a>    <span class="k">return</span> <span class="p">{</span>
</span><span id="__span-0-119"><a id="__codelineno-0-119" name="__codelineno-0-119"></a>        <span class="s2">"num_associated_symptoms"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"associated_symptoms"</span><span class="p">,</span> <span class="p">[])),</span>
</span><span id="__span-0-120"><a id="__codelineno-0-120" name="__codelineno-0-120"></a>        <span class="s2">"num_red_flags_inferred"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"red_flags"</span><span class="p">,</span> <span class="p">[])),</span>
</span><span id="__span-0-121"><a id="__codelineno-0-121" name="__codelineno-0-121"></a>        <span class="s2">"has_chief_complaint"</span><span class="p">:</span> <span class="nb">bool</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"chief_complaint"</span><span class="p">)),</span>
</span><span id="__span-0-122"><a id="__codelineno-0-122" name="__codelineno-0-122"></a>        <span class="s2">"has_pain_location"</span><span class="p">:</span> <span class="nb">bool</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"pain_location"</span><span class="p">)),</span>
</span><span id="__span-0-123"><a id="__codelineno-0-123" name="__codelineno-0-123"></a>        <span class="s2">"has_pain_severity"</span><span class="p">:</span> <span class="nb">bool</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"pain_severity"</span><span class="p">)),</span>
</span><span id="__span-0-124"><a id="__codelineno-0-124" name="__codelineno-0-124"></a>        <span class="s2">"has_duration"</span><span class="p">:</span> <span class="nb">bool</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"duration"</span><span class="p">)),</span>
</span><span id="__span-0-125"><a id="__codelineno-0-125" name="__codelineno-0-125"></a>        <span class="s2">"vitals_known"</span><span class="p">:</span> <span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"vitals_known"</span><span class="p">,</span> <span class="p">[]),</span>
</span><span id="__span-0-126"><a id="__codelineno-0-126" name="__codelineno-0-126"></a>        <span class="s2">"num_vitals_known"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"vitals_known"</span><span class="p">,</span> <span class="p">[])),</span>
</span><span id="__span-0-127"><a id="__codelineno-0-127" name="__codelineno-0-127"></a>    <span class="p">}</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/metrics.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-135">135</a></span>
<span class="normal"><a href="#__codelineno-0-136">136</a></span>
<span class="normal"><a href="#__codelineno-0-137">137</a></span>
<span class="normal"><a href="#__codelineno-0-138">138</a></span>
<span class="normal"><a href="#__codelineno-0-139">139</a></span>
<span class="normal"><a href="#__codelineno-0-140">140</a></span>
<span class="normal"><a href="#__codelineno-0-141">141</a></span>
<span class="normal"><a href="#__codelineno-0-142">142</a></span>
<span class="normal"><a href="#__codelineno-0-143">143</a></span>
<span class="normal"><a href="#__codelineno-0-144">144</a></span>
<span class="normal"><a href="#__codelineno-0-145">145</a></span>
<span class="normal"><a href="#__codelineno-0-146">146</a></span>
<span class="normal"><a href="#__codelineno-0-147">147</a></span>
<span class="normal"><a href="#__codelineno-0-148">148</a></span>
<span class="normal"><a href="#__codelineno-0-149">149</a></span>
<span class="normal"><a href="#__codelineno-0-150">150</a></span>
<span class="normal"><a href="#__codelineno-0-151">151</a></span>
<span class="normal"><a href="#__codelineno-0-152">152</a></span>
<span class="normal"><a href="#__codelineno-0-153">153</a></span>
<span class="normal"><a href="#__codelineno-0-154">154</a></span>
<span class="normal"><a href="#__codelineno-0-155">155</a></span>
<span class="normal"><a href="#__codelineno-0-156">156</a></span>
<span class="normal"><a href="#__codelineno-0-157">157</a></span>
<span class="normal"><a href="#__codelineno-0-158">158</a></span>
<span class="normal"><a href="#__codelineno-0-159">159</a></span>
<span class="normal"><a href="#__codelineno-0-160">160</a></span>
<span class="normal"><a href="#__codelineno-0-161">161</a></span>
<span class="normal"><a href="#__codelineno-0-162">162</a></span>
<span class="normal"><a href="#__codelineno-0-163">163</a></span>
<span class="normal"><a href="#__codelineno-0-164">164</a></span>
<span class="normal"><a href="#__codelineno-0-165">165</a></span>
<span class="normal"><a href="#__codelineno-0-166">166</a></span>
<span class="normal"><a href="#__codelineno-0-167">167</a></span>
<span class="normal"><a href="#__codelineno-0-168">168</a></span>
<span class="normal"><a href="#__codelineno-0-169">169</a></span>
<span class="normal"><a href="#__codelineno-0-170">170</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-135"><a id="__codelineno-0-135" name="__codelineno-0-135"></a><span class="k">def</span><span class="w"> </span><span class="nf">red_flag_metrics</span><span class="p">(</span>
</span><span id="__span-0-136"><a id="__codelineno-0-136" name="__codelineno-0-136"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-137"><a id="__codelineno-0-137" name="__codelineno-0-137"></a>    <span class="n">expert_red_flags</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-138"><a id="__codelineno-0-138" name="__codelineno-0-138"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="__span-0-139"><a id="__codelineno-0-139" name="__codelineno-0-139"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-140"><a id="__codelineno-0-140" name="__codelineno-0-140"></a><span class="sd">    Metrics for explicitly logged red flags.</span>
</span><span id="__span-0-141"><a id="__codelineno-0-141" name="__codelineno-0-141"></a>
</span><span id="__span-0-142"><a id="__codelineno-0-142" name="__codelineno-0-142"></a><span class="sd">    Works even without expert annotations.</span>
</span><span id="__span-0-143"><a id="__codelineno-0-143" name="__codelineno-0-143"></a><span class="sd">    """</span>
</span><span id="__span-0-144"><a id="__codelineno-0-144" name="__codelineno-0-144"></a>    <span class="n">logged</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"red_flags_logged"</span><span class="p">,</span> <span class="p">[]))</span>
</span><span id="__span-0-145"><a id="__codelineno-0-145" name="__codelineno-0-145"></a>
</span><span id="__span-0-146"><a id="__codelineno-0-146" name="__codelineno-0-146"></a>    <span class="n">metrics</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-0-147"><a id="__codelineno-0-147" name="__codelineno-0-147"></a>        <span class="s2">"num_red_flags_logged"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">logged</span><span class="p">),</span>
</span><span id="__span-0-148"><a id="__codelineno-0-148" name="__codelineno-0-148"></a>        <span class="s2">"logged_any"</span><span class="p">:</span> <span class="nb">bool</span><span class="p">(</span><span class="n">logged</span><span class="p">),</span>
</span><span id="__span-0-149"><a id="__codelineno-0-149" name="__codelineno-0-149"></a>        <span class="s2">"logged_flags"</span><span class="p">:</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">logged</span><span class="p">),</span>
</span><span id="__span-0-150"><a id="__codelineno-0-150" name="__codelineno-0-150"></a>    <span class="p">}</span>
</span><span id="__span-0-151"><a id="__codelineno-0-151" name="__codelineno-0-151"></a>
</span><span id="__span-0-152"><a id="__codelineno-0-152" name="__codelineno-0-152"></a>    <span class="k">if</span> <span class="n">expert_red_flags</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-153"><a id="__codelineno-0-153" name="__codelineno-0-153"></a>        <span class="k">return</span> <span class="n">metrics</span>
</span><span id="__span-0-154"><a id="__codelineno-0-154" name="__codelineno-0-154"></a>
</span><span id="__span-0-155"><a id="__codelineno-0-155" name="__codelineno-0-155"></a>    <span class="n">tp</span> <span class="o">=</span> <span class="n">logged</span> <span class="o">&amp;</span> <span class="n">expert_red_flags</span>
</span><span id="__span-0-156"><a id="__codelineno-0-156" name="__codelineno-0-156"></a>    <span class="n">fp</span> <span class="o">=</span> <span class="n">logged</span> <span class="o">-</span> <span class="n">expert_red_flags</span>
</span><span id="__span-0-157"><a id="__codelineno-0-157" name="__codelineno-0-157"></a>    <span class="n">fn</span> <span class="o">=</span> <span class="n">expert_red_flags</span> <span class="o">-</span> <span class="n">logged</span>
</span><span id="__span-0-158"><a id="__codelineno-0-158" name="__codelineno-0-158"></a>
</span><span id="__span-0-159"><a id="__codelineno-0-159" name="__codelineno-0-159"></a>    <span class="n">metrics</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
</span><span id="__span-0-160"><a id="__codelineno-0-160" name="__codelineno-0-160"></a>        <span class="p">{</span>
</span><span id="__span-0-161"><a id="__codelineno-0-161" name="__codelineno-0-161"></a>            <span class="s2">"expert_red_flags"</span><span class="p">:</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">expert_red_flags</span><span class="p">),</span>
</span><span id="__span-0-162"><a id="__codelineno-0-162" name="__codelineno-0-162"></a>            <span class="s2">"true_positives"</span><span class="p">:</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">tp</span><span class="p">),</span>
</span><span id="__span-0-163"><a id="__codelineno-0-163" name="__codelineno-0-163"></a>            <span class="s2">"false_positives"</span><span class="p">:</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">fp</span><span class="p">),</span>
</span><span id="__span-0-164"><a id="__codelineno-0-164" name="__codelineno-0-164"></a>            <span class="s2">"false_negatives"</span><span class="p">:</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">fn</span><span class="p">),</span>
</span><span id="__span-0-165"><a id="__codelineno-0-165" name="__codelineno-0-165"></a>            <span class="s2">"precision"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">tp</span><span class="p">)</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">logged</span><span class="p">)</span> <span class="k">if</span> <span class="n">logged</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-166"><a id="__codelineno-0-166" name="__codelineno-0-166"></a>            <span class="s2">"recall"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">tp</span><span class="p">)</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">expert_red_flags</span><span class="p">)</span> <span class="k">if</span> <span class="n">expert_red_flags</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-167"><a id="__codelineno-0-167" name="__codelineno-0-167"></a>        <span class="p">}</span>
</span><span id="__span-0-168"><a id="__codelineno-0-168" name="__codelineno-0-168"></a>    <span class="p">)</span>
</span><span id="__span-0-169"><a id="__codelineno-0-169" name="__codelineno-0-169"></a>
</span><span id="__span-0-170"><a id="__codelineno-0-170" name="__codelineno-0-170"></a>    <span class="k">return</span> <span class="n">metrics</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/metrics.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-178">178</a></span>
<span class="normal"><a href="#__codelineno-0-179">179</a></span>
<span class="normal"><a href="#__codelineno-0-180">180</a></span>
<span class="normal"><a href="#__codelineno-0-181">181</a></span>
<span class="normal"><a href="#__codelineno-0-182">182</a></span>
<span class="normal"><a href="#__codelineno-0-183">183</a></span>
<span class="normal"><a href="#__codelineno-0-184">184</a></span>
<span class="normal"><a href="#__codelineno-0-185">185</a></span>
<span class="normal"><a href="#__codelineno-0-186">186</a></span>
<span class="normal"><a href="#__codelineno-0-187">187</a></span>
<span class="normal"><a href="#__codelineno-0-188">188</a></span>
<span class="normal"><a href="#__codelineno-0-189">189</a></span>
<span class="normal"><a href="#__codelineno-0-190">190</a></span>
<span class="normal"><a href="#__codelineno-0-191">191</a></span>
<span class="normal"><a href="#__codelineno-0-192">192</a></span>
<span class="normal"><a href="#__codelineno-0-193">193</a></span>
<span class="normal"><a href="#__codelineno-0-194">194</a></span>
<span class="normal"><a href="#__codelineno-0-195">195</a></span>
<span class="normal"><a href="#__codelineno-0-196">196</a></span>
<span class="normal"><a href="#__codelineno-0-197">197</a></span>
<span class="normal"><a href="#__codelineno-0-198">198</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-178"><a id="__codelineno-0-178" name="__codelineno-0-178"></a><span class="k">def</span><span class="w"> </span><span class="nf">explanation_support_metrics</span><span class="p">(</span>
</span><span id="__span-0-179"><a id="__codelineno-0-179" name="__codelineno-0-179"></a>    <span class="n">trace</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
</span><span id="__span-0-180"><a id="__codelineno-0-180" name="__codelineno-0-180"></a>    <span class="n">belief</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-181"><a id="__codelineno-0-181" name="__codelineno-0-181"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="__span-0-182"><a id="__codelineno-0-182" name="__codelineno-0-182"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-183"><a id="__codelineno-0-183" name="__codelineno-0-183"></a><span class="sd">    Placeholder for explanation faithfulness metrics.</span>
</span><span id="__span-0-184"><a id="__codelineno-0-184" name="__codelineno-0-184"></a>
</span><span id="__span-0-185"><a id="__codelineno-0-185" name="__codelineno-0-185"></a><span class="sd">    Future ideas:</span>
</span><span id="__span-0-186"><a id="__codelineno-0-186" name="__codelineno-0-186"></a><span class="sd">    - Citation overlap</span>
</span><span id="__span-0-187"><a id="__codelineno-0-187" name="__codelineno-0-187"></a><span class="sd">    - Evidence hallucination checks</span>
</span><span id="__span-0-188"><a id="__codelineno-0-188" name="__codelineno-0-188"></a><span class="sd">    """</span>
</span><span id="__span-0-189"><a id="__codelineno-0-189" name="__codelineno-0-189"></a>    <span class="n">final</span> <span class="o">=</span> <span class="n">_extract_final_nurse_action</span><span class="p">(</span><span class="n">trace</span><span class="p">)</span>
</span><span id="__span-0-190"><a id="__codelineno-0-190" name="__codelineno-0-190"></a>    <span class="n">explanation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="__span-0-191"><a id="__codelineno-0-191" name="__codelineno-0-191"></a>
</span><span id="__span-0-192"><a id="__codelineno-0-192" name="__codelineno-0-192"></a>    <span class="k">if</span> <span class="n">final</span><span class="p">:</span>
</span><span id="__span-0-193"><a id="__codelineno-0-193" name="__codelineno-0-193"></a>        <span class="n">explanation</span> <span class="o">=</span> <span class="n">final</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"action"</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"explanation"</span><span class="p">)</span>
</span><span id="__span-0-194"><a id="__codelineno-0-194" name="__codelineno-0-194"></a>
</span><span id="__span-0-195"><a id="__codelineno-0-195" name="__codelineno-0-195"></a>    <span class="k">return</span> <span class="p">{</span>
</span><span id="__span-0-196"><a id="__codelineno-0-196" name="__codelineno-0-196"></a>        <span class="s2">"has_explanation"</span><span class="p">:</span> <span class="n">explanation</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-197"><a id="__codelineno-0-197" name="__codelineno-0-197"></a>        <span class="s2">"explanation_length"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">explanation</span><span class="o">.</span><span class="n">split</span><span class="p">())</span> <span class="k">if</span> <span class="n">explanation</span> <span class="k">else</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="__span-0-198"><a id="__codelineno-0-198" name="__codelineno-0-198"></a>    <span class="p">}</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/utils/text_control.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-1"> 1</a></span>
<span class="normal"><a href="#__codelineno-0-2"> 2</a></span>
<span class="normal"><a href="#__codelineno-0-3"> 3</a></span>
<span class="normal"><a href="#__codelineno-0-4"> 4</a></span>
<span class="normal"><a href="#__codelineno-0-5"> 5</a></span>
<span class="normal"><a href="#__codelineno-0-6"> 6</a></span>
<span class="normal"><a href="#__codelineno-0-7"> 7</a></span>
<span class="normal"><a href="#__codelineno-0-8"> 8</a></span>
<span class="normal"><a href="#__codelineno-0-9"> 9</a></span>
<span class="normal"><a href="#__codelineno-0-10">10</a></span>
<span class="normal"><a href="#__codelineno-0-11">11</a></span>
<span class="normal"><a href="#__codelineno-0-12">12</a></span>
<span class="normal"><a href="#__codelineno-0-13">13</a></span>
<span class="normal"><a href="#__codelineno-0-14">14</a></span>
<span class="normal"><a href="#__codelineno-0-15">15</a></span>
<span class="normal"><a href="#__codelineno-0-16">16</a></span>
<span class="normal"><a href="#__codelineno-0-17">17</a></span>
<span class="normal"><a href="#__codelineno-0-18">18</a></span>
<span class="normal"><a href="#__codelineno-0-19">19</a></span>
<span class="normal"><a href="#__codelineno-0-20">20</a></span>
<span class="normal"><a href="#__codelineno-0-21">21</a></span>
<span class="normal"><a href="#__codelineno-0-22">22</a></span>
<span class="normal"><a href="#__codelineno-0-23">23</a></span>
<span class="normal"><a href="#__codelineno-0-24">24</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-1"><a id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="k">def</span><span class="w"> </span><span class="nf">enforce_response_budget</span><span class="p">(</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">response_length</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="__span-0-2"><a id="__codelineno-0-2" name="__codelineno-0-2"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-3"><a id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="sd">    Trims patient utterance ONLY if it clearly violates</span>
</span><span id="__span-0-4"><a id="__codelineno-0-4" name="__codelineno-0-4"></a><span class="sd">    the persona response_length budget.</span>
</span><span id="__span-0-5"><a id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="sd">    """</span>
</span><span id="__span-0-6"><a id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="n">sentences</span> <span class="o">=</span> <span class="p">[</span><span class="n">s</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"."</span><span class="p">)</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">strip</span><span class="p">()]</span>
</span><span id="__span-0-7"><a id="__codelineno-0-7" name="__codelineno-0-7"></a>
</span><span id="__span-0-8"><a id="__codelineno-0-8" name="__codelineno-0-8"></a>    <span class="n">limits</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="__span-0-9"><a id="__codelineno-0-9" name="__codelineno-0-9"></a>        <span class="s2">"low"</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
</span><span id="__span-0-10"><a id="__codelineno-0-10" name="__codelineno-0-10"></a>        <span class="s2">"medium"</span><span class="p">:</span> <span class="mi">4</span><span class="p">,</span>
</span><span id="__span-0-11"><a id="__codelineno-0-11" name="__codelineno-0-11"></a>        <span class="s2">"high"</span><span class="p">:</span> <span class="mi">6</span><span class="p">,</span>
</span><span id="__span-0-12"><a id="__codelineno-0-12" name="__codelineno-0-12"></a>    <span class="p">}</span>
</span><span id="__span-0-13"><a id="__codelineno-0-13" name="__codelineno-0-13"></a>
</span><span id="__span-0-14"><a id="__codelineno-0-14" name="__codelineno-0-14"></a>    <span class="n">max_sentences</span> <span class="o">=</span> <span class="n">limits</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">response_length</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="__span-0-15"><a id="__codelineno-0-15" name="__codelineno-0-15"></a>
</span><span id="__span-0-16"><a id="__codelineno-0-16" name="__codelineno-0-16"></a>    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sentences</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">max_sentences</span><span class="p">:</span>
</span><span id="__span-0-17"><a id="__codelineno-0-17" name="__codelineno-0-17"></a>        <span class="k">return</span> <span class="n">text</span>  <span class="c1"># no violation</span>
</span><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18"></a>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19"></a>    <span class="c1"># Trim conservatively</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20"></a>    <span class="n">trimmed</span> <span class="o">=</span> <span class="s2">". "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">sentences</span><span class="p">[:</span><span class="n">max_sentences</span><span class="p">])</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">trimmed</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"."</span><span class="p">):</span>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22"></a>        <span class="n">trimmed</span> <span class="o">+=</span> <span class="s2">"."</span>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23"></a>
</span><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24"></a>    <span class="k">return</span> <span class="n">trimmed</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
