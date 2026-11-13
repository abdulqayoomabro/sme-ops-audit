# Operations Audit — Example Fabric Wholesaler

> **Fictional example.** Business, people and numbers are invented to show the skill's output. Not a real client.

Faisalabad · Prepared for the owner

## 1. Summary
Sales are healthy, but cash is leaking through **udhaar kept in two paper registers** (~PKR 9 lakh outstanding [Owner said]) and orders taken on WhatsApp that get mixed up. Fixing udhaar first pays back in under a month [Estimate, roi.py]. A shared inbox is **not** worth it yet at this size.

## 2. Scorecard
| Area | Score | Pain | Priority | Evidence |
|------|-----:|-----:|-----:|----------|
| Billing & udhaar | 1 | 3 | 9 | Two registers, no due dates, recoveries by memory [Owner said] |
| Orders & delivery | 1 | 3 | 9 | Orders in 3 WhatsApp groups; ~6 wrong dispatches/month [Owner said] |
| Inventory | 2 | 2 | 4 | Excel updated weekly by the munshi |
| Customer service | 1 | 1 | 3 | Owner replies personally; customers are mostly repeat buyers |
| Accounts & reporting | 1 | 2 | 6 | Profit known only at month-end |

## 3. Top opportunities

### 1. Udhaar to a digital khata + reminders
- **Problem:** No due dates; old balances forgotten; disputes over amounts
- **Fix:** Every credit sale recorded digitally the same day; weekly reminder to customers past 30 days
- **Tools:** Shared Google Sheet (free) · a digital khata app with export
- **Owner:** Munshi · **Effort:** 1 week to move open balances · **Risk:** Low

### 2. Orders through one form
- **Problem:** Orders scattered across WhatsApp groups
- **Fix:** One Google Form; every order gets a number that goes on the parcel
- **Tools:** Google Forms + Sheets (free) · AppSheet later
- **Owner:** Sales boy · **Effort:** 3 days · **Risk:** Medium — customers keep messaging; staff enters for them

### 3. Shared WhatsApp inbox — **not now**
Costs more than it saves at current volume. Revisit above ~80 chats/day.

### ROI
| Opportunity | Hours saved/month | Monthly benefit | Monthly cost | Net/month | Setup cost | Payback (months) | 12-month net | Basis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Udhaar to digital khata + payment reminders | 17 | PKR 63,750 | PKR 0 | PKR 63,750 | PKR 15,000 | 0.2 | PKR 750,000 | Owner said |
| Orders via Google Form + order numbers | 26 | PKR 29,375 | PKR 0 | PKR 29,375 | PKR 10,000 | 0.3 | PKR 342,500 | Estimate |
| Shared WhatsApp inbox (Chatwoot) | 22 | PKR 3,646 | PKR 6,000 | PKR -2,354 | PKR 40,000 | never | PKR -68,250 | Assumption |
| **TOTAL** | 65 | PKR 96,771 | PKR 6,000 | PKR 90,771 | PKR 65,000 | 0.7 | PKR 1,024,250 |  |

_Estimates built from the inputs above, not guarantees._

## 4. Roadmap
| When | What | Who | Done when |
|------|------|-----|-----------|
| Days 1–30 | Udhaar sheet live; order form live | Munshi, sales boy | All new credit + orders recorded digitally |
| Days 31–60 | Daily close sheet; weekly reminder routine | Owner | Owner knows yesterday's sales by 10am |
| Days 61–90 | Evaluate ERPNext for inventory + billing | Owner + consultant | Go / no-go decision with costs |

## 5. Risks & people
The munshi has kept the registers for 12 years and may see this as distrust. Make him the owner of the new sheet, not its victim.

## 6. Still need to know
Exact monthly bad-debt write-offs; whether the business falls under FBR POS integration requirements (verify with an accountant).

## Next step
**Kal se har udhaar wali sale isi sheet mein, usi din.**
