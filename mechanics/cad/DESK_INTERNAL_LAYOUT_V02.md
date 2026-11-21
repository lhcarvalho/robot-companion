# RC-MECH-003 — Desk layout V02 using measured board STEP extents

**Source:** Waveshare ESP32-P4-Module-DEV-KIT official STEP, dated 2025-04-27.
**Acquisition:** GitHub Actions run [44849989183](https://github.com/lhcarvalho/robot-companion/actions/runs/44849989183).
**STEP parsing:** CadQuery + OpenCascade in GitHub Actions run [44850219227](https://github.com/lhcarvalho/robot-companion/actions/runs/44850219227).

## Manufacturer assembly axis-aligned bounding box

| Vendor STEP axis | Minimum (mm) | Maximum (mm) | Extent (mm) |
|---|---:|---:|---:|
| X | -0.353236 | 88.005832 | **88.359069** |
| Y | -1.081719 | 56.009306 | **57.091026** |
| Z | -3.900000 | 16.200000 | **20.100000** |

ZIP SHA-256: `c626e82afea53b75c2f02559055fedb08eb773cd18e5089f544d19f28e5c0506`. Contains one STEP, DXF and PDF. Model extents come from the entire STEP imported as CAD geometry, **not a hand-measured board outline**.

## Changes from V01

- Preserve `desk_internal_layout_v01.scad` and V01 exports unchanged.
- Introduce `desk_internal_layout_v02.scad`, using whole-assembly `88.3591 × 57.0910 × 20.1000` bounding proxy in place of **unverified 95×70×18 mm**.
- Current board translation, posture and assumed torso `125 × 100 × 61 mm` remain **design hypotheses**.
- The model draws a single board assembly box; detailed USB/Ethernet/camera and connector keepouts are not represented.
- PNG/STL/GLB will be generated as assets with matching V02 stem by GitHub Actions, preserving V01 assets.

## What this does NOT prove

The source STEP axes and mounting coordinates haven't yet been aligned to the actual robot coordinate frame. No bolt-hole dimensions, port openings, service panel clearance, thermal ventilation or cable bend space is checked. A single 3D bounding box is **not a collision/assembly analysis**, and overlapping dummy blocks in the concept CAD are expected.

## Next mechanical engineering gates

1. Extract **PCB-specific** mounting-hole centers and the exact connector locations from STEP and manufacturer DXF.
2. Transform the imported vendor STEP into torso coordinates and check collisions for every service and cable envelope.
3. Obtain exact CSI FFC bend/cycle specification and validate motion across ±45° pan and ±20° tilt.
4. Estimate assembled head mass and center of mass; size the yoke and servo/bearing accordingly.
5. Design V03 split shell and mounting bosses, then generate new PNG/STL/GLB.
6. Real test print and fit are mandatory before marking this assembly print-ready.

**Status:** V02 is a volume study; not a finished model for printing.
