# ICFI 2027 — Babcock Filament CMS Staff Editing Guide

This guide explains how non-developers can safely find and update content inside `Web Admin -> Infos -> ICFI (287) -> Edit`.

> **Important Technical Note:** Babcock's server limits rapid multi-block Livewire requests (`Add to blocks` triggered `403 Forbidden`), so the live/preview page safely uses **1 clean `General 2` block** between `Canvas navbar 1` and `Canvas footer 3`—organized with clean CSS classes, a **top `Ctrl+F` Quick Navigation index**, plain-English banner comments before every section, and an **`ICFI_STAFF_CONFIG`** Easy Settings block.  
> *(Individual section backups are also kept in [cms_blocks/](file:///c:/Users/IT%20Support%2003/OneDrive/Desktop/ICFI/cms_blocks) for reference.)*

---

## How to Jump Straight to What You Want to Edit (`Ctrl+F`)

Open `General 2 -> Content *`, click inside the code box, press **`Ctrl+F`**, and search for any tag below:

| Search Tag (`Ctrl+F`) | What You Can Edit There |
|---|---|
| `SECTION 1: HERO BANNER` | Main 3-line headline, dates badge, quote, and 4 Hero portraits |
| `SECTION 2: GOLD ANNOUNCEMENT BAR` | Quick Info banner text & Key Figures highlight boxes |
| `SECTION 3: 8 ACADEMIC TRACKS` | Call for Papers text, 2 session photos, and Tracks 01–08 |
| `SECTION 4: CONVENER'S DESK` | Prof. Constance C. Nwosu's bio/title/phone, Chief Host / Host, and 4 Keynote Scholars |
| `SECTION 5: CORE VALUES` | 6 `E-I-A-S-T-H` pillars + Vision & Mission |
| `SECTION 6: ROADMAP & ABSTRACTS` | Milestone date cards & 250-word Abstract Submission instructions |
| `SECTION 7: PASS FEES & FORMS` | NGN/USD pass prices (`data-ngn`, `data-usd`, visible price), UBA/GTBank accounts, Registration & 8-clause Membership terms *(keep `id="..."` and `name="..."` unchanged)* |
| `SECTION 8: JOURNAL, GALLERY & FAQ` | IJFI card, YouTube recap link, 4 PDF links, 5 Gallery photos, FAQs, and 4 Coordinators |
| `STEP 1: EASY STAFF CONFIGURATION` | **`ICFI_STAFF_CONFIG`**: conference countdown date, Early Bird cutoff date, max upload MB, Google Sheet endpoint URL, and `Day 1`–`Day 5` programme timetable |

---

## Quick How-To Tasks

1. **Change a Photo (Hero, Speaker, Convener, or Gallery):**
   - Go to **Web Admin -> Media -> Create**, upload the photo, and copy its **File URL** (`https://babcock.edu.ng/storage/media/...`).
   - Use `Ctrl+F` to jump to the speaker/section, and replace only the link inside `src="..."`.
2. **Edit the Live Countdown Date or `Day 1–5` Programme Schedule:**
   - Search `STEP 1: EASY STAFF CONFIGURATION` (`ICFI_STAFF_CONFIG`).
   - Edit only the words inside single quotes `'...'` (`conferenceStartIso`, `earlyBirdDeadlineIso`, `programmeDays`). Keep all quotes, colons `:`, and commas `,` intact.
3. **Always Leave `General 2 -> Header` Blank:**
   - Babcock's `Canvas 2` template renders a large heading box above the hero if `Header` has text inside it.
4. **`Save changes` vs. `Publish`:**
   - **`Save changes`** saves only to the **Draft Preview** ([`/preview-info/287?status=1`](https://babcock.edu.ng/preview-info/287?status=1)). When you reload `/edit`, Filament still displays the older published content until **Publish** is clicked.
   - **`Publish`** pushes your updated code to the live `/ifi/icfi` URL and updates what `/edit` loads next time.
