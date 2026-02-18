# TCP Sales Tool — WordPress Deployment Log
**Date:** February 17, 2026

---

## What Was Done

### 1. Made TCP Sales Tool Responsive
- **File:** `/Users/ljoequick/Downloads/TCP_Sales_Tool_16.html`
- Replaced all table layouts with CSS Grid/Flexbox
- Added viewport meta tag for mobile
- 3 breakpoints: Desktop (>768px), Tablet (<=768px), Mobile (<=480px)
- Columns stack vertically on mobile
- Removed fixed 11in x 8.5in page dimensions (kept for print only)
- Fixed `overflow: hidden` → `overflow: visible` so page scrolls
- Fixed footer from `position: absolute` → `position: relative`

### 2. Connected to WordPress (joequick.com)
- **API:** `https://joequick.com/wp-json/wp/v2/`
- **Auth:** joe.quick / Application Password
- **Credentials found in:** `batch_post_dec2.py`

### 3. Created Menu Item: I-TOOLS
- **Menu:** Primary Menu (ID: 28)
- **I-TOOLS menu item ID:** 25391
- URL set to `#` (dropdown only, no landing page)
- Positioned at slot 3 (MANNA moved to 4)

### 4. Created TCP Sales Tool Page
- **Page ID:** 25392
- **URL:** https://joequick.com/tcp-sales-tool/
- **Template:** Elementor Canvas (blank, no theme interference)
- Content wrapped in `<!-- wp:html -->` block to prevent WordPress from injecting `<p>` tags

### 5. Menu Item: TCP Sales Tool
- **Menu Item ID:** 25393
- **Parent:** I-TOOLS (25391)
- **Target:** `_blank` (opens in new window)

---

## Final Menu Structure
1. Home
2. Calculators → GWYW, SCP (Coming Soon)
3. **I-TOOLS** → **TCP Sales Tool** (opens new window)
4. MANNA

---

## Key WordPress IDs
| Item | ID |
|---|---|
| Primary Menu | 28 |
| I-TOOLS menu item | 25391 |
| TCP Sales Tool page | 25392 |
| TCP Sales Tool menu item | 25393 |

---

## Files
- **Source HTML:** `/Users/ljoequick/Downloads/TCP_Sales_Tool_16.html`
- **Live URL:** https://joequick.com/tcp-sales-tool/
