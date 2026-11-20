# Project status — 2026-11-20

**Phase:** concept engineering / packaging feasibility, **NOT** assembly-ready.
**Last merged technical milestone:** desk internal packaging V0.1 (PR #4).
**No physical component installation, electrical bench test, validated complete CAD assembly, firmware compilation, motor calibration, or printed enclosure is recorded in this repository.** If any happened elsewhere, require evidence before updating status.

## What was completed
| PR | Content | State | Evidence |
|---|---|---|---|
| [#1](https://github.com/lhcarvalho/robot-companion/pull/1) | Camera OV5647 selection, MIPI cable and risk checklist | Merged | docs/hardware/camera-selection.md |
| [#2](https://github.com/lhcarvalho/robot-companion/pull/2) | Head envelope and LCD/camera proxies | Merged | mechanics/cad/head_layout_v01.scad; HEAD_LAYOUT_V01.md |
| [#3](https://github.com/lhcarvalho/robot-companion/pull/3) | Pan/tilt kinematic volumes and MG90S torque sensitivity | Merged | mechanics/cad/neck_kinematics_v01.scad; NECK_DESIGN_V01.md |
| [#4](https://github.com/lhcarvalho/robot-companion/pull/4) | Desk packaging / motherboard, audio and power reservations | Merged | mechanics/cad/desk_internal_layout_v01.scad; DESK_INTERNAL_LAYOUT_V01.md |

## Reality check
- **Selected != validated != purchased != tested.**
- Head/torso CAD uses provisional dimensions and overlapping proxies; no printable mounting brackets yet.
- **P4 board outer size/connector envelopes** have NOT been established from STEP in repository; 95×70×18 mm is a mockup.
- **Camera moving FFC cable through pan/tilt neck** is the top mechanical risk.
- Screen's SPI GPIO mapping, power/backlight and simultaneous camera + screen + audio operation are not bench-tested.
- Servo safe operating torque, head mass and power budget are unknown.
- LCD, camera, servos, power parts and speakers have not been marked ordered or received.

## Parallel tasks opened
- [#5 — Mechanical STEP + moving-neck fit](https://github.com/lhcarvalho/robot-companion/issues/5)
- [#6 — Electrical pinout + power + BOM](https://github.com/lhcarvalho/robot-companion/issues/6)
- [#7 — ESP-IDF firmware scaffold + smoke tests](https://github.com/lhcarvalho/robot-companion/issues/7)

## Current next action
Acquire/import official dimensioned STEP of Waveshare board, camera and LCD drawings; determine actual 3D collision-free placement and moving-cable route, while an independent electrical agent verifies GPIO/power allocation. See [ROADMAP](ROADMAP.md) and [TASKS](TASKS.md).

## Handoff recipe for a model with zero chat history
1. Read root [README](../README.md) and [AGENTS.md](../AGENTS.md).
2. Read this file, [PROJECT_BRIEF](PROJECT_BRIEF.md), [DECISIONS](DECISIONS.md), [OPEN_QUESTIONS](OPEN_QUESTIONS.md), [ROADMAP](ROADMAP.md).
3. Read linked hardware/CAD sources. Inspect the actual files; do not infer their content from summaries.
4. Check open issues and PRs before choosing a task; claim a narrow task in an issue and use your own branch.
5. Do not change approved architecture silently. Attach tests/evidence, update this status and open questions in the PR.
6. No hardware fit claim without manufacturer drawings or measured artifact; no working firmware claim without logs.

## Parallel-work integration — 2026-11-20
- **Mechanical PR #9 merged:** `mechanics/MECHANICAL_INTERFACE_AUDIT.md` and `mechanics/check_envelope.py`. Nominal cavity arithmetic validated; manufacturer STEP could not be downloaded/imported here. **Issue #5 remains open.**
- **Electrical PR #10 merged:** `electronics/INTERFACE_MATRIX.md` and `electronics/POWER_BUDGET.csv`. Wiring GPIO pin numbers and load currents explicitly UNKNOWN. **Issue #6 remains open.**
- **Firmware PR #11 merged:** `firmware/` ESP-IDF scaffold for P4, safe-idle loop, `tests/SMOKE_TEST_MATRIX.md`. ESP-IDF unavailable in this execution; **NOT COMPILED / NOT RUN**. **Issue #7 remains open.**

**Next owner actions:** vendor STEP/import and cable routing (A), J6 physical pinout and protected servo supply (B), compile scaffold with ESP-IDF and provide build log (C). Completion of PRs is partial progress, not completion of G1/G2/G3.

## Governance update — 2026-11-20
Repository visibility confirmed **public** through GitHub API. Owner requests PR review and merges **only by `lhcarvalho`**; AI agents must stop after creating PRs. The earlier automatic merge practice is superseded. This change does not imply branch protection has been configured. Current firmware motion-safety implementation is proposed in an unmerged PR; keep issue #7 open until build/bench validation.
