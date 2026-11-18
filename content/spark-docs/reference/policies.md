---
title: "Policies"
type: "docsite"
docSite: "spark-docs"
---

<h1 id="policies">Policies<a class="headerlink" href="#policies" title="Permanent link">¶</a></h1>
<p>The Spark machines are shared by a small group, so a few rules keep them fair and safe.</p>
<h2 id="what-the-machines-are-for">What the machines are for<a class="headerlink" href="#what-the-machines-are-for" title="Permanent link">¶</a></h2>
<p>The Spark machines are for <strong>proof of concept</strong>: trying ideas, debugging, and small experiments.
When work is ready to run at scale (long training runs, sweeps, large evaluations), move it to
<a href="https://docs.restech.unsw.edu.au/">Katana</a>. That keeps the Sparks free for the next person's quick experiment.</p>
<h2 id="accounts">Accounts<a class="headerlink" href="#accounts" title="Permanent link">¶</a></h2>
<ul>
<li>Accounts are personal. Don't share your password or let others use your account.</li>
<li>Every account has an expiry date. When it passes, you can't log in; your files stay until the
  maintainer cleans up after a grace period. Ask for an extension before it runs out.</li>
<li>Use the machines for UNSW-NLP research and teaching only.</li>
</ul>
<h2 id="fair-use">Fair use<a class="headerlink" href="#fair-use" title="Permanent link">¶</a></h2>
<ul>
<li>Run heavy work as Slurm jobs, never in your login session.</li>
<li>Ask for what you need: memory and GPU you request but don't use are kept from others.</li>
<li>Cancel jobs (servers, notebooks) when you're done with them.</li>
<li>Use shards for most work; take the whole GPU (<code>--gres=gpu:1</code>) only when you need it.</li>
<li>For a long run on a whole GPU (or both of spark-1's nodes), give the group a heads-up first.</li>
</ul>
<h2 id="data">Data<a class="headerlink" href="#data" title="Permanent link">¶</a></h2>
<ul>
<li><strong>Nothing on the machines is backed up.</strong> Keep code in git and results elsewhere.</li>
<li>Don't keep sensitive or identifiable data (for example health records) on the machines unless your
  project's ethics approval allows it, and talk to the maintainer first.</li>
<li>Scratch files unused for 100 days are deleted, with a week's warning at login.</li>
</ul>
<h2 id="privacy">Privacy<a class="headerlink" href="#privacy" title="Permanent link">¶</a></h2>
<ul>
<li>Other users can't see your jobs, your processes or your files. You can't see theirs.</li>
<li><code>nodestat</code> shows how busy the machine is, without names.</li>
<li>The maintainer can see everything, for running the machine, and doesn't look at your files
  otherwise.</li>
</ul>
<h2 id="maintenance">Maintenance<a class="headerlink" href="#maintenance" title="Permanent link">¶</a></h2>
<p>The machines need occasional updates and reboots. They're announced ahead of time where possible;
a reboot ends running jobs, so save checkpoints in long runs.</p>
<h2 id="scheduling">Scheduling<a class="headerlink" href="#scheduling" title="Permanent link">¶</a></h2>
<p>Waiting jobs are ordered by fair share and waiting time. The one exception is the maintainer's
account, which has a higher priority and no time limit, for maintenance and long runs on the
machine's behalf.</p>
