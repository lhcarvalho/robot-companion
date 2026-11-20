# Contributing and collaboration — humans and multiple AI agents

## Branching and PRs
- `main` is the shared, stable source of truth.
- Every task uses a dedicated `agent/<lane>/issue-<number>-<topic>` branch from fresh main. Example: `agent/mech/issue-12-board-step`.
- Before starting: check current issues/PRs, comment on issue with intended file ownership and blockers. Avoid overlapping edits.
- Keep PR small and scoped; reference its issue; include **what changed / sources / validation / assumptions / risks / follow-up**.
- **Never force-push to main; never direct commit to main as an agent.** Merge PRs after checks and conflicts have been resolved.
- **Only `lhcarvalho` reviews/approves and merges PRs. Agents must not call the merge endpoint or bypass branch protection, even when GitHub credentials technically allow it.** External contributors should fork and propose PRs, not receive write access.

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
The repository is public. Anyone can read or fork and submit a PR. Review and merge are **reserved for human owner @lhcarvalho**. Never claim CODEOWNERS/branch protection are enabled until verified in GitHub settings. Do not treat a mergeable PR as permission for an AI agent to merge it.
