---
title: "triagesim.personas"
type: "docsite"
docSite: "triagesim"
---

<h1 id="triagesimpersonas"><code>triagesim.personas</code><a class="headerlink" href="#triagesimpersonas" title="Permanent link">¶</a></h1>
<p>Persona schemas and the helpers for loading, sampling and filtering them.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.personas</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">PatientPersona</span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">NursePersona</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">load_patient_personas</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="n">load_nurse_personas</span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a>    <span class="n">sample_patient_personas</span><span class="p">,</span>
</span><span id="__span-0-7"><a href="#__codelineno-0-7" id="__codelineno-0-7" name="__codelineno-0-7"></a>    <span class="n">sample_nurse_personas</span><span class="p">,</span>
</span><span id="__span-0-8"><a href="#__codelineno-0-8" id="__codelineno-0-8" name="__codelineno-0-8"></a>    <span class="n">filter_patient_personas</span><span class="p">,</span>
</span><span id="__span-0-9"><a href="#__codelineno-0-9" id="__codelineno-0-9" name="__codelineno-0-9"></a>    <span class="n">filter_nurse_personas</span><span class="p">,</span>
</span><span id="__span-0-10"><a href="#__codelineno-0-10" id="__codelineno-0-10" name="__codelineno-0-10"></a><span class="p">)</span>
</span></code></pre></div>
<p>See <a href="/triagesim/guide/personas/">Personas</a> for the full field reference and YAML
examples.</p>
<h2 id="schemas">Schemas<a class="headerlink" href="#schemas" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.personas.schema.PatientPersona">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">PatientPersona</span>
<a class="headerlink" href="#triagesim.personas.schema.PatientPersona" title="Permanent link">¶</a></h3>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><span title="pydantic.BaseModel">BaseModel</span></code></p>
<div class="doc doc-children">
</div>
</div>
</div>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.personas.schema.NursePersona">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">NursePersona</span>
<a class="headerlink" href="#triagesim.personas.schema.NursePersona" title="Permanent link">¶</a></h3>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><span title="pydantic.BaseModel">BaseModel</span></code></p>
<div class="doc doc-children">
</div>
</div>
</div><h2 id="loading">Loading<a class="headerlink" href="#loading" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.load_patient_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">load_patient_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.load_patient_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">load_patient_personas</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">filepath</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.PatientPersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientPersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.PatientPersona&lt;/code&gt;)'>PatientPersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/personas/loader.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-30">30</a></span>
<span class="normal"><a href="#__codelineno-0-31">31</a></span>
<span class="normal"><a href="#__codelineno-0-32">32</a></span>
<span class="normal"><a href="#__codelineno-0-33">33</a></span>
<span class="normal"><a href="#__codelineno-0-34">34</a></span>
<span class="normal"><a href="#__codelineno-0-35">35</a></span>
<span class="normal"><a href="#__codelineno-0-36">36</a></span>
<span class="normal"><a href="#__codelineno-0-37">37</a></span>
<span class="normal"><a href="#__codelineno-0-38">38</a></span>
<span class="normal"><a href="#__codelineno-0-39">39</a></span>
<span class="normal"><a href="#__codelineno-0-40">40</a></span>
<span class="normal"><a href="#__codelineno-0-41">41</a></span>
<span class="normal"><a href="#__codelineno-0-42">42</a></span>
<span class="normal"><a href="#__codelineno-0-43">43</a></span>
<span class="normal"><a href="#__codelineno-0-44">44</a></span>
<span class="normal"><a href="#__codelineno-0-45">45</a></span>
<span class="normal"><a href="#__codelineno-0-46">46</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-30"><a id="__codelineno-0-30" name="__codelineno-0-30"></a><span class="k">def</span><span class="w"> </span><span class="nf">load_patient_personas</span><span class="p">(</span><span class="n">filepath</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">PatientPersona</span><span class="p">]:</span>
</span><span id="__span-0-31"><a id="__codelineno-0-31" name="__codelineno-0-31"></a>    <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">filepath</span><span class="p">)</span>
</span><span id="__span-0-32"><a id="__codelineno-0-32" name="__codelineno-0-32"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">():</span>
</span><span id="__span-0-33"><a id="__codelineno-0-33" name="__codelineno-0-33"></a>        <span class="k">raise</span> <span class="ne">FileNotFoundError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Patient persona file not found: </span><span class="si">{</span><span class="n">filepath</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-0-34"><a id="__codelineno-0-34" name="__codelineno-0-34"></a>
</span><span id="__span-0-35"><a id="__codelineno-0-35" name="__codelineno-0-35"></a>    <span class="n">raw_list</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">path</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
</span><span id="__span-0-36"><a id="__codelineno-0-36" name="__codelineno-0-36"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">raw_list</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
</span><span id="__span-0-37"><a id="__codelineno-0-37" name="__codelineno-0-37"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Patient persona YAML must be a list"</span><span class="p">)</span>
</span><span id="__span-0-38"><a id="__codelineno-0-38" name="__codelineno-0-38"></a>
</span><span id="__span-0-39"><a id="__codelineno-0-39" name="__codelineno-0-39"></a>    <span class="n">required_fields</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">PatientPersona</span><span class="o">.</span><span class="n">model_fields</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="__span-0-40"><a id="__codelineno-0-40" name="__codelineno-0-40"></a>
</span><span id="__span-0-41"><a id="__codelineno-0-41" name="__codelineno-0-41"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">PatientPersona</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-0-42"><a id="__codelineno-0-42" name="__codelineno-0-42"></a>    <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">raw_list</span><span class="p">:</span>
</span><span id="__span-0-43"><a id="__codelineno-0-43" name="__codelineno-0-43"></a>        <span class="n">entry</span> <span class="o">=</span> <span class="n">_fill_defaults</span><span class="p">(</span><span class="n">entry</span><span class="p">,</span> <span class="n">required_fields</span><span class="p">)</span>
</span><span id="__span-0-44"><a id="__codelineno-0-44" name="__codelineno-0-44"></a>        <span class="n">personas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">PatientPersona</span><span class="o">.</span><span class="n">model_validate</span><span class="p">(</span><span class="n">entry</span><span class="p">))</span>
</span><span id="__span-0-45"><a id="__codelineno-0-45" name="__codelineno-0-45"></a>
</span><span id="__span-0-46"><a id="__codelineno-0-46" name="__codelineno-0-46"></a>    <span class="k">return</span> <span class="n">personas</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.load_nurse_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">load_nurse_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.load_nurse_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">load_nurse_personas</span><span class="p">(</span><span class="n">filepath</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.NursePersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/personas/loader.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-49">49</a></span>
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
<span class="normal"><a href="#__codelineno-0-65">65</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-49"><a id="__codelineno-0-49" name="__codelineno-0-49"></a><span class="k">def</span><span class="w"> </span><span class="nf">load_nurse_personas</span><span class="p">(</span><span class="n">filepath</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NursePersona</span><span class="p">]:</span>
</span><span id="__span-0-50"><a id="__codelineno-0-50" name="__codelineno-0-50"></a>    <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">filepath</span><span class="p">)</span>
</span><span id="__span-0-51"><a id="__codelineno-0-51" name="__codelineno-0-51"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">():</span>
</span><span id="__span-0-52"><a id="__codelineno-0-52" name="__codelineno-0-52"></a>        <span class="k">raise</span> <span class="ne">FileNotFoundError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Nurse persona file not found: </span><span class="si">{</span><span class="n">filepath</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-0-53"><a id="__codelineno-0-53" name="__codelineno-0-53"></a>
</span><span id="__span-0-54"><a id="__codelineno-0-54" name="__codelineno-0-54"></a>    <span class="n">raw_list</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">path</span><span class="o">.</span><span class="n">read_text</span><span class="p">())</span>
</span><span id="__span-0-55"><a id="__codelineno-0-55" name="__codelineno-0-55"></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">raw_list</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
</span><span id="__span-0-56"><a id="__codelineno-0-56" name="__codelineno-0-56"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Nurse persona YAML must be a list"</span><span class="p">)</span>
</span><span id="__span-0-57"><a id="__codelineno-0-57" name="__codelineno-0-57"></a>
</span><span id="__span-0-58"><a id="__codelineno-0-58" name="__codelineno-0-58"></a>    <span class="n">required_fields</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">NursePersona</span><span class="o">.</span><span class="n">model_fields</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="__span-0-59"><a id="__codelineno-0-59" name="__codelineno-0-59"></a>
</span><span id="__span-0-60"><a id="__codelineno-0-60" name="__codelineno-0-60"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NursePersona</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-0-61"><a id="__codelineno-0-61" name="__codelineno-0-61"></a>    <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">raw_list</span><span class="p">:</span>
</span><span id="__span-0-62"><a id="__codelineno-0-62" name="__codelineno-0-62"></a>        <span class="n">entry</span> <span class="o">=</span> <span class="n">_fill_defaults</span><span class="p">(</span><span class="n">entry</span><span class="p">,</span> <span class="n">required_fields</span><span class="p">)</span>
</span><span id="__span-0-63"><a id="__codelineno-0-63" name="__codelineno-0-63"></a>        <span class="n">personas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NursePersona</span><span class="o">.</span><span class="n">model_validate</span><span class="p">(</span><span class="n">entry</span><span class="p">))</span>
</span><span id="__span-0-64"><a id="__codelineno-0-64" name="__codelineno-0-64"></a>
</span><span id="__span-0-65"><a id="__codelineno-0-65" name="__codelineno-0-65"></a>    <span class="k">return</span> <span class="n">personas</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div><h2 id="sampling">Sampling<a class="headerlink" href="#sampling" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.sample_patient_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">sample_patient_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.sample_patient_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">sample_patient_personas</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.PatientPersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientPersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.PatientPersona&lt;/code&gt;)'>PatientPersona</a></span><span class="p">],</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">k</span><span class="p">:</span> <span class="n"><span title="int">int</span></span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">seed</span><span class="p">:</span> <span class="n"><span title="int">int</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.PatientPersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientPersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.PatientPersona&lt;/code&gt;)'>PatientPersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/personas/loader.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-73">73</a></span>
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
<span class="normal"><a href="#__codelineno-0-84">84</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-73"><a id="__codelineno-0-73" name="__codelineno-0-73"></a><span class="k">def</span><span class="w"> </span><span class="nf">sample_patient_personas</span><span class="p">(</span>
</span><span id="__span-0-74"><a id="__codelineno-0-74" name="__codelineno-0-74"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">PatientPersona</span><span class="p">],</span>
</span><span id="__span-0-75"><a id="__codelineno-0-75" name="__codelineno-0-75"></a>    <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="__span-0-76"><a id="__codelineno-0-76" name="__codelineno-0-76"></a>    <span class="n">seed</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-77"><a id="__codelineno-0-77" name="__codelineno-0-77"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">PatientPersona</span><span class="p">]:</span>
</span><span id="__span-0-78"><a id="__codelineno-0-78" name="__codelineno-0-78"></a>    <span class="k">if</span> <span class="n">k</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">personas</span><span class="p">):</span>
</span><span id="__span-0-79"><a id="__codelineno-0-79" name="__codelineno-0-79"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
</span><span id="__span-0-80"><a id="__codelineno-0-80" name="__codelineno-0-80"></a>            <span class="sa">f</span><span class="s2">"Cannot sample k=</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2"> personas from population of size </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">personas</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
</span><span id="__span-0-81"><a id="__codelineno-0-81" name="__codelineno-0-81"></a>        <span class="p">)</span>
</span><span id="__span-0-82"><a id="__codelineno-0-82" name="__codelineno-0-82"></a>
</span><span id="__span-0-83"><a id="__codelineno-0-83" name="__codelineno-0-83"></a>    <span class="n">rng</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">Random</span><span class="p">(</span><span class="n">seed</span><span class="p">)</span>
</span><span id="__span-0-84"><a id="__codelineno-0-84" name="__codelineno-0-84"></a>    <span class="k">return</span> <span class="n">rng</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">personas</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.sample_nurse_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">sample_nurse_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.sample_nurse_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">sample_nurse_personas</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.NursePersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">],</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">k</span><span class="p">:</span> <span class="n"><span title="int">int</span></span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">seed</span><span class="p">:</span> <span class="n"><span title="int">int</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.NursePersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/personas/loader.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-87">87</a></span>
<span class="normal"><a href="#__codelineno-0-88">88</a></span>
<span class="normal"><a href="#__codelineno-0-89">89</a></span>
<span class="normal"><a href="#__codelineno-0-90">90</a></span>
<span class="normal"><a href="#__codelineno-0-91">91</a></span>
<span class="normal"><a href="#__codelineno-0-92">92</a></span>
<span class="normal"><a href="#__codelineno-0-93">93</a></span>
<span class="normal"><a href="#__codelineno-0-94">94</a></span>
<span class="normal"><a href="#__codelineno-0-95">95</a></span>
<span class="normal"><a href="#__codelineno-0-96">96</a></span>
<span class="normal"><a href="#__codelineno-0-97">97</a></span>
<span class="normal"><a href="#__codelineno-0-98">98</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-87"><a id="__codelineno-0-87" name="__codelineno-0-87"></a><span class="k">def</span><span class="w"> </span><span class="nf">sample_nurse_personas</span><span class="p">(</span>
</span><span id="__span-0-88"><a id="__codelineno-0-88" name="__codelineno-0-88"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NursePersona</span><span class="p">],</span>
</span><span id="__span-0-89"><a id="__codelineno-0-89" name="__codelineno-0-89"></a>    <span class="n">k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="__span-0-90"><a id="__codelineno-0-90" name="__codelineno-0-90"></a>    <span class="n">seed</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-91"><a id="__codelineno-0-91" name="__codelineno-0-91"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NursePersona</span><span class="p">]:</span>
</span><span id="__span-0-92"><a id="__codelineno-0-92" name="__codelineno-0-92"></a>    <span class="k">if</span> <span class="n">k</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">personas</span><span class="p">):</span>
</span><span id="__span-0-93"><a id="__codelineno-0-93" name="__codelineno-0-93"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
</span><span id="__span-0-94"><a id="__codelineno-0-94" name="__codelineno-0-94"></a>            <span class="sa">f</span><span class="s2">"Cannot sample k=</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2"> personas from population of size </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">personas</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
</span><span id="__span-0-95"><a id="__codelineno-0-95" name="__codelineno-0-95"></a>        <span class="p">)</span>
</span><span id="__span-0-96"><a id="__codelineno-0-96" name="__codelineno-0-96"></a>
</span><span id="__span-0-97"><a id="__codelineno-0-97" name="__codelineno-0-97"></a>    <span class="n">rng</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">Random</span><span class="p">(</span><span class="n">seed</span><span class="p">)</span>
</span><span id="__span-0-98"><a id="__codelineno-0-98" name="__codelineno-0-98"></a>    <span class="k">return</span> <span class="n">rng</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">personas</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div><h2 id="filtering">Filtering<a class="headerlink" href="#filtering" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.filter_patient_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">filter_patient_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.filter_patient_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">filter_patient_personas</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.PatientPersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientPersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.PatientPersona&lt;/code&gt;)'>PatientPersona</a></span><span class="p">],</span> <span class="n">criteria</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="str">str</span></span><span class="p">]</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.PatientPersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientPersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.PatientPersona&lt;/code&gt;)'>PatientPersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/personas/loader.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-106">106</a></span>
<span class="normal"><a href="#__codelineno-0-107">107</a></span>
<span class="normal"><a href="#__codelineno-0-108">108</a></span>
<span class="normal"><a href="#__codelineno-0-109">109</a></span>
<span class="normal"><a href="#__codelineno-0-110">110</a></span>
<span class="normal"><a href="#__codelineno-0-111">111</a></span>
<span class="normal"><a href="#__codelineno-0-112">112</a></span>
<span class="normal"><a href="#__codelineno-0-113">113</a></span>
<span class="normal"><a href="#__codelineno-0-114">114</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-106"><a id="__codelineno-0-106" name="__codelineno-0-106"></a><span class="k">def</span><span class="w"> </span><span class="nf">filter_patient_personas</span><span class="p">(</span>
</span><span id="__span-0-107"><a id="__codelineno-0-107" name="__codelineno-0-107"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">PatientPersona</span><span class="p">],</span>
</span><span id="__span-0-108"><a id="__codelineno-0-108" name="__codelineno-0-108"></a>    <span class="n">criteria</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
</span><span id="__span-0-109"><a id="__codelineno-0-109" name="__codelineno-0-109"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">PatientPersona</span><span class="p">]:</span>
</span><span id="__span-0-110"><a id="__codelineno-0-110" name="__codelineno-0-110"></a>    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-0-111"><a id="__codelineno-0-111" name="__codelineno-0-111"></a>    <span class="k">for</span> <span class="n">persona</span> <span class="ow">in</span> <span class="n">personas</span><span class="p">:</span>
</span><span id="__span-0-112"><a id="__codelineno-0-112" name="__codelineno-0-112"></a>        <span class="k">if</span> <span class="nb">all</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">persona</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span> <span class="o">==</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">criteria</span><span class="o">.</span><span class="n">items</span><span class="p">()):</span>
</span><span id="__span-0-113"><a id="__codelineno-0-113" name="__codelineno-0-113"></a>            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">persona</span><span class="p">)</span>
</span><span id="__span-0-114"><a id="__codelineno-0-114" name="__codelineno-0-114"></a>    <span class="k">return</span> <span class="n">results</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.filter_nurse_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">filter_nurse_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.filter_nurse_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">filter_nurse_personas</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.NursePersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">],</span> <span class="n">criteria</span><span class="p">:</span> <span class="n"><span title="typing.Dict">Dict</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><span title="str">str</span></span><span class="p">]</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.NursePersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/personas/loader.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-117">117</a></span>
<span class="normal"><a href="#__codelineno-0-118">118</a></span>
<span class="normal"><a href="#__codelineno-0-119">119</a></span>
<span class="normal"><a href="#__codelineno-0-120">120</a></span>
<span class="normal"><a href="#__codelineno-0-121">121</a></span>
<span class="normal"><a href="#__codelineno-0-122">122</a></span>
<span class="normal"><a href="#__codelineno-0-123">123</a></span>
<span class="normal"><a href="#__codelineno-0-124">124</a></span>
<span class="normal"><a href="#__codelineno-0-125">125</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-117"><a id="__codelineno-0-117" name="__codelineno-0-117"></a><span class="k">def</span><span class="w"> </span><span class="nf">filter_nurse_personas</span><span class="p">(</span>
</span><span id="__span-0-118"><a id="__codelineno-0-118" name="__codelineno-0-118"></a>    <span class="n">personas</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NursePersona</span><span class="p">],</span>
</span><span id="__span-0-119"><a id="__codelineno-0-119" name="__codelineno-0-119"></a>    <span class="n">criteria</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
</span><span id="__span-0-120"><a id="__codelineno-0-120" name="__codelineno-0-120"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NursePersona</span><span class="p">]:</span>
</span><span id="__span-0-121"><a id="__codelineno-0-121" name="__codelineno-0-121"></a>    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-0-122"><a id="__codelineno-0-122" name="__codelineno-0-122"></a>    <span class="k">for</span> <span class="n">persona</span> <span class="ow">in</span> <span class="n">personas</span><span class="p">:</span>
</span><span id="__span-0-123"><a id="__codelineno-0-123" name="__codelineno-0-123"></a>        <span class="k">if</span> <span class="nb">all</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">persona</span><span class="p">,</span> <span class="n">k</span><span class="p">)</span> <span class="o">==</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">criteria</span><span class="o">.</span><span class="n">items</span><span class="p">()):</span>
</span><span id="__span-0-124"><a id="__codelineno-0-124" name="__codelineno-0-124"></a>            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">persona</span><span class="p">)</span>
</span><span id="__span-0-125"><a id="__codelineno-0-125" name="__codelineno-0-125"></a>    <span class="k">return</span> <span class="n">results</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
