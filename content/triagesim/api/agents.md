---
title: "triagesim.agents"
type: "docsite"
docSite: "triagesim"
---

<h1 id="triagesimagents"><code>triagesim.agents</code><a class="headerlink" href="#triagesimagents" title="Permanent link">¶</a></h1>
<p>Agents and the LLM backends that drive them.</p>
<div class="language-python highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="kn">from</span><span class="w"> </span><span class="nn">triagesim.agents</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseLLM</span><span class="p">,</span> <span class="n">OpenRouterLLM</span><span class="p">,</span> <span class="n">NurseAgent</span><span class="p">,</span> <span class="n">PatientAgent</span>
</span></code></pre></div>
<p>See <a href="/triagesim/guide/agents/">Agents and LLM backends</a> for usage and for how to write
a custom backend.</p>
<h2 id="llm-backends">LLM backends<a class="headerlink" href="#llm-backends" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.agents.base_agent.BaseLLM">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">BaseLLM</span>
<a class="headerlink" href="#triagesim.agents.base_agent.BaseLLM" title="Permanent link">¶</a></h3>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><span title="abc.ABC">ABC</span></code></p>
<p>Abstract interface for ALL language model backends.
Agents will call <code>.generate()</code> to produce structured outputs.</p>
<div class="doc doc-children">
<div class="doc doc-object doc-function">
<h4 class="doc doc-heading" id="triagesim.agents.base_agent.BaseLLM.generate">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <span class="doc doc-object-name doc-function-name">generate</span>
<span class="doc doc-labels">
<small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
</span>
<a class="headerlink" href="#triagesim.agents.base_agent.BaseLLM.generate" title="Permanent link">¶</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">generate</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">prompt</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">max_tokens</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="int">int</span></span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">stop</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Union">Union</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents">
<p>Generate a response given a prompt.</p>
<p>This method must return either:
- raw text (for unstructured outputs), or
- a structured Pydantic model (if output_type was provided).</p>
<p>The calling agent assumes the correct model/schema is applied
via the backend's <code>output_type</code> during instantiation.</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>prompt</code>
</td>
<td>
<code><span title="str">str</span></code>
</td>
<td>
<div class="doc-md-description">
<p>the model input text</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>max_tokens</code>
</td>
<td>
<code><span title="typing.Optional">Optional</span>[<span title="int">int</span>]</code>
</td>
<td>
<div class="doc-md-description">
<p>optional token cap</p>
</div>
</td>
<td>
<code>None</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>stop</code>
</td>
<td>
<code><span title="typing.Optional">Optional</span>[<span title="typing.List">List</span>[<span title="str">str</span>]]</code>
</td>
<td>
<div class="doc-md-description">
<p>optional stop sequences</p>
</div>
</td>
<td>
<code>None</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>**kwargs</code>
</td>
<td>
</td>
<td>
<div class="doc-md-description">
<p>backend-specific overrides</p>
</div>
</td>
<td>
<code>{}</code>
</td>
</tr>
</tbody>
</table>
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
<code><span title="typing.Union">Union</span>[<span title="str">str</span>, <a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a>]</code>
</td>
<td>
<div class="doc-md-description">
<p>Model output (string or Pydantic output model)</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.agents.base_agent.OpenRouterLLM">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">OpenRouterLLM</span>
<a class="headerlink" href="#triagesim.agents.base_agent.OpenRouterLLM" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">OpenRouterLLM</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">model_name</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">output_type</span><span class="p">:</span> <span class="n"><span title="typing.Type">Type</span></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a></span><span class="p">],</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="o">**</span><span class="n">agent_kwargs</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="p">)</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" href="#triagesim.agents.base_agent.BaseLLM" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseLLM&lt;/span&gt; (&lt;code&gt;triagesim.agents.base_agent.BaseLLM&lt;/code&gt;)'>BaseLLM</a></code></p>
<p>LLM backend using OpenRouter via the <code>pydantic_ai</code> SDK.</p>
<p>This wraps an <code>Agent</code> configured with a given output model type
so that <code>.generate()</code> returns a structured output or text.</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>model_name</code>
</td>
<td>
<code><span title="str">str</span></code>
</td>
<td>
<div class="doc-md-description">
<p>OpenRouter model specifier (e.g., "google/gemini-3-pro-preview")</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>output_type</code>
</td>
<td>
<code><span title="typing.Type">Type</span>[<a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a>]</code>
</td>
<td>
<div class="doc-md-description">
<p>a subclass of BaseAgentOutput Pydantic model
         that the Agent will produce directly.</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
</tbody>
</table>
<details class="usage" open="">
<summary>Usage</summary>
<p>llm = OpenRouterLLM("google/gemini-3-pro-preview", output_type=NurseOutput)
nurse_action = llm.generate(prompt)</p>
</details>
<p>Create an Agent configured to produce the right output type.</p>
<p>The API key is resolved from triagesim.config.OPENROUTER_API_KEY.</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>model_name</code>
</td>
<td>
<code><span title="str">str</span></code>
</td>
<td>
<div class="doc-md-description">
<p>the OpenRouter model identifier</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>output_type</code>
</td>
<td>
<code><span title="typing.Type">Type</span>[<a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a>]</code>
</td>
<td>
<div class="doc-md-description">
<p>Pydantic model to enforce output structure</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>agent_kwargs</code>
</td>
<td>
</td>
<td>
<div class="doc-md-description">
<p>any extra fields passed to Agent()</p>
</div>
</td>
<td>
<code>{}</code>
</td>
</tr>
</tbody>
</table>
<div class="doc doc-children">
<div class="doc doc-object doc-function">
<h4 class="doc doc-heading" id="triagesim.agents.base_agent.OpenRouterLLM.generate">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <span class="doc doc-object-name doc-function-name">generate</span>
<a class="headerlink" href="#triagesim.agents.base_agent.OpenRouterLLM.generate" title="Permanent link">¶</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">generate</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">prompt</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">max_tokens</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="int">int</span></span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">stop</span><span class="p">:</span> <span class="n"><span title="typing.Optional">Optional</span></span><span class="p">[</span><span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
</span><span id="__span-0-6"><a href="#__codelineno-0-6" id="__codelineno-0-6" name="__codelineno-0-6"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.Union">Union</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents">
<p>Run a synchronous request against the configured agent.</p>
<p>Because the agent is configured with <code>output_type</code>, this method
should return a structured Pydantic model or a simple string</p>
<p><span class="doc-section-title">Parameters:</span></p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="doc-section-item">
<td>
<code>prompt</code>
</td>
<td>
<code><span title="str">str</span></code>
</td>
<td>
<div class="doc-md-description">
<p>the text prompt</p>
</div>
</td>
<td>
<em>required</em>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>max_tokens</code>
</td>
<td>
<code><span title="typing.Optional">Optional</span>[<span title="int">int</span>]</code>
</td>
<td>
<div class="doc-md-description">
<p>optionally limit tokens</p>
</div>
</td>
<td>
<code>None</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>stop</code>
</td>
<td>
<code><span title="typing.Optional">Optional</span>[<span title="typing.List">List</span>[<span title="str">str</span>]]</code>
</td>
<td>
<div class="doc-md-description">
<p>optional stop sequences</p>
</div>
</td>
<td>
<code>None</code>
</td>
</tr>
<tr class="doc-section-item">
<td>
<code>**kwargs</code>
</td>
<td>
</td>
<td>
<div class="doc-md-description">
<p>passed to agent.run_sync()</p>
</div>
</td>
<td>
<code>{}</code>
</td>
</tr>
</tbody>
</table>
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
<code><span title="typing.Union">Union</span>[<span title="str">str</span>, <a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseAgentOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.BaseAgentOutput&lt;/code&gt;)'>BaseAgentOutput</a>]</code>
</td>
<td>
<div class="doc-md-description">
<p>Model output from the LLM call</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div><h2 id="agents">Agents<a class="headerlink" href="#agents" title="Permanent link">¶</a></h2>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.agents.nurse_agent.NurseAgent">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">NurseAgent</span>
<a class="headerlink" href="#triagesim.agents.nurse_agent.NurseAgent" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">NurseAgent</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">llm</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="#triagesim.agents.base_agent.BaseLLM" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseLLM&lt;/span&gt; (&lt;code&gt;triagesim.agents.base_agent.BaseLLM&lt;/code&gt;)'>BaseLLM</a></span><span class="p">,</span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a>    <span class="n">persona</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/personas/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NursePersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.NursePersona&lt;/code&gt;)'>NursePersona</a></span><span class="p">,</span>
</span><span id="__span-0-4"><a href="#__codelineno-0-4" id="__codelineno-0-4" name="__codelineno-0-4"></a>    <span class="n">algorithm</span><span class="p">:</span> <span class="n"><span title="str">str</span></span> <span class="o">=</span> <span class="s2">"esi"</span><span class="p">,</span>
</span><span id="__span-0-5"><a href="#__codelineno-0-5" id="__codelineno-0-5" name="__codelineno-0-5"></a><span class="p">)</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>Nurse agent responsible for:
- Choosing the next triage action (NurseOutput)
- Inferring belief updates from the nurse's perspective</p>
<p>The SAME LLM + persona is used for both decision-making
and belief inference.</p>
<div class="doc doc-children">
<div class="doc doc-object doc-function">
<h4 class="doc doc-heading" id="triagesim.agents.nurse_agent.NurseAgent.act">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <span class="doc doc-object-name doc-function-name">act</span>
<a class="headerlink" href="#triagesim.agents.nurse_agent.NurseAgent.act" title="Permanent link">¶</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">act</span><span class="p">(</span><span class="n">history</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n">known_vitals</span><span class="p">:</span> <span class="n"><span title="set">set</span></span><span class="p">[</span><span class="n"><span title="str">str</span></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;NurseOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.NurseOutput&lt;/code&gt;)'>NurseOutput</a></span>
</span></code></pre></div>
<div class="doc doc-contents">
<p>Given dialogue history, produce the next nurse action
as a structured NurseOutput.</p>
</div>
</div>
<div class="doc doc-object doc-function">
<h4 class="doc doc-heading" id="triagesim.agents.nurse_agent.NurseAgent.infer_belief_updates">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <span class="doc doc-object-name doc-function-name">infer_belief_updates</span>
<a class="headerlink" href="#triagesim.agents.nurse_agent.NurseAgent.infer_belief_updates" title="Permanent link">¶</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">infer_belief_updates</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">history</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n">last_utterance</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n">turn</span><span class="p">:</span> <span class="n"><span title="int">int</span></span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><span title="typing.List">List</span></span><span class="p">[</span><span class="n"><span title="triagesim.core.belief_graph.BeliefSlotUpdate">BeliefSlotUpdate</span></span><span class="p">]</span>
</span></code></pre></div>
<div class="doc doc-contents">
<p>Infer belief updates from the nurse's perspective.</p>
<p>This is called by the environment AFTER a patient utterance.
Failures must never crash the episode.</p>
</div>
</div>
</div>
</div>
</div>
<div class="doc doc-object doc-class">
<h3 class="doc doc-heading" id="triagesim.agents.patient_agent.PatientAgent">
<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code> <span class="doc doc-object-name doc-class-name">PatientAgent</span>
<a class="headerlink" href="#triagesim.agents.patient_agent.PatientAgent" title="Permanent link">¶</a></h3>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">PatientAgent</span><span class="p">(</span><span class="n">llm</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="#triagesim.agents.base_agent.BaseLLM" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;BaseLLM&lt;/span&gt; (&lt;code&gt;triagesim.agents.base_agent.BaseLLM&lt;/code&gt;)'>BaseLLM</a></span><span class="p">,</span> <span class="n">persona</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/personas/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientPersona&lt;/span&gt; (&lt;code&gt;triagesim.personas.schema.PatientPersona&lt;/code&gt;)'>PatientPersona</a></span><span class="p">)</span>
</span></code></pre></div>
<div class="doc doc-contents first">
<p>PatientAgent generates patient utterances conditioned on:
- dialogue history
- a categorical persona
- explicit response budget rules</p>
<div class="doc doc-children">
<div class="doc doc-object doc-function">
<h4 class="doc doc-heading" id="triagesim.agents.patient_agent.PatientAgent.act">
<code class="doc-symbol doc-symbol-heading doc-symbol-method"></code> <span class="doc doc-object-name doc-function-name">act</span>
<a class="headerlink" href="#triagesim.agents.patient_agent.PatientAgent.act" title="Permanent link">¶</a></h4>
<div class="language-python doc-signature highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a><span class="nf">act</span><span class="p">(</span>
</span><span id="__span-0-2"><a href="#__codelineno-0-2" id="__codelineno-0-2" name="__codelineno-0-2"></a>    <span class="n">history</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n">chief_complaint</span><span class="p">:</span> <span class="n"><span title="str">str</span></span><span class="p">,</span> <span class="n">pain</span><span class="p">:</span> <span class="n"><span title="int">int</span></span>
</span><span id="__span-0-3"><a href="#__codelineno-0-3" id="__codelineno-0-3" name="__codelineno-0-3"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" href="/triagesim/api/core/" title='&lt;code class="doc-symbol doc-symbol-heading doc-symbol-class"&gt;&lt;/code&gt;            &lt;span class="doc doc-object-name doc-class-name"&gt;PatientOutput&lt;/span&gt; (&lt;code&gt;triagesim.core.output_schema.PatientOutput&lt;/code&gt;)'>PatientOutput</a></span>
</span></code></pre></div>
<div class="doc doc-contents">
<p>Generate the patient's next utterance as a structured PatientOutput.</p>
<details class="the-llm-backend-must-have-been-initialized-with" open="">
<summary>The LLM backend MUST have been initialized with</summary>
<p>output_type = PatientOutput</p>
</details>
</div>
</div>
</div>
</div>
</div>
