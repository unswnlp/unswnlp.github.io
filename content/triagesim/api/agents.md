---
title: "triagesim.agents"
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/base_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-18">18</a></span>
<span class="normal"><a href="#__codelineno-0-19">19</a></span>
<span class="normal"><a href="#__codelineno-0-20">20</a></span>
<span class="normal"><a href="#__codelineno-0-21">21</a></span>
<span class="normal"><a href="#__codelineno-0-22">22</a></span>
<span class="normal"><a href="#__codelineno-0-23">23</a></span>
<span class="normal"><a href="#__codelineno-0-24">24</a></span>
<span class="normal"><a href="#__codelineno-0-25">25</a></span>
<span class="normal"><a href="#__codelineno-0-26">26</a></span>
<span class="normal"><a href="#__codelineno-0-27">27</a></span>
<span class="normal"><a href="#__codelineno-0-28">28</a></span>
<span class="normal"><a href="#__codelineno-0-29">29</a></span>
<span class="normal"><a href="#__codelineno-0-30">30</a></span>
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
<span class="normal"><a href="#__codelineno-0-45">45</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-18"><a id="__codelineno-0-18" name="__codelineno-0-18"></a><span class="nd">@abstractmethod</span>
</span><span id="__span-0-19"><a id="__codelineno-0-19" name="__codelineno-0-19"></a><span class="k">def</span><span class="w"> </span><span class="nf">generate</span><span class="p">(</span>
</span><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20"></a>    <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21"></a>    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22"></a>    <span class="n">max_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23"></a>    <span class="n">stop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
</span><span id="__span-0-25"><a id="__codelineno-0-25" name="__codelineno-0-25"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseAgentOutput</span><span class="p">]:</span>
</span><span id="__span-0-26"><a id="__codelineno-0-26" name="__codelineno-0-26"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-27"><a id="__codelineno-0-27" name="__codelineno-0-27"></a><span class="sd">    Generate a response given a prompt.</span>
</span><span id="__span-0-28"><a id="__codelineno-0-28" name="__codelineno-0-28"></a>
</span><span id="__span-0-29"><a id="__codelineno-0-29" name="__codelineno-0-29"></a><span class="sd">    This method must return either:</span>
</span><span id="__span-0-30"><a id="__codelineno-0-30" name="__codelineno-0-30"></a><span class="sd">    - raw text (for unstructured outputs), or</span>
</span><span id="__span-0-31"><a id="__codelineno-0-31" name="__codelineno-0-31"></a><span class="sd">    - a structured Pydantic model (if output_type was provided).</span>
</span><span id="__span-0-32"><a id="__codelineno-0-32" name="__codelineno-0-32"></a>
</span><span id="__span-0-33"><a id="__codelineno-0-33" name="__codelineno-0-33"></a><span class="sd">    The calling agent assumes the correct model/schema is applied</span>
</span><span id="__span-0-34"><a id="__codelineno-0-34" name="__codelineno-0-34"></a><span class="sd">    via the backend's `output_type` during instantiation.</span>
</span><span id="__span-0-35"><a id="__codelineno-0-35" name="__codelineno-0-35"></a>
</span><span id="__span-0-36"><a id="__codelineno-0-36" name="__codelineno-0-36"></a><span class="sd">    Args:</span>
</span><span id="__span-0-37"><a id="__codelineno-0-37" name="__codelineno-0-37"></a><span class="sd">        prompt: the model input text</span>
</span><span id="__span-0-38"><a id="__codelineno-0-38" name="__codelineno-0-38"></a><span class="sd">        max_tokens: optional token cap</span>
</span><span id="__span-0-39"><a id="__codelineno-0-39" name="__codelineno-0-39"></a><span class="sd">        stop: optional stop sequences</span>
</span><span id="__span-0-40"><a id="__codelineno-0-40" name="__codelineno-0-40"></a><span class="sd">        **kwargs: backend-specific overrides</span>
</span><span id="__span-0-41"><a id="__codelineno-0-41" name="__codelineno-0-41"></a>
</span><span id="__span-0-42"><a id="__codelineno-0-42" name="__codelineno-0-42"></a><span class="sd">    Returns:</span>
</span><span id="__span-0-43"><a id="__codelineno-0-43" name="__codelineno-0-43"></a><span class="sd">        Model output (string or Pydantic output model)</span>
</span><span id="__span-0-44"><a id="__codelineno-0-44" name="__codelineno-0-44"></a><span class="sd">    """</span>
</span><span id="__span-0-45"><a id="__codelineno-0-45" name="__codelineno-0-45"></a>    <span class="k">pass</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/base_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-65">65</a></span>
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
<span class="normal"><a href="#__codelineno-0-84">84</a></span>
<span class="normal"><a href="#__codelineno-0-85">85</a></span>
<span class="normal"><a href="#__codelineno-0-86">86</a></span>
<span class="normal"><a href="#__codelineno-0-87">87</a></span>
<span class="normal"><a href="#__codelineno-0-88">88</a></span>
<span class="normal"><a href="#__codelineno-0-89">89</a></span>
<span class="normal"><a href="#__codelineno-0-90">90</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-65"><a id="__codelineno-0-65" name="__codelineno-0-65"></a><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
</span><span id="__span-0-66"><a id="__codelineno-0-66" name="__codelineno-0-66"></a>    <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-67"><a id="__codelineno-0-67" name="__codelineno-0-67"></a>    <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-0-68"><a id="__codelineno-0-68" name="__codelineno-0-68"></a>    <span class="n">output_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">BaseAgentOutput</span><span class="p">],</span>
</span><span id="__span-0-69"><a id="__codelineno-0-69" name="__codelineno-0-69"></a>    <span class="o">**</span><span class="n">agent_kwargs</span><span class="p">,</span>
</span><span id="__span-0-70"><a id="__codelineno-0-70" name="__codelineno-0-70"></a><span class="p">):</span>
</span><span id="__span-0-71"><a id="__codelineno-0-71" name="__codelineno-0-71"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-72"><a id="__codelineno-0-72" name="__codelineno-0-72"></a><span class="sd">    Create an Agent configured to produce the right output type.</span>
</span><span id="__span-0-73"><a id="__codelineno-0-73" name="__codelineno-0-73"></a>
</span><span id="__span-0-74"><a id="__codelineno-0-74" name="__codelineno-0-74"></a><span class="sd">    The API key is resolved from triagesim.config.OPENROUTER_API_KEY.</span>
</span><span id="__span-0-75"><a id="__codelineno-0-75" name="__codelineno-0-75"></a>
</span><span id="__span-0-76"><a id="__codelineno-0-76" name="__codelineno-0-76"></a><span class="sd">    Args:</span>
</span><span id="__span-0-77"><a id="__codelineno-0-77" name="__codelineno-0-77"></a><span class="sd">        model_name: the OpenRouter model identifier</span>
</span><span id="__span-0-78"><a id="__codelineno-0-78" name="__codelineno-0-78"></a><span class="sd">        output_type: Pydantic model to enforce output structure</span>
</span><span id="__span-0-79"><a id="__codelineno-0-79" name="__codelineno-0-79"></a><span class="sd">        agent_kwargs: any extra fields passed to Agent()</span>
</span><span id="__span-0-80"><a id="__codelineno-0-80" name="__codelineno-0-80"></a><span class="sd">    """</span>
</span><span id="__span-0-81"><a id="__codelineno-0-81" name="__codelineno-0-81"></a>    <span class="c1"># Instantiate the provider with the API key</span>
</span><span id="__span-0-82"><a id="__codelineno-0-82" name="__codelineno-0-82"></a>    <span class="n">provider</span> <span class="o">=</span> <span class="n">OpenRouterProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">OPENROUTER_API_KEY</span><span class="p">)</span>
</span><span id="__span-0-83"><a id="__codelineno-0-83" name="__codelineno-0-83"></a>    <span class="n">settings</span> <span class="o">=</span> <span class="n">OpenRouterModelSettings</span><span class="p">(</span><span class="n">openrouter_reasoning</span><span class="o">=</span><span class="p">{</span><span class="s2">"effort"</span><span class="p">:</span> <span class="s2">"low"</span><span class="p">})</span>
</span><span id="__span-0-84"><a id="__codelineno-0-84" name="__codelineno-0-84"></a>    <span class="c1"># Create the model via pydantic_ai</span>
</span><span id="__span-0-85"><a id="__codelineno-0-85" name="__codelineno-0-85"></a>    <span class="n">model</span> <span class="o">=</span> <span class="n">OpenRouterModel</span><span class="p">(</span><span class="n">model_name</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">provider</span><span class="p">)</span>
</span><span id="__span-0-86"><a id="__codelineno-0-86" name="__codelineno-0-86"></a>
</span><span id="__span-0-87"><a id="__codelineno-0-87" name="__codelineno-0-87"></a>    <span class="c1"># Create the agent that enforces the output_type schema</span>
</span><span id="__span-0-88"><a id="__codelineno-0-88" name="__codelineno-0-88"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
</span><span id="__span-0-89"><a id="__codelineno-0-89" name="__codelineno-0-89"></a>        <span class="n">model</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">output_type</span><span class="p">,</span> <span class="n">model_settings</span><span class="o">=</span><span class="n">settings</span><span class="p">,</span> <span class="o">**</span><span class="n">agent_kwargs</span>
</span><span id="__span-0-90"><a id="__codelineno-0-90" name="__codelineno-0-90"></a>    <span class="p">)</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/base_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-92"> 92</a></span>
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
<span class="normal"><a href="#__codelineno-0-128">128</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-92"><a id="__codelineno-0-92" name="__codelineno-0-92"></a><span class="k">def</span><span class="w"> </span><span class="nf">generate</span><span class="p">(</span>
</span><span id="__span-0-93"><a id="__codelineno-0-93" name="__codelineno-0-93"></a>    <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-94"><a id="__codelineno-0-94" name="__codelineno-0-94"></a>    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-0-95"><a id="__codelineno-0-95" name="__codelineno-0-95"></a>    <span class="n">max_tokens</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-96"><a id="__codelineno-0-96" name="__codelineno-0-96"></a>    <span class="n">stop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="__span-0-97"><a id="__codelineno-0-97" name="__codelineno-0-97"></a>    <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
</span><span id="__span-0-98"><a id="__codelineno-0-98" name="__codelineno-0-98"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">BaseAgentOutput</span><span class="p">]:</span>
</span><span id="__span-0-99"><a id="__codelineno-0-99" name="__codelineno-0-99"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-100"><a id="__codelineno-0-100" name="__codelineno-0-100"></a><span class="sd">    Run a synchronous request against the configured agent.</span>
</span><span id="__span-0-101"><a id="__codelineno-0-101" name="__codelineno-0-101"></a>
</span><span id="__span-0-102"><a id="__codelineno-0-102" name="__codelineno-0-102"></a><span class="sd">    Because the agent is configured with `output_type`, this method</span>
</span><span id="__span-0-103"><a id="__codelineno-0-103" name="__codelineno-0-103"></a><span class="sd">    should return a structured Pydantic model or a simple string</span>
</span><span id="__span-0-104"><a id="__codelineno-0-104" name="__codelineno-0-104"></a>
</span><span id="__span-0-105"><a id="__codelineno-0-105" name="__codelineno-0-105"></a><span class="sd">    Args:</span>
</span><span id="__span-0-106"><a id="__codelineno-0-106" name="__codelineno-0-106"></a><span class="sd">        prompt: the text prompt</span>
</span><span id="__span-0-107"><a id="__codelineno-0-107" name="__codelineno-0-107"></a><span class="sd">        max_tokens: optionally limit tokens</span>
</span><span id="__span-0-108"><a id="__codelineno-0-108" name="__codelineno-0-108"></a><span class="sd">        stop: optional stop sequences</span>
</span><span id="__span-0-109"><a id="__codelineno-0-109" name="__codelineno-0-109"></a><span class="sd">        **kwargs: passed to agent.run_sync()</span>
</span><span id="__span-0-110"><a id="__codelineno-0-110" name="__codelineno-0-110"></a>
</span><span id="__span-0-111"><a id="__codelineno-0-111" name="__codelineno-0-111"></a><span class="sd">    Returns:</span>
</span><span id="__span-0-112"><a id="__codelineno-0-112" name="__codelineno-0-112"></a><span class="sd">        Model output from the LLM call</span>
</span><span id="__span-0-113"><a id="__codelineno-0-113" name="__codelineno-0-113"></a><span class="sd">    """</span>
</span><span id="__span-0-114"><a id="__codelineno-0-114" name="__codelineno-0-114"></a>    <span class="c1"># Build kwargs for pydantic_ai if provided</span>
</span><span id="__span-0-115"><a id="__codelineno-0-115" name="__codelineno-0-115"></a>    <span class="n">run_kwargs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">object</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
</span><span id="__span-0-116"><a id="__codelineno-0-116" name="__codelineno-0-116"></a>    <span class="k">if</span> <span class="n">max_tokens</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-117"><a id="__codelineno-0-117" name="__codelineno-0-117"></a>        <span class="n">run_kwargs</span><span class="p">[</span><span class="s2">"max_tokens"</span><span class="p">]</span> <span class="o">=</span> <span class="n">max_tokens</span>
</span><span id="__span-0-118"><a id="__codelineno-0-118" name="__codelineno-0-118"></a>    <span class="k">if</span> <span class="n">stop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="__span-0-119"><a id="__codelineno-0-119" name="__codelineno-0-119"></a>        <span class="n">run_kwargs</span><span class="p">[</span><span class="s2">"stop"</span><span class="p">]</span> <span class="o">=</span> <span class="n">stop</span>
</span><span id="__span-0-120"><a id="__codelineno-0-120" name="__codelineno-0-120"></a>
</span><span id="__span-0-121"><a id="__codelineno-0-121" name="__codelineno-0-121"></a>    <span class="n">run_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="__span-0-122"><a id="__codelineno-0-122" name="__codelineno-0-122"></a>
</span><span id="__span-0-123"><a id="__codelineno-0-123" name="__codelineno-0-123"></a>    <span class="c1"># Run the model</span>
</span><span id="__span-0-124"><a id="__codelineno-0-124" name="__codelineno-0-124"></a>    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="o">**</span><span class="n">run_kwargs</span><span class="p">)</span>
</span><span id="__span-0-125"><a id="__codelineno-0-125" name="__codelineno-0-125"></a>
</span><span id="__span-0-126"><a id="__codelineno-0-126" name="__codelineno-0-126"></a>    <span class="c1"># Return whatever the parsed agent returns; if output_type is set,</span>
</span><span id="__span-0-127"><a id="__codelineno-0-127" name="__codelineno-0-127"></a>    <span class="c1"># the result should be an instance of that Pydantic model.</span>
</span><span id="__span-0-128"><a id="__codelineno-0-128" name="__codelineno-0-128"></a>    <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">output</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/nurse_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-20">20</a></span>
<span class="normal"><a href="#__codelineno-0-21">21</a></span>
<span class="normal"><a href="#__codelineno-0-22">22</a></span>
<span class="normal"><a href="#__codelineno-0-23">23</a></span>
<span class="normal"><a href="#__codelineno-0-24">24</a></span>
<span class="normal"><a href="#__codelineno-0-25">25</a></span>
<span class="normal"><a href="#__codelineno-0-26">26</a></span>
<span class="normal"><a href="#__codelineno-0-27">27</a></span>
<span class="normal"><a href="#__codelineno-0-28">28</a></span>
<span class="normal"><a href="#__codelineno-0-29">29</a></span>
<span class="normal"><a href="#__codelineno-0-30">30</a></span>
<span class="normal"><a href="#__codelineno-0-31">31</a></span>
<span class="normal"><a href="#__codelineno-0-32">32</a></span>
<span class="normal"><a href="#__codelineno-0-33">33</a></span>
<span class="normal"><a href="#__codelineno-0-34">34</a></span>
<span class="normal"><a href="#__codelineno-0-35">35</a></span>
<span class="normal"><a href="#__codelineno-0-36">36</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-20"><a id="__codelineno-0-20" name="__codelineno-0-20"></a><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
</span><span id="__span-0-21"><a id="__codelineno-0-21" name="__codelineno-0-21"></a>    <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-22"><a id="__codelineno-0-22" name="__codelineno-0-22"></a>    <span class="n">llm</span><span class="p">:</span> <span class="n">BaseLLM</span><span class="p">,</span>
</span><span id="__span-0-23"><a id="__codelineno-0-23" name="__codelineno-0-23"></a>    <span class="n">persona</span><span class="p">:</span> <span class="n">NursePersona</span><span class="p">,</span>
</span><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24"></a>    <span class="n">algorithm</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"esi"</span><span class="p">,</span>
</span><span id="__span-0-25"><a id="__codelineno-0-25" name="__codelineno-0-25"></a><span class="p">):</span>
</span><span id="__span-0-26"><a id="__codelineno-0-26" name="__codelineno-0-26"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
</span><span id="__span-0-27"><a id="__codelineno-0-27" name="__codelineno-0-27"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">persona</span> <span class="o">=</span> <span class="n">persona</span>
</span><span id="__span-0-28"><a id="__codelineno-0-28" name="__codelineno-0-28"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">seen_vital</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="__span-0-29"><a id="__codelineno-0-29" name="__codelineno-0-29"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">logged_flag</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="__span-0-30"><a id="__codelineno-0-30" name="__codelineno-0-30"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">algorithm</span> <span class="o">=</span> <span class="n">algorithm</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
</span><span id="__span-0-31"><a id="__codelineno-0-31" name="__codelineno-0-31"></a>
</span><span id="__span-0-32"><a id="__codelineno-0-32" name="__codelineno-0-32"></a>    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">algorithm</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">{</span><span class="s2">"esi"</span><span class="p">,</span> <span class="s2">"ats"</span><span class="p">}:</span>
</span><span id="__span-0-33"><a id="__codelineno-0-33" name="__codelineno-0-33"></a>        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unsupported triage algorithm: </span><span class="si">{</span><span class="n">algorithm</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</span><span id="__span-0-34"><a id="__codelineno-0-34" name="__codelineno-0-34"></a>
</span><span id="__span-0-35"><a id="__codelineno-0-35" name="__codelineno-0-35"></a>    <span class="c1"># Belief inference uses the SAME LLM and persona</span>
</span><span id="__span-0-36"><a id="__codelineno-0-36" name="__codelineno-0-36"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">_belief_detector</span> <span class="o">=</span> <span class="n">LLMEvidenceDetector</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/nurse_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-42">42</a></span>
<span class="normal"><a href="#__codelineno-0-43">43</a></span>
<span class="normal"><a href="#__codelineno-0-44">44</a></span>
<span class="normal"><a href="#__codelineno-0-45">45</a></span>
<span class="normal"><a href="#__codelineno-0-46">46</a></span>
<span class="normal"><a href="#__codelineno-0-47">47</a></span>
<span class="normal"><a href="#__codelineno-0-48">48</a></span>
<span class="normal"><a href="#__codelineno-0-49">49</a></span>
<span class="normal"><a href="#__codelineno-0-50">50</a></span>
<span class="normal"><a href="#__codelineno-0-51">51</a></span>
<span class="normal"><a href="#__codelineno-0-52">52</a></span>
<span class="normal"><a href="#__codelineno-0-53">53</a></span>
<span class="normal"><a href="#__codelineno-0-54">54</a></span>
<span class="normal"><a href="#__codelineno-0-55">55</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-42"><a id="__codelineno-0-42" name="__codelineno-0-42"></a><span class="k">def</span><span class="w"> </span><span class="nf">act</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">history</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">known_vitals</span><span class="p">:</span> <span class="nb">set</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">NurseOutput</span><span class="p">:</span>
</span><span id="__span-0-43"><a id="__codelineno-0-43" name="__codelineno-0-43"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-44"><a id="__codelineno-0-44" name="__codelineno-0-44"></a><span class="sd">    Given dialogue history, produce the next nurse action</span>
</span><span id="__span-0-45"><a id="__codelineno-0-45" name="__codelineno-0-45"></a><span class="sd">    as a structured NurseOutput.</span>
</span><span id="__span-0-46"><a id="__codelineno-0-46" name="__codelineno-0-46"></a><span class="sd">    """</span>
</span><span id="__span-0-47"><a id="__codelineno-0-47" name="__codelineno-0-47"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">start</span> <span class="o">=</span> <span class="kc">True</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">history</span> <span class="k">else</span> <span class="kc">False</span>
</span><span id="__span-0-48"><a id="__codelineno-0-48" name="__codelineno-0-48"></a>
</span><span id="__span-0-49"><a id="__codelineno-0-49" name="__codelineno-0-49"></a>    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_prompt</span><span class="p">(</span><span class="n">history</span><span class="p">,</span> <span class="n">known_vitals</span><span class="p">)</span>
</span><span id="__span-0-50"><a id="__codelineno-0-50" name="__codelineno-0-50"></a>
</span><span id="__span-0-51"><a id="__codelineno-0-51" name="__codelineno-0-51"></a>    <span class="c1"># IMPORTANT:</span>
</span><span id="__span-0-52"><a id="__codelineno-0-52" name="__codelineno-0-52"></a>    <span class="c1"># llm.generate() MUST return a NurseOutput</span>
</span><span id="__span-0-53"><a id="__codelineno-0-53" name="__codelineno-0-53"></a>    <span class="c1"># because output_type=NurseOutput was set on the backend</span>
</span><span id="__span-0-54"><a id="__codelineno-0-54" name="__codelineno-0-54"></a>    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
</span><span id="__span-0-55"><a id="__codelineno-0-55" name="__codelineno-0-55"></a>    <span class="k">return</span> <span class="n">result</span>  <span class="c1"># type: ignore[return-value]</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/nurse_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-61"> 61</a></span>
<span class="normal"><a href="#__codelineno-0-62"> 62</a></span>
<span class="normal"><a href="#__codelineno-0-63"> 63</a></span>
<span class="normal"><a href="#__codelineno-0-64"> 64</a></span>
<span class="normal"><a href="#__codelineno-0-65"> 65</a></span>
<span class="normal"><a href="#__codelineno-0-66"> 66</a></span>
<span class="normal"><a href="#__codelineno-0-67"> 67</a></span>
<span class="normal"><a href="#__codelineno-0-68"> 68</a></span>
<span class="normal"><a href="#__codelineno-0-69"> 69</a></span>
<span class="normal"><a href="#__codelineno-0-70"> 70</a></span>
<span class="normal"><a href="#__codelineno-0-71"> 71</a></span>
<span class="normal"><a href="#__codelineno-0-72"> 72</a></span>
<span class="normal"><a href="#__codelineno-0-73"> 73</a></span>
<span class="normal"><a href="#__codelineno-0-74"> 74</a></span>
<span class="normal"><a href="#__codelineno-0-75"> 75</a></span>
<span class="normal"><a href="#__codelineno-0-76"> 76</a></span>
<span class="normal"><a href="#__codelineno-0-77"> 77</a></span>
<span class="normal"><a href="#__codelineno-0-78"> 78</a></span>
<span class="normal"><a href="#__codelineno-0-79"> 79</a></span>
<span class="normal"><a href="#__codelineno-0-80"> 80</a></span>
<span class="normal"><a href="#__codelineno-0-81"> 81</a></span>
<span class="normal"><a href="#__codelineno-0-82"> 82</a></span>
<span class="normal"><a href="#__codelineno-0-83"> 83</a></span>
<span class="normal"><a href="#__codelineno-0-84"> 84</a></span>
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
<span class="normal"><a href="#__codelineno-0-162">162</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-61"><a id="__codelineno-0-61" name="__codelineno-0-61"></a><span class="k">def</span><span class="w"> </span><span class="nf">infer_belief_updates</span><span class="p">(</span>
</span><span id="__span-0-62"><a id="__codelineno-0-62" name="__codelineno-0-62"></a>    <span class="bp">self</span><span class="p">,</span>
</span><span id="__span-0-63"><a id="__codelineno-0-63" name="__codelineno-0-63"></a>    <span class="n">history</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-0-64"><a id="__codelineno-0-64" name="__codelineno-0-64"></a>    <span class="n">last_utterance</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
</span><span id="__span-0-65"><a id="__codelineno-0-65" name="__codelineno-0-65"></a>    <span class="n">turn</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
</span><span id="__span-0-66"><a id="__codelineno-0-66" name="__codelineno-0-66"></a><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BeliefSlotUpdate</span><span class="p">]:</span>
</span><span id="__span-0-67"><a id="__codelineno-0-67" name="__codelineno-0-67"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-68"><a id="__codelineno-0-68" name="__codelineno-0-68"></a><span class="sd">    Infer belief updates from the nurse's perspective.</span>
</span><span id="__span-0-69"><a id="__codelineno-0-69" name="__codelineno-0-69"></a>
</span><span id="__span-0-70"><a id="__codelineno-0-70" name="__codelineno-0-70"></a><span class="sd">    This is called by the environment AFTER a patient utterance.</span>
</span><span id="__span-0-71"><a id="__codelineno-0-71" name="__codelineno-0-71"></a><span class="sd">    Failures must never crash the episode.</span>
</span><span id="__span-0-72"><a id="__codelineno-0-72" name="__codelineno-0-72"></a><span class="sd">    """</span>
</span><span id="__span-0-73"><a id="__codelineno-0-73" name="__codelineno-0-73"></a>    <span class="n">updates</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BeliefSlotUpdate</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="__span-0-74"><a id="__codelineno-0-74" name="__codelineno-0-74"></a>
</span><span id="__span-0-75"><a id="__codelineno-0-75" name="__codelineno-0-75"></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="__span-0-76"><a id="__codelineno-0-76" name="__codelineno-0-76"></a>        <span class="c1"># Pain</span>
</span><span id="__span-0-77"><a id="__codelineno-0-77" name="__codelineno-0-77"></a>        <span class="n">pain</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_belief_detector</span><span class="o">.</span><span class="n">detect_pain</span><span class="p">(</span><span class="n">last_utterance</span><span class="p">)</span>
</span><span id="__span-0-78"><a id="__codelineno-0-78" name="__codelineno-0-78"></a>        <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">pain</span><span class="p">,</span> <span class="s2">"pain_severity"</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="__span-0-79"><a id="__codelineno-0-79" name="__codelineno-0-79"></a>            <span class="n">updates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-0-80"><a id="__codelineno-0-80" name="__codelineno-0-80"></a>                <span class="n">BeliefSlotUpdate</span><span class="p">(</span>
</span><span id="__span-0-81"><a id="__codelineno-0-81" name="__codelineno-0-81"></a>                    <span class="n">slot</span><span class="o">=</span><span class="s2">"pain_severity"</span><span class="p">,</span>
</span><span id="__span-0-82"><a id="__codelineno-0-82" name="__codelineno-0-82"></a>                    <span class="n">value</span><span class="o">=</span><span class="n">pain</span><span class="o">.</span><span class="n">pain_severity</span><span class="p">,</span>
</span><span id="__span-0-83"><a id="__codelineno-0-83" name="__codelineno-0-83"></a>                    <span class="n">evidence</span><span class="o">=</span><span class="n">last_utterance</span><span class="p">,</span>
</span><span id="__span-0-84"><a id="__codelineno-0-84" name="__codelineno-0-84"></a>                    <span class="n">source</span><span class="o">=</span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-0-85"><a id="__codelineno-0-85" name="__codelineno-0-85"></a>                    <span class="n">turn</span><span class="o">=</span><span class="n">turn</span><span class="p">,</span>
</span><span id="__span-0-86"><a id="__codelineno-0-86" name="__codelineno-0-86"></a>                    <span class="n">certainty</span><span class="o">=</span><span class="s2">"explicit"</span><span class="p">,</span>
</span><span id="__span-0-87"><a id="__codelineno-0-87" name="__codelineno-0-87"></a>                <span class="p">)</span>
</span><span id="__span-0-88"><a id="__codelineno-0-88" name="__codelineno-0-88"></a>            <span class="p">)</span>
</span><span id="__span-0-89"><a id="__codelineno-0-89" name="__codelineno-0-89"></a>
</span><span id="__span-0-90"><a id="__codelineno-0-90" name="__codelineno-0-90"></a>        <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">pain</span><span class="p">,</span> <span class="s2">"pain_location"</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="__span-0-91"><a id="__codelineno-0-91" name="__codelineno-0-91"></a>            <span class="n">updates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-0-92"><a id="__codelineno-0-92" name="__codelineno-0-92"></a>                <span class="n">BeliefSlotUpdate</span><span class="p">(</span>
</span><span id="__span-0-93"><a id="__codelineno-0-93" name="__codelineno-0-93"></a>                    <span class="n">slot</span><span class="o">=</span><span class="s2">"pain_location"</span><span class="p">,</span>
</span><span id="__span-0-94"><a id="__codelineno-0-94" name="__codelineno-0-94"></a>                    <span class="n">value</span><span class="o">=</span><span class="n">pain</span><span class="o">.</span><span class="n">pain_location</span><span class="p">,</span>
</span><span id="__span-0-95"><a id="__codelineno-0-95" name="__codelineno-0-95"></a>                    <span class="n">evidence</span><span class="o">=</span><span class="n">last_utterance</span><span class="p">,</span>
</span><span id="__span-0-96"><a id="__codelineno-0-96" name="__codelineno-0-96"></a>                    <span class="n">source</span><span class="o">=</span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-0-97"><a id="__codelineno-0-97" name="__codelineno-0-97"></a>                    <span class="n">turn</span><span class="o">=</span><span class="n">turn</span><span class="p">,</span>
</span><span id="__span-0-98"><a id="__codelineno-0-98" name="__codelineno-0-98"></a>                    <span class="n">certainty</span><span class="o">=</span><span class="s2">"explicit"</span><span class="p">,</span>
</span><span id="__span-0-99"><a id="__codelineno-0-99" name="__codelineno-0-99"></a>                <span class="p">)</span>
</span><span id="__span-0-100"><a id="__codelineno-0-100" name="__codelineno-0-100"></a>            <span class="p">)</span>
</span><span id="__span-0-101"><a id="__codelineno-0-101" name="__codelineno-0-101"></a>
</span><span id="__span-0-102"><a id="__codelineno-0-102" name="__codelineno-0-102"></a>        <span class="c1"># Symptoms</span>
</span><span id="__span-0-103"><a id="__codelineno-0-103" name="__codelineno-0-103"></a>        <span class="n">symptoms</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_belief_detector</span><span class="o">.</span><span class="n">detect_symptoms</span><span class="p">(</span><span class="n">last_utterance</span><span class="p">)</span>
</span><span id="__span-0-104"><a id="__codelineno-0-104" name="__codelineno-0-104"></a>        <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">symptoms</span><span class="p">,</span> <span class="s2">"symptoms"</span><span class="p">,</span> <span class="p">[])</span> <span class="ow">or</span> <span class="p">[]:</span>
</span><span id="__span-0-105"><a id="__codelineno-0-105" name="__codelineno-0-105"></a>            <span class="n">updates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-0-106"><a id="__codelineno-0-106" name="__codelineno-0-106"></a>                <span class="n">BeliefSlotUpdate</span><span class="p">(</span>
</span><span id="__span-0-107"><a id="__codelineno-0-107" name="__codelineno-0-107"></a>                    <span class="n">slot</span><span class="o">=</span><span class="s2">"associated_symptom"</span><span class="p">,</span>
</span><span id="__span-0-108"><a id="__codelineno-0-108" name="__codelineno-0-108"></a>                    <span class="n">value</span><span class="o">=</span><span class="n">s</span><span class="p">,</span>
</span><span id="__span-0-109"><a id="__codelineno-0-109" name="__codelineno-0-109"></a>                    <span class="n">evidence</span><span class="o">=</span><span class="n">last_utterance</span><span class="p">,</span>
</span><span id="__span-0-110"><a id="__codelineno-0-110" name="__codelineno-0-110"></a>                    <span class="n">source</span><span class="o">=</span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-0-111"><a id="__codelineno-0-111" name="__codelineno-0-111"></a>                    <span class="n">turn</span><span class="o">=</span><span class="n">turn</span><span class="p">,</span>
</span><span id="__span-0-112"><a id="__codelineno-0-112" name="__codelineno-0-112"></a>                    <span class="n">certainty</span><span class="o">=</span><span class="s2">"explicit"</span><span class="p">,</span>
</span><span id="__span-0-113"><a id="__codelineno-0-113" name="__codelineno-0-113"></a>                <span class="p">)</span>
</span><span id="__span-0-114"><a id="__codelineno-0-114" name="__codelineno-0-114"></a>            <span class="p">)</span>
</span><span id="__span-0-115"><a id="__codelineno-0-115" name="__codelineno-0-115"></a>
</span><span id="__span-0-116"><a id="__codelineno-0-116" name="__codelineno-0-116"></a>        <span class="c1"># Chief complaint</span>
</span><span id="__span-0-117"><a id="__codelineno-0-117" name="__codelineno-0-117"></a>        <span class="n">chief</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_belief_detector</span><span class="o">.</span><span class="n">detect_chief_complaint</span><span class="p">(</span><span class="n">last_utterance</span><span class="p">)</span>
</span><span id="__span-0-118"><a id="__codelineno-0-118" name="__codelineno-0-118"></a>        <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">chief</span><span class="p">,</span> <span class="s2">"chief_complaint"</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="__span-0-119"><a id="__codelineno-0-119" name="__codelineno-0-119"></a>            <span class="n">updates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-0-120"><a id="__codelineno-0-120" name="__codelineno-0-120"></a>                <span class="n">BeliefSlotUpdate</span><span class="p">(</span>
</span><span id="__span-0-121"><a id="__codelineno-0-121" name="__codelineno-0-121"></a>                    <span class="n">slot</span><span class="o">=</span><span class="s2">"chief_complaint"</span><span class="p">,</span>
</span><span id="__span-0-122"><a id="__codelineno-0-122" name="__codelineno-0-122"></a>                    <span class="n">value</span><span class="o">=</span><span class="n">chief</span><span class="o">.</span><span class="n">chief_complaint</span><span class="p">,</span>
</span><span id="__span-0-123"><a id="__codelineno-0-123" name="__codelineno-0-123"></a>                    <span class="n">evidence</span><span class="o">=</span><span class="n">last_utterance</span><span class="p">,</span>
</span><span id="__span-0-124"><a id="__codelineno-0-124" name="__codelineno-0-124"></a>                    <span class="n">source</span><span class="o">=</span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-0-125"><a id="__codelineno-0-125" name="__codelineno-0-125"></a>                    <span class="n">turn</span><span class="o">=</span><span class="n">turn</span><span class="p">,</span>
</span><span id="__span-0-126"><a id="__codelineno-0-126" name="__codelineno-0-126"></a>                    <span class="n">certainty</span><span class="o">=</span><span class="s2">"explicit"</span><span class="p">,</span>
</span><span id="__span-0-127"><a id="__codelineno-0-127" name="__codelineno-0-127"></a>                <span class="p">)</span>
</span><span id="__span-0-128"><a id="__codelineno-0-128" name="__codelineno-0-128"></a>            <span class="p">)</span>
</span><span id="__span-0-129"><a id="__codelineno-0-129" name="__codelineno-0-129"></a>
</span><span id="__span-0-130"><a id="__codelineno-0-130" name="__codelineno-0-130"></a>        <span class="c1"># Duration</span>
</span><span id="__span-0-131"><a id="__codelineno-0-131" name="__codelineno-0-131"></a>        <span class="n">duration</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_belief_detector</span><span class="o">.</span><span class="n">detect_duration</span><span class="p">(</span><span class="n">last_utterance</span><span class="p">)</span>
</span><span id="__span-0-132"><a id="__codelineno-0-132" name="__codelineno-0-132"></a>        <span class="k">if</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">duration</span><span class="p">,</span> <span class="s2">"duration"</span><span class="p">,</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="__span-0-133"><a id="__codelineno-0-133" name="__codelineno-0-133"></a>            <span class="n">updates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-0-134"><a id="__codelineno-0-134" name="__codelineno-0-134"></a>                <span class="n">BeliefSlotUpdate</span><span class="p">(</span>
</span><span id="__span-0-135"><a id="__codelineno-0-135" name="__codelineno-0-135"></a>                    <span class="n">slot</span><span class="o">=</span><span class="s2">"duration"</span><span class="p">,</span>
</span><span id="__span-0-136"><a id="__codelineno-0-136" name="__codelineno-0-136"></a>                    <span class="n">value</span><span class="o">=</span><span class="n">duration</span><span class="o">.</span><span class="n">duration</span><span class="p">,</span>
</span><span id="__span-0-137"><a id="__codelineno-0-137" name="__codelineno-0-137"></a>                    <span class="n">evidence</span><span class="o">=</span><span class="n">last_utterance</span><span class="p">,</span>
</span><span id="__span-0-138"><a id="__codelineno-0-138" name="__codelineno-0-138"></a>                    <span class="n">source</span><span class="o">=</span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-0-139"><a id="__codelineno-0-139" name="__codelineno-0-139"></a>                    <span class="n">turn</span><span class="o">=</span><span class="n">turn</span><span class="p">,</span>
</span><span id="__span-0-140"><a id="__codelineno-0-140" name="__codelineno-0-140"></a>                    <span class="n">certainty</span><span class="o">=</span><span class="s2">"explicit"</span><span class="p">,</span>
</span><span id="__span-0-141"><a id="__codelineno-0-141" name="__codelineno-0-141"></a>                <span class="p">)</span>
</span><span id="__span-0-142"><a id="__codelineno-0-142" name="__codelineno-0-142"></a>            <span class="p">)</span>
</span><span id="__span-0-143"><a id="__codelineno-0-143" name="__codelineno-0-143"></a>
</span><span id="__span-0-144"><a id="__codelineno-0-144" name="__codelineno-0-144"></a>        <span class="c1"># Red flags (suspected)</span>
</span><span id="__span-0-145"><a id="__codelineno-0-145" name="__codelineno-0-145"></a>        <span class="n">red_flags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_belief_detector</span><span class="o">.</span><span class="n">detect_red_flags</span><span class="p">(</span><span class="n">last_utterance</span><span class="p">)</span>
</span><span id="__span-0-146"><a id="__codelineno-0-146" name="__codelineno-0-146"></a>        <span class="k">for</span> <span class="n">rf</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">red_flags</span><span class="p">,</span> <span class="s2">"red_flags"</span><span class="p">,</span> <span class="p">[])</span> <span class="ow">or</span> <span class="p">[]:</span>
</span><span id="__span-0-147"><a id="__codelineno-0-147" name="__codelineno-0-147"></a>            <span class="n">updates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
</span><span id="__span-0-148"><a id="__codelineno-0-148" name="__codelineno-0-148"></a>                <span class="n">BeliefSlotUpdate</span><span class="p">(</span>
</span><span id="__span-0-149"><a id="__codelineno-0-149" name="__codelineno-0-149"></a>                    <span class="n">slot</span><span class="o">=</span><span class="s2">"red_flag"</span><span class="p">,</span>
</span><span id="__span-0-150"><a id="__codelineno-0-150" name="__codelineno-0-150"></a>                    <span class="n">value</span><span class="o">=</span><span class="n">rf</span><span class="p">,</span>
</span><span id="__span-0-151"><a id="__codelineno-0-151" name="__codelineno-0-151"></a>                    <span class="n">evidence</span><span class="o">=</span><span class="n">last_utterance</span><span class="p">,</span>
</span><span id="__span-0-152"><a id="__codelineno-0-152" name="__codelineno-0-152"></a>                    <span class="n">source</span><span class="o">=</span><span class="s2">"patient"</span><span class="p">,</span>
</span><span id="__span-0-153"><a id="__codelineno-0-153" name="__codelineno-0-153"></a>                    <span class="n">turn</span><span class="o">=</span><span class="n">turn</span><span class="p">,</span>
</span><span id="__span-0-154"><a id="__codelineno-0-154" name="__codelineno-0-154"></a>                    <span class="n">certainty</span><span class="o">=</span><span class="s2">"suspected"</span><span class="p">,</span>
</span><span id="__span-0-155"><a id="__codelineno-0-155" name="__codelineno-0-155"></a>                <span class="p">)</span>
</span><span id="__span-0-156"><a id="__codelineno-0-156" name="__codelineno-0-156"></a>            <span class="p">)</span>
</span><span id="__span-0-157"><a id="__codelineno-0-157" name="__codelineno-0-157"></a>
</span><span id="__span-0-158"><a id="__codelineno-0-158" name="__codelineno-0-158"></a>    <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
</span><span id="__span-0-159"><a id="__codelineno-0-159" name="__codelineno-0-159"></a>        <span class="c1"># Safety guarantee: belief inference must never crash the episode</span>
</span><span id="__span-0-160"><a id="__codelineno-0-160" name="__codelineno-0-160"></a>        <span class="k">return</span> <span class="p">[]</span>
</span><span id="__span-0-161"><a id="__codelineno-0-161" name="__codelineno-0-161"></a>
</span><span id="__span-0-162"><a id="__codelineno-0-162" name="__codelineno-0-162"></a>    <span class="k">return</span> <span class="n">updates</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/patient_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-24">24</a></span>
<span class="normal"><a href="#__codelineno-0-25">25</a></span>
<span class="normal"><a href="#__codelineno-0-26">26</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-24"><a id="__codelineno-0-24" name="__codelineno-0-24"></a><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">llm</span><span class="p">:</span> <span class="n">BaseLLM</span><span class="p">,</span> <span class="n">persona</span><span class="p">:</span> <span class="n">PatientPersona</span><span class="p">):</span>
</span><span id="__span-0-25"><a id="__codelineno-0-25" name="__codelineno-0-25"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>
</span><span id="__span-0-26"><a id="__codelineno-0-26" name="__codelineno-0-26"></a>    <span class="bp">self</span><span class="o">.</span><span class="n">persona</span> <span class="o">=</span> <span class="n">persona</span>
</span></code></pre></div></td></tr></table></div>
</details>
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
<details class="mkdocstrings-source">
<summary>Source code in <code>.venv/lib/python3.13/site-packages/triagesim/agents/patient_agent.py</code></summary>
<div class="language-python highlight"><table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"><a href="#__codelineno-0-28">28</a></span>
<span class="normal"><a href="#__codelineno-0-29">29</a></span>
<span class="normal"><a href="#__codelineno-0-30">30</a></span>
<span class="normal"><a href="#__codelineno-0-31">31</a></span>
<span class="normal"><a href="#__codelineno-0-32">32</a></span>
<span class="normal"><a href="#__codelineno-0-33">33</a></span>
<span class="normal"><a href="#__codelineno-0-34">34</a></span>
<span class="normal"><a href="#__codelineno-0-35">35</a></span>
<span class="normal"><a href="#__codelineno-0-36">36</a></span>
<span class="normal"><a href="#__codelineno-0-37">37</a></span>
<span class="normal"><a href="#__codelineno-0-38">38</a></span>
<span class="normal"><a href="#__codelineno-0-39">39</a></span></pre></div></td><td class="code"><div><pre><span></span><code><span id="__span-0-28"><a id="__codelineno-0-28" name="__codelineno-0-28"></a><span class="k">def</span><span class="w"> </span><span class="nf">act</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">history</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chief_complaint</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">pain</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PatientOutput</span><span class="p">:</span>
</span><span id="__span-0-29"><a id="__codelineno-0-29" name="__codelineno-0-29"></a><span class="w">    </span><span class="sd">"""</span>
</span><span id="__span-0-30"><a id="__codelineno-0-30" name="__codelineno-0-30"></a><span class="sd">    Generate the patient's next utterance as a structured PatientOutput.</span>
</span><span id="__span-0-31"><a id="__codelineno-0-31" name="__codelineno-0-31"></a>
</span><span id="__span-0-32"><a id="__codelineno-0-32" name="__codelineno-0-32"></a><span class="sd">    The LLM backend MUST have been initialized with:</span>
</span><span id="__span-0-33"><a id="__codelineno-0-33" name="__codelineno-0-33"></a><span class="sd">        output_type = PatientOutput</span>
</span><span id="__span-0-34"><a id="__codelineno-0-34" name="__codelineno-0-34"></a><span class="sd">    """</span>
</span><span id="__span-0-35"><a id="__codelineno-0-35" name="__codelineno-0-35"></a>    <span class="n">prompt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_prompt</span><span class="p">(</span><span class="n">history</span><span class="p">,</span> <span class="n">chief_complaint</span><span class="p">,</span> <span class="n">pain</span><span class="p">)</span>
</span><span id="__span-0-36"><a id="__codelineno-0-36" name="__codelineno-0-36"></a>
</span><span id="__span-0-37"><a id="__codelineno-0-37" name="__codelineno-0-37"></a>    <span class="c1"># Structured generation enforced by pydantic-ai</span>
</span><span id="__span-0-38"><a id="__codelineno-0-38" name="__codelineno-0-38"></a>    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
</span><span id="__span-0-39"><a id="__codelineno-0-39" name="__codelineno-0-39"></a>    <span class="k">return</span> <span class="n">result</span>  <span class="c1"># type: ignore[return-value]</span>
</span></code></pre></div></td></tr></table></div>
</details>
</div>
</div>
</div>
</div>
</div>
