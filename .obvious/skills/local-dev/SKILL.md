---
name: local-dev
description: How to get the hodor Selenium scripts running locally in the obvious sandbox
---

# Local dev — andresvanegas19/hodor

Recorded by the onboarding run of 2026-09-24. dev_stack_healthy: true.

## Environment setup (from a fresh snapshot)

```bash
pip3 install selenium            # 4.49.0
sudo apt-get update && sudo apt-get install -y chromium chromium-driver xvfb
```

chromedriver and Chromium are both 153 from Debian 13 repos, so no manual
driver matching is needed.

## Gotchas

1. **No dependency manifest.** Selenium must be installed by hand; there is no
   requirements.txt/pyproject.toml to install from.
2. **Deprecated Selenium APIs.** Every script uses `find_element_by_name`
   and/or `chrome_options=`, both removed in Selenium 4.3. Scripts that invoke
   their vote loop crash with `AttributeError`. The onboarding verification
   used a modern-API harness instead of patching repo source.
3. **Side-effect scripts.** Root `script`, `level_1/script1.py`, and
   `level_2/script2.py` fire 2000–4048 automated votes at the external server
   immediately on run. Only `level_0/script.py` is inert.
4. **No display.** `webdriver.Chrome()` is headed; run scripts under
   `xvfb-run -a` or add headless options.
5. **External target must be up.** `curl -m 10 http://158.69.76.135/level0.php`
   should return HTTP 200; if not, flows cannot be verified
   (`service_unreachable`).

## Verified primary flow (2026-09-24)

Headless Chromium via Selenium: load `level0.php` → send `1565` to
`input[name="id"]` → click `input[name="holdthedoor"]` → the id appears in the
results table. Exactly one vote submitted (deliberately not the script's loop
count). Screenshot: `/tmp/hodor_flow_proof.png` (208 KB). Exit code 0.

## Checks run

- `python3 -m py_compile script level_0/script.py level_1/script1.py level_2/script2.py` → OK
- `xvfb-run -a python3 level_0/script.py` → exit 0
- No lint/typecheck/test config exists in the repo to run.
