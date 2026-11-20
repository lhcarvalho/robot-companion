# Robot Companion

**Status:** engineering concept / first CAD packaging studies. **Not yet built or physically validated.**

A modular hobby **AI companion robot** designed for a desk and, later, a detachable wheeled base for supervised interaction at home. Friendly, expressive rounded-square face, 2-axis head, compact local vision, and optional higher-quality speech/intelligence via an RTX 3080 PC or cloud API. The robot must retain basic sensing/reactions and movement safety offline.

## Read this first

| Document | Purpose |
|---|---|
| [Product brief](docs/PROJECT_BRIEF.md) | Objective, user experience, product constraints and MVP success |
| [Current status / resume guide](docs/STATUS.md) | **Where we are, what is real and next action** |
| [Roadmap](docs/ROADMAP.md) | Gated milestones and priorities |
| [Decision register](docs/DECISIONS.md) | Selected vs provisional vs unresolved choices |
| [Open questions and risks](docs/OPEN_QUESTIONS.md) | Blockers and required evidence |
| [System architecture](docs/ARCHITECTURE.md) | Hardware/software boundaries and interactions |
| [BOM](bom/BOM.csv) | Item-by-item selection and verification states |
| [CAD / drawings index](docs/MECHANICAL_INDEX.md) | Models and diagrams with maturity notes |
| [Tasks / agent lanes](docs/TASKS.md) | Parallel work packages and ownership |
| [Agent onboarding](AGENTS.md) / [Contribution guide](CONTRIBUTING.md) | How AI agents and people contribute without conflicts |

## At a glance
- **Compute:** Waveshare ESP32-P4-Module-DEV-KIT with ESP32-C6 connectivity; kit A with matching OV5647 MIPI-CSI camera/cable is a candidate.
- **Face:** Waveshare 2.4-inch ILI9341 SPI LCD, OV5647 camera above display.
- **Form:** rounded-square head, proposed 105×85×60 mm; full robot target 150 mm.
- **Actuation:** pan/tilt neck, 2 × MG90S candidate servos; fixed electronics in torso.
- **Modes:** USB-powered desk MVP first; future mobile base with wheels, encoders, obstacle/cliff sensing and safety layer.
- **Local/offline:** expressions and appropriate lightweight AI perception when validated. **No realistic ChatGPT-level offline conversation on P4 alone.**

## Current build maturity
Four previous PRs produced component selections and OpenSCAD **bounding-volume concepts**, not completed fabrication files. Vendor STEP/actual cable clearance, SPI pin allocation, proper power system, hardware tests and final mechanical structure are outstanding. Read [STATUS](docs/STATUS.md).

## Project diagrams
[System architecture](docs/diagrams/system-architecture.svg) · [Mechanical envelope](docs/diagrams/mechanical-envelope.svg).

## For a new model arriving with zero context
Open [AGENTS.md](AGENTS.md), follow its reading order, and consult GitHub Issues/PRs before selecting a work package. **Do not rely on earlier conversations.** The repository should always contain enough validated context to resume work.

## Working method
ChatGPT for research, product decisions and technical review; Codex/agents for scoped implementation, tests and CAD. Branch -> PR -> verified merge. Source files and evidentiary logs live here, not solely in chat.
