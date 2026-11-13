# SME Ops Audit

**Turn a business that runs on registers, WhatsApp and Excel into a clear, scored digitisation plan — with honest ROI — in one conversation.**

An agent skill for Claude, Codex and other skill-compatible AI assistants. Built for small and medium businesses in **Pakistan and South Asia**, works in **English, Roman Urdu and Urdu**.

> *"Mera business kaagaz aur WhatsApp par chal raha hai. Kahan se shuru karoon?"*
> This skill answers that question.

---

## What it does

1. **Interviews the owner** about how work really happens (8 areas: sales, orders, inventory, billing & udhaar, customer service, people, accounts, marketing)
2. **Scores maturity 0–4** per area, strictly: a busy WhatsApp group is still a 1
3. **Recommends fixes in three tiers:** quick wins (free, ≤ 2 weeks) → one core system → automation & AI
4. **Calculates ROI in code**, not guesswork: hours saved, losses avoided, costs, payback
5. **Writes a phone-readable report** with a 30/60/90-day roadmap and the people risks nobody mentions

Every number is labelled *Owner said*, *Estimate* or *Assumption*. The skill will tell an owner when a tool is **not** worth it.

👉 See a full [example report](examples/fabric-wholesaler/report.md) (fictional business).

## Install

**Claude Code**
```
/plugin marketplace add abdulqayoomabro/sme-ops-audit
/plugin install sme-ops-audit@sme-ops-audit
```

**Claude app (claude.ai / desktop)**
Download this repo as a ZIP, zip the `skills/sme-ops-audit` folder, and upload it in **Customize → Skills**.

**Codex / other agents**
Copy `skills/sme-ops-audit` into your agent's skills folder (e.g. `.agents/skills/`).

## Use

```
Use sme-ops-audit. I run a fabric wholesale shop in Faisalabad with 6 staff.
Udhaar is in registers and orders come on WhatsApp.
```

Roman Urdu works too:

```
sme-ops-audit chalao. Meri clinic hai Karachi mein, appointments diary mein likhte hain
aur patients WhatsApp par reminder maangte hain.
```

## ROI calculator (standalone)

```bash
python3 skills/sme-ops-audit/scripts/roi.py examples/fabric-wholesaler/opportunities.json
python3 skills/sme-ops-audit/scripts/roi.py examples/fabric-wholesaler/opportunities.json --lang ur
```

No dependencies — Python 3 standard library only. Input format is documented at the top of `roi.py`.

## For consultants & agencies

Use the report as the first step of a paid engagement: the **core system** tier becomes a fixed-scope offer, the roadmap becomes the project plan. Credit appreciated, not required (MIT).

## What it won't do

- Sign up for, buy or connect any software
- Give legal, tax or financial advice (it flags FBR/tax questions for an accountant)
- Promise results — ROI figures are estimates from the inputs

## Repo layout

```
skills/sme-ops-audit/
  SKILL.md                     workflow the agent follows
  references/                  interview guide, scoring, solutions catalog, report template
  scripts/roi.py               ROI calculator
examples/fabric-wholesaler/    sample input + report (fictional)
```

## Contributing

Ideas especially welcome for: industry-specific question sets (clinics, schools, restaurants, distributors), more local tools in the catalog, and Urdu (نستعلیق) report output. Open an issue or PR.

---

Built by **[Abdul Qayoom Abro](https://github.com/abdulqayoomabro)**, founder of ITwala — systems for SMEs in Pakistan.

## License

MIT
