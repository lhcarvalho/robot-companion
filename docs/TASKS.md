# Concurrent agent work queue

**Coordination:** GitHub Issues are the task ownership ledger. This file is a stable decomposition, **not a claim that an issue is already assigned**. A working agent must check live issues and open PRs before editing.

## Recommended 3-agent split
| Lane | Agent role | Exclusive primary paths (unless arranged in issue) | Deliverable |
|---|---|---|---|
| A | Mechanical / CAD | `mechanics/`, `docs/hardware/mechanical-interfaces.md` | STEP import, clearance, neck and head packaging |
| B | Electrical / BOM | `electronics/`, `bom/`, `docs/hardware/pinout.md` | GPIO allocation, power budget, parts sourcing with provenance |
| C | Embedded / test | `firmware/`, `tests/` | ESP-IDF scaffolding, drivers, compile/log evidence |

Coordinator/maintainer owns **`README.md`, `AGENTS.md`, `docs/STATUS.md`, `docs/DECISIONS.md`, `docs/ROADMAP.md`, `docs/OPEN_QUESTIONS.md`** and reconciles contributions. Other agents may propose updates to these in PR but must keep changes small and flag potential merge conflicts.

## Ready tasks
- A1: obtain exact Waveshare P4 board STEP/drawings; replace torso placeholder; document port and hole clearance.
- A2: obtain exact camera/lcd fixing dimensions; design first collision-aware head layout.
- A3: evaluate cable flex/FFC routing across 2-DOF neck, alternative architecture and servo support.
- B1: verify full pin allocation from schematic; document conflicts with camera/USB/SDIO/C6.
- B2: select speaker and regulated servo power design, fuse/protection; budget peaks.
- B3: BOM with exact SKU, quantities, vendor datasheet, purchase/verification state.
- C1: pin ESP-IDF version and create minimal P4+C6 firmware project with build steps.
- C2: create test interfaces for SPI LCD, CSI camera and concurrent operation (no unmeasured claims).
- C3: document local AI ESP-DL/ESP-WHO sample compatibility and safety isolation.

## Task lifecycle
`backlog -> claimed -> in-progress -> PR -> verified -> done`. Post on an issue before beginning: "Claim: lane X, branch agent/X/issue-N-short-name, files...". Keep status comments when blocked; never overwrite another agent's ongoing files. Review cross-lane dependencies explicitly.

## Dependencies
A1 before final A2/print-ready drawings. B1 before C2 GPIO choices. B2 before powered servos. A3 before final G3. G1 before irreversible purchases and custom manufacturing.
