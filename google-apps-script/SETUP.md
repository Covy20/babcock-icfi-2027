# 7th ICFI 2027 — Google Sheet & Apps Script Setup

Your live Google Sheet has already been created and formatted:

- **Spreadsheet:** `7th ICFI 2027 - Conference Registrations`
- **URL:** https://docs.google.com/spreadsheets/d/1fcFFE9HhvhhrbAhNqyhgaSSukuKprC0aa9EDQfYq79Q/edit

## 2-Minute Deployment Steps

1. Open the spreadsheet above and click **Extensions → Apps Script**.
2. Delete any default starter code in `Code.gs`, paste the contents of [`Code.gs`](./Code.gs), and click **Save**.
3. Click **Deploy → New deployment**.
4. Next to *Select type*, choose **Web app**:
   - **Description:** `ICFI 2027 Registration API`
   - **Execute as:** `Me`
   - **Who has access:** `Anyone` *(required so website delegates can submit without logging into Google)*
5. Click **Deploy**, authorize Drive/Sheets/Mail permissions when Google asks, and copy the **Web app URL** (`https://script.google.com/macros/s/.../exec`).
6. Open [`index.html`](../index.html), paste that URL into:
   ```js
   const REGISTRATION_ENDPOINT = "YOUR_WEB_APP_URL_HERE";
   ```
   then commit and push to GitHub so Netlify updates live.

## Uploaded Receipts & Privacy

- Payment receipts and membership proofs are automatically saved into a Google Drive folder named **`7th ICFI 2027 - Uploaded Receipts & Proofs`** inside the deploying Google account's Drive.
- Files stay private to the owner and anyone you explicitly share that Google Drive folder with (recommended for committee members verifying payments).
