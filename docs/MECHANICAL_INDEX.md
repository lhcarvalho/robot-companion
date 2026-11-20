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
