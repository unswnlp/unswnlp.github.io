---
title: "Accounts and first login"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="accounts-and-first-login">Accounts and first login<a class="headerlink" href="#accounts-and-first-login" title="Permanent link">¶</a></h1>
<h2 id="getting-an-account">Getting an account<a class="headerlink" href="#getting-an-account" title="Permanent link">¶</a></h2>
<p>Accounts are for invited members of UNSW-NLP and close collaborators. Each
<a href="/spark-docs/getting-started/machines/">machine</a> has its own accounts. The maintainer creates yours and sends you,
separately:</p>
<ul>
<li>which machine it's on, and your <strong>username</strong> there,</li>
<li>a <strong>temporary password</strong>,</li>
<li>the machine's <strong>address</strong> (addresses aren't published here).</li>
</ul>
<p>Every account has an <strong>expiry date</strong>, usually the end of your project or degree. Ask the
maintainer to extend it if you need longer.</p>
<p>You also need to be able to log in to CSE's login server, <code>login.cse.unsw.edu.au</code>, because the
machines are reached through it. CSE students and staff can, with their zID and zPass. If you
can't, tell the maintainer.</p>
<h2 id="first-login">First login<a class="headerlink" href="#first-login" title="Permanent link">¶</a></h2>
<ol>
<li>Set up the connection as in <a href="/spark-docs/getting-started/connecting/">Connecting</a>, then run <code>ssh spark-2</code> (or
   <code>ssh spark-1</code>).</li>
<li>Enter your <strong>zPass</strong> when CSE's login server asks for it.</li>
<li>Enter the <strong>temporary password</strong> when the machine asks for it.</li>
<li>It then asks you to change it: type the temporary password once more, then your new password
   twice. The connection closes after that.</li>
<li>Log in again with your new password.</li>
</ol>
<p>On every login you'll see TARS (the resident calico) and a table of your storage:</p>
<div class="highlight"><pre><span></span><code>  --------------------------------------------------------------------------
  Filesystem            Used   Quota   Limit  Use%     Files   Quota   Limit  Use%
  --------------------------------------------------------------------------
  /home/alice           645M     10G     11G    6%        3k    100k    110k    2%
  /scratch/alice         26G    100G    105G   26%        5k    200k    220k    2%
  --------------------------------------------------------------------------
</code></pre></div>
<p>If you go over a quota, or some of your scratch files are about to be deleted, a line starting
with <code>!</code> appears under the table. See <a href="/spark-docs/guide/storage/">Storage</a>.</p>
<p>To turn TARS off, create an empty file called <code>.hushlogin</code> in your home folder
(<code>touch ~/.hushlogin</code>). The storage table still shows.</p>
<h2 id="using-an-ssh-key-instead-of-a-password">Using an SSH key instead of a password<a class="headerlink" href="#using-an-ssh-key-instead-of-a-password" title="Permanent link">¶</a></h2>
<p>After your first login you can add a key, so you don't type your password each time. From your
laptop:</p>
<div class="highlight"><pre><span></span><code>ssh-keygen<span class="w"> </span>-t<span class="w"> </span>ed25519<span class="w">      </span><span class="c1"># only if you don't have a key yet</span>
ssh-copy-id<span class="w"> </span>spark-2<span class="w">        </span><span class="c1"># and/or spark-1</span>
</code></pre></div>
<p>Your public key goes onto the machine; the private key never leaves your laptop. Do the same for
CSE's login server (<code>ssh-copy-id cse</code>) to skip the zPass prompt too.</p>
<h2 id="changing-your-password">Changing your password<a class="headerlink" href="#changing-your-password" title="Permanent link">¶</a></h2>
<p>Run <code>passwd</code> on the machine. Passwords are separate on each machine.</p>
