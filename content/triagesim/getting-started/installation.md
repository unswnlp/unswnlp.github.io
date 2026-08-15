---
title: "Installation"
type: "docsite"
docSite: "triagesim"
---

<h1 id="installation">Installation<a class="headerlink" href="#installation" title="Permanent link">¶</a></h1>
<h2 id="requirements">Requirements<a class="headerlink" href="#requirements" title="Permanent link">¶</a></h2>
<p>TriageSim requires <strong>Python 3.11 or newer</strong>. It is tested against 3.11, 3.12
and 3.13.</p>
<p>Running a simulation also requires an <a href="https://openrouter.ai/">OpenRouter</a> API
key, since both agents call a hosted model. See
<a href="/triagesim/getting-started/configuration/">Configuration</a>.</p>
<h2 id="from-pypi">From PyPI<a class="headerlink" href="#from-pypi" title="Permanent link">¶</a></h2>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-0-1"><a href="#__codelineno-0-1" id="__codelineno-0-1" name="__codelineno-0-1"></a>pip<span class="w"> </span>install<span class="w"> </span>triagesim
</span></code></pre></div>
<p>This installs the core framework and its four runtime dependencies:
<code>pydantic</code>, <code>pydantic-ai[openrouter]</code>, <code>python-dotenv</code>, and <code>PyYAML</code>.</p>
<h2 id="optional-extras">Optional extras<a class="headerlink" href="#optional-extras" title="Permanent link">¶</a></h2>
<div class="tabbed-set tabbed-alternate" data-tabs="1:3"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><input id="__tabbed_1_3" name="__tabbed_1" type="radio"><div class="tabbed-labels"><label for="__tabbed_1_1">Redis state store</label><label for="__tabbed_1_2">Audio rendering</label><label for="__tabbed_1_3">Development</label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<p>Persist run state to Redis instead of process memory, so runs survive the
Python process and can be inspected or replayed later.</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-1-1"><a href="#__codelineno-1-1" id="__codelineno-1-1" name="__codelineno-1-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[redis]"</span>
</span></code></pre></div>
<p>Requires a reachable Redis server. See
<a href="/triagesim/guide/runner/">Redis-backed runs</a>.</p>
</div>
<div class="tabbed-block">
<p>Synthesise multi-speaker speech from a finished dialogue using XTTS-v2.</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-2-1"><a href="#__codelineno-2-1" id="__codelineno-2-1" name="__codelineno-2-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[audio]"</span>
</span></code></pre></div>
<p>This pulls in <code>torch</code> and <code>TTS</code>, which are large. Install it only if you
need speech output. See <a href="/triagesim/guide/audio/">Audio rendering</a>.</p>
</div>
<div class="tabbed-block">
<p>Test dependencies, plus the <code>redis</code> extra.</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-3-1"><a href="#__codelineno-3-1" id="__codelineno-3-1" name="__codelineno-3-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[dev]"</span>
</span></code></pre></div>
</div>
</div>
</input></input></input></div>
<p>Extras compose, so you can combine them:</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-4-1"><a href="#__codelineno-4-1" id="__codelineno-4-1" name="__codelineno-4-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"triagesim[redis,audio]"</span>
</span></code></pre></div>
<h2 id="from-source">From source<a class="headerlink" href="#from-source" title="Permanent link">¶</a></h2>
<p>To track the latest unreleased changes:</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-5-1"><a href="#__codelineno-5-1" id="__codelineno-5-1" name="__codelineno-5-1"></a>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"git+https://github.com/dipankarsrirag/triage-sim.git"</span>
</span></code></pre></div>
<p>Or clone and install in editable mode to modify the framework itself:</p>
<div class="language-bash highlight"><pre><span></span><code><span id="__span-6-1"><a href="#__codelineno-6-1" id="__codelineno-6-1" name="__codelineno-6-1"></a>git<span class="w"> </span>clone<span class="w"> </span>https://github.com/dipankarsrirag/triage-sim.git
</span><span id="__span-6-2"><a href="#__codelineno-6-2" id="__codelineno-6-2" name="__codelineno-6-2"></a><span class="nb">cd</span><span class="w"> </span>triage-sim
</span><span id="__span-6-3"><a href="#__codelineno-6-3" id="__codelineno-6-3" name="__codelineno-6-3"></a>pip<span class="w"> </span>install<span class="w"> </span>-e<span class="w"> </span><span class="s2">".[dev]"</span>
</span><span id="__span-6-4"><a href="#__codelineno-6-4" id="__codelineno-6-4" name="__codelineno-6-4"></a>pytest
</span></code></pre></div>
<h2 id="verifying">Verifying<a class="headerlink" href="#verifying" title="Permanent link">¶</a></h2>
<div class="language-python highlight"><pre><span></span><code><span id="__span-7-1"><a href="#__codelineno-7-1" id="__codelineno-7-1" name="__codelineno-7-1"></a><span class="kn">import</span><span class="w"> </span><span class="nn">triagesim</span>
</span><span id="__span-7-2"><a href="#__codelineno-7-2" id="__codelineno-7-2" name="__codelineno-7-2"></a>
</span><span id="__span-7-3"><a href="#__codelineno-7-3" id="__codelineno-7-3" name="__codelineno-7-3"></a><span class="nb">print</span><span class="p">(</span><span class="n">triagesim</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
</span></code></pre></div>
<p>The package ships a <code>py.typed</code> marker, so type checkers such as <code>mypy</code> and
<code>pyright</code> will resolve its annotations without stubs.</p>
