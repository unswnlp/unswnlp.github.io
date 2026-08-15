---
title: "triagesim.core"
type: "docsite"
docSite: "triagesim"
---

<h1 id="triagesimcore"><code>triagesim.core</code><a class="headerlink" href="#triagesimcore" title="Permanent link">¶</a></h1>
<p>The structured output schemas that agents must produce.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.core</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseAgentOutput</span><span class="p">,</span> <span class="n">NurseOutput</span><span class="p">,</span> <span class="n">PatientOutput</span>
</span></code></pre></div>
<p>Each schema forbids extra fields, so a model cannot introduce keys the
environment never sanctioned. See <a href="/triagesim/guide/agents/">Output schemas</a>.</p>
<h2 id="base">Base<a class="headerlink" href="#base" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.core.base_schema.BaseAgentOutput">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">BaseAgentOutput</span>
<a class="headerlink" href="#triagesim.core.base_schema.BaseAgentOutput" title="Permanent link">¶</a></h3>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><span title="pydantic.BaseModel">BaseModel</span></code></p>
<p>Base class for all agent outputs.
Enforces JSON-only, structured communication.</p>
<div class="doc doc-children">
</div>
</div>
</div><h2 id="agent-outputs">Agent outputs<a class="headerlink" href="#agent-outputs" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.core.output_schema.PatientOutput">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">PatientOutput</span>
<a class="headerlink" href="#triagesim.core.output_schema.PatientOutput" title="Permanent link">¶</a></h3>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" href="#triagesim.core.base_schema.BaseAgentOutput" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.base_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a></code></p>
<div class="doc doc-children">
</div>
</div>
</div>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.core.output_schema.NurseOutput">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">NurseOutput</span>
<a class="headerlink" href="#triagesim.core.output_schema.NurseOutput" title="Permanent link">¶</a></h3>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" href="#triagesim.core.base_schema.BaseAgentOutput" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.base_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a></code></p>
<div class="doc doc-children">
</div>
</div>
</div><h2 id="internal-modules">Internal modules<a class="headerlink" href="#internal-modules" title="Permanent link">¶</a></h2>
<p>The rest of <code>triagesim.core</code> — the environment, belief graph, state stores and
action mapping — is internal and not re-exported. Its behaviour is described in
<a href="/triagesim/guide/concepts/">Core concepts</a>.</p>
