# CAD previews and versioning — project policy

**Every versioned OpenSCAD source must have a preview PNG, STL and GLB committed to this repository.** The outputs are exploratory models until the corresponding technical drawing has passed the assembly and mechanical validation gates. An STL file is **not** a declaration that the part is print-ready.

## Versioned immutable files
- CAD source: `mechanics/cad/<component>_v01.scad`, then `_v02.scad`, etc.
- Generated assets: `mechanics/exports/<component>_v01.png`, `.stl`, `.glb`.
- **Never delete or silently overwrite an old revision.** On a changed geometry, create the next named revision and keep all historical files.
- Human-readability: link to latest recommended revision from `docs/MECHANICAL_INDEX.md` and preserve direct links to old versions.
- All outputs are deterministic-source artifacts, not manufacturer STEP files. Where parts are provisional, preserve that warning in the relevant documentation.
- When historical source geometry is defective, make a new revision; describe the fix. Do not rewrite history.

## Agent workflow
1. Read `AGENTS.md`, `docs/STATUS.md`, `docs/MECHANICAL_INDEX.md`.
2. Edit **a new** versioned SCAD filename; record changes to dimensions, assumptions and collision constraints.
3. Run `python scripts/render_cad_assets.py mechanics/cad/<name>_vNN.scad` (requires openscad, xvfb-run, trimesh).
4. Commit corresponding PNG/STL/GLB under `mechanics/exports/`, and update the index.
5. Open PR with a picture link and list of checks. For automated branches, CI can generate/commit missing exports; review the resulting commits before merging.
6. Never represent a preview or an untested STL as a mechanically validated deliverable.

## Automation
- `.github/workflows/cad-exports.yml` runs when an agent pushes a CAD-related branch, exporting missing models and committing binaries back to that branch using GitHub Actions token (subject to repository workflow permissions).
- It also validates that every SCAD has the 3 matching exports and checks PNG/GLB/STL formats on PRs.
- Current models are feasibility mockups. The official board STEP, servo fixing geometry, moving camera FFC reliability, and final fit remain open.
