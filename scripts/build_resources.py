#!/usr/bin/env python3
"""Assemble the resources hub + guide pages from the shared brand shell.
Run from repo root: python3 scripts/build_resources.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "resources"
OUT.mkdir(exist_ok=True)

YT = '<svg class="yt-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="#F00" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8z"/><path fill="#fff" d="M9.6 15.6V8.4L15.8 12l-6.2 3.6z"/></svg>'

SHELL = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Just a Boring Banker</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://justaboringbanker.com/resources/{fname}">
  <link rel="icon" href="/assets/images/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500..700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
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
      <li><a href="/tools/">The Machines</a></li>
      <li><a href="/resources/"{current}>Resources</a></li>
      <li><a href="/toolkit/">The Toolkit</a></li>
      <li><a class="btn btn-primary" href="https://www.youtube.com/@JustABoringBanker">{yt}Subscribe on YouTube</a></li>
    </ul>
  </div>
</header>

<main>
{body}
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
</body>
</html>
"""

GUIDE_BODY = """  <section class="hero deco" style="padding-block: clamp(56px,8vw,88px) 0">
    <div class="wrap">
      <span class="kicker">Resources · {read_min}-minute read</span>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
    </div>
  </section>
  <section class="prose">
    <div class="wrap">
{content}
      <h2>Do this next</h2>
      <ul class="credentials">
{checklist}
      </ul>
      <div class="hero-ctas">
{ctas}
      </div>
    </div>
  </section>
"""

def check(items):
    return "\n".join(f"        <li>☐ {i}</li>" for i in items)

def cta(href, label, primary=True):
    return f'        <a class="btn {"btn-primary" if primary else "btn-ghost"}" href="{href}">{label}</a>'

GUIDES = {}

GUIDES["the-boring-budget.html"] = dict(
    title="The Boring Budget", read_min=4,
    desc="A budget you'll actually keep: know your number, pay yourself first, automate the rest. No spreadsheet guilt required.",
    h1="The Boring Budget",
    lede="Most budgets fail because they're built like diets — all restriction, no system. This one is built like plumbing. Set it up once and let it run.",
    content="""      <h2>Step one: know your number</h2>
      <p>Before any system works, you need one honest month of data. Pull your last 30 days of transactions and sort them into three piles: needs (housing, groceries, transport, minimum debt payments), wants (everything fun), and future-you (savings, investing, extra debt payments). Don't judge it. Just measure it.</p>
      <h2>Step two: pick a split, not a straitjacket</h2>
      <p>The classic starting point is 50/30/20 — half your after-tax income to needs, 30% to wants, 20% to future-you. In expensive Canadian cities, needs often eat more than half; that's reality, not failure. The number that matters most is the future-you percentage. Start where you can, even at 5%, and raise it every time your income does.</p>
      <h2>Step three: pay yourself first, automatically</h2>
      <p>The whole trick of boring budgeting is removing willpower from the process. Set an automatic transfer to savings or investments for the day after payday. Money you never see is money you never argue with. What's left in the account is genuinely spendable — no tracking apps, no guilt, no Sunday-night spreadsheet sessions.</p>
      <h2>Why this beats the fancy version</h2>
      <p>Detailed category budgets work brilliantly for the 5% of people who enjoy maintaining them. For everyone else, the automated split wins because the default action — doing nothing — is the right action. That's good plumbing.</p>""",
    checklist=check([
        "Pull one month of transactions and sort into needs / wants / future-you",
        "Pick your future-you percentage — any number beats no number",
        "Set an automatic transfer for the day after payday",
        "Raise the transfer every raise, bonus, or debt you finish paying off",
    ]),
    ctas=cta("/tools/html_machines/The_Hindsight_Machine.html", "See what your monthly amount becomes") + "\n" + cta("/resources/", "More resources", False),
)

GUIDES["debt-payoff-playbook.html"] = dict(
    title="The Debt Payoff Playbook", read_min=5,
    desc="Avalanche vs snowball, which debts to attack first, and the traps that keep Canadians in debt longer than they should be.",
    h1="The Debt Payoff Playbook",
    lede="There are exactly two good ways to pay off debt, and the best one is whichever you'll actually finish. Here's how to choose — and the traps to step around.",
    content="""      <h2>First, the non-negotiable</h2>
      <p>Every debt gets its minimum payment, every month, no exceptions. Missed minimums damage your credit and trigger penalty rates. Everything below is about where your <em>extra</em> money goes.</p>
      <h2>The avalanche: mathematically best</h2>
      <p>List your debts by interest rate, highest first. All extra money attacks the top of the list while everything else gets minimums. A credit card at 21% is a guaranteed 21% return when you pay it down — no investment reliably beats that. If you're motivated by efficiency, this is your play.</p>
      <h2>The snowball: psychologically best</h2>
      <p>List your debts by balance, smallest first, and attack the smallest. Each debt you eliminate frees up its minimum payment and hands you a win. The maths is slightly worse than the avalanche; the completion rate, for many people, is better. A plan you finish beats a plan you abandon.</p>
      <h2>The traps</h2>
      <p>Consolidation loans can genuinely help — but only if you close the cards afterward. Rolling credit-card debt into your mortgage or a line of credit while keeping the cards open is how people end up with both. And beware minimum-payment maths: on a typical credit card, minimums are designed to keep you paying for decades. The statement now shows you how long — read that number once and you'll never pay minimums again.</p>""",
    checklist=check([
        "List every debt: balance, rate, minimum payment",
        "Pick avalanche (by rate) or snowball (by balance) — then stop re-deciding",
        "Automate minimums on everything, extra on the target",
        "If you consolidate, close the paid-off accounts' spending access",
        "When the last debt dies, redirect the whole payment to future-you",
    ]),
    ctas=cta("/tools/html_machines/action_versus_consequences.html", "See what decisions cost") + "\n" + cta("/resources/the-boring-budget.html", "The Boring Budget", False),
)

GUIDES["tfsa-vs-rrsp.html"] = dict(
    title="TFSA vs RRSP", read_min=5,
    desc="The one question that settles the TFSA vs RRSP debate, how each account actually works, and the order most Canadians should fill them.",
    h1="TFSA vs RRSP: the boring answer",
    lede="Canada's most-asked money question has a genuinely boring answer: it depends on one comparison. Your tax rate now versus your tax rate later.",
    content="""      <h2>How each one actually works</h2>
      <p>An <strong>RRSP</strong> is a tax-later account. Contributions come off this year's taxable income (that's the refund), growth is untaxed, and withdrawals are taxed as income — ideally in retirement, when your income and tax rate are lower. A <strong>TFSA</strong> is a tax-never account. You contribute after-tax dollars, and everything after that — growth, withdrawals, all of it — is tax-free, at any age, for any reason. Neither is an investment itself; both are containers you put investments inside.</p>
      <h2>The one question</h2>
      <p>Will your tax rate be higher now or in retirement? Higher now (peak earning years) → the RRSP's deduction is worth more. Lower now (early career, variable income) → the TFSA wins, and you preserve RRSP room for higher-earning years. Genuinely unsure → the TFSA is the flexible default; you can't really regret it.</p>
      <h2>The order of operations</h2>
      <p>Before either: if your employer matches RRSP or pension contributions, capture every matched dollar first — that's an instant 50–100% return and it outranks everything else in personal finance. After the match, fill TFSA or RRSP based on the question above. Contribution room for both accumulates and carries forward; your exact numbers live in your CRA My Account, which beats any rule of thumb.</p>
      <h2>The classic mistakes</h2>
      <p>Using the TFSA as a chequing account (withdrawals only re-add to your room the following January — track it, because over-contributing draws penalties). Contributing to an RRSP in a low-income year instead of just carrying the room forward. And parking either account in cash for decades — the container is tax-advantaged, but the growth still has to come from what's inside it.</p>""",
    checklist=check([
        "Capture every employer-matched dollar before anything else",
        "Answer the one question: tax rate higher now, or in retirement?",
        "Check your real contribution room in CRA My Account",
        "Automate a monthly contribution to the winner",
        "Make sure the money inside is invested, not parked in cash",
    ]),
    ctas=cta("/tools/html_machines/The_Hindsight_Machine.html", "See what tax-free compounding does") + "\n" + cta("/resources/fhsa-first-home.html", "Buying a first home? Read this", False),
)

GUIDES["fhsa-first-home.html"] = dict(
    title="The FHSA, Explained", read_min=4,
    desc="Canada's first home savings account combines the RRSP's deduction with the TFSA's tax-free withdrawal. If a first home is anywhere in your plans, read this.",
    h1="The FHSA: the account that double-dips",
    lede="Canada built an account that takes the RRSP's best feature and the TFSA's best feature and gives both to first-time buyers. It is the least boring thing in this library.",
    content="""      <h2>Why it's unusual</h2>
      <p>The FHSA (First Home Savings Account) double-dips: contributions are tax-deductible like an RRSP, <em>and</em> a qualifying withdrawal to buy your first home comes out entirely tax-free like a TFSA. No other Canadian account does both. If you qualify and a home purchase is plausibly in your future, it's generally the first account to fill after any employer match.</p>
      <h2>The mechanics that matter</h2>
      <p>You open one as a Canadian resident of qualifying age who counts as a first-time buyer (broadly: you haven't lived in a home you or your spouse owned in the recent qualifying period — the CRA definition is specific, so check it). Annual and lifetime contribution limits apply, unused annual room carries forward within limits, and the account has a maximum lifespan of 15 years — after which unused funds can roll into your RRSP without using RRSP room. That rollover is the safety net: worst case, it becomes extra retirement savings.</p>
      <h2>It stacks with the HBP</h2>
      <p>The Home Buyers' Plan lets you also borrow from your RRSP for the same purchase (repayable over time). FHSA plus HBP on one home is allowed — a meaningful chunk of a Canadian down payment can come out of tax-advantaged accounts.</p>
      <h2>What to hold inside it</h2>
      <p>Match the investment to the timeline. Buying within a few years: capital preservation — high-interest savings or GICs — because a market dip the year you buy is the one risk this account can't afford. Five-plus years out: a more grown-up mix can make sense. The container is generous; don't wreck it with the wrong contents.</p>""",
    checklist=check([
        "Check the CRA's first-time-buyer definition against your situation",
        "Open the account even with a small deposit — it starts your room accumulating",
        "Automate contributions; claim the deduction in a year it's worth the most",
        "Match what's inside to your buying timeline",
        "Buying with a partner? You each get your own FHSA",
    ]),
    ctas=cta("/resources/tfsa-vs-rrsp.html", "TFSA vs RRSP") + "\n" + cta("/resources/", "More resources", False),
)

GUIDES["emergency-fund.html"] = dict(
    title="The Emergency Fund", read_min=3,
    desc="How much cash to hold, where to keep it in Canada, and what actually counts as an emergency.",
    h1="The emergency fund: boring money's bodyguard",
    lede="An emergency fund earns almost nothing and does almost everything. It's the reason a job loss is a bad month instead of a debt spiral — and the reason you never have to panic-sell.",
    content="""      <h2>How much</h2>
      <p>The standard target is three to six months of <em>core</em> expenses — rent or mortgage, food, utilities, insurance, minimum debt payments. Not your full lifestyle; the survival version. Lean toward three months with two stable incomes in the house, six with one income, variable income, or dependants. Self-employed? Aim past six.</p>
      <h2>Where to keep it (Canada edition)</h2>
      <p>The job description is: safe, boring, reachable within days. That means a high-interest savings account — the online banks routinely pay multiples of what the big banks' regular savings accounts do — or cashable GICs, all under CDIC deposit insurance limits. Not stocks, not crypto, and ideally at a different bank than your chequing account: friction against yourself is a feature.</p>
      <h2>What counts as an emergency</h2>
      <p>Job loss. The furnace in February. The transmission. The vet. What doesn't: a sale, a trip, a wedding gift, Christmas. Those are irregular expenses, not emergencies — predictable in category if not in date, and they deserve their own savings line so they stop ambushing your credit card.</p>
      <h2>The quiet superpower</h2>
      <p>Beyond the obvious protection, cash reserves are what let your investments behave. Every panic-seller in a crash is someone who needed money at the worst moment. The fund's real return isn't the interest — it's every terrible decision it lets you not make.</p>""",
    checklist=check([
        "Calculate your monthly core-expenses number",
        "Pick your target: 3, 6, or more months",
        "Open a high-interest account at a separate institution",
        "Automate a transfer until the target's hit, then redirect to investing",
        "Give irregular expenses (car, gifts, travel) their own savings line",
    ]),
    ctas=cta("/tools/html_machines/Withdrawal_Scenarios.html", "See what a cash cushion protects") + "\n" + cta("/resources/the-boring-budget.html", "The Boring Budget", False),
)

GUIDES["fee-check.html"] = dict(
    title="The Fee Check", read_min=4,
    desc="Canadians pay some of the highest investment fund fees in the world. Here's how to find yours, what they cost over 25 years, and what to do about it.",
    h1="The Fee Check: the leak in your bucket",
    lede="Fees are the only part of investing that's guaranteed. Canadians pay some of the world's highest — and most people can't name theirs. Let's fix that in ten minutes.",
    content="""      <h2>The number to find: your MER</h2>
      <p>Every mutual fund and ETF charges a Management Expense Ratio — a percentage skimmed off the top each year, invisible on your statements because it's deducted before returns are reported. Canadian bank mutual funds commonly charge around 2%; broad index ETFs and index mutual funds often charge a tenth of that or less. Look up each fund you own by its name or code — the MER is in the fund facts document your provider must publish.</p>
      <h2>What 2% actually costs</h2>
      <p>Two percent sounds like a tip. Compounded, it's a co-owner. $100,000 growing 25 years at 6% after fees becomes about $429,000. The same money at 4% — same market, 2% higher fees — becomes about $267,000. That's roughly $162,000, gone quietly, for the same underlying investments. Fees compound with exactly the same machinery as returns; they just compound against you.</p>
      <h2>What you're allowed to pay for</h2>
      <p>Fees aren't evil — undisclosed ones are. Real financial planning, behavioural coaching, and tax strategy can be worth paying for, transparently. What's rarely worth 2% is a fund that quietly hugs the index while charging active prices. The question for any fee: what am I getting that a near-free index fund doesn't do?</p>
      <h2>The fix</h2>
      <p>For most people it's a one-time renovation: identify the MERs, compare against low-cost index equivalents, and switch — carefully, since selling in non-registered accounts can trigger taxes, and some funds carry deferred sales charges. Inside a TFSA or RRSP, switching funds has no tax consequence. When in doubt about the exit costs, that's a fair question for a fee-transparent professional.</p>""",
    checklist=check([
        "List every fund you own and look up each MER in its fund facts",
        "Total your blended fee across the portfolio",
        "Compare each fund against a low-cost index equivalent",
        "Check for deferred sales charges and tax consequences before switching",
        "Re-run this check any time someone sells you a new product",
    ]),
    ctas=cta("/tools/html_machines/The_Hindsight_Machine.html", "Compound the difference yourself") + "\n" + cta("/resources/new-investor-checklist.html", "New investor checklist", False),
)

GUIDES["panic-protocol.html"] = dict(
    title="The Panic Protocol", read_min=4,
    desc="A written plan for market crashes, made in calm weather. What to do — and mostly not do — when your portfolio drops 30%.",
    h1="The Panic Protocol",
    lede="One day your portfolio will drop 30% and every headline will explain why this time is different. You can't prevent that day. You can decide, today, exactly what you'll do on it.",
    content="""      <h2>Why you write this now</h2>
      <p>In a crash, the part of your brain that does long-term planning goes offline and the part that runs from bears takes the wheel. Airline pilots don't improvise emergencies; they run checklists written in calm weather. This is yours. Write it, date it, keep it where future panicking-you will find it.</p>
      <h2>The protocol</h2>
      <p><strong>Hour one: do nothing.</strong> No selling, no logging in "just to look." Volatility is the price of admission, and you've already paid it. <strong>Day one: reread your plan</strong> — the one that said crashes would happen and you'd hold. The market falling doesn't change why you invested. <strong>Week one: check the boring facts.</strong> Is your emergency fund intact? Income stable? Timeline unchanged? If all three are yes, nothing about your situation has actually changed — only prices have. <strong>If you must act:</strong> the historically sensible actions in a crash are continuing your automatic contributions (you're buying at a discount) and rebalancing back to your target mix. Both are the opposite of what your gut wants.</p>
      <h2>What the record shows</h2>
      <p>Every major crash on record — 1974, 1987, 2000, 2008, 2020 — looked permanent from the inside and temporary from ten years later. The people hurt worst weren't the ones who rode it down; they were the ones who sold at the bottom and waited to feel safe again, missing the recovery that tends to arrive violently and without an invitation.</p>""",
    checklist=check([
        "Write your one-page plan: why you invest, your timeline, your target mix",
        "Add the sentence: \"Drops of 30%+ are expected and are not a reason to sell\"",
        "Confirm the emergency fund exists so a crash never forces a sale",
        "Keep contributions automatic — automation doesn't panic",
        "Date it, sign it, and reread it before reading any market news",
    ]),
    ctas=cta("/tools/html_machines/The_Hindsight_Machine.html", "Tour past panics with hindsight") + "\n" + cta("/tools/html_machines/action_versus_consequences.html", "Play the panic game", False),
)

GUIDES["new-investor-checklist.html"] = dict(
    title="The New Investor Checklist", read_min=5,
    desc="The order of operations for a first-time Canadian investor: what to do before investing, where to open an account, and what to actually buy.",
    h1="The New Investor Checklist",
    lede="Starting to invest is a ten-step errand that the industry dresses up as a lifestyle. Here's the whole errand, in order.",
    content="""      <h2>Before a single dollar gets invested</h2>
      <p>The order of operations matters more than any stock pick. First: capture any employer match — free money outranks everything. Second: kill high-interest debt; paying off a 21% credit card is a guaranteed 21% return, and the market guarantees nothing. Third: a starter emergency fund, so a surprise never forces you to sell. Only then does investing money become investing money.</p>
      <h2>Open the account</h2>
      <p>For most Canadians starting out, that means a TFSA (or FHSA if a first home is in the plan) at either a self-directed discount brokerage or a robo-advisor. The robo costs a little more and does the maintenance for you; self-directed costs almost nothing and asks you to press the buttons yourself. Both beat the 2%-fee mutual fund at the bank branch by a distance. Compare trading commissions — several Canadian brokerages now offer zero-commission ETF purchases.</p>
      <h2>What to actually buy</h2>
      <p>The boring answer: broad, diversified, low-fee index funds — and Canada has made this absurdly easy with single-ticket asset-allocation ETFs, where one fund holds thousands of companies across the world at a target stock/bond mix. Pick the mix that matches your timeline and stomach, buy the same thing every month, and you've replicated most of what a portfolio manager does, minus the fees.</p>
      <h2>What to ignore</h2>
      <p>Hot tips, single stocks as a starting point, anything a friend got rich on last month, anything you'd need to watch daily, and every product whose fees you can't find in two minutes. If it's exciting, it's probably expensive. You're allowed a small "play money" account for the fun stuff — after the boring machine is running.</p>""",
    checklist=check([
        "Capture the full employer match, if one exists",
        "Pay off any debt above roughly 7–8% interest first",
        "Park a starter emergency fund in high-interest savings",
        "Open a TFSA (or FHSA) at a discount brokerage or robo-advisor",
        "Buy a broad, low-fee index fund on an automatic monthly schedule",
        "Ignore everything exciting",
    ]),
    ctas=cta("/tools/html_machines/Allocation_in_Action.html", "Test your mix in history") + "\n" + cta("/resources/fee-check.html", "Run the Fee Check", False),
)

# ---- Hub page ----
def hub_card(fname, g):
    return f"""        <a class="machine" href="/resources/{fname}">
          <span class="dial">{g['read_min']}′</span>
          <h3>{g['title']}</h3>
          <p>{g['lede'].split('.')[0]}.</p>
          <span class="try">Read it</span>
        </a>"""

HUB_BODY = """  <section class="hero deco" style="padding-block: clamp(56px,8vw,88px) 0">
    <div class="wrap">
      <span class="kicker">Resources</span>
      <h1>The boring library</h1>
      <p class="lede">Short, practical guides to the money basics school skipped — written for Canadians, free of hype, and honest about what they don't cover. Each one ends with a checklist you can actually do this week.</p>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="machine-grid">
{cards}
      </div>
      <p class="fine" style="margin-top:28px">Rules and limits change. These guides stay evergreen by pointing you at the CRA and licensed professionals for the numbers that move.</p>
    </div>
  </section>
"""

# Need the machine-card styles on resources pages
EXTRA_CSS = '<link rel="stylesheet" href="/assets/css/style.css">'
EXTRA_CSS_HUB = EXTRA_CSS  # same stylesheet has .machine styles

for fname, g in GUIDES.items():
    body = GUIDE_BODY.format(**g)
    html = SHELL.format(fname=fname, title=g["title"], desc=g["desc"], body=body, yt=YT, current="")
    (OUT / fname).write_text(html)
    print("built", fname)

cards = "\n".join(hub_card(f, g) for f, g in GUIDES.items())
hub = SHELL.format(fname="", title="Resources", desc="Short, practical personal finance guides for Canadians — budgeting, debt, TFSA vs RRSP, FHSA, fees, and staying calm in crashes.",
                   body=HUB_BODY.format(cards=cards), yt=YT, current=' aria-current="page"')
(OUT / "index.html").write_text(hub)
print("built index.html (hub)")
