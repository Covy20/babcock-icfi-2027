# ICFI 2027 — Babcock Filament CMS Staff Editing Guide

This conference page is split into **small, labeled `General` blocks** inside `Web Admin -> Infos -> ICFI (287) -> Edit`, between **Canvas navbar** (top menu) and **Canvas footer** (bottom footer).

> **Important Rule:** Always leave each `General` block's **Header** input **blank** so Filament does not inject an extra heading box above that section. Look at Line 1 inside `Content *` to see which section a block controls.

---

## Which Block Do I Open to Edit Something?

| Filament Block | Line 1 Label | What You Can Edit Inside It | Size |
|---|---|---|---|
| **Block 1** (`Canvas navbar`) | *(Built-in)* | Babcock IFI top menu *(leave untouched)* | — |
| **Block 2** (`General`) | `PAGE DESIGN STYLES, HERO BANNER & LIVE COUNTDOWN` | Main 3-line headline, dates badge, hero plenary photo, 4 hero portraits, Quick Info bar, and the 4 Key Figures boxes | ~150 HTML lines (after `</style>`) |
| **Block 3** (`General`) | `8 ACADEMIC TRACKS & CALL FOR PAPERS` | Call for Papers intro, 2 session photos, and Tracks 01–08 titles & keywords | ~90 lines |
| **Block 4** (`General`) | `CONVENER'S DESK, UNIVERSITY HOSTS & KEYNOTE SCHOLARS` | Convener portrait/message/title, Chief Host/Host/Convener cards, and 4 Keynote Scholars | ~120 lines |
| **Block 5** (`General`) | `E-I-A-S-T-H CORE VALUES, VISION & MISSION` | 6 Core Value cards (`E-I-A-S-T-H`) + Vision & Mission boxes | ~65 lines |
| **Block 6** (`General`) | `CONFERENCE ROADMAP, 6-DAY PROGRAMME & ABSTRACTS` | Milestone dates + 250-word Abstract Guidelines & email button | ~85 lines |
| **Block 7** (`General`) | `PASS FEES, BANKING & REGISTRATION / MEMBERSHIP FORMS` | NGN/USD pass prices (`data-ngn`, `data-usd`, visible price), UBA/GTBank accounts, Registration & Membership form fields & legal terms *(keep `id="..."` and `name="..."` unchanged)* | ~365 lines |
| **Block 8** (`General`) | `IJFI JOURNAL, VIDEO, PDF PAPERS, GALLERY, FAQS & SECRETARIAT` | IJFI card, YouTube recap link, 4 PDF links, 5 Gallery photos, FAQs, and 4 Coordinators & phone numbers | ~145 lines |
| **Block 9** (`General`) | `EASY STAFF SETTINGS & PAGE INTERACTION SCRIPT` | **`ICFI_STAFF_CONFIG`** at the top: countdown target date, Early Bird cutoff date, upload MB limit, Google Sheet URL, and `Day 1`–`Day 5` timetable items | ~40 config lines + engine script |
| **Block 10** (`Canvas footer`) | *(Built-in)* | Babcock bottom footer *(leave untouched)* | — |

---

## How to Make Common Updates Safely

1. **Change a Photo (Hero, Speaker, Convener, or Gallery):**
   - Go to **Web Admin -> Media -> Create**, upload your image, and copy its **File URL** (`https://babcock.edu.ng/storage/media/...`).
   - Open the matching `General` block (e.g. Block 4 for Speakers, Block 8 for Gallery) and paste the new URL inside `src="..."` on that photo's `<img>` tag.
2. **Change the Day 1–5 Programme Schedule or Countdown Date:**
   - Open **Block 9** (`EASY STAFF SETTINGS & PAGE INTERACTION SCRIPT`).
   - Edit only text inside `'...'` quotes under `ICFI_STAFF_CONFIG` (`conferenceStartIso`, `earlyBirdDeadlineIso`, or `programmeDays`). Keep quotes, colons `:`, and commas `,` intact.
3. **Preview vs. Going Live (`Save changes` vs `Publish`):**
   - **`Save changes`** saves only to the **Draft Preview** ([`/preview-info/287?status=1`](https://babcock.edu.ng/preview-info/287?status=1)) and leaves the live `/ifi/icfi` URL unchanged. Note: reloading `/edit` after clicking *Save changes* will still show the older published version until **Publish** is clicked.
   - **`Publish`** pushes all your blocks to the live public page (`/ifi/icfi`) and updates what `/edit` loads next time.
