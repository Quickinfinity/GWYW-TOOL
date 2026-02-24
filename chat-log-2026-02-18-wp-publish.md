# Chat Log — WordPress Publishing Session
**Date:** 2026-02-18

## Summary
Reconfigured TCP Sales Tool and SCP Calculator for WordPress publishing at joequick.com.

## Pages
- **TCP Calculator**: https://joequick.com/tcp-calculator/ (Page ID: 25404)
- **SCP Calculator**: https://joequick.com/scp-calculator/ (Page ID: 25398)
- **GWYW Calculator**: https://joequick.com/business-calculator/ (Page ID: 25232, reference)

## WordPress Credentials
- User: joe.quick
- Pass: A4eZRwAwtv1HN9gQz7pk3Yae

## Local Files
- `TCP SALES TOOL/TCP-Sales-Tool-Standalone.html` — TCP standalone tool (~920 lines)
- `SCP CALCULATOR /Claude scp-calculator.html` — SCP standalone tool (~1075 lines)
- `publish_tcp_page.py` — Publishes TCP to WP page 25404
- `publish_scp_page.py` — Publishes SCP to WP page 25398

## What Was Done

### Problem
TCP Sales Tool tabs weren't working on WordPress. Root cause: Cloudflare Rocket Loader (`rocket-loader.min.js`) intercepts and modifies inline JavaScript event handlers (`onclick`, `oninput`, `onchange`), prepending `if (!window.__cfRLUnblockHandlers) return false;` to every handler.

### Approaches Tried
1. **`data-cfasync="false"` on script tags** — Prevents Rocket Loader from deferring script execution, but does NOT stop it from modifying inline HTML event handlers.
2. **GWYW direct HTML pattern** — Scoped CSS under `#tcp-calc`/`#scp-calc`, Astra theme overrides, `elementor_canvas` template. CSS scoping worked perfectly (141 scoped rules), but Rocket Loader still broke all inline handlers.
3. **`window.__cfRLUnblockHandlers = true`** — Set Rocket Loader's unblock flag early. Still unreliable.
4. **Iframe sandbox (FINAL - WORKING)** — Base64-encode the entire standalone HTML, decode in JS, inject into an iframe via `srcdoc`. The iframe is a completely separate document context that Rocket Loader cannot reach.

### Final Architecture
```
WordPress Page (elementor_canvas template)
  └── <!-- wp:html --> block
       └── <div id="tcp-app"> wrapper
            ├── Loading spinner (visible while iframe loads)
            └── <script data-cfasync="false">
                 └── Decodes base64 → creates iframe → sets srcdoc
                      └── Standalone HTML runs in complete isolation
```

### Key Findings
- `elementor_canvas` template removes WP theme header/footer but still loads all head scripts/styles
- Cloudflare Rocket Loader modifies ALL inline event handlers in HTML, regardless of `data-cfasync="false"`
- The GWYW calculator works with direct HTML because it was built for WordPress (uses JS event listeners, not inline handlers)
- TCP/SCP use extensive inline handlers and must use iframe isolation
- WordPress REST API: POST to `/wp-json/wp/v2/pages/{id}` with basic auth
- Password protection was accidentally set; cleared via API with `{"password":""}`

### Git
- Commit: `166c7f9` — "Add iframe sandbox publish scripts for TCP and SCP calculators"
- Pushed to: https://github.com/Quickinfinity/GWYW-TOOL.git (main branch)

## How to Republish
```bash
cd "/Users/ljoequick/Desktop/2026/VS STUDIO "
python3 publish_tcp_page.py   # TCP → joequick.com/tcp-calculator/
python3 publish_scp_page.py   # SCP → joequick.com/scp-calculator/
```
