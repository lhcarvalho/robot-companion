# Roadmap and gated milestones

This is a **dependency-ordered**, not time-promised, plan. Gate completion requires linked evidence; tasks can be worked in parallel before gate completion.

| Gate | Scope | Definition of done | Current |
|---|---|---|---|
| G0 Context | Repo documentation, inventory, workflow, task ownership | New agent can continue without chat history | Created in documentation PR; confirm after merge |
| G1 Hardware interface validation | Exact board/camera/LCD mechanical docs, IO map, power, speaker SKU | Vendor evidence and mechanical package; compatibility matrix; purchase-ready provisional BOM | Open |
| G2 Bench bring-up | P4+C6, screen SPI, CSI camera, audio and Wi-Fi | Versioned ESP-IDF build, logs, photos/measurements and reproducible steps | Baseline cross-compilation passed; hardware bring-up NOT started |
| G3 Head/neck engineering | Collision-checked CAD, servos, cable routing, brackets | Dimensioned files, torque/CoM analysis, cyclic cable stress plan | Mockups only |
| G4 Desk physical MVP | Fabrication + safe articulated face/vision/audio | Physical prototype demonstrations and failures documented | Not started |
| G5 Offline behaviors | Face/people detection/enrollment, wake word where supported, reactions | Measured precision, privacy deletion, fallback without Wi-Fi | Not started |
| G6 Optional AI gateway | PC RTX 3080 + cloud APIs; voice dialogue | Authenticated connections, latency/failure tests | Not started |
| G7 Mobile base | Encoders, motors, wheels, proximity/cliff/contact detection, battery | Low-speed safe navigation in controlled area | Not started |
| G8 Advanced navigation | LiDAR, odometry, localization/SLAM, room travel | Independent safety layer, measured reliability | Optional later |

## Immediate prioritized work packages (can run in parallel)
- **Mechanical A:** get board/vendor mechanical files, replace proxy dimensions and design connector/service clearance; investigate FFC neck alternatives.
- **Electrical B:** build pinmap/rail/current/spec matrix including SPI LCD and CSI camera; select power, interface plan; no unsupported PWM claims.
- **Software C:** scaffold ESP-IDF, build minimal board and SPI/CSI smoke tests *without claiming hardware validation*.
- **Product/QA coordination:** integrate results, owner decisions, evidence and PRs.

See [TASKS](TASKS.md) and [CONTRIBUTING](../CONTRIBUTING.md). Do not claim milestones completed based solely on file creation.

## Workstreams checkpoint — 2026-11-20
Three independent branches and PRs (#9 mechanical, #10 electrical, #11 firmware) merged partial deliverables. They did **not** pass G1 or G2: no board STEP import, no verified physical pinout, no currents measured and no firmware build performed. Continue the existing Issues #5–#7 in follow-up branches, preserving lane ownership.

## Build/CAD automation checkpoint — 2026-11-20
- Baseline C firmware compiles for ESP32-P4 using ESP-IDF v5.5 (PR #16). Physical validation remains pending.
- CAD exports (PNG, STL, GLB) and historical version preservation enabled (PR #15). For every new SCAD revision, commit assets with identical versioned stem.
- A 2D head envelope check was added in PR #17. It does **not** establish 3D mounting compatibility.

## Verified stage G1 progress — 2026-11-20
- Manufacturer board CAD ZIP available and imported in GitHub Actions; the whole model envelope was measured. **Mounting-holes, ports and neck cable reliability not verified**.
- P6 schematic contacts documented, but physical revision/orientation and GPIO electrical compatibility not signed off.
- ESP-IDF target compile now includes explicit opt-in ILI9341 driver (PR #20); **peripheral hardware bring-up has not happened**.
- Kit A includes camera, FFC and speaker; no extra duplicate buy implied. BOM purchase state remains not-recorded.
- Desk V02 with official STEP-derived bounding extent and matched PNG/STL/GLB passed CAD export and merged via PR #24.

**G1 not complete. G2 bench testing not complete. G3 printed/mechanical assembly not complete.**
