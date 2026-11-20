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
- If tasked with implementation, make a small scoped branch and PR. **Repository is public; all merges are HUMAN-ONLY by GitHub user `lhcarvalho`. AI agents MUST NOT merge PRs, approve their own PRs or push directly to `main`, even if connector permissions technically permit it.**
- Document specific tests run and failures honestly. If hardware/tools unavailable, state "not tested" and leave validation gate open.
- Update docs where behavior/decisions changed, preferably via coordinator to avoid 3-agent merge conflicts.
- Respect lanes and issue ownership in `docs/TASKS.md`; ask only when a truly new product decision needs owner input.
- Keep source-controlled CAD parametric and explicitly annotate assumed dimensions. Commit original vendor files only with licenses/usage rights verified, otherwise link to them.
- Do not start a mobile SLAM implementation before desk mechanics and electrical safety gates.

## Current task suggestion
Prioritize G1: board STEP + physical connectors, moving camera FFC route, electrical pin map and power. Consult live issues and PRs before choosing the first available item.
