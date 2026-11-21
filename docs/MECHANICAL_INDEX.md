# Mechanical drawings and CAD index

No manufacturer STEP files, final dimensioned drawings, or print-ready STL are committed at this point.

| File | Intended view | Maturity / warning |
|---|---|---|
| [head_layout_v01.scad](../mechanics/cad/head_layout_v01.scad) | Rounded head, camera and LCD nominal bounding volumes | Proxy feasibility only; assumes offsets and lens |
| [HEAD_LAYOUT_V01.md](../mechanics/cad/HEAD_LAYOUT_V01.md) | Fit calculations, source limits | Camera top clearance only 2.1 mm in one projection |
| [neck_kinematics_v01.scad](../mechanics/cad/neck_kinematics_v01.scad) | Two-servo pan/tilt proposal | No real hardware axle, yoke or cable fatigue model |
| [NECK_DESIGN_V01.md](../mechanics/cad/NECK_DESIGN_V01.md) | MG90S sizing and risk checklist | Torque estimate only |
| [desk_internal_layout_v01.scad](../mechanics/cad/desk_internal_layout_v01.scad) | Desk robot internal envelopes | P4 board 95×70×18 mm is **arbitrary placeholder** |
| [DESK_INTERNAL_LAYOUT_V01.md](../mechanics/cad/DESK_INTERNAL_LAYOUT_V01.md) | Mechanical packaging risks | Torso 125×100×61 mm not frozen |
| [mechanical-envelope.svg](diagrams/mechanical-envelope.svg) | Quick concept for humans/new agents | NOT to scale nor manufacturing plan |

## Coordinate conventions
- `head_layout_v01.scad`: head local axes **X width, Y height, Z depth**, +Z toward face.
- `desk_internal_layout_v01.scad` and `neck_kinematics_v01.scad`: assembly global **X width, Y depth, Z height**, **front = -Y**.
**Important:** Current CAD files are not coordinate-aligned. Treat each as separate exploratory model and convert explicitly when making an integrated assembly.

## Rendering (if OpenSCAD available)
```bash
openscad -o /tmp/head.stl -D 'show_components=false' -D 'show_clearance=false' mechanics/cad/head_layout_v01.scad
openscad -o /tmp/desk.stl mechanics/cad/desk_internal_layout_v01.scad
```
**Warning:** exporting STL here does NOT make a manufacturing-ready design; proxy components and shells may overlap, lack mounting features, or be nonfunctional. Prefer generating 3D previews for concept review.

## Drawing completion criteria
Part number; real model or measurement source; dimensions/tolerances; mount points; cable path; tool access; fastener list; revision; manufacturing process; physical test fit evidence.


## Rendered previews and mesh downloads

Every source `mechanics/cad/<stem>.scad` must have version-matched binary previews in `mechanics/exports/`. Existing versions remain preserved and never silently overwritten. Read [CAD asset policy](CAD_ASSET_POLICY.md).

| Model | Preview (PNG) | 3D Android (GLB) | STL | Design maturity |
|---|---|---|---|---|
| Head v01 | [PNG](../mechanics/exports/head_layout_v01.png) | [GLB](../mechanics/exports/head_layout_v01.glb) | [STL](../mechanics/exports/head_layout_v01.stl) | Proxy; not print-ready |
| Neck v01 | [PNG](../mechanics/exports/neck_kinematics_v01.png) | [GLB](../mechanics/exports/neck_kinematics_v01.glb) | [STL](../mechanics/exports/neck_kinematics_v01.stl) | Proxy; not print-ready |
| **Desk v02 — current concept** | [PNG](../mechanics/exports/desk_internal_layout_v02.png) | [GLB](../mechanics/exports/desk_internal_layout_v02.glb) | [STL](../mechanics/exports/desk_internal_layout_v02.stl) | Official P4 STEP whole-assembly dimensions; mounting/port locations not yet aligned |
| Desk v01 | [PNG](../mechanics/exports/desk_internal_layout_v01.png) | [GLB](../mechanics/exports/desk_internal_layout_v01.glb) | [STL](../mechanics/exports/desk_internal_layout_v01.stl) | Proxy; not print-ready |

To regenerate missing versions locally: `python scripts/render_cad_assets.py`. GitHub Actions generates/commits missing exports on CAD agent branches. If the pipeline cannot push due to settings, do not merge until files exist on the PR branch.

**Export verification (2026-11-20):** Nine initial binary assets (`.png`, `.stl`, `.glb`) were generated and added to this branch by the CAD GitHub Actions job. These are concept-model exports, not manufacturing-approved files.

## Manufacturer STEP verification — 2026-11-20
The exact Waveshare ESP32-P4-Module-DEV-KIT STEP was downloaded and parsed by CadQuery on GitHub Actions; source ZIP SHA-256 and dimensional evidence in [Desk V02 notes](../mechanics/cad/DESK_INTERNAL_LAYOUT_V02.md). Bounding extents are **88.359 × 57.091 × 20.100 mm**. This does not establish connector mounting positions or 3D fit.

## Base coupling concept — 2026-11-21
[Modular base coupling concept V01](../mechanics/BASE_COUPLING_CONCEPT_V01.md) · [SVG 2D view](diagrams/base-coupling-concept-v01.svg). **Conceptual slide cradle/latch with manual plug**; no dimensioned print-ready CAD/mesh, real connector placement, tolerance or locking force claim. Existing V01/V02 CAD models unchanged. A subsequent mechanically measured CAD revision must be created as a new numbered `_vNN.scad` and exported with matched PNG/STL/GLB.
