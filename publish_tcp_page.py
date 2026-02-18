#!/usr/bin/env python3
"""Publish TCP Sales Tool to joequick.com/tcp-calculator/ via iframe sandbox.

Uses elementor_canvas template with an iframe that loads the entire standalone
HTML tool via srcdoc. This completely isolates from Cloudflare Rocket Loader,
WordPress themes, jQuery, and any other page-level scripts.
"""

import base64, json, subprocess, sys, tempfile, os

# ── Config ──────────────────────────────────────────────────
WP_URL  = "https://joequick.com/wp-json/wp/v2/pages/25404"
USER    = "joe.quick"
PASS    = "A4eZRwAwtv1HN9gQz7pk3Yae"
SRC     = "TCP SALES TOOL/TCP-Sales-Tool-Standalone.html"

# ── Read standalone HTML ────────────────────────────────────
print(f"Reading {SRC}...")
with open(SRC, "r", encoding="utf-8") as f:
    html_raw = f.read()

# ── Base64 encode (UTF-8 safe) ──────────────────────────────
b64 = base64.b64encode(html_raw.encode("utf-8")).decode("ascii")
print(f"  HTML size: {len(html_raw):,} bytes")
print(f"  Base64 size: {len(b64):,} chars")

# ── Build iframe wrapper ────────────────────────────────────
# The tool lives in a completely isolated iframe document.
# Rocket Loader, WordPress CSS, jQuery — none of it can reach inside.
wrapper = f'''<!-- wp:html -->
<div id="tcp-app" style="width:100%;background:#0f1117;min-height:100vh;">
<div id="tcp-loading" style="display:flex;align-items:center;justify-content:center;min-height:60vh;flex-direction:column;gap:12px;">
<div style="font-family:sans-serif;font-size:14px;color:#8b92a5;">Loading TCP Sales Tool...</div>
<div style="width:40px;height:40px;border:3px solid #2a2f3e;border-top-color:#f5c518;border-radius:50%;animation:tcpspin 1s linear infinite;"></div>
<style>@keyframes tcpspin{{from{{transform:rotate(0deg)}}to{{transform:rotate(360deg)}}}}</style>
</div>
<script data-cfasync="false" type="text/javascript">
(function(){{
  var b64="{b64}";
  try{{
    var bin=atob(b64);
    var bytes=new Uint8Array(bin.length);
    for(var i=0;i<bin.length;i++)bytes[i]=bin.charCodeAt(i);
    var html=new TextDecoder("utf-8").decode(bytes);
  }}catch(e){{
    document.getElementById("tcp-loading").innerHTML="<div style=\\"color:#f87171;font-family:sans-serif;font-size:14px;\\">Error: "+e.message+"</div>";
    return;
  }}
  var app=document.getElementById("tcp-app");
  var iframe=document.createElement("iframe");
  iframe.title="TCP Sales Tool";
  iframe.style.cssText="width:100%;height:100vh;border:none;display:none;background:#0f1117;";
  iframe.setAttribute("allow","clipboard-write");
  app.appendChild(iframe);
  iframe.srcdoc=html;
  iframe.onload=function(){{
    document.getElementById("tcp-loading").style.display="none";
    iframe.style.display="block";
    /* Auto-resize iframe to content height */
    try{{
      var resizeObserver=new ResizeObserver(function(){{
        var h=iframe.contentDocument.documentElement.scrollHeight;
        if(h>200)iframe.style.height=h+"px";
      }});
      resizeObserver.observe(iframe.contentDocument.documentElement);
    }}catch(e){{}}
  }};
}})();
</script>
</div>
<!-- /wp:html -->'''

print(f"  Wrapper size: {len(wrapper):,} chars")

# ── Publish to WordPress ────────────────────────────────────
payload = {
    "title": "TCP SALES Calculator (Beta)",
    "content": wrapper,
    "status": "publish",
    "slug": "tcp-calculator",
    "author": 16,
    "template": "elementor_canvas",
}

# Write JSON to temp file (avoids shell arg length limits)
tmpfile = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8')
json.dump(payload, tmpfile, ensure_ascii=False)
tmpfile.close()

print(f"\nPublishing to {WP_URL} ...")
print(f"  Template: elementor_canvas")
try:
    proc = subprocess.run(
        ["curl", "-s", "-X", "POST", WP_URL,
         "-u", f"{USER}:{PASS}",
         "-H", "Content-Type: application/json",
         "-d", f"@{tmpfile.name}"],
        capture_output=True, text=True, timeout=120
    )
    try:
        resp = json.loads(proc.stdout)
        page_id = resp.get("id")
        link = resp.get("link")
        if page_id:
            print(f"\nSUCCESS! Page updated:")
            print(f"  ID:   {page_id}")
            print(f"  URL:  {link}")
            print(f"  Slug: {resp.get('slug')}")
            print(f"  Template: {resp.get('template')}")
        else:
            print(f"\nERROR: {resp.get('message', 'Unknown error')}")
            print(f"Code: {resp.get('code')}")
            if resp.get("data"):
                print(f"Data: {resp.get('data')}")
    except Exception as e:
        print(f"Failed to parse response: {e}")
        print(f"Raw output: {proc.stdout[:500]}")
finally:
    os.unlink(tmpfile.name)
