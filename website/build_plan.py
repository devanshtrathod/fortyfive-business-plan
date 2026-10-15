"""Build the FortyFive website plan: plan_src/*.md -> 'FortyFive website plan.md' + website-plan.html.

Markdown is GitHub-flavoured (lists may follow a paragraph directly; nest by the list marker's width).
Converted with pandoc:  python website/build_plan.py
"""
import glob
import html as H
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PANDOC = os.path.expandvars(r'%LOCALAPPDATA%\Pandoc\pandoc.exe')
parts = sorted(glob.glob(os.path.join(HERE, 'plan_src', '*.md')))
src = '\n\n'.join(open(p, encoding='utf-8').read().strip() for p in parts) + '\n'
assert '—' not in src, 'em dash found'

open(os.path.join(HERE, 'FortyFive website plan.md'), 'w', encoding='utf-8', newline='\n').write(src)

out = subprocess.run([PANDOC, '-f', 'gfm', '-t', 'html', '--wrap=none'], input=src.encode('utf-8'),
                     capture_output=True, check=True).stdout
body = out.decode('utf-8').replace(chr(13), '')  # pandoc on Windows writes CRLF
body = re.sub(r'<table[^>]*>', '<div class="tw"><table>', body).replace('</table>', '</table></div>')
body = body.replace('<pre><code>', '<pre class="wf"><code>')

# contents list from the h2/h3/h4 headings
heads = re.findall(r'<h([234]) id="([^"]+)"[^>]*>(.*?)</h\1>', body, flags=re.S)
toc, depth = ['<div><ul>'], 2
for lvl, hid, txt in heads:
    lvl = int(lvl)
    label = H.escape(H.unescape(re.sub(r'<[^>]+>', '', txt)).strip())
    if toc[-1].endswith('</a>') and lvl <= depth:
        toc.append('</li>')
    while depth > lvl:
        toc.append('</ul></li>')
        depth -= 1
    while depth < lvl:
        toc.append('<ul>')
        depth += 1
    toc.append('<li><a href="#%s">%s</a>' % (hid, label))
toc.append('</li>')
while depth > 2:
    toc.append('</ul></li>')
    depth -= 1
toc.append('</ul></div>')
toc = ''.join(toc)

CSS = r'''
:root{color-scheme:light;--paper:#f6f4ee;--surface:#fffffe;--wash:#efede6;--ink:#121211;--ink-2:#4a4945;--muted:#7a7873;--rule:#dcdad2;--blue:#2a78d6;--blue-wash:#e9f1fb;--red:#b42a2a}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){color-scheme:dark;--paper:#0f0f0e;--surface:#1a1a19;--wash:#232321;--ink:#f4f2ec;--ink-2:#c3c2b7;--muted:#8f8d86;--rule:#2f2f2c;--blue:#5b9be8;--blue-wash:#16263a;--red:#e06a6a}}
:root[data-theme="dark"]{color-scheme:dark;--paper:#0f0f0e;--surface:#1a1a19;--wash:#232321;--ink:#f4f2ec;--ink-2:#c3c2b7;--muted:#8f8d86;--rule:#2f2f2c;--blue:#5b9be8;--blue-wash:#16263a;--red:#e06a6a}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--paper);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--blue)}
.top{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1px solid var(--rule)}
.top .in{max-width:1240px;margin:0 auto;padding:12px 16px;display:flex;gap:12px;align-items:center}
.mark{width:32px;height:32px;border-radius:7px;background:var(--ink);color:var(--paper);display:grid;place-items:center;font-weight:800;font-size:13px;flex:none}
.top b{font-size:15px}.top .sp{flex:1}
.btn{font:inherit;font-size:13px;border:1px solid var(--rule);background:var(--surface);color:var(--ink);border-radius:8px;padding:6px 10px;cursor:pointer;text-decoration:none}
.layout{max-width:1240px;margin:0 auto;padding:0 16px;display:grid;grid-template-columns:270px minmax(0,1fr);gap:40px}
nav.toc{position:sticky;top:58px;align-self:start;max-height:calc(100vh - 70px);overflow:auto;padding:18px 0 40px;font-size:13.5px}
nav.toc ul{list-style:none;margin:0;padding:0}
nav.toc ul ul{padding-left:12px;border-left:1px solid var(--rule);margin:2px 0 6px 4px}
nav.toc li{margin:2px 0}
nav.toc a{color:var(--ink-2);text-decoration:none}
nav.toc a:hover{color:var(--blue)}
nav.toc > div > ul > li > a{color:var(--ink);font-weight:650}
details.mtoc{display:none}
main{padding:22px 0 80px;min-width:0}
h1{font-size:34px;line-height:1.15;letter-spacing:-.5px;margin:6px 0 10px}
h2{font-size:26px;letter-spacing:-.3px;margin:48px 0 10px;padding-top:18px;border-top:1px solid var(--rule)}
h3{font-size:19px;margin:30px 0 8px}
h4{font-size:16px;margin:26px 0 6px}
p,li{color:var(--ink-2)} strong{color:var(--ink)}
ul,ol{padding-left:22px}
hr{border:0;border-top:1px solid var(--rule);margin:26px 0}
code{font:13.5px ui-monospace,SFMono-Regular,Consolas,monospace;background:var(--wash);padding:1px 5px;border-radius:5px;color:var(--ink)}
pre.wf{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:14px 16px;overflow-x:auto;white-space:pre;line-height:1.35;margin:14px 0}
pre.wf code{background:none;padding:0;font-size:12.5px;color:var(--ink)}
.tw{overflow-x:auto;border:1px solid var(--rule);border-radius:10px;background:var(--surface);margin:12px 0}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:8px 11px;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);background:var(--wash)}
tr:last-child td{border-bottom:0}
td{color:var(--ink-2)}
@media (max-width:900px){
  .layout{grid-template-columns:minmax(0,1fr);gap:0}
  nav.toc{display:none}
  details.mtoc{display:block;margin:14px 0 0;border:1px solid var(--rule);border-radius:10px;background:var(--surface);padding:10px 14px;font-size:14px}
  details.mtoc ul{list-style:none;padding-left:12px}
  .top{position:static}
}
@media print{.top,nav.toc,details.mtoc{display:none}.layout{display:block}}
'''

JS = r'''
(function(){
  var r=document.documentElement;
  function st(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v);}catch(e){return null;}}
  var s=st('ffp-theme'); if(s==='light'||s==='dark') r.setAttribute('data-theme',s);
  document.getElementById('th').addEventListener('click',function(){
    var c=r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
    var n=c==='dark'?'light':'dark'; r.setAttribute('data-theme',n); st('ffp-theme',n);
  });
})();
'''

html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FortyFive Website Plan</title>
<style>%s</style>
</head>
<body>
<header class="top"><div class="in"><div class="mark">45.</div><b>Website plan</b><span class="sp"></span>
<a class="btn" href="../index.html#website">Business plan</a><button class="btn" id="th" type="button">Theme</button></div></header>
<div class="layout">
<nav class="toc" aria-label="Contents">%s</nav>
<main>
<details class="mtoc"><summary>Contents</summary>%s</details>
%s
</main>
</div>
<script>%s</script>
</body>
</html>
''' % (CSS, toc, toc, body, JS)
open(os.path.join(HERE, 'website-plan.html'), 'w', encoding='utf-8', newline='\n').write(html)
print('wrote', len(src), 'chars of markdown,', len(html), 'chars of html')
