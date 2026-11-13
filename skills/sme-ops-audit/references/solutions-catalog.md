# Solutions catalog

Options by area and tier. Always offer at least one free or open-source option. **Prices, licences and regulations change — tell the owner to verify on the official site before deciding.**

Tiers: **Q** = quick win (≤ 2 weeks), **C** = core system (1–3 months), **A** = automation/AI (after clean data exists).

## Cross-cutting building blocks
| Tool | Type | Good for | Watch out |
|------|------|----------|-----------|
| WhatsApp Business app | Free app | Catalog, quick replies, labels, away messages | Not a database; chats can't be reported on |
| Google Forms + Sheets | Free | First structured data capture, from any phone | Gets messy past a few thousand rows without discipline |
| AppSheet (on Google Sheets) | No-code | Simple mobile apps for orders, stock, attendance | Check plan limits for team size |
| ERPNext | Open source ERP | Inventory, billing, purchasing, HR, accounts in one | Needs hosting + setup help; plan training |
| Odoo (Community) | Open source ERP | Same space as ERPNext, big app ecosystem | Some modules only in paid edition |
| n8n | Workflow automation (self-host or cloud) | Connect forms, sheets, WhatsApp, email, CRM | "Fair-code" licence — check terms before reselling |
| Metabase / Looker Studio | Dashboards | Owner's daily numbers on phone | Only as good as the data behind it |

## By area

### 1. Leads & sales
- **Q:** WhatsApp Business labels (New / Quoted / Won / Lost) + a weekly follow-up hour
- **C:** CRM — Twenty (open source), HubSpot free tier, Zoho CRM
- **A:** Auto-reminders for unanswered quotes; AI draft of follow-up messages

### 2. Orders & delivery
- **Q:** One Google Form per order; order number written on every parcel
- **C:** Order module in ERPNext/Odoo, or AppSheet order app
- **A:** Auto WhatsApp status message on dispatch; courier tracking pulled into the sheet

### 3. Inventory & purchasing
- **Q:** Weekly count of top 20 items only (Pareto); minimum-stock list on the wall
- **C:** Inventory in ERPNext/Odoo or POS with stock; barcode labels
- **A:** Low-stock alert to owner's WhatsApp; reorder suggestions from sales history

### 4. Billing, payments & udhaar
- **Q:** Move udhaar to a digital khata app or a shared sheet (one row per customer, per transaction); take payments by Raast QR / JazzCash / Easypaisa to reduce cash handling
- **C:** Invoicing + receivables in the ERP or accounting software
- **A:** Automatic payment reminders on due dates
- **Regulation flag:** some retailers must integrate POS with FBR — verify current FBR requirements for the business's category.

### 5. Customer service
- **Q:** Quick replies for the top 10 questions; one shared number instead of personal phones
- **C:** Shared inbox — Chatwoot (open source) for WhatsApp, Instagram, web chat
- **A:** AI assistant answering FAQs from a written knowledge base, with human hand-off

### 6. People
- **Q:** Written duty list per person; attendance on a Google Form with time stamp
- **C:** HR & payroll module (ERPNext HR, or a local payroll tool); biometric device export to sheet
- **A:** Monthly salary sheet generated automatically from attendance

### 7. Accounts & reporting
- **Q:** Daily close sheet: sales, cash, digital receipts, expenses — 10 minutes, every day
- **C:** Accounting software or ERP accounts; monthly close checklist with an accountant
- **A:** Owner dashboard (Metabase / Looker Studio) on the phone

### 8. Marketing & content
- **Q:** One content calendar sheet; post 3×/week; ask every new customer "kahan se pata chala?"
- **C:** Scheduler (e.g. Postiz, open source) + simple lead-source tracking in the CRM
- **A:** AI-assisted content drafts in the brand's voice; monthly what-worked report

## Choosing between options
1. Can the current team use it on their phones in Urdu/Roman Urdu or simple English?
2. Can data be exported (no lock-in)?
3. Who will support it locally when it breaks?
4. Total cost for 12 months, including setup and training — run it through `scripts/roi.py`.
