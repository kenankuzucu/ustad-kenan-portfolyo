#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ustad Kenan Kuzucu portfolyo sitesi -> GitHub + yerel ayna yedegi.
Kullanim:  python arac/github-yedekle.py "degisiklik aciklamasi"
Token ~/AppData/Local/hermes/.env icindeki GITHUB_TOKEN'dan okunur; ekrana yazilmaz.
"""
import io, os, sys, json, subprocess

KUL = "kenankuzucu"
DEPO = "ustad-kenan-portfolyo"
PROJE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = os.path.join(os.path.expanduser("~"), "AppData", "Local", "hermes", ".env")
AYNA = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "USTAD-GITHUB-YEDEK",
                    __import__("datetime").date.today().isoformat(), DEPO + ".git")

def token():
    for satir in io.open(ENV, encoding="utf-8", errors="replace"):
        if satir.strip().startswith("GITHUB_TOKEN="):
            return satir.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("GITHUB_TOKEN bulunamadi: " + ENV)

TOK = token()
def git(*a, cwd=PROJE):
    r = subprocess.run(["git"] + list(a), cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout.replace(TOK, "***").strip(), r.stderr.replace(TOK, "***").strip()

mesaj = sys.argv[1] if len(sys.argv) > 1 else "Guncelleme"
git("add", "-A")
rc, out, _ = git("commit", "-m", mesaj)
print("commit:", "yeni kayit olustu" if rc == 0 else "degisiklik yok")

url = "https://%s:%s@github.com/%s/%s.git" % (KUL, TOK, KUL, DEPO)
rc, out, err = git("push", url, "main")
print("push:", "tamam" if rc == 0 else err[-300:])

rc, yerel, _ = git("rev-parse", "HEAD")
if os.path.isdir(AYNA):
    git("remote", "update", "--prune", cwd=AYNA)
else:
    os.makedirs(os.path.dirname(AYNA), exist_ok=True)
    r = subprocess.run(["git", "clone", "--mirror", url, AYNA], capture_output=True, text=True)
    print("ayna klon:", "tamam" if r.returncode == 0 else r.stderr[-200:])
_, refsay, _ = git("show-ref", cwd=AYNA)
_, commitlar, _ = git("rev-list", "--all", "--count", cwd=AYNA)
_, aynah, _ = git("rev-parse", "HEAD", cwd=AYNA)
print("yerel HEAD :", yerel[:12])
print("ayna  HEAD :", aynah[:12], "->", "AYNI" if aynah == yerel else "FARKLI")
print("ayna  ref  :", len(refsay.splitlines()), "| commit:", commitlar)
print("ayna  yol  :", AYNA)
