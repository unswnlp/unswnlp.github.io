---
title: "Connecting"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="connecting">Connecting<a class="headerlink" href="#connecting" title="Permanent link">¶</a></h1>
<p>The Spark machines aren't reachable directly from campus Wi-Fi or from home. You connect through
CSE's login server, <code>login.cse.unsw.edu.au</code>, which passes your connection on. SSH does this in one
step if you describe both hops in your SSH config.</p>
<h2 id="ssh-config">SSH config<a class="headerlink" href="#ssh-config" title="Permanent link">¶</a></h2>
<p>On your laptop, add this to <code>~/.ssh/config</code> (create the file if it doesn't exist). Replace
<code>&lt;zID&gt;</code> with your zID, and <code>&lt;address&gt;</code> and <code>&lt;username&gt;</code> with what you were sent with your account.
Keep only the machines you have an account on.</p>
<div class="highlight"><pre><span></span><code>Host cse
    HostName login.cse.unsw.edu.au
    User &lt;zID&gt;

Host spark-1
    HostName &lt;address of spark-1&gt;
    User &lt;username&gt;
    ProxyJump cse

Host spark-2
    HostName &lt;address of spark-2&gt;
    User &lt;username&gt;
    ProxyJump cse
</code></pre></div>
<p>Then connect with:</p>
<div class="highlight"><pre><span></span><code>ssh<span class="w"> </span>spark-2<span class="w">        </span><span class="c1"># or: ssh spark-1</span>
</code></pre></div>
<p>You'll be asked for your zPass (for CSE), then your password on the machine. Adding SSH keys
for both removes the prompts: see
<a href="/spark-docs/getting-started/accounts/">Using an SSH key</a>.</p>
<details class="tip">
<summary>Without a config file</summary>
<p>The same thing as one command:</p>
<div class="highlight"><pre><span></span><code>ssh<span class="w"> </span>-J<span class="w"> </span>&lt;zID&gt;@login.cse.unsw.edu.au<span class="w"> </span>&lt;username&gt;@&lt;address&gt;
</code></pre></div>
</details>
<details class="tip">
<summary>Fewer zPass prompts</summary>
<p>Add these lines under <code>Host cse</code> to reuse one CSE connection for 10 minutes:</p>
<div class="highlight"><pre><span></span><code>    ControlMaster auto
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlPersist 10m
</code></pre></div>
</details>
<h2 id="copying-files">Copying files<a class="headerlink" href="#copying-files" title="Permanent link">¶</a></h2>
<p><code>scp</code> and <code>rsync</code> use the same config:</p>
<div class="highlight"><pre><span></span><code>scp<span class="w"> </span>results.csv<span class="w"> </span>spark-2:/scratch/&lt;username&gt;/
rsync<span class="w"> </span>-avh<span class="w"> </span>--info<span class="o">=</span>progress2<span class="w"> </span>my-data/<span class="w"> </span>spark-2:/scratch/&lt;username&gt;/my-data/
</code></pre></div>
<p>The two machines have separate storage. To move files between them, copy through your laptop
the same way, or ask the maintainer about a direct copy for large data.</p>
<p>To bring data over from Katana, run <code>rsync</code> <strong>on the Spark machine</strong> and pull from Katana's data
mover:</p>
<div class="highlight"><pre><span></span><code>rsync<span class="w"> </span>-avh<span class="w"> </span>--info<span class="o">=</span>progress2<span class="w"> </span>&lt;zID&gt;@kdm.restech.unsw.edu.au:/srv/scratch/&lt;zID&gt;/my-data/<span class="w"> </span>/scratch/&lt;username&gt;/my-data/
</code></pre></div>
<p>Run it inside <code>tmux</code>, so it keeps going if your connection drops.</p>
<h2 id="vs-code">VS Code<a class="headerlink" href="#vs-code" title="Permanent link">¶</a></h2>
<ol>
<li>Install the <strong>Remote - SSH</strong> extension.</li>
<li>Set up the SSH config above. VS Code reads the same file.</li>
<li>Run <strong>Remote-SSH: Connect to Host…</strong> and choose <code>spark-1</code> or <code>spark-2</code>.</li>
</ol>
<p>Open folders under <code>/scratch/&lt;username&gt;</code>, not your home. VS Code's server files already live in
scratch (your <code>~/.vscode-server</code> points there), so they don't fill your home quota.</p>
<div class="admonition warning">
<p class="admonition-title">VS Code runs in your login session</p>
<p>The VS Code server, its terminals and any Python you run from them are limited like any login:
8 GB of memory, 2 CPU cores, and no GPU. For GPU work in notebooks, see
<a href="/spark-docs/howto/jupyter/">Jupyter in VS Code</a>.</p>
</div>
<h2 id="login-sessions">Login sessions<a class="headerlink" href="#login-sessions" title="Permanent link">¶</a></h2>
<p>Everything you start outside a Slurm job (SSH, VS Code, <code>tmux</code>) shares these limits:</p>
<table>
<thead>
<tr>
<th></th>
<th>Limit per user</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory</td>
<td>8 GB (a program that goes over is stopped)</td>
</tr>
<tr>
<td>CPU</td>
<td>2 cores</td>
</tr>
<tr>
<td>Processes</td>
<td>1,024</td>
</tr>
<tr>
<td>GPU</td>
<td>none</td>
</tr>
</tbody>
</table>
<p>That's plenty for editing, git, small scripts and submitting jobs. Anything heavier goes in a
<a href="/spark-docs/guide/jobs/">job</a>.</p>
