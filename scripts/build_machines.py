#!/usr/bin/env python3
"""Assemble the four machine pages from a shared brand shell.
Run from repo root: python3 scripts/build_machines.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "tools" / "html_machines"

SHELL = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Just a Boring Banker</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://justaboringbanker.com/tools/html_machines/{fname}">
  <link rel="icon" href="/assets/images/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500..700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
  <link rel="stylesheet" href="/tools/html_machines/machines.css">
</head>
<body>

<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/">
      <img src="/assets/images/alex.png" alt="" height="34">
      Just a Boring Banker
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Menu">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <ul class="nav-links" id="nav-links">
      <li><a href="/">Home</a></li>
      <li><a href="/about.html">Meet the Banker</a></li>
      <li><a href="/series/">The Series</a></li>
      <li><a href="/tools/" aria-current="page">The Machines</a></li>
      <li><a href="/resources/">Resources</a></li>
      <li><a href="/toolkit/">The Toolkit</a></li>
      <li><a class="btn btn-primary" href="https://www.youtube.com/@JustABoringBanker"><svg class="yt-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="#F00" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8z"/><path fill="#fff" d="M9.6 15.6V8.4L15.8 12l-6.2 3.6z"/></svg>Subscribe on YouTube</a></li>
    </ul>
  </div>
</header>

<main class="machine-page">
  <div class="wrap">
    <div class="machine-head">
      <span class="kicker">The Machines</span>
      <h1>{title}</h1>
      <p class="lede">{lede}</p>
    </div>

    <div class="machine-layout">
      <div class="panel-stack">
{controls}
      </div>

      <div class="panel chart-card">
        <div class="chart-wrap">
          <canvas id="chart"></canvas>
          <div class="tooltip" id="tooltip" hidden></div>
        </div>
        <div class="window-row">
          <span>Window: <strong id="win-label"></strong></span>
          <span class="ranges">
            <input type="range" id="win-lo" aria-label="Window start year">
            <input type="range" id="win-hi" aria-label="Window end year">
          </span>
        </div>
        <div class="stat-strip" id="stats">{stats}</div>
      </div>
    </div>

    <div class="machine-explainer">
{explainer}
    </div>

    <p class="data-note">Figures use approximate annual historical total returns (S&amp;P 500 in USD, broad bond proxy, GIC at a flat 4%), in dollars of the day, ignoring fees, taxes, and currency. Built for learning how markets behave, not for planning real money. In Canada, where this grows matters too — TFSA and RRSP room change the after-tax picture; that's a conversation for a licensed professional.</p>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <p>© 2026 Just a Boring Banker · Ryan Garneau</p>
      <ul class="footer-links">
        <li><a href="https://www.youtube.com/@JustABoringBanker">YouTube</a></li>
        <li><a href="https://x.com/johsapb">X</a></li>
        <li><a href="https://www.facebook.com/justaboring">Facebook</a></li>
      </ul>
    </div>
    <nav class="footer-map" aria-label="Site map">
      <ul class="footer-links footer-col">
        <li><strong>The Machines</strong></li>
        <li><a href="/tools/html_machines/The_Hindsight_Machine.html">The Hindsight Machine</a></li>
        <li><a href="/tools/html_machines/Withdrawal_Scenarios.html">Withdrawal Scenarios</a></li>
        <li><a href="/tools/html_machines/Allocation_in_Action.html">Allocation in Action</a></li>
        <li><a href="/tools/html_machines/action_versus_consequences.html">Actions vs Consequences</a></li>
      </ul>
      <ul class="footer-links footer-col">
        <li><strong>Learn</strong></li>
        <li><a href="/series/">The Series</a></li>
        <li><a href="/resources/">Resources</a></li>
      <li><a href="/toolkit/">The Toolkit</a></li>
        <li><a href="/toolkit/">The Toolkit</a></li>
        <li><a href="/about.html">Meet the Banker</a></li>
      </ul>
    </nav>
    <p class="disclaimer">Everything here is educational content, not financial advice. I don't know your situation, and no calculator does either. Talk to a licensed professional before making financial decisions.</p>
  </div>
</footer>

<script src="/assets/js/main.js"></script>
<script src="/tools/html_machines/data.js"></script>
<script src="/tools/html_machines/engine.js"></script>
<script>
{script}
</script>
</body>
</html>
"""

def stat(id_, label):
    return f'<div class="stat" id="stat-{id_}"><div class="k">{label}</div><div class="v" id="{id_}">$0</div></div>'

PAGES = {}

# ---------------------------------------------------------------- Hindsight
PAGES["The_Hindsight_Machine.html"] = dict(
    title="The Hindsight Machine",
    desc="See what your money would have done through five decades of real market history — crashes included. Regret, quantified.",
    lede="Pick your numbers, pick your years, and watch what actually happened — panics and all. The lesson isn't the ending. It's how bad it looked in the middle.",
    controls="""        <div class="panel">
          <h2>Starting amounts</h2>
          <div class="field"><label for="start">Starting investment ($)</label>
            <input type="number" id="start" value="10000" min="0" step="500"></div>
          <div class="field"><label for="monthly">Monthly contribution ($)</label>
            <input type="number" id="monthly" value="250" min="0" step="25"></div>
          <label class="check"><input type="checkbox" id="panics" checked> Show panic events</label>
        </div>
        <div class="panel">
          <h2>Drive it</h2>
          <button class="btn btn-primary" id="play" style="width:100%">Play the years</button>
          <button class="btn btn-ghost" id="jump20" style="width:100%;margin-top:10px">Last 20 years</button>
        </div>""",
    stats=stat("v-port", "Portfolio") + stat("v-inv", "Invested") + stat("v-ret", "Return (ann.)") + stat("v-gic", "GIC at 4%"),
    explainer="""      <h2>What this machine teaches</h2>
      <p>Every crash on this chart felt like the end of the world at the time. The shaded bands are the moments people panicked — and the line that keeps climbing is what happened to the people who didn't. Hover anywhere to see the year-by-year numbers, and compare against the GIC line: safety has a price, and now you can see exactly what it is.</p>""",
    script="""const $ = id => document.getElementById(id);
const ch = JBB.chart($("chart"), $("tooltip"));
const MIN = JBB.minYear(), MAX = JBB.maxYear();
["win-lo","win-hi"].forEach(id => { $(id).min = MIN; $(id).max = MAX; });
$("win-lo").value = 1990; $("win-hi").value = MAX;
let reveal = null; // when animating, show only first N points

function run() {
  const lo = +$("win-lo").value, hi = +$("win-hi").value;
  const start = +$("start").value || 0, monthly = +$("monthly").value || 0;
  const port = JBB.simulate({ fromY: lo, toY: hi, start, monthly, profile: { eq: 1, bd: 0 } });
  const gic  = JBB.simulate({ fromY: lo, toY: hi, start, monthly, profile: { gic: true } });
  const cut = a => reveal === null ? a : a.slice(0, reveal);
  ch.set([
    { name: "Portfolio", data: cut(port.value), color: "#1d4d3b", width: 3 },
    { name: "Invested",  data: cut(port.invested), color: "#3d4f47", width: 1.5, dash: [5,5] },
    { name: "GIC at 4%", data: cut(gic.value), color: "#2fa872", width: 1.5, dash: [2,4] }
  ], cut(port.years), $("panics").checked);
  const i = (reveal === null ? port.value.length : reveal) - 1;
  if (i >= 0) {
    $("v-port").textContent = JBB.fmt(port.value[i]);
    $("v-inv").textContent  = JBB.fmt(port.invested[i]);
    $("v-ret").textContent  = JBB.pct(JBB.annualized(port.value[i], port.invested[i], i + 1));
    $("v-gic").textContent  = JBB.fmt(gic.value[i]);
  }
  return port.years.length;
}
const win = JBB.rangeWindow($("win-lo"), $("win-hi"), $("win-label"), () => { reveal = null; run(); });
["start","monthly","panics"].forEach(id => $(id).addEventListener("input", () => { reveal = null; run(); }));
const anim = JBB.animator(() => { reveal++; return reveal <= run(); }, () => { reveal = null; run(); });
$("play").addEventListener("click", () => { reveal = 1; anim.play(); });
$("jump20").addEventListener("click", () => win.set(MAX - 20, MAX));
win.fire();"""
)

# ---------------------------------------------------------------- Withdrawal
PAGES["Withdrawal_Scenarios.html"] = dict(
    title="Withdrawal Scenarios",
    desc="Build the nest egg, then draw it down through real market history and see how long the money lasts.",
    lede="Building the money is step one. Living off it is where things get interesting — especially when the market picks the wrong decade to have a bad mood.",
    controls="""        <div class="panel">
          <h2>Accumulation</h2>
          <div class="field"><label for="start">Starting investment ($)</label>
            <input type="number" id="start" value="25000" min="0" step="500"></div>
          <div class="field"><label for="monthly">Monthly contribution ($)</label>
            <input type="number" id="monthly" value="500" min="0" step="25"></div>
        </div>
        <div class="panel">
          <h2>Withdrawal</h2>
          <div class="field"><label for="wstart">Withdrawals begin (year)</label>
            <input type="number" id="wstart" value="2010" step="1"></div>
          <div class="field"><label for="wamt">Monthly withdrawal ($)</label>
            <input type="number" id="wamt" value="3000" min="0" step="100"></div>
        </div>
        <div class="panel">
          <h2>Show</h2>
          <label class="check"><input type="checkbox" id="show-port" checked> Portfolio line</label>
          <label class="check"><input type="checkbox" id="show-inv" checked> Invested line</label>
          <label class="check"><input type="checkbox" id="show-gic" checked> GIC line</label>
          <label class="check"><input type="checkbox" id="panics" checked> Panic events</label>
        </div>""",
    stats=stat("v-port", "Portfolio") + stat("v-inv", "Invested") + stat("v-ret", "Return (ann.)") + stat("v-wd", "Withdrawn") + stat("v-gic", "GIC at 4%"),
    explainer="""      <h2>What this machine teaches</h2>
      <p>The order of returns matters enormously once you start withdrawing. Retire into a crash and the same portfolio, same withdrawals, tells a very different story than retiring into a boom. Slide the withdrawal start year around and watch the ending change — that's sequence risk, and it's the whole reason retirement income planning exists.</p>""",
    script="""const $ = id => document.getElementById(id);
const ch = JBB.chart($("chart"), $("tooltip"));
const MIN = JBB.minYear(), MAX = JBB.maxYear();
["win-lo","win-hi"].forEach(id => { $(id).min = MIN; $(id).max = MAX; });
$("win-lo").value = 1990; $("win-hi").value = MAX;

function run() {
  const lo = +$("win-lo").value, hi = +$("win-hi").value;
  const start = +$("start").value || 0, monthly = +$("monthly").value || 0;
  const ws = Math.min(Math.max(+$("wstart").value || hi, lo), hi), wa = +$("wamt").value || 0;
  const port = JBB.simulate({ fromY: lo, toY: hi, start, monthly, profile: { eq: 1, bd: 0 }, withdrawStart: ws, withdrawMonthly: wa });
  const gic  = JBB.simulate({ fromY: lo, toY: hi, start, monthly, profile: { gic: true }, withdrawStart: ws, withdrawMonthly: wa });
  const series = [];
  if ($("show-port").checked) series.push({ name: "Portfolio", data: port.value, color: "#1d4d3b", width: 3 });
  if ($("show-inv").checked)  series.push({ name: "Invested",  data: port.invested, color: "#3d4f47", width: 1.5, dash: [5,5] });
  if ($("show-gic").checked)  series.push({ name: "GIC at 4%", data: gic.value, color: "#2fa872", width: 1.5, dash: [2,4] });
  ch.set(series, port.years, $("panics").checked);
  const i = port.value.length - 1;
  $("v-port").textContent = JBB.fmt(port.value[i]);
  $("v-inv").textContent  = JBB.fmt(port.invested[i]);
  $("v-ret").textContent  = JBB.pct(JBB.annualized(port.value[i] + port.withdrawn[i], port.invested[i], i + 1));
  $("v-wd").textContent   = JBB.fmt(port.withdrawn[i]);
  $("v-gic").textContent  = JBB.fmt(gic.value[i]);
  const dead = port.value.findIndex((v, k) => v <= 0 && port.years[k] >= ws);
  $("stat-v-port").classList.toggle("bad", dead >= 0);
}
const win = JBB.rangeWindow($("win-lo"), $("win-hi"), $("win-label"), run);
["start","monthly","wstart","wamt","show-port","show-inv","show-gic","panics"]
  .forEach(id => $(id).addEventListener("input", run));
win.fire();"""
)

# ---------------------------------------------------------------- Allocation
GAME_CONTROLS = """        <div class="panel">
          <h2>Starting amounts</h2>
          <div class="field"><label for="start">Starting investment ($)</label>
            <input type="number" id="start" value="10000" min="0" step="500"></div>
          <div class="field"><label for="monthly">Monthly contribution ($)</label>
            <input type="number" id="monthly" value="250" min="0" step="25"></div>
        </div>
"""

PAGES["Allocation_in_Action.html"] = dict(
    title="Allocation in Action",
    desc="Pick a portfolio mix, trade against the market through real history, and see if timing beats holding.",
    lede="Choose your mix, then try to outsmart it. Sell before the crashes, buy back at the bottoms — if market timing works, this is where you prove it.",
    controls=GAME_CONTROLS + """        <div class="panel">
          <h2>Your allocation</h2>
          <div class="field"><label for="profile">Portfolio mix</label>
            <select id="profile">
              <option value="safety">Safety (GIC at 4%)</option>
              <option value="stable">Stable (100% bonds)</option>
              <option value="prudent">Prudent (30/70)</option>
              <option value="measured" selected>Measured (60/40)</option>
              <option value="bold">Bold (100% stocks)</option>
            </select></div>
          <div class="field"><label for="compare">Compare against (hold)</label>
            <select id="compare">
              <option value="">— none —</option>
              <option value="safety">Safety (GIC at 4%)</option>
              <option value="stable">Stable (100% bonds)</option>
              <option value="prudent">Prudent (30/70)</option>
              <option value="measured">Measured (60/40)</option>
              <option value="bold" selected>Bold (100% stocks)</option>
            </select></div>
        </div>
        <div class="panel">
          <h2>Trade</h2>
          <p style="margin:0 0 10px"><span class="status-pill" id="status">INVESTED</span></p>
          <div class="trade-row">
            <button class="btn btn-sell" id="sell">Sell</button>
            <button class="btn btn-buy" id="buy" disabled>Buy</button>
          </div>
          <button class="btn btn-primary" id="step" style="width:100%;margin-top:10px">Next year</button>
          <button class="btn btn-ghost" id="reset" style="width:100%;margin-top:10px">Reset</button>
        </div>""",
    stats=stat("v-you", "Your portfolio") + stat("v-hold", "Hold strategy") + stat("v-diff", "Outperforming by") + stat("v-inv", "Net invested") + stat("v-cash", "Cash sidelined"),
    explainer="""      <h2>What this machine teaches</h2>
      <p>Two lessons hide in here. First, allocation: watch how the mixes behave differently through the same years — the bold line falls harder and climbs higher; the stable one barely notices. Second, timing: the hold line never blinks, never mistimes, never sits in cash during the good years. Play a few rounds and count how often you beat it. Then count what it cost you to try.</p>""",
    script="""const $ = id => document.getElementById(id);
const ch = JBB.chart($("chart"), $("tooltip"));
const MIN = JBB.minYear(), MAX = JBB.maxYear();
["win-lo","win-hi"].forEach(id => { $(id).min = MIN; $(id).max = MAX; });
$("win-lo").value = 2000; $("win-hi").value = MAX;

let g = null; // game state
function newGame() {
  const lo = +$("win-lo").value, hi = +$("win-hi").value;
  const start = +$("start").value || 0, monthly = +$("monthly").value || 0;
  g = { lo, hi, y: lo, invested: true, value: start, cash: 0, netIn: start, monthly,
        you: [], years: [], profile: JBB_DATA.profiles[$("profile").value] };
  $("buy").disabled = true; $("sell").disabled = false;
  $("status").textContent = "INVESTED"; $("status").classList.remove("out");
  draw();
}
function ret(profile, y) {
  const row = JBB_DATA.years[JBB.yearIndex(y)];
  return profile.gic ? JBB_DATA.gicRate : profile.eq * row[1] + profile.bd * row[2];
}
function stepYear() {
  if (g.y > g.hi) return false;
  const c = g.monthly * 12; g.netIn += c;
  if (g.invested) { g.value += c; g.value *= 1 + ret(g.profile, g.y) / 100; }
  else g.cash += c;
  g.you.push(g.value + g.cash); g.years.push(g.y); g.y++;
  draw();
  return g.y <= g.hi;
}
function draw() {
  const start = +$("start").value || 0, monthly = +$("monthly").value || 0;
  const hold = JBB.simulate({ fromY: g.lo, toY: g.hi, start, monthly, profile: g.profile });
  const n = g.you.length;
  const series = [
    { name: "Hold", data: hold.value.slice(0, Math.max(n, 1)), color: "#3d4f47", width: 2, dash: [5,5] },
    { name: "You",  data: n ? g.you : [start], color: "#1d4d3b", width: 3 }
  ];
  const cmp = $("compare").value;
  if (cmp) {
    const c = JBB.simulate({ fromY: g.lo, toY: g.hi, start, monthly, profile: JBB_DATA.profiles[cmp] });
    series.unshift({ name: JBB_DATA.profiles[cmp].label, data: c.value.slice(0, Math.max(n, 1)), color: "#2fa872", width: 1.5, dash: [2,4] });
  }
  ch.set(series, n ? g.years : [g.lo], true);
  const you = n ? g.you[n-1] : start, hv = n ? hold.value[n-1] : start;
  $("v-you").textContent = JBB.fmt(you);
  $("v-hold").textContent = JBB.fmt(hv);
  $("v-diff").textContent = JBB.fmt(you - hv);
  $("stat-v-diff").classList.toggle("good", you - hv >= 0);
  $("stat-v-diff").classList.toggle("bad", you - hv < 0);
  $("v-inv").textContent = JBB.fmt(g.netIn);
  $("v-cash").textContent = JBB.fmt(g.cash);
}
$("sell").addEventListener("click", () => { g.cash += g.value; g.value = 0; g.invested = false;
  $("sell").disabled = true; $("buy").disabled = false;
  $("status").textContent = "IN CASH"; $("status").classList.add("out"); });
$("buy").addEventListener("click", () => { g.value += g.cash; g.cash = 0; g.invested = true;
  $("buy").disabled = true; $("sell").disabled = false;
  $("status").textContent = "INVESTED"; $("status").classList.remove("out"); });
$("step").addEventListener("click", stepYear);
$("reset").addEventListener("click", newGame);
JBB.rangeWindow($("win-lo"), $("win-hi"), $("win-label"), newGame).fire();
["start","monthly","profile","compare"].forEach(id => $(id).addEventListener("input", newGame));"""
)

# ------------------------------------------------------- Actions vs Consequences
PAGES["action_versus_consequences.html"] = dict(
    title="Actions vs Consequences",
    desc="A market-timing game against real history. Sell when you're scared, buy when you're brave — then meet the investor who did nothing.",
    lede="You get two buttons and five decades of real markets. Your opponent never trades, never panics, never checks the news. Good luck.",
    controls=GAME_CONTROLS + """        <div class="panel">
          <h2>Trade</h2>
          <p style="margin:0 0 10px"><span class="status-pill" id="status">INVESTED</span></p>
          <div class="trade-row">
            <button class="btn btn-sell" id="sell">Sell</button>
            <button class="btn btn-buy" id="buy" disabled>Buy</button>
          </div>
          <button class="btn btn-primary" id="step" style="width:100%;margin-top:10px">Next year</button>
          <button class="btn btn-ghost" id="reset" style="width:100%;margin-top:10px">Reset</button>
        </div>""",
    stats=stat("v-you", "Your portfolio") + stat("v-hold", "Stayed invested") + stat("v-diff", "Outperforming by") + stat("v-ret", "Return (ann.)") + stat("v-cash", "Cash sidelined"),
    explainer="""      <h2>What this machine teaches</h2>
      <p>Missing the crash feels like genius. But the market's best years tend to arrive right beside its worst ones, and cash on the sidelines earns nothing while you wait to feel confident again. The gap between your line and the do-nothing line is the price of your feelings — this machine just puts a number on it.</p>""",
    script="""const $ = id => document.getElementById(id);
const ch = JBB.chart($("chart"), $("tooltip"));
const MIN = JBB.minYear(), MAX = JBB.maxYear();
["win-lo","win-hi"].forEach(id => { $(id).min = MIN; $(id).max = MAX; });
$("win-lo").value = 2000; $("win-hi").value = MAX;
const SP = { eq: 1, bd: 0 };

let g = null;
function newGame() {
  const lo = +$("win-lo").value, hi = +$("win-hi").value;
  const start = +$("start").value || 0;
  g = { lo, hi, y: lo, invested: true, value: start, cash: 0, netIn: start,
        monthly: +$("monthly").value || 0, you: [], years: [] };
  $("buy").disabled = true; $("sell").disabled = false;
  $("status").textContent = "INVESTED"; $("status").classList.remove("out");
  draw();
}
function stepYear() {
  if (g.y > g.hi) return false;
  const row = JBB_DATA.years[JBB.yearIndex(g.y)];
  const c = g.monthly * 12; g.netIn += c;
  if (g.invested) { g.value += c; g.value *= 1 + row[1] / 100; }
  else g.cash += c;
  g.you.push(g.value + g.cash); g.years.push(g.y); g.y++;
  draw();
  return g.y <= g.hi;
}
function draw() {
  const start = +$("start").value || 0, monthly = +$("monthly").value || 0;
  const hold = JBB.simulate({ fromY: g.lo, toY: g.hi, start, monthly, profile: SP });
  const n = g.you.length;
  ch.set([
    { name: "Stayed invested", data: hold.value.slice(0, Math.max(n, 1)), color: "#3d4f47", width: 2, dash: [5,5] },
    { name: "You", data: n ? g.you : [start], color: "#1d4d3b", width: 3 }
  ], n ? g.years : [g.lo], true);
  const you = n ? g.you[n-1] : start, hv = n ? hold.value[n-1] : start;
  $("v-you").textContent = JBB.fmt(you);
  $("v-hold").textContent = JBB.fmt(hv);
  $("v-diff").textContent = JBB.fmt(you - hv);
  $("stat-v-diff").classList.toggle("good", you - hv >= 0);
  $("stat-v-diff").classList.toggle("bad", you - hv < 0);
  $("v-ret").textContent = JBB.pct(JBB.annualized(you, g.netIn, Math.max(n, 1)));
  $("v-cash").textContent = JBB.fmt(g.cash);
}
$("sell").addEventListener("click", () => { g.cash += g.value; g.value = 0; g.invested = false;
  $("sell").disabled = true; $("buy").disabled = false;
  $("status").textContent = "IN CASH"; $("status").classList.add("out"); });
$("buy").addEventListener("click", () => { g.value += g.cash; g.cash = 0; g.invested = true;
  $("buy").disabled = true; $("sell").disabled = false;
  $("status").textContent = "INVESTED"; $("status").classList.remove("out"); });
$("step").addEventListener("click", stepYear);
$("reset").addEventListener("click", newGame);
JBB.rangeWindow($("win-lo"), $("win-hi"), $("win-label"), newGame).fire();
["start","monthly"].forEach(id => $(id).addEventListener("input", newGame));"""
)


# ---------------------------------------------------------------- Fee Machine
PAGES["The_Fee_Machine.html"] = dict(
    title="The Fee Machine",
    desc="The same portfolio, the same markets, two different fees. Watch what a 2% MER quietly takes over decades.",
    lede="Fees are the only part of investing that's guaranteed. This machine runs the same money through the same markets twice — once at index-fund fees, once at typical Canadian mutual-fund fees — and shows you the bill.",
    controls="""        <div class="panel">
          <h2>Starting amounts</h2>
          <div class="field"><label for="start">Starting investment ($)</label>
            <input type="number" id="start" value="25000" min="0" step="500"></div>
          <div class="field"><label for="monthly">Monthly contribution ($)</label>
            <input type="number" id="monthly" value="500" min="0" step="25"></div>
        </div>
        <div class="panel">
          <h2>The two fees</h2>
          <div class="field"><label for="fee-low">Low fee (% per year)</label>
            <input type="number" id="fee-low" value="0.2" min="0" max="5" step="0.05"></div>
          <div class="field"><label for="fee-high">High fee (% per year)</label>
            <input type="number" id="fee-high" value="2.0" min="0" max="5" step="0.05"></div>
          <p class="fine" style="margin:6px 0 0">Typical Canadian bank mutual funds sit near 2%; broad index funds near 0.2% or less.</p>
        </div>""",
    stats=stat("v-low", "Low-fee portfolio") + stat("v-high", "High-fee portfolio") + stat("v-cost", "Cost of the fee gap") + stat("v-inv", "Invested"),
    explainer="""      <h2>What this machine teaches</h2>
      <p>Both lines hold the exact same investments through the exact same years. The only difference is the skim. Fees compound with the same machinery as returns — they just compound against you, silently, deducted before your statement is printed. Find your own funds' MERs, plug them in, and meet your co-owner. Then read <a href="/resources/fee-check.html">the Fee Check</a> for what to do about it.</p>""",
    script="""const $ = id => document.getElementById(id);
const ch = JBB.chart($("chart"), $("tooltip"));
const MIN = JBB.minYear(), MAX = JBB.maxYear();
["win-lo","win-hi"].forEach(id => { $(id).min = MIN; $(id).max = MAX; });
$("win-lo").value = 2000; $("win-hi").value = MAX;

function run() {
  const lo = +$("win-lo").value, hi = +$("win-hi").value;
  const start = +$("start").value || 0, monthly = +$("monthly").value || 0;
  const feeL = Math.max(0, +$("fee-low").value || 0), feeH = Math.max(0, +$("fee-high").value || 0);
  const low  = JBB.simulate({ fromY: lo, toY: hi, start, monthly, profile: { eq: 1, bd: 0 }, fee: feeL });
  const high = JBB.simulate({ fromY: lo, toY: hi, start, monthly, profile: { eq: 1, bd: 0 }, fee: feeH });
  ch.set([
    { name: "Low fee (" + feeL + "%)", data: low.value, color: "#1d4d3b", width: 3 },
    { name: "High fee (" + feeH + "%)", data: high.value, color: "#b4432f", width: 2.5 },
    { name: "Invested", data: low.invested, color: "#3d4f47", width: 1.5, dash: [5,5] }
  ], low.years, false);
  const i = low.value.length - 1;
  $("v-low").textContent  = JBB.fmt(low.value[i]);
  $("v-high").textContent = JBB.fmt(high.value[i]);
  $("v-cost").textContent = JBB.fmt(low.value[i] - high.value[i]);
  document.getElementById("stat-v-cost").classList.add("bad");
  $("v-inv").textContent  = JBB.fmt(low.invested[i]);
}
JBB.rangeWindow($("win-lo"), $("win-hi"), $("win-label"), run).fire();
["start","monthly","fee-low","fee-high"].forEach(id => $(id).addEventListener("input", run));"""
)

# ---------------------------------------------------------------- Debt Machine
PAGES["The_Debt_Machine.html"] = dict(
    title="The Debt Machine",
    desc="Race the avalanche against the snowball on your real debts. See which pays off faster and how much interest each costs.",
    lede="Two proven ways to kill debt: highest rate first, or smallest balance first. Enter your debts and one total monthly payment, then watch both strategies race your balances to zero.",
    controls="""        <div class="panel">
          <h2>Your debts</h2>
          <div class="field"><label for="b1">Debt 1 — balance ($) &amp; rate (%)</label>
            <input type="number" id="b1" value="6500" min="0" step="100" aria-label="Debt 1 balance">
            <input type="number" id="r1" value="21" min="0" max="60" step="0.1" style="margin-top:8px" aria-label="Debt 1 interest rate"></div>
          <div class="field"><label for="b2">Debt 2 — balance ($) &amp; rate (%)</label>
            <input type="number" id="b2" value="14000" min="0" step="100" aria-label="Debt 2 balance">
            <input type="number" id="r2" value="8" min="0" max="60" step="0.1" style="margin-top:8px" aria-label="Debt 2 interest rate"></div>
          <div class="field"><label for="b3">Debt 3 — balance ($) &amp; rate (%)</label>
            <input type="number" id="b3" value="3000" min="0" step="100" aria-label="Debt 3 balance">
            <input type="number" id="r3" value="12" min="0" max="60" step="0.1" style="margin-top:8px" aria-label="Debt 3 interest rate"></div>
        </div>
        <div class="panel">
          <h2>Your firepower</h2>
          <div class="field"><label for="pay">Total monthly payment ($)</label>
            <input type="number" id="pay" value="800" min="0" step="25"></div>
          <p class="fine" style="margin:6px 0 0">Everything you can put at all debts combined, each month.</p>
        </div>""",
    stats=stat("v-av", "Avalanche: debt-free in") + stat("v-avint", "Avalanche interest") + stat("v-sn", "Snowball: debt-free in") + stat("v-snint", "Snowball interest") + stat("v-save", "Avalanche saves"),
    explainer="""      <h2>What this machine teaches</h2>
      <p>The avalanche (highest rate first) almost always wins on interest — the gap between the two strategies is the price of the snowball's psychology. Sometimes that price is tiny, and the quick wins are worth it; sometimes it's thousands. This machine tells you which situation you're in, so you can choose with your eyes open. The chart's horizontal axis counts months from today. Full playbook: <a href="/resources/debt-payoff-playbook.html">the Debt Payoff Playbook</a>.</p>""",
    script="""const $ = id => document.getElementById(id);
document.querySelector(".window-row").style.display = "none";
const ch = JBB.chart($("chart"), $("tooltip"));

function payoff(debts, budget, mode) {
  debts = debts.map(d => ({ ...d })).filter(d => d.bal > 0);
  let months = 0, interest = 0; const totals = [debts.reduce((a,d)=>a+d.bal,0)];
  while (debts.some(d => d.bal > 0.005) && months < 600) {
    months++;
    debts.forEach(d => { const i = d.bal * d.rate / 1200; d.bal += i; interest += i; });
    const order = [...debts].sort((a,b) => mode === "av" ? b.rate - a.rate : a.bal - b.bal);
    let left = budget;
    for (const d of order) { const p = Math.min(d.bal, left); d.bal -= p; left -= p; if (left <= 0) break; }
    totals.push(debts.reduce((a,d)=>a+d.bal,0));
  }
  return { months, interest, totals, done: months < 600 };
}
function label(m, done) {
  if (!done) return "600+ months";
  const y = Math.floor(m/12), r = m%12;
  return (y ? y + "y " : "") + r + "m";
}
function run() {
  const debts = [1,2,3].map(n => ({ bal: +$("b"+n).value || 0, rate: +$("r"+n).value || 0 }));
  const budget = +$("pay").value || 0;
  const av = payoff(debts, budget, "av"), sn = payoff(debts, budget, "sn");
  const n = Math.max(av.totals.length, sn.totals.length);
  const pad = (t) => t.concat(Array(n - t.length).fill(0));
  ch.set([
    { name: "Avalanche", data: pad(av.totals), color: "#1d4d3b", width: 3 },
    { name: "Snowball",  data: pad(sn.totals), color: "#2fa872", width: 2.5, dash: [6,4] }
  ], Array.from({length: n}, (_, i) => i), false);
  const monthlyInterest = debts.reduce((a,d) => a + d.bal * d.rate / 1200, 0);
  const tooLow = budget <= monthlyInterest && debts.some(d => d.bal > 0);
  $("v-av").textContent = tooLow ? "Never — payment too low" : label(av.months, av.done);
  $("v-avint").textContent = JBB.fmt(av.interest);
  $("v-sn").textContent = tooLow ? "Never — payment too low" : label(sn.months, sn.done);
  $("v-snint").textContent = JBB.fmt(sn.interest);
  $("v-save").textContent = JBB.fmt(Math.max(0, sn.interest - av.interest));
  document.getElementById("stat-v-save").classList.add("good");
}
["b1","r1","b2","r2","b3","r3","pay"].forEach(id => $(id).addEventListener("input", run));
run();"""
)


for fname, cfg in PAGES.items():
    html = SHELL.format(fname=fname, **cfg)
    (OUT / fname).write_text(html)
    print("built", fname)
