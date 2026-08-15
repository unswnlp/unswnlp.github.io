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
</div>
</div>
<div class="doc doc-object doc-function">
<h3 class="doc doc-heading" id="triagesim.personas.loader.load_nurse_personas">
<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code> <span class="doc doc-object-name doc-function-name">load_nurse_personas</span>
<a class="headerlink" href="#triagesim.personas.loader.load_nurse_personas" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">load_nurse_personas</span><span class="p">(</span><span class="n">filepath</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="#triagesim.personas.schema.NursePersona" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents first">
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
</div>
</div>
