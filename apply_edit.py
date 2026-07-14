#!/usr/bin/env python3
"""구글 폼 중계 반영: 게시된 응답 CSV에서 최신 제출을 읽어 index.html의 <main>을 교체한다."""
import csv, io, os, re, sys, urllib.request

CSV_URL = os.environ.get("CSV_URL", "")
PASS = os.environ.get("PASS", "").strip()
if not CSV_URL or not PASS:
    print("시크릿 미설정 — 건너뜀"); sys.exit(0)

with urllib.request.urlopen(CSV_URL, timeout=30) as r:
    raw = r.read().decode("utf-8")

rows = list(csv.reader(io.StringIO(raw)))
if len(rows) < 2:
    print("제출 없음"); sys.exit(0)

# 헤더: 타임스탬프, 암구호, content — 암구호가 맞는 마지막 행
passes = {p.strip() for p in PASS.split(",") if p.strip()}
valid = [row for row in rows[1:] if len(row) >= 3 and row[1].strip() in passes]
rejected = len(rows) - 1 - len(valid)
if rejected:
    print(f"암구호 불일치 제출 {rejected}건 무시")
if not valid:
    print("유효한 제출 없음"); sys.exit(0)

ts, _, content = valid[-1][0], valid[-1][1], valid[-1][2]

last = ""
if os.path.exists(".last-sync"):
    last = open(".last-sync", encoding="utf-8").read().strip()
if ts == last:
    print("이미 반영된 제출"); sys.exit(0)

# 안전 점검: 편집 영역으로서 최소한의 형태를 갖췄는지
checks = [len(content) > 5000, content.count("<section") >= 8,
          content.count("<section") == content.count("</section>"),
          'class="hero' in content]
if not all(checks):
    print(f"안전 점검 실패 — 반영 중단 (len={len(content)}, sec={content.count('<section')})")
    sys.exit(1)

content = content.replace("reveal in", "reveal")  # 스크롤 리빌 상태 클래스 제거

html = open("index.html", encoding="utf-8").read()
new_html, n = re.subn(r'(<main id="top">).*?(</main>)',
                      lambda m: m.group(1) + "\n" + content.strip() + "\n" + m.group(2),
                      html, count=1, flags=re.S)
if n != 1:
    print("main 블록을 찾지 못함"); sys.exit(1)

open("index.html", "w", encoding="utf-8").write(new_html)
open(".last-sync", "w", encoding="utf-8").write(ts)
print(f"반영 완료: 제출 시각 {ts}, content {len(content)}자")
