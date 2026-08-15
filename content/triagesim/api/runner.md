---
title: "triagesim"
---

<h1 id="triagesim"><code>triagesim</code><a class="headerlink" href="#triagesim" title="Permanent link">¶</a></h1>
<p>The top-level package exports the two objects needed to run a simulation.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim</span><span class="w"> </span><span class="kn">import</span> <span class="n">TriageRunner</span><span class="p">,</span> <span class="n">RunnerConfig</span>
</span></code></pre></div>
<p>See <a href="/triagesim/guide/runner/">Running a simulation</a> for usage.</p>
<h2 id="configuration">Configuration<a class="headerlink" href="#configuration" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.runner.RunnerConfig">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">RunnerConfig</span>
<span class="doc doc-labels">
<small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
</span>
<a class="headerlink" href="#triagesim.runner.RunnerConfig" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">RunnerConfig</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">max_turns</span><span class="p">:</span> <span class="n"><span title="int">int</span></span> <span class="o">=</span> <span class="mi">6</span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">enable_llm</span><span class="p">:</span> <span class="n"><span title="bool">bool</span></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">store_backend</span><span class="p">:</span> <span class="n"><span title="str">str</span></span> <span class="o">=</span> <span class="s2">"memory"</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">redis_db</span><span class="p">:</span> <span class="n"><span title="int">int</span></span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="n">seed</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="int">int</span></span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a><span class="p">)</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Configuration for a single simulation run.</p>
<div class="doc doc-children">
</div>
</div>
</div><h2 id="runner">Runner<a class="headerlink" href="#runner" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.runner.TriageRunner">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">TriageRunner</span>
<a class="headerlink" href="#triagesim.runner.TriageRunner" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">TriageRunner</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">nurse_agent</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/agents/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NurseAgent&lt;/span&gt; (&lt;code&gt;triagesim.agents.nurse_agent.NurseAgent&lt;/code&gt;)'>NurseAgent</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">patient_agent</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/agents/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientAgent&lt;/span&gt; (&lt;code&gt;triagesim.agents.patient_agent.PatientAgent&lt;/code&gt;)'>PatientAgent</a></span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">],</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="#triagesim.runner.RunnerConfig" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;RunnerConfig&lt;/span&gt;


  &lt;span class="doc doc-labels"&gt;
      &lt;small class="doc doc-label doc-label-dataclass"&gt;&lt;code&gt;dataclass&lt;/code&gt;&lt;/small&gt;
  &lt;/span&gt; (&lt;code&gt;triagesim.runner.RunnerConfig&lt;/code&gt;)'>RunnerConfig</a></span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a><span class="p">)</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Orchestrates a single triage simulation episode.</p>
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/runner.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-48">48</a></span>
<span class="normal"><a href="#__codelineno-0-49">49</a></span>
<span class="normal"><a href="#__codelineno-0-50">50</a></span>
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
<span class="normal"><a href="#__codelineno-0-74">74</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-48"><a id="__codelineno-0-48" name="__codelineno-0-48"></a><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
</span><span id="__span-0-49"><a id="__codelineno-0-49" name="__codelineno-0-49"></a>    <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-50"><a id="__codelineno-0-50" name="__codelineno-0-50"></a>    <span class="n">nurse_agent</span><span class="p">:</span> <span class="n">NurseAgent</span><span class="p">,</span>
</span><span id="__span-0-51"><a id="__codelineno-0-51" name="__codelineno-0-51"></a>    <span class="n">patient_agent</span><span class="p">:</span> <span class="n">PatientAgent</span><span class="p">,</span>
</span><span id="__span-0-52"><a id="__codelineno-0-52" name="__codelineno-0-52"></a>    <span class="n">ground_truth</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
</span><span id="__span-0-53"><a id="__codelineno-0-53" name="__codelineno-0-53"></a>    <span class="n">config</span><span class="p">:</span> <span class="n">RunnerConfig</span><span class="p">,</span>
</span><span id="__span-0-54"><a id="__codelineno-0-54" name="__codelineno-0-54"></a><span class="p">):</span>
</span><span id="__span-0-55"><a id="__codelineno-0-55" name="__codelineno-0-55"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">nurse_agent</span> <span class="o">=</span> <span class="n">nurse_agent</span>
</span><span id="__span-0-56"><a id="__codelineno-0-56" name="__codelineno-0-56"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">patient_agent</span> <span class="o">=</span> <span class="n">patient_agent</span>
</span><span id="__span-0-57"><a id="__codelineno-0-57" name="__codelineno-0-57"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">ground_truth</span> <span class="o">=</span> <span class="n">ground_truth</span>
</span><span id="__span-0-58"><a id="__codelineno-0-58" name="__codelineno-0-58"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">config</span> <span class="o">=</span> <span class="n">config</span>
</span><span id="__span-0-59"><a id="__codelineno-0-59" name="__codelineno-0-59"></a>
</span><span id="__span-0-60"><a id="__codelineno-0-60" name="__codelineno-0-60"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">store</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_init_store</span><span class="p">()</span>
</span><span id="__span-0-61"><a id="__codelineno-0-61" name="__codelineno-0-61"></a>
</span><span id="__span-0-62"><a id="__codelineno-0-62" name="__codelineno-0-62"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">env</span> <span class="o">=</span> <span class="n">TriageEnv</span><span class="p">(</span>
</span><span id="__span-0-63"><a id="__codelineno-0-63" name="__codelineno-0-63"></a>        <span class="n">nurse_agent</span><span class="o">=</span><span class="n">nurse_agent</span><span class="p">,</span>
</span><span id="__span-0-64"><a id="__codelineno-0-64" name="__codelineno-0-64"></a>        <span class="n">store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">store</span><span class="p">,</span>
</span><span id="__span-0-65"><a id="__codelineno-0-65" name="__codelineno-0-65"></a>        <span class="n">max_turns</span><span class="o">=</span><span class="n">config</span><span class="o">.</span><span class="n">max_turns</span><span class="p">,</span>
</span><span id="__span-0-66"><a id="__codelineno-0-66" name="__codelineno-0-66"></a>    <span class="p">)</span>
</span><span id="__span-0-67"><a id="__codelineno-0-67" name="__codelineno-0-67"></a>
</span><span id="__span-0-68"><a id="__codelineno-0-68" name="__codelineno-0-68"></a>    <span class="c1"># Feature flag: enable or disable LLM-backed belief updates</span>
</span><span id="__span-0-69"><a id="__codelineno-0-69" name="__codelineno-0-69"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">belief_updater</span><span class="o">.</span><span class="n">enable_llm</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">enable_llm</span>
</span><span id="__span-0-70"><a id="__codelineno-0-70" name="__codelineno-0-70"></a>
</span><span id="__span-0-71"><a id="__codelineno-0-71" name="__codelineno-0-71"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">seed</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-72"><a id="__codelineno-0-72" name="__codelineno-0-72"></a>        <span class="kn">import</span><span class="w"> </span><span class="nn">random</span>
</span><span id="__span-0-73"><a id="__codelineno-0-73" name="__codelineno-0-73"></a>
</span><span id="__span-0-74"><a id="__codelineno-0-74" name="__codelineno-0-74"></a>        <span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">seed</span><span class="p">)</span>
</span></code></pre></div></td></tr></table></div>
</details>
<div class="doc doc-children">
<div class="doc doc-object doc-function">
<h4 class="doc doc-heading" id="triagesim.runner.TriageRunner.run">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <span class="doc doc-object-name doc-function-name">run</span>
<a class="headerlink" href="#triagesim.runner.TriageRunner.run" title="Permanent link">¶</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">run</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="typing.Any">Any</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents">
<p>Execute one full triage simulation.</p>
<p>Nurse may act multiple times per turn (e.g. check vital → speak).
Patient acts once per cycle.</p>
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/runner.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-84"> 84</a></span>
<span class="normal"><a href="#__codelineno-0-85"> 85</a></span>
<span class="normal"><a href="#__codelineno-0-86"> 86</a></span>
<span class="normal"><a href="#__codelineno-0-87"> 87</a></span>
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
<span class="normal"><a href="#__codelineno-0-104">104</a></span>
<span class="normal"><a href="#__codelineno-0-105">105</a></span>
<span class="normal"><a href="#__codelineno-0-106">106</a></span>
<span class="normal"><a href="#__codelineno-0-107">107</a></span>
<span class="normal"><a href="#__codelineno-0-108">108</a></span>
<span class="normal"><a href="#__codelineno-0-109">109</a></span>
<span class="normal"><a href="#__codelineno-0-110">110</a></span>
<span class="normal"><a href="#__codelineno-0-111">111</a></span>
<span class="normal"><a href="#__codelineno-0-112">112</a></span>
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
<span class="normal"><a href="#__codelineno-0-127">127</a></span>
<span class="normal"><a href="#__codelineno-0-128">128</a></span>
<span class="normal"><a href="#__codelineno-0-129">129</a></span>
<span class="normal"><a href="#__codelineno-0-130">130</a></span>
<span class="normal"><a href="#__codelineno-0-131">131</a></span>
<span class="normal"><a href="#__codelineno-0-132">132</a></span>
<span class="normal"><a href="#__codelineno-0-133">133</a></span>
<span class="normal"><a href="#__codelineno-0-134">134</a></span>
<span class="normal"><a href="#__codelineno-0-135">135</a></span>
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
<span class="normal"><a href="#__codelineno-0-170">170</a></span>
<span class="normal"><a href="#__codelineno-0-171">171</a></span>
<span class="normal"><a href="#__codelineno-0-172">172</a></span>
<span class="normal"><a href="#__codelineno-0-173">173</a></span>
<span class="normal"><a href="#__codelineno-0-174">174</a></span>
<span class="normal"><a href="#__codelineno-0-175">175</a></span>
<span class="normal"><a href="#__codelineno-0-176">176</a></span>
<span class="normal"><a href="#__codelineno-0-177">177</a></span>
<span class="normal"><a href="#__codelineno-0-178">178</a></span>
<span class="normal"><a href="#__codelineno-0-179">179</a></span>
<span class="normal"><a href="#__codelineno-0-180">180</a></span>
<span class="normal"><a href="#__codelineno-0-181">181</a></span>
<span class="normal"><a href="#__codelineno-0-182">182</a></span>
<span class="normal"><a href="#__codelineno-0-183">183</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-84"><a id="__codelineno-0-84" name="__codelineno-0-84"></a><span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="__span-0-85"><a id="__codelineno-0-85" name="__codelineno-0-85"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-86"><a id="__codelineno-0-86" name="__codelineno-0-86"></a><span class="sd">    Execute one full triage simulation.</span>
</span><span id="__span-0-87"><a id="__codelineno-0-87" name="__codelineno-0-87"></a>
</span><span id="__span-0-88"><a id="__codelineno-0-88" name="__codelineno-0-88"></a><span class="sd">    Nurse may act multiple times per turn (e.g. check vital → speak).</span>
</span><span id="__span-0-89"><a id="__codelineno-0-89" name="__codelineno-0-89"></a><span class="sd">    Patient acts once per cycle.</span>
</span><span id="__span-0-90"><a id="__codelineno-0-90" name="__codelineno-0-90"></a><span class="sd">    """</span>
</span><span id="__span-0-91"><a id="__codelineno-0-91" name="__codelineno-0-91"></a>
</span><span id="__span-0-92"><a id="__codelineno-0-92" name="__codelineno-0-92"></a>    <span class="n">run_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">reset</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ground_truth</span><span class="p">)</span>
</span><span id="__span-0-93"><a id="__codelineno-0-93" name="__codelineno-0-93"></a>    <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="__span-0-94"><a id="__codelineno-0-94" name="__codelineno-0-94"></a>
</span><span id="__span-0-95"><a id="__codelineno-0-95" name="__codelineno-0-95"></a>    <span class="c1"># Hard safety cap (nurse + patient steps)</span>
</span><span id="__span-0-96"><a id="__codelineno-0-96" name="__codelineno-0-96"></a>    <span class="n">max_steps</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">max_turns</span> <span class="o">*</span> <span class="mi">4</span>
</span><span id="__span-0-97"><a id="__codelineno-0-97" name="__codelineno-0-97"></a>    <span class="n">steps</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="__span-0-98"><a id="__codelineno-0-98" name="__codelineno-0-98"></a>
</span><span id="__span-0-99"><a id="__codelineno-0-99" name="__codelineno-0-99"></a>    <span class="k">while</span> <span class="ow">not</span> <span class="n">done</span> <span class="ow">and</span> <span class="n">steps</span> <span class="o">&lt;</span> <span class="n">max_steps</span><span class="p">:</span>
</span><span id="__span-0-100"><a id="__codelineno-0-100" name="__codelineno-0-100"></a>        <span class="n">steps</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="__span-0-101"><a id="__codelineno-0-101" name="__codelineno-0-101"></a>
</span><span id="__span-0-102"><a id="__codelineno-0-102" name="__codelineno-0-102"></a>        <span class="c1"># ─────────────────────────────────────────</span>
</span><span id="__span-0-103"><a id="__codelineno-0-103" name="__codelineno-0-103"></a>        <span class="c1"># Nurse phase (may contain multiple actions)</span>
</span><span id="__span-0-104"><a id="__codelineno-0-104" name="__codelineno-0-104"></a>        <span class="c1"># ─────────────────────────────────────────</span>
</span><span id="__span-0-105"><a id="__codelineno-0-105" name="__codelineno-0-105"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">nurse_agent</span><span class="o">.</span><span class="n">seen_vital</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="__span-0-106"><a id="__codelineno-0-106" name="__codelineno-0-106"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">nurse_agent</span><span class="o">.</span><span class="n">logged_flag</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="__span-0-107"><a id="__codelineno-0-107" name="__codelineno-0-107"></a>
</span><span id="__span-0-108"><a id="__codelineno-0-108" name="__codelineno-0-108"></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="__span-0-109"><a id="__codelineno-0-109" name="__codelineno-0-109"></a>            <span class="n">obs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">observe</span><span class="p">(</span><span class="n">run_id</span><span class="p">)</span>
</span><span id="__span-0-110"><a id="__codelineno-0-110" name="__codelineno-0-110"></a>            <span class="n">belief</span> <span class="o">=</span> <span class="n">obs</span><span class="p">[</span><span class="s2">"belief"</span><span class="p">]</span>
</span><span id="__span-0-111"><a id="__codelineno-0-111" name="__codelineno-0-111"></a>            <span class="n">known_vitals</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">belief</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"vitals_known"</span><span class="p">,</span> <span class="p">[]))</span>
</span><span id="__span-0-112"><a id="__codelineno-0-112" name="__codelineno-0-112"></a>            <span class="n">history_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_history</span><span class="p">(</span><span class="n">obs</span><span class="p">[</span><span class="s2">"history"</span><span class="p">])</span>
</span><span id="__span-0-113"><a id="__codelineno-0-113" name="__codelineno-0-113"></a>
</span><span id="__span-0-114"><a id="__codelineno-0-114" name="__codelineno-0-114"></a>            <span class="n">nurse_action</span><span class="p">:</span> <span class="n">NurseOutput</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">nurse_agent</span><span class="o">.</span><span class="n">act</span><span class="p">(</span>
</span><span id="__span-0-115"><a id="__codelineno-0-115" name="__codelineno-0-115"></a>                <span class="n">history</span><span class="o">=</span><span class="n">history_text</span><span class="p">,</span>
</span><span id="__span-0-116"><a id="__codelineno-0-116" name="__codelineno-0-116"></a>                <span class="n">known_vitals</span><span class="o">=</span><span class="n">known_vitals</span><span class="p">,</span>
</span><span id="__span-0-117"><a id="__codelineno-0-117" name="__codelineno-0-117"></a>            <span class="p">)</span>
</span><span id="__span-0-118"><a id="__codelineno-0-118" name="__codelineno-0-118"></a>
</span><span id="__span-0-119"><a id="__codelineno-0-119" name="__codelineno-0-119"></a>            <span class="n">obs</span><span class="p">,</span> <span class="n">done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">step</span><span class="p">(</span>
</span><span id="__span-0-120"><a id="__codelineno-0-120" name="__codelineno-0-120"></a>                <span class="n">run_id</span><span class="o">=</span><span class="n">run_id</span><span class="p">,</span>
</span><span id="__span-0-121"><a id="__codelineno-0-121" name="__codelineno-0-121"></a>                <span class="n">actor</span><span class="o">=</span><span class="n">NURSE</span><span class="p">,</span>
</span><span id="__span-0-122"><a id="__codelineno-0-122" name="__codelineno-0-122"></a>                <span class="n">action</span><span class="o">=</span><span class="n">nurse_action</span><span class="p">,</span>
</span><span id="__span-0-123"><a id="__codelineno-0-123" name="__codelineno-0-123"></a>            <span class="p">)</span>
</span><span id="__span-0-124"><a id="__codelineno-0-124" name="__codelineno-0-124"></a>
</span><span id="__span-0-125"><a id="__codelineno-0-125" name="__codelineno-0-125"></a>            <span class="c1"># print(obs)</span>
</span><span id="__span-0-126"><a id="__codelineno-0-126" name="__codelineno-0-126"></a>
</span><span id="__span-0-127"><a id="__codelineno-0-127" name="__codelineno-0-127"></a>            <span class="k">if</span> <span class="n">done</span><span class="p">:</span>
</span><span id="__span-0-128"><a id="__codelineno-0-128" name="__codelineno-0-128"></a>                <span class="k">break</span>
</span><span id="__span-0-129"><a id="__codelineno-0-129" name="__codelineno-0-129"></a>
</span><span id="__span-0-130"><a id="__codelineno-0-130" name="__codelineno-0-130"></a>            <span class="c1"># print(f"------- NURSE ACTION: {nurse_action.action}")</span>
</span><span id="__span-0-131"><a id="__codelineno-0-131" name="__codelineno-0-131"></a>            <span class="c1"># Enforce at most ONE vital request per nurse phase</span>
</span><span id="__span-0-132"><a id="__codelineno-0-132" name="__codelineno-0-132"></a>            <span class="k">if</span> <span class="n">nurse_action</span><span class="o">.</span><span class="n">action</span> <span class="o">==</span> <span class="s2">"check_vital"</span><span class="p">:</span>
</span><span id="__span-0-133"><a id="__codelineno-0-133" name="__codelineno-0-133"></a>                <span class="bp">self</span><span class="o">.</span><span class="n">nurse_agent</span><span class="o">.</span><span class="n">seen_vital</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="__span-0-134"><a id="__codelineno-0-134" name="__codelineno-0-134"></a>                <span class="c1"># latest = obs["history"][-1]</span>
</span><span id="__span-0-135"><a id="__codelineno-0-135" name="__codelineno-0-135"></a>                <span class="c1"># print(f"[VITAL | {latest['name']}]: {latest['value']}")</span>
</span><span id="__span-0-136"><a id="__codelineno-0-136" name="__codelineno-0-136"></a>                <span class="k">continue</span>  <span class="c1"># nurse gets to act again after system vital</span>
</span><span id="__span-0-137"><a id="__codelineno-0-137" name="__codelineno-0-137"></a>
</span><span id="__span-0-138"><a id="__codelineno-0-138" name="__codelineno-0-138"></a>            <span class="c1"># Nurse utterance hands control to patient</span>
</span><span id="__span-0-139"><a id="__codelineno-0-139" name="__codelineno-0-139"></a>            <span class="k">if</span> <span class="n">nurse_action</span><span class="o">.</span><span class="n">action</span> <span class="o">==</span> <span class="s2">"utterance"</span><span class="p">:</span>
</span><span id="__span-0-140"><a id="__codelineno-0-140" name="__codelineno-0-140"></a>                <span class="c1"># print("Nurse:", nurse_action.utterance)</span>
</span><span id="__span-0-141"><a id="__codelineno-0-141" name="__codelineno-0-141"></a>                <span class="k">break</span>
</span><span id="__span-0-142"><a id="__codelineno-0-142" name="__codelineno-0-142"></a>
</span><span id="__span-0-143"><a id="__codelineno-0-143" name="__codelineno-0-143"></a>            <span class="c1"># Logging red flags does NOT end nurse phase</span>
</span><span id="__span-0-144"><a id="__codelineno-0-144" name="__codelineno-0-144"></a>            <span class="k">if</span> <span class="n">nurse_action</span><span class="o">.</span><span class="n">action</span> <span class="o">==</span> <span class="s2">"log_red_flag"</span><span class="p">:</span>
</span><span id="__span-0-145"><a id="__codelineno-0-145" name="__codelineno-0-145"></a>                <span class="bp">self</span><span class="o">.</span><span class="n">nurse_agent</span><span class="o">.</span><span class="n">logged_flag</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="__span-0-146"><a id="__codelineno-0-146" name="__codelineno-0-146"></a>                <span class="c1"># latest = obs["trace"][-1]["action"]["red_flags"]</span>
</span><span id="__span-0-147"><a id="__codelineno-0-147" name="__codelineno-0-147"></a>                <span class="c1"># print(f"[RED FLAGS]: {latest}")</span>
</span><span id="__span-0-148"><a id="__codelineno-0-148" name="__codelineno-0-148"></a>                <span class="k">continue</span>
</span><span id="__span-0-149"><a id="__codelineno-0-149" name="__codelineno-0-149"></a>
</span><span id="__span-0-150"><a id="__codelineno-0-150" name="__codelineno-0-150"></a>            <span class="c1"># Explicit end</span>
</span><span id="__span-0-151"><a id="__codelineno-0-151" name="__codelineno-0-151"></a>            <span class="k">if</span> <span class="n">nurse_action</span><span class="o">.</span><span class="n">action</span> <span class="o">==</span> <span class="s2">"end"</span><span class="p">:</span>
</span><span id="__span-0-152"><a id="__codelineno-0-152" name="__codelineno-0-152"></a>                <span class="n">done</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="__span-0-153"><a id="__codelineno-0-153" name="__codelineno-0-153"></a>                <span class="k">break</span>
</span><span id="__span-0-154"><a id="__codelineno-0-154" name="__codelineno-0-154"></a>
</span><span id="__span-0-155"><a id="__codelineno-0-155" name="__codelineno-0-155"></a>        <span class="k">if</span> <span class="n">done</span><span class="p">:</span>
</span><span id="__span-0-156"><a id="__codelineno-0-156" name="__codelineno-0-156"></a>            <span class="k">break</span>
</span><span id="__span-0-157"><a id="__codelineno-0-157" name="__codelineno-0-157"></a>
</span><span id="__span-0-158"><a id="__codelineno-0-158" name="__codelineno-0-158"></a>        <span class="c1"># ─────────────────────────────────────────</span>
</span><span id="__span-0-159"><a id="__codelineno-0-159" name="__codelineno-0-159"></a>        <span class="c1"># Patient turn (exactly one)</span>
</span><span id="__span-0-160"><a id="__codelineno-0-160" name="__codelineno-0-160"></a>        <span class="c1"># ─────────────────────────────────────────</span>
</span><span id="__span-0-161"><a id="__codelineno-0-161" name="__codelineno-0-161"></a>        <span class="n">obs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">observe</span><span class="p">(</span><span class="n">run_id</span><span class="p">)</span>
</span><span id="__span-0-162"><a id="__codelineno-0-162" name="__codelineno-0-162"></a>        <span class="n">history_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_history</span><span class="p">(</span><span class="n">obs</span><span class="p">[</span><span class="s2">"history"</span><span class="p">])</span>
</span><span id="__span-0-163"><a id="__codelineno-0-163" name="__codelineno-0-163"></a>
</span><span id="__span-0-164"><a id="__codelineno-0-164" name="__codelineno-0-164"></a>        <span class="c1"># print(self.ground_truth)</span>
</span><span id="__span-0-165"><a id="__codelineno-0-165" name="__codelineno-0-165"></a>
</span><span id="__span-0-166"><a id="__codelineno-0-166" name="__codelineno-0-166"></a>        <span class="n">patient_action</span><span class="p">:</span> <span class="n">PatientOutput</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">patient_agent</span><span class="o">.</span><span class="n">act</span><span class="p">(</span>
</span><span id="__span-0-167"><a id="__codelineno-0-167" name="__codelineno-0-167"></a>            <span class="n">history</span><span class="o">=</span><span class="n">history_text</span><span class="p">,</span>
</span><span id="__span-0-168"><a id="__codelineno-0-168" name="__codelineno-0-168"></a>            <span class="n">chief_complaint</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ground_truth</span><span class="p">[</span><span class="s2">"chiefcomplaint"</span><span class="p">],</span>
</span><span id="__span-0-169"><a id="__codelineno-0-169" name="__codelineno-0-169"></a>            <span class="n">pain</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ground_truth</span><span class="p">[</span><span class="s2">"pain"</span><span class="p">],</span>
</span><span id="__span-0-170"><a id="__codelineno-0-170" name="__codelineno-0-170"></a>        <span class="p">)</span>
</span><span id="__span-0-171"><a id="__codelineno-0-171" name="__codelineno-0-171"></a>
</span><span id="__span-0-172"><a id="__codelineno-0-172" name="__codelineno-0-172"></a>        <span class="c1"># print("Patient:", patient_action.utterance)</span>
</span><span id="__span-0-173"><a id="__codelineno-0-173" name="__codelineno-0-173"></a>
</span><span id="__span-0-174"><a id="__codelineno-0-174" name="__codelineno-0-174"></a>        <span class="n">obs</span><span class="p">,</span> <span class="n">done</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">step</span><span class="p">(</span>
</span><span id="__span-0-175"><a id="__codelineno-0-175" name="__codelineno-0-175"></a>            <span class="n">run_id</span><span class="o">=</span><span class="n">run_id</span><span class="p">,</span>
</span><span id="__span-0-176"><a id="__codelineno-0-176" name="__codelineno-0-176"></a>            <span class="n">actor</span><span class="o">=</span><span class="n">PATIENT</span><span class="p">,</span>
</span><span id="__span-0-177"><a id="__codelineno-0-177" name="__codelineno-0-177"></a>            <span class="n">action</span><span class="o">=</span><span class="n">patient_action</span><span class="p">,</span>
</span><span id="__span-0-178"><a id="__codelineno-0-178" name="__codelineno-0-178"></a>        <span class="p">)</span>
</span><span id="__span-0-179"><a id="__codelineno-0-179" name="__codelineno-0-179"></a>    <span class="c1"># print("------------------------------")</span>
</span><span id="__span-0-180"><a id="__codelineno-0-180" name="__codelineno-0-180"></a>    <span class="c1"># history_text = self._format_history(obs["history"])</span>
</span><span id="__span-0-181"><a id="__codelineno-0-181" name="__codelineno-0-181"></a>    <span class="c1"># print(history_text)</span>
</span><span id="__span-0-182"><a id="__codelineno-0-182" name="__codelineno-0-182"></a>    <span class="c1"># print("------------------------------")</span>
</span><span id="__span-0-183"><a id="__codelineno-0-183" name="__codelineno-0-183"></a>    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_finalize_run</span><span class="p">(</span><span class="n">run_id</span><span class="p">)</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
</div>
</div>
</div><h2 id="version">Version<a class="headerlink" href="#version" title="Permanent link">¶</a></h2>
<p>The installed version is available as <code>triagesim.__version__</code>:</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">triagesim</span>
</span><span id="__span-1-2"><a href="#__codelineno-1-2" id="__codelineno-1-2" name="__codelineno-1-2"></a>
</span><span id="__span-1-3"><a href="#__codelineno-1-3" id="__codelineno-1-3" name="__codelineno-1-3"></a><span class="nb">print</span><span class="p">(</span><span class="n">triagesim</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
</span></code></pre></div>
