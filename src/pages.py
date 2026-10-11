"""Static SEO pages: one page per prompt (p/<id>/), one per category (c/<slug>/), plus sitemap.xml and robots.txt.

The interactive library stays in index.html; these pages give search engines a real URL,
title and description for every prompt and link back into the app to fill inputs.
"""
import json, re, shutil, datetime
from html import escape

CSS = """
:root { --bg:#F2F3EF; --surface:#FFFFFF; --sunk:#E9EBE5; --ink:#15181D; --muted:#5A6170; --line:#D8DBD3;
  --accent:#1F48C9; --accent-ink:#FFFFFF; --accent-soft:#E3E9FB; --var-bg:#FCE8B6; --var-ink:#5E3E00;
  --f-display:"Bricolage Grotesque","Segoe UI",system-ui,sans-serif; --f-body:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;
  --f-mono:"JetBrains Mono",ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#0E1114; --surface:#161A1F; --sunk:#1D2228; --ink:#E7E9EC;
  --muted:#98A0AC; --line:#2A3038; --accent:#86A3FF; --accent-ink:#0B1020; --accent-soft:#1C2540; --var-bg:#3B2F12; --var-ink:#FFD47E; color-scheme:dark; } }
:root[data-theme="dark"] { --bg:#0E1114; --surface:#161A1F; --sunk:#1D2228; --ink:#E7E9EC; --muted:#98A0AC; --line:#2A3038;
  --accent:#86A3FF; --accent-ink:#0B1020; --accent-soft:#1C2540; --var-bg:#3B2F12; --var-ink:#FFD47E; color-scheme:dark; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:16px/1.6 var(--f-body); }
a { color:var(--accent); }
.wrap { max-width:900px; margin:0 auto; padding-inline:16px; }
header { border-bottom:1px solid var(--line); }
header .wrap { display:flex; justify-content:space-between; align-items:center; gap:12px; padding-block:14px; flex-wrap:wrap; }
.brand { font:700 22px/1 var(--f-display); color:var(--ink); text-decoration:none; }
.brand b { color:var(--accent); }
.crumbs { color:var(--muted); font-size:14px; margin:22px 0 6px; }
.crumbs a { color:inherit; }
h1 { font:700 clamp(28px,5vw,40px)/1.15 var(--f-display); letter-spacing:-.02em; margin:0 0 10px; text-wrap:balance; }
h2 { font:600 20px var(--f-display); margin:32px 0 10px; }
.lead { color:var(--muted); font-size:18px; margin:0 0 14px; }
.pills { display:flex; gap:6px; flex-wrap:wrap; margin-bottom:18px; }
.pill { font:12px var(--f-mono); padding:2px 8px; border-radius:5px; background:var(--sunk); color:var(--muted); }
.actions { display:flex; gap:10px; flex-wrap:wrap; margin:18px 0; }
.btn { display:inline-flex; align-items:center; border:1px solid var(--line); background:var(--surface); color:var(--ink); border-radius:9px; padding:9px 14px; font:500 15px var(--f-body); cursor:pointer; text-decoration:none; }
.btn.primary { background:var(--accent); color:var(--accent-ink); border-color:var(--accent); }
pre { white-space:pre-wrap; word-break:break-word; font:14px/1.65 var(--f-mono); background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:16px; margin:0; }
pre .h { color:var(--accent); font-weight:600; } pre .v { background:var(--var-bg); color:var(--var-ink); border-radius:3px; padding:0 2px; }
table { width:100%; border-collapse:collapse; font-size:15px; }
th, td { text-align:left; padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top; }
td code { font:13px var(--f-mono); background:var(--var-bg); color:var(--var-ink); padding:1px 5px; border-radius:4px; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:10px; }
.card { display:block; background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:12px 14px; color:var(--ink); text-decoration:none; }
.card:hover { border-color:var(--accent); }
.card strong { display:block; font-weight:600; } .card span { color:var(--muted); font-size:14px; }
.box { margin-top:32px; padding:18px 20px; border-radius:12px; background:var(--accent-soft); display:grid; gap:8px; }
.box h3 { margin:0; font:600 18px var(--f-display); } .box p { margin:0; color:var(--muted); }
.box form { display:flex; gap:8px; flex-wrap:wrap; }
.box input[type=email] { flex:1 1 220px; min-width:0; padding:9px 12px; border:1px solid var(--line); border-radius:9px; background:var(--surface); color:var(--ink); font:inherit; }
footer { border-top:1px solid var(--line); margin-top:48px; padding-block:20px 40px; color:var(--muted); font-size:14px; }
footer .wrap { display:flex; gap:14px; flex-wrap:wrap; justify-content:space-between; }
footer a { color:inherit; }
.toast { position:fixed; left:50%; bottom:24px; transform:translateX(-50%); background:var(--ink); color:var(--bg); padding:9px 16px; border-radius:9px; }
"""

COPY_JS = """<script>
document.querySelectorAll("[data-copy]").forEach(b => b.addEventListener("click", async () => {
  const t = document.getElementById(b.dataset.copy).innerText;
  let msg = "Prompt copied";
  try { await navigator.clipboard.writeText(t); } catch { msg = "Copy blocked. Select the text and press Ctrl+C."; }
  const d = document.createElement("div"); d.className = "toast"; d.textContent = msg; document.body.appendChild(d); setTimeout(() => d.remove(), 1800);
  try { window.goatcounter && window.goatcounter.count({ path: "event/copy-" + b.dataset.id, title: "copy", event: true }); } catch {}
}));
</script>"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700'
         '&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">')


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def highlight(text):
    out = []
    for line in escape(text, quote=False).split("\n"):
        if line.startswith("# "):
            out.append(f'<span class="h">{line}</span>')
        else:
            out.append(re.sub(r"\{\{(\w+)\}\}", r'<span class="v">{{\1}}</span>', line))
    return "\n".join(out)


def page(title, desc, url, root, body, analytics, jsonld):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
{FONTS}
<link rel="stylesheet" href="{root}assets/page.css">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False).replace("</", "<\\/")}</script>
{analytics}
</head>
<body>
<header><div class="wrap"><a class="brand" href="{root}">Prompt <b>Atlas</b></a><a class="btn" href="{root}#pro">Pro Pack</a></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><span>Prompt Atlas. Free prompts for developers everywhere.</span><span>{{FOOT}}</span></div></footer>
{COPY_JS}
</body>
</html>
"""


def money_box(cfg, pro, root):
    parts = []
    if cfg.get("newsletter_action"):
        parts.append(f"""<div class="box"><h3>Get one new prompt every week</h3>
<p>Join the Prompt Atlas newsletter for a battle-tested prompt each week and a launch discount on the Pro Pack.</p>
<form method="post" target="_blank" action="{escape(cfg['newsletter_action'])}"><input type="email" name="email" required placeholder="you@company.com" aria-label="Email address"><input type="hidden" name="tag" value="prompt-page"><button class="btn primary" type="submit">Subscribe</button></form></div>""")
    if pro:
        cta = (f'<a class="btn primary" href="{escape(cfg["pro_checkout_url"])}" target="_blank" rel="noopener">Get the Pro Pack {escape(cfg.get("pro_price", ""))}</a>'
               if cfg.get("pro_checkout_url") else f'<a class="btn" href="{root}#pro">See the Pro Pack</a>')
        parts.append(f"""<div class="box"><h3>Want the advanced versions?</h3>
<p>The Pro Pack adds {len(pro)} expert prompts for agents, system design, incidents, security reviews, performance and tech leadership.</p>
<div>{cta}</div></div>""")
    return "\n".join(parts)


def footer(cfg, root):
    links = [(root, "All prompts"), (cfg.get("repo_url"), "GitHub"), (cfg.get("support_url"), "Buy me a coffee"),
             (cfg.get("sponsors_url"), "Sponsor")]
    return " · ".join(f'<a href="{escape(u)}">{t}</a>' for u, t in links if u)


def build(prompts, cfg, pro, analytics, out):
    site = cfg["site_url"].rstrip("/") + "/"
    for d in ("p", "c"):
        shutil.rmtree(out / d, ignore_errors=True)
    (out / "assets").mkdir(exist_ok=True)
    (out / "assets" / "page.css").write_text(CSS.strip() + "\n")
    by_cat = {}
    for p in prompts:
        by_cat.setdefault(p["category"], []).append(p)
    urls = [site]
    foot_p, foot_c = footer(cfg, "../../"), footer(cfg, "../../")
    for p in prompts:
        root = "../../"
        url = f"{site}p/{p['id']}/"
        urls.append(url)
        cslug = slug(p["category"])
        rows = "".join(f"<tr><td><code>{{{{{escape(v['name'])}}}}}</code></td><td>{escape(v['hint'] or v['name'].replace('_', ' '))}</td></tr>"
                       for v in p["variables"])
        related = [q for q in by_cat[p["category"]] if q["id"] != p["id"]][:6]
        rel = "".join(f'<a class="card" href="../{q["id"]}/"><strong>{escape(q["title"])}</strong><span>{escape(q["description"])}</span></a>' for q in related)
        body = f"""<div class="crumbs"><a href="{root}">Prompt Atlas</a> / <a href="{root}c/{cslug}/">{escape(p['category'])}</a></div>
<h1>{escape(p['title'])} prompt</h1>
<p class="lead">{escape(p['description'])}</p>
<div class="pills">{''.join(f'<span class="pill">{escape(t)}</span>' for t in p['tags'])}</div>
<div class="actions"><a class="btn primary" href="{root}#{p['id']}">Fill in the inputs and copy</a><button class="btn" data-copy="prompt" data-id="{p['id']}">Copy template</button></div>
<h2>Inputs you provide</h2>
<table><thead><tr><th>Placeholder</th><th>What to put there</th></tr></thead><tbody>{rows}</tbody></table>
<h2>The prompt</h2>
<pre id="prompt">{highlight(p['prompt'])}</pre>
<h2>How to use it</h2>
<p>Replace each highlighted <code>{{{{placeholder}}}}</code> with your details, or open the <a href="{root}#{p['id']}">interactive editor</a> to fill them in and copy the finished prompt. It works in Claude, ChatGPT, Gemini and any other chat model.</p>
{money_box(cfg, pro, root)}
<h2>More {escape(p['category'])} prompts</h2>
<div class="grid">{rel}</div>"""
        jsonld = {"@context": "https://schema.org", "@graph": [
            {"@type": "CreativeWork", "name": p["title"], "description": p["description"], "url": url,
             "keywords": ", ".join(p["tags"]), "genre": p["category"], "isAccessibleForFree": True,
             "isPartOf": {"@type": "WebSite", "name": "Prompt Atlas", "url": site}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Prompt Atlas", "item": site},
                {"@type": "ListItem", "position": 2, "name": p["category"], "item": f"{site}c/{cslug}/"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}]}
        html = page(f"{p['title']} prompt for ChatGPT, Claude & Gemini | Prompt Atlas",
                    f"{p['description']} A complete, copy-ready AI prompt with role, inputs, steps, constraints and output format.",
                    url, root, body, analytics, jsonld).replace("{FOOT}", foot_p)
        d = out / "p" / p["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(html)
    for cat, items in by_cat.items():
        root = "../../"
        cslug = slug(cat)
        url = f"{site}c/{cslug}/"
        urls.append(url)
        cards = "".join(f'<a class="card" href="../../p/{q["id"]}/"><strong>{escape(q["title"])}</strong><span>{escape(q["description"])}</span></a>' for q in items)
        others = "".join(f'<a class="pill" href="../{slug(c)}/">{escape(c)}</a>' for c in by_cat if c != cat)
        body = f"""<div class="crumbs"><a href="{root}">Prompt Atlas</a> / {escape(cat)}</div>
<h1>{escape(cat)} prompts</h1>
<p class="lead">{len(items)} complete, ready-to-run AI prompts for {escape(cat.lower())}. Each one sets a role, goal, inputs, step-by-step instructions, constraints and an exact output format.</p>
<div class="grid">{cards}</div>
{money_box(cfg, pro, root)}
<h2>Other categories</h2>
<div class="pills">{others}</div>"""
        jsonld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": f"{cat} prompts", "url": url,
                  "hasPart": [{"@type": "CreativeWork", "name": q["title"], "url": f"{site}p/{q['id']}/"} for q in items]}
        html = page(f"{cat} AI prompts ({len(items)} free, copy-ready) | Prompt Atlas",
                    f"{len(items)} free, complete AI prompts for {cat.lower()}: " + "; ".join(q["title"] for q in items[:4]) + ".",
                    url, root, body, analytics, jsonld).replace("{FOOT}", foot_c)
        d = out / "c" / cslug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(html)
    today = datetime.date.today().isoformat()
    sm = "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    (out / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n')
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {site}sitemap.xml\n")
    print(len(urls), "URLs in sitemap.xml")
