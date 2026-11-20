# Project history — persistent change log

This document records **what happened**, distinguishable from aspirations. A PR merge means documentation/code landed, **not** that a physical robot was constructed.

## Design evolution before and through 2026-11-20
1. Explored ESP32-S3, ESP32-P4+C6, ESP32-S3+Grove Vision AI V2, Raspberry Pi 5 with AI HAT+ 2. Selected **P4+C6** to balance cost, offline lightweight perception and modular hardware.
2. Defined **desk + later wheeled robot** sharing a central module, optional PC RTX 3080/cloud for advanced AI, safety always on-device.
3. Selected medium physical class (12–18 cm) targeting **15 cm** height.
4. Chose **rounded-square head** over oval or separate individual eye modules.
5. Selected **Waveshare 2.4-inch ILI9341 LCD** (SKU 18366), nominal board 70.5×43.3 mm, visible area 48.96×36.72 mm, still requiring pin/electrical/integration validation.
6. Selected **Waveshare RPi Camera (B), OV5647**, ideally the official P4-A kit with matched cable; pending camera module lens/connector/cyclic-flex verification.
7. Created first head CAD mockup (PR #2), neck servo/yoke mockup (PR #3), desk packaging mockup (PR #4). All concept-only OpenSCAD volumes; no dimensioned manufacturing assembly.
8. Current documentation milestone: source-of-truth docs, agent instructions, BOM/risks, diagrams, and 3 independent GitHub Issues for simultaneous agents.

## Merged PRs
- #1 Camera selection: https://github.com/lhcarvalho/robot-companion/pull/1
- #2 Head model: https://github.com/lhcarvalho/robot-companion/pull/2
- #3 Pan/tilt model: https://github.com/lhcarvalho/robot-companion/pull/3
- #4 Internal desk packaging: https://github.com/lhcarvalho/robot-companion/pull/4

## Work not recorded as completed
No purchased part verification, STEP import, real fit, firmware bring-up, compile log, physical print, servo load measurement, camera recognition accuracy or mobile base fabrication. New agents must **not infer** any completion from rendered diagrams.

## Updating this history
Add dated, concise entries with linked commits/issues/PRs after substantive milestones. Product/architectural decisions belong in `DECISIONS.md`; operational readiness belongs in `STATUS.md`.

## 2026-11-20 — Three parallel workstreams integrated
- [PR #9](https://github.com/lhcarvalho/robot-companion/pull/9): first mechanical audit and envelope checker; dimensions remain provisional.
- [PR #10](https://github.com/lhcarvalho/robot-companion/pull/10): electrical interface planning and unknown-current budget.
- [PR #11](https://github.com/lhcarvalho/robot-companion/pull/11): uncompiled ESP-IDF P4 safe-idle scaffold and test matrix.
- Issues [#5](https://github.com/lhcarvalho/robot-companion/issues/5), [#6](https://github.com/lhcarvalho/robot-companion/issues/6), [#7](https://github.com/lhcarvalho/robot-companion/issues/7) deliberately **remain open**; core validation tasks are not done.
