---
title: "triagesim"
type: "docsite"
docSite: "triagesim"
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
