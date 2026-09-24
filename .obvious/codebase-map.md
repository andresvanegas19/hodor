# Codebase map — andresvanegas19/hodor

Sole dependency: Selenium (pip). Sole external target: http://158.69.76.135.

| Path | Type | Purpose |
|---|---|---|
| `script` | Python script | Level-2 voter; uses spoofed User-Agent; runs a 2000-vote loop on execution |
| `level_0/` | Python script + README | Level-0 voter; vote loop defined but never invoked (safe to run) |
| `level_1/` | Python script + README | Level-1 voter; runs a 4048-vote loop on execution |
| `level_2/` | Python script + README | Level-2 voter; runs a 4048-vote loop on execution |

Depth cap 2 reached. No tests, no manifests, no CI config anywhere in the tree.
