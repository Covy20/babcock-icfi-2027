# 7th ICFI 2027 — Google Sheet & Apps Script Setup

Your live Google Sheet has three formatted tabs inside one spreadsheet:

- **Spreadsheet:** `7th ICFI 2027 - Conference Registrations`
- **URL:** https://docs.google.com/spreadsheets/d/1fcFFE9HhvhhrbAhNqyhgaSSukuKprC0aa9EDQfYq79Q/edit
- **Tabs:**
  - `Registrations` — 7th ICFI Conference delegates (`ICFI27-...`)
  - `Membership` — ICFI Association Membership applications (`ICFI-MEM-...`)
  - `Summary` — Live `COUNTA` / `COUNTIF` KPI totals across both tabs

## Updating Your Deployed Web App (Keeps the Exact Same `/exec` URL)

1. Open the spreadsheet above and click **Extensions → Apps Script**.
2. Replace `Code.gs` with the updated [`Code.gs`](./Code.gs) in this repo and click **Save**.
3. Click **Deploy → Manage deployments → Edit (pencil icon)**.
4. Set **Version** to **New version**, keep **Execute as:** `Me` and **Who has access:** `Anyone`, and click **Deploy**.
   - Keeping the same deployment preserves the existing `REGISTRATION_ENDPOINT` URL already saved in [`index.html`](../index.html).

## Uploaded Receipts & Privacy

- Both conference payment receipts (`ICFI27-...`) and membership payment evidence (`ICFI-MEM-...`) are automatically saved into the Google Drive folder **`7th ICFI 2027 - Uploaded Receipts & Proofs`**.
- Files stay private to the owner and anyone you explicitly share that Google Drive folder with.
