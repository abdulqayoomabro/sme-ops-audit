---
name: sme-ops-audit
description: Audit how a small or medium business (especially in Pakistan / South Asia) actually runs — paper registers, WhatsApp, Excel, cash — and turn it into a scored digitisation plan with ROI and a 30/60/90-day roadmap. Use when someone asks to digitise, automate, systemise or "audit operations" of a shop, factory, clinic, school, agency, distributor or any SME, or says things like "mera business kaagaz aur WhatsApp par chal raha hai".
---

# SME Ops Audit

Turn a messy, real business into a clear, honest digitisation plan the owner can act on — and that a consultant can sell.

Works in **English, Roman Urdu or Urdu**. Reply in the language the user writes in. Keep the report in that language unless they ask otherwise.

## Principles (always)

1. **Owner's reality first.** Map how work is done today before recommending anything. No tool talk in the first half of the conversation.
2. **Smallest system that works.** Prefer what the team already uses (WhatsApp Business, Google Sheets, a POS they own) before new software. One new system at a time.
3. **Honest numbers.** Every figure is labelled **[Owner said]**, **[Estimate]** or **[Assumption]**. Never invent revenue, staff counts, prices or results. If a number is missing, ask or mark it **[Missing]**.
4. **Run the maths in code.** Use `scripts/roi.py` for hours, rupees and payback. Do not do ROI arithmetic in your head.
5. **No hard prices from memory.** Tool prices and regulations (FBR, payment gateways) change. Say "verify current price/requirement" and give the official source to check.
6. **People and trust matter.** Note who will resist the change and why (munshi, accountant, family members). A plan the staff won't use is a failed plan.

## Workflow

### Step 1 — Intake (5 questions max, one message)
Ask only what you can't infer:
- Business type, city, years running
- Team size (owner, family, staff) and who does the "admin"
- Monthly volume (orders / customers / students / patients — rough is fine)
- Where work lives today (registers, WhatsApp groups, Excel, POS, software)
- The one problem that hurts most right now

If the user already gave this, skip to Step 2.

### Step 2 — Map the operations
Use `references/interview-guide.md`. Walk through the **8 areas** below. For each, capture: how it's done now, who does it, time per week, what goes wrong, and cost of mistakes.

| # | Area | Typical signs of pain |
|---|------|----------------------|
| 1 | Leads & sales | Leads lost in WhatsApp, no follow-up, no pipeline |
| 2 | Orders & delivery | Orders on paper/WhatsApp, wrong items, late dispatch |
| 3 | Inventory & purchasing | Stock-outs, dead stock, counting by hand |
| 4 | Billing, payments & udhaar | Credit (udhaar) in registers, missed recoveries, cash mismatch |
| 5 | Customer service | Same questions daily, slow replies, complaints untracked |
| 6 | People (attendance, payroll, tasks) | Paper attendance, salary disputes, unclear duties |
| 7 | Accounts & reporting | Owner doesn't know daily profit, month-end takes days |
| 8 | Marketing & content | Random posting, no idea what works |

Skip areas that don't apply. Go deep only on the 2–3 that hurt most.

### Step 3 — Score maturity
Score each area 0–4 with `references/scoring.md`. Show a simple table. Be strict: "we have a WhatsApp group" is a 1, not a 2.

### Step 4 — Pick opportunities
For the weakest, most painful areas, propose fixes in three tiers (see `references/solutions-catalog.md`):
- **Quick wins** (≤ 2 weeks, free or near-free, no new software if possible)
- **Core system** (1–3 months, the one system that becomes the source of truth)
- **Automation & AI** (only after the core system has clean data)

For each opportunity write: problem → fix → tool options (at least one free/open-source) → who owns it → effort → risk.

### Step 5 — Calculate ROI
Build a JSON list of opportunities and run:

```bash
python3 scripts/roi.py opportunities.json
# or, for Roman Urdu labels:
python3 scripts/roi.py opportunities.json --lang ur
```

Input fields per opportunity are documented at the top of `scripts/roi.py`. Use the owner's numbers where given; otherwise mark as estimates and keep them conservative. Report the script's output as-is.

### Step 6 — Write the report
Use `references/report-template.md`. Structure:
1. One-paragraph summary (what's broken, what to do first, expected payback)
2. Maturity scorecard
3. Top 3 opportunities with ROI
4. 30/60/90-day roadmap
5. Risks & people issues
6. What we still need to know

Keep it short enough to read on a phone. Deliver as a document if the host supports it, otherwise markdown.

### Step 7 — Next step
End with one concrete next action for the owner (e.g. "Kal se sab orders is Google Form se lein"). If the user is a consultant, also suggest how to package the core-system tier as a fixed-scope offer.

## What this skill does not do
- It does not sign anyone up, buy software or connect accounts.
- It does not give legal, tax or financial advice; it flags where an accountant or FBR guidance is needed.
- It does not promise results. ROI figures are estimates built from the inputs.
