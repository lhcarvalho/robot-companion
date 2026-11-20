# Contributing and collaboration — humans and multiple AI agents

## Branching and PRs
- `main` is the shared, stable source of truth.
- Every task uses a dedicated `agent/<lane>/issue-<number>-<topic>` branch from fresh main. Example: `agent/mech/issue-12-board-step`.
- Before starting: check current issues/PRs, comment on issue with intended file ownership and blockers. Avoid overlapping edits.
- Keep PR small and scoped; reference its issue; include **what changed / sources / validation / assumptions / risks / follow-up**.
- **Never force-push to main; never direct commit to main as an agent.** Merge PRs after checks and conflicts have been resolved.
- **Owner-authorized agents using GitHub identity `lhcarvalho` may review and merge PRs autonomously after checks pass; no separate approval is required for routine valid PRs.** External contributors should fork and propose PRs, not receive write access. Do not bypass branch protection.

## Parallel-agent protocol
1. Split into mechanical, electrical/BOM, firmware/test lanes, coordinate via issues.
2. Claim issue and declared files; if cross-lane modification needed, ask for a specific interface decision in issue and notify other agent there.
3. Work only in your branch, update from latest main before PR/merge.
4. Avoid having three agents edit `README.md`, `AGENTS.md`, `docs/STATUS.md` concurrently. Coordinator reconciles handoff docs after merging lane PRs.
5. If one PR merged, remaining branches must refresh and resolve conflicts rather than assuming their branches include the update.
6. Verification state must be explicit: doc-reviewed, compile-tested, bench-tested, fit-tested, field-tested. A mockup is not proof of physical compatibility.

## Review checklist
- [ ] Specific issue and acceptance criteria referenced
- [ ] No fabricated datasheets, SKU, prices, CAD STEP, test logs
- [ ] Pinouts / cable dimensions backed by official schematic or real measurement
- [ ] Hardware safety and privacy impact documented
- [ ] Build/render/test commands and actual results provided
- [ ] Changes to hardware decisions explained in `docs/DECISIONS.md`
- [ ] Coordinator updated `docs/STATUS.md` and `docs/OPEN_QUESTIONS.md`
- [ ] No secrets, tokens, face templates, private images or biometric data committed

## Automation later
CI should validate Markdown links, CSV format, OpenSCAD syntax and ESP-IDF firmware when that code exists. Branch protection, CODEOWNERS and required reviews can be added when collaborators grow; do not claim these are currently enabled.

## Public contribution policy (effective 2026-11-20)
The repository is public. Anyone can read or fork and submit a PR. Review and merge are reserved for **GitHub account @lhcarvalho, including agents explicitly authorized by that account**. Other GitHub accounts can submit PRs but must not get write/merge permission. Before an automated merge, check CI, conflicts and scope; with failing checks, high-risk/security-sensitive changes or missing validation, do not merge. Never claim branch protection or CODEOWNERS are configured unless verified in GitHub settings. GitHub's review system generally disallows formal approval of one's own PR; owner-authorized agents may merge without self-approval only when repository rules allow it.


## OpenSCAD contribution requirements
A new CAD revision must have a **new filename** (`_v01`, `_v02`, etc.); do not replace or delete older version files. Every revision must include PNG, STL and GLB assets in `mechanics/exports/`, with the same stem. Update `docs/MECHANICAL_INDEX.md` and clearly state whether physical fit and vendor dimensions were validated. See [docs/CAD_ASSET_POLICY.md](docs/CAD_ASSET_POLICY.md). CI validates asset presence/format and prevents modifications of archived SCAD/exports.
