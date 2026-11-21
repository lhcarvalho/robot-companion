# Project status — 2026-11-20

**Phase:** concept engineering / packaging feasibility, **NOT** assembly-ready.
**Last merged technical milestones:** official Waveshare STEP retrieved and measured (PRs #19/#22), preliminary P6 pin map (#21), SPI ILI9341 driver compiles (#20), Waveshare kit BOM/first power checklist (#23). CAD desk V02 (#24) merged with matching PNG/STL/GLB generated and verified.
**No physical component installation, electrical bench test, validated complete CAD assembly, motor calibration, or printed enclosure is recorded in this repository. The baseline firmware DOES compile in GitHub Actions for ESP32-P4; physical bring-up is still untested.** If any happened elsewhere, require evidence before updating status.

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
- **P4 STEP whole-assembly bounds** measured: 88.359 × 57.091 × 20.100 mm. Actual mounting hole coordinates, connector clearance/orientation and physical revision remain unverified. Old 95×70×18 mm V01 proxy is superseded for board volume planning.
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

**Next owner actions:** vendor STEP/import and cable routing (A), pinout and protected servo supply (B), then flash/bench test and camera/LCD/audio integration (C). Baseline cross-compilation passed, but does not complete G1/G2/G3.

## Governance update — 2026-11-20
Repository visibility confirmed **public** through GitHub API. **Superseded governance note:** project-owner-authorized agents operating under `lhcarvalho` may review and merge routine PRs after checks. Other accounts may open PRs but should have no write/merge rights. This is a process rule, not proof of enforced branch protection. Firmware motion-safety PR #13 was merged after successful CI; ESP-IDF hardware integration remains untested and issue #7 stays open.

## Verified checkpoint — 2026-11-20 (PRs #15–#17)
- **CAD #15**: GitHub Actions generated and committed 3 PNG + 3 STL + 3 GLB for the V01 models. Preview and file-preservation checks passed. See `mechanics/exports/`, `docs/CAD_ASSET_POLICY.md` and `docs/MECHANICAL_INDEX.md`.
- **Firmware #16**: ESP-IDF v5.5 / esp32p4 cross-compile passed in GitHub Actions [run 44801017376](https://github.com/lhcarvalho/robot-companion/actions/runs/44801017376). No flash or bench test.
- **Mechanical #17**: added head 2D envelope calculation and assembly acceptance plan. No vendor STEP import, moving-cable fatigue test or confirmed 3D fit. Issue #5 remains open.
- **Electrical #6**: exact pin/rail verification and regulated servo power still open; do not wire against provisional assignments.
- **All CAD assets remain exploratory**, not validated printable parts. Next: physical board models, reliable CSI FFC neck design, GPIO/power engineering and actual hardware bring-up.

## November 20, 2026 — STEP, P6, ILI9341 update
- PR [#19](https://github.com/lhcarvalho/robot-companion/pull/19): vendor ZIP retrieved, CRC and SHA-256 verified; includes 29.86 MB STEP plus DXF/PDF. No manufacturer CAD binaries redistributed.
- PR [#22](https://github.com/lhcarvalho/robot-companion/pull/22): OpenCascade/CadQuery import successfully measured overall STEP bounding extents **88.359 × 57.091 × 20.100 mm**. [CI measurement](https://github.com/lhcarvalho/robot-companion/actions/runs/44850219227). These are not PCB-hole or port-mount dimensions and do not prove fit.
- PR [#21](https://github.com/lhcarvalho/robot-companion/pull/21): preliminary 40-pin P6 schematic contacts and provisional SPI/servo signals. Actual physical header orientation and GPIO collision checks remain open.
- PR [#20](https://github.com/lhcarvalho/robot-companion/pull/20): `robot_display` ILI9341 driver compiled with ESP-IDF v5.5 on the P4; **no display was connected**. GPIO pin allocation and BL circuit unverified, driver only initializes on explicit call.
- PR [#23](https://github.com/lhcarvalho/robot-companion/pull/23): BOM now records Waveshare KIT-A bundles camera/FFC and 8Ω 2W speaker, plus pre-power checklist and BOM CI.
- PR [#24](https://github.com/lhcarvalho/robot-companion/pull/24): desk layout V02 uses measured STEP whole-assembly envelope and preserves V01; PNG/STL/GLB generated and PR merged.

**Next technical priorities:** real board mounting holes/connector clearance, verified flex-rated CSI cable in moving neck, P6 physical pin-1 and power loads, then LCD/camera/audio bench tests. Issues #5/#6/#7 remain open. No physical hardware tests recorded.

## Product architecture update — 2026-11-21
**New approved decision:** no main battery in reusable electronics/head core. Each interchangeable base provides its own regulated energy solution; bench stand starts with a cable and current-limited supply. Desktop/mobile bases can differ in battery capacity or chemistry provided their interface is properly regulated and protected. See [ADR-001](adr/ADR-001-modular-base-power.md). Actual mating connector/pinout, current, charger and power-path behavior are **not selected or tested**. CAD V01/V02 remains historical concept only.

## Modular attachment concept — 2026-11-21
Candidate design: structural slide-on rail/cradle + positive latch, accessible manual keyed electrical harness for initial bench/desk prototypes, no hot swapping. Frequent consumer base swapping will require a separately qualified high-cycle blind-mate/other connector. See [concept V01](../mechanics/BASE_COUPLING_CONCEPT_V01.md) and [SVG](diagrams/base-coupling-concept-v01.svg). **No dimensional CAD, source pinout, physical tests, approved connector or batteries.**
