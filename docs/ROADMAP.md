# Roadmap and gated milestones

This is a **dependency-ordered**, not time-promised, plan. Gate completion requires linked evidence; tasks can be worked in parallel before gate completion.

| Gate | Scope | Definition of done | Current |
|---|---|---|---|
| G0 Context | Repo documentation, inventory, workflow, task ownership | New agent can continue without chat history | In progress as of this documentation PR |
| G1 Hardware interface validation | Exact board/camera/LCD mechanical docs, IO map, power, speaker SKU | Vendor evidence and mechanical package; compatibility matrix; purchase-ready provisional BOM | Open |
| G2 Bench bring-up | P4+C6, screen SPI, CSI camera, audio and Wi-Fi | Versioned ESP-IDF build, logs, photos/measurements and reproducible steps | Not started |
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
