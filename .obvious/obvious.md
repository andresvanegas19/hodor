# obvious.md — andresvanegas19/hodor

## What this repo is

Automation scripts for the "Hold the Door" (Holberton School) voting challenge.
Each script drives a browser with Selenium to submit votes on an external
challenge server. This is a scripts-only repo: no web app, no API, no tests,
no dependency manifest, no CI.

## Stack

| Component | Version / source | Notes |
|---|---|---|
| Python | 3.13 | system python3 on Debian 13 |
| Selenium | 4.49.0 | `pip3 install selenium` (no requirements file — TODO(confirm) pin one) |
| Chromium | 153 (Debian apt) | `sudo apt-get install chromium chromium-driver` |
| chromedriver | 153 (Debian apt) | matched to Chromium |
| xvfb | apt | needed for headed `webdriver.Chrome()` runs (no display in sandbox) |

## External services

| Service | URL | Purpose |
|---|---|---|
| Hold the Door challenge | http://158.69.76.135 | target site for level0/1/2 voting pages; verified reachable (HTTP 200) |

No env vars, no `.env.example`, no secrets required.

## Commands

There is no canonical dev command or dev server. All entries are standalone
scripts.

```bash
# install runtime deps (not committed — no manifest in repo)
pip3 install selenium
sudo apt-get install chromium chromium-driver xvfb

# syntax check all scripts
python3 -m py_compile script level_0/script.py level_1/script1.py level_2/script2.py

# run the one script that is safe to execute as-is
xvfb-run -a python3 level_0/script.py
```

## ⚠️ Scripts with side effects on run

These execute their vote loops **on run** (hundreds to thousands of automated
votes against the external server). Do not run them casually:

- `script` (root) — runs a 2000-vote loop against `level2.php`
- `level_1/script1.py` — runs a 4048-vote loop
- `level_2/script2.py` — runs a 4048-vote loop

`level_0/script.py` defines its loop but never invokes it, so it only opens the
page and exits.

## Known issues (TODO(confirm))

- All scripts use Selenium APIs removed in Selenium 4.3
  (`find_element_by_name`, `chrome_options=` kwarg). Any script that actually
  invokes its vote loop raises `AttributeError` on Selenium 4.x. Either pin
  `selenium<4` or migrate to `find_element(By.NAME, ...)`.
- No pinned dependency manifest exists.

## Codebase map

Tiny repo — full map inlined here; see `codebase-map.md` for the table.

## Local verification (what "works" looks like)

1. `python3 -m py_compile script level_0/script.py level_1/script1.py level_2/script2.py` exits 0.
2. Primary user flow (headless Chromium + Selenium): load
   `http://158.69.76.135/level0.php` → fill `input[name="id"]` → click
   `input[name="holdthedoor"]` → id appears in the results table. Verified
   2026-09-24 with exactly one vote; screenshot at `/tmp/hodor_flow_proof.png`
   in the onboarding sandbox.
3. `xvfb-run -a python3 level_0/script.py` exits 0.

## Snapshot

| Field | Value |
|---|---|
| snapshotId | `fksiubm9ol9a9ei59k4h:default` |
| capturedAt | `2026-09-24T18:26:20.200Z` (ISO-8601, UTC) |
| dev_stack_healthy | `true` |
