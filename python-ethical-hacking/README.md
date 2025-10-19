# Python 101 for Hackers — Retention and Efficiency Playbook

## 1) Set the goal
- Write: “I’ll exit with X tools I can build in 20–40 min: scraper, hash cracker wrapper, log parser, port scanner, brute-force harness, simple C2 client.”
- Track time-to-implement. Aim to cut it by 30% by the end.

## 2) Run a tight learn loop for each lesson
- Watch at 1.25× while taking **task bullets** only.
- Code along once.
- Close video. Re-implement from memory in a fresh file.
- Add a 10-line “challenge” variant (e.g., add argparse, logging, and tests).
- Make 3–5 spaced-repetition cards (see §6).

## 3) Build a small, reusable `secutils` repo
```
secutils/
  README.md
  requirements.txt
  secutils/
    __init__.py
    http.py      # requests wrapper, retries, headers
    net.py       # sockets, port scan, CIDR utils
    fs.py        # safe file ops, hashing
    crypto.py    # hash/encode helpers
    parse.py     # regex helpers, log parsing
  tools/
    portscan.py
    dirbuster.py
    login_spray.py
    loggrep.py
  tests/
```
- Every lesson adds or improves one module or tool.
- Keep everything CLI-ready with `argparse` and `--help`.

## 4) Enforce speed and quality
- Editor: VS Code + Python, Pylance, Ruff (lint/format), GitLens.
- Env: `uv` or `pipx` + venv.
- Templates: create a **script template** you paste for every new tool:
```python
#!/usr/bin/env python3
import argparse, logging, sys
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    # TODO
if __name__ == "__main__":
    sys.exit(main())
```
- Tests: one tiny `pytest` test per tool.
- Timebox: 45–60 min per lesson including re-build.

## 5) Convert course code into workflows you’ll reuse
- Add `--wordlist`, `--proxy`, `--timeout`, `--threads` to network tools.
- Always support `--input file` and `--output file.jsonl`.
- Standardize logs: `INFO`, `WARN`, `ERROR`.
- Save run metadata (start, end, targets) to a JSON next to outputs.

## 6) Spaced repetition for retention
Use Anki. Card types:
- **Concept:** “What does `requests.Session()` buy you?” → “Keep-alive, cookies, headers once.”
- **Snippet:** “argparse pattern for required file input?” → minimal code.
- **Debug:** “Why does `bytes` vs `str` break sockets on Windows?” → rule + fix.
Review 5–10 cards/day. Add after every lesson.

## 7) Drill the “must-know” katas weekly
- Parse Nmap XML to CSV/JSONL.
- Threaded TCP port scanner with banner grab.
- HTML form login with CSRF token handling.
- Simple log parser: extract IPs, status, URIs, count uniques.
- Rate-limited HTTP brute harness with backoff and `429` handling.

## 8) Tie to your security work now
- Your Nextcloud lab: write `loggrep.py` to pull auth failures from Nginx and Nextcloud logs, and `evidence_pack.py` to zip findings with hashes.
- Build `db_env_audit.py` to list sensitive env vars from containers.
- Result: course knowledge turns into lab deliverables.

## 9) Weekly cadence (4 weeks)
- Mon–Wed: 2–3 lessons/day using the loop.
- Thu: refactor secutils + add tests.
- Fri: build one new tool from scratch without video.
- Sat: 45-min timed rebuild of any earlier tool.
- Sun: Anki + short write-up of what sped you up.

## 10) Measure improvement
- For each tool log: LOC, time, bugs found by tests, rerun time after refactor.
- Aim for: fewer lines, same features, fewer bugs, faster runs.
