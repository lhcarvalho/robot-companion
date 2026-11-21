# AGENTS.md — entrypoint for any new agent

**Read this BEFORE making edits. No chat history is needed.** This repository is the single source of truth for a modular ESP32-P4 + ESP32-C6 companion robot.

## Mandatory startup order
1. [README.md](README.md)
2. [docs/PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md)
3. [docs/STATUS.md](docs/STATUS.md)
4. [docs/DECISIONS.md](docs/DECISIONS.md)
5. [docs/ROADMAP.md](docs/ROADMAP.md)
6. [docs/OPEN_QUESTIONS.md](docs/OPEN_QUESTIONS.md)
7. [docs/TASKS.md](docs/TASKS.md) and [CONTRIBUTING.md](CONTRIBUTING.md)
8. **Read actual domain files** under `docs/hardware/`, `mechanics/cad/`, `bom/`; do not assume summaries replace source files.
9. Query open GitHub Issues/PRs and select a non-overlapping task.

## Non-negotiable engineering truth
- Product selection and manufacturer catalog facts are not full electrical/mechanical validation.
- The current OpenSCAD files are **exploratory volume mockups**, not functional parts or print-ready manufacturing files.
- Motherboard `95×70×18` mm, speaker and regulator envelopes are placeholders; don't carry them into purchasing or final manufacturing.
- Camera 15-pin CSI FFC crossing a moving neck is a **critical unsolved risk**.
- Treat LCD SPI GPIO proposals as provisional until cross-checked against the Waveshare schematic, C6/CSI and actual runtime.
- Two MG90S servos are candidates, NOT confirmed torque-safe.
- No physical measurements, fit tests, firmware builds or electronics test logs are in the repo as of 2026-11-20.
- Never invent prices, filenames, sources, compatible pinouts, successful tests, CAD drawings or specific child's biometrics.
- No external LLM/network dependency for motor safety; enforce failsafe locally. Sensitive child-related camera data should be opt-in and stay local by default.

## Execution policy
- If tasked with implementation, make a small scoped branch and PR. **Public repository: project-owner-authorized agents operating through GitHub identity `lhcarvalho` MAY review and merge PRs autonomously after applicable checks and conflict review. Other GitHub users may view, fork, and open PRs but MUST NOT receive merge/write permission. No agent may push directly to `main` or bypass protections.**
- Document specific tests run and failures honestly. If hardware/tools unavailable, state "not tested" and leave validation gate open.
- Update docs where behavior/decisions changed, preferably via coordinator to avoid 3-agent merge conflicts.
- Respect lanes and issue ownership in `docs/TASKS.md`; ask only when a truly new product decision needs owner input.
- Keep source-controlled CAD parametric and explicitly annotate assumed dimensions. Commit original vendor files only with licenses/usage rights verified, otherwise link to them.
- Do not start a mobile SLAM implementation before desk mechanics and electrical safety gates.

## Current task suggestion
Prioritize G1: board STEP + physical connectors, moving camera FFC route, electrical pin map and power. Consult live issues and PRs before choosing the first available item.


## Mandatory CAD versioning and mobile previews
Whenever creating or changing a model in `mechanics/cad/`, **do not overwrite older versions**: use the next sequential `_vNN.scad` filename. Generate and commit `mechanics/exports/<stem>.png`, `<stem>.stl` and `<stem>.glb` for each source revision. Use `python scripts/render_cad_assets.py`, update `docs/MECHANICAL_INDEX.md`, and comply with [CAD_ASSET_POLICY](docs/CAD_ASSET_POLICY.md). The GitHub Actions pipeline auto-generates missing files on agent branches and checks PRs; never merge if required exports are missing. Conceptual STL ≠ validated printable part.

## New architecture constraint — modular power (ADR-001)
The shared head/electronics core contains **no main battery**. Bench prototype uses cable/regulated source; desk and mobile base variants supply their own protected energy. No agent should embed a battery in the shared core, select an unvalidated connector, or treat charging while running/live hot-swapping as approved. Consult [ADR-001](docs/adr/ADR-001-modular-base-power.md) and [interface requirements](electronics/BASE_INTERFACE_V01.md). New geometry revisions must follow immutable CAD+PNG/STL/GLB rules.

## Base attachment concept V01
Read [mechanics/BASE_COUPLING_CONCEPT_V01.md](mechanics/BASE_COUPLING_CONCEPT_V01.md) before designing the interface. Initial concept is slide rails + positive latch + manually accessible keyed plug, *not* pogo/magnets or proven blind-mate. Molex Micro-Fit 3.0 typically has only 30 mating cycles; not a high-cycle base-change interface. No mechanical dimensions, current rating, final wiring or validated printable component are approved. Do not call the explanatory SVG printable CAD. Future _vNN SCAD must preserve old models and include generated PNG/STL/GLB.
