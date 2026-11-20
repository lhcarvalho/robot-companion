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

## Current next action
Acquire/import official dimensioned STEP of Waveshare board, camera and LCD drawings; determine actual 3D collision-free placement and moving-cable route, while an independent electrical agent verifies GPIO/power allocation. See [ROADMAP](ROADMAP.md) and [TASKS](TASKS.md).

## Handoff recipe for a model with zero chat history
1. Read root [README](../README.md) and [AGENTS.md](../AGENTS.md).
2. Read this file, [PROJECT_BRIEF](PROJECT_BRIEF.md), [DECISIONS](DECISIONS.md), [OPEN_QUESTIONS](OPEN_QUESTIONS.md), [ROADMAP](ROADMAP.md).
3. Read linked hardware/CAD sources. Inspect the actual files; do not infer their content from summaries.
4. Check open issues and PRs before choosing a task; claim a narrow task in an issue and use your own branch.
5. Do not change approved architecture silently. Attach tests/evidence, update this status and open questions in the PR.
6. No hardware fit claim without manufacturer drawings or measured artifact; no working firmware claim without logs.
