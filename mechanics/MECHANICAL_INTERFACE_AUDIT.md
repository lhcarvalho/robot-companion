# Mechanical interface audit — issue #5, revision 0.2

**Status: DOCUMENTARY ANALYSIS ONLY.** Manufacturer STEP/model not imported. No physical hardware measured, no print-ready geometry.

## Evidence reviewed
- Waveshare P4 kit documentation: https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT
- Official resources: https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT/Resources-And-Documents
- Vendor STEP/drawing archive: https://files.waveshare.com/wiki/ESP32-P4-Module-DEV-KIT/ESP32-P4-Module-DEV-KIT-20250427.zip (published by vendor, **download unavailable** in this execution)
- Prior concepts: `mechanics/cad/{HEAD_LAYOUT_V01,NECK_DESIGN_V01,DESK_INTERNAL_LAYOUT_V01}.md`.

## Constraints known from existing design (mm)
| Item | Current value | Type |
|---|---:|---|
| Head width × height × depth | 105 × 85 × 60 | concept, NOT frozen |
| LCD PCB width × height | 70.5 × 43.3 | module catalog nominal |
| LCD visible area | 48.96 × 36.72 | module catalog nominal |
| OV5647 camera PCB | 32 × 32 | module catalog nominal |
| P4 host board envelope | UNKNOWN | **blocker** |
| Moving camera lens and connector envelope | UNKNOWN | **blocker** |
| Current torso | 125 × 100 × 61 | proxy, NOT approved |
| Pan/tilt travel | ±45° / ±20° | target, NOT validated |

## Geometry calculations (reproducible)
With head height 85 mm and nominal centered 32+43.3 mm stacked camera and LCD boards, vertical free space is `85-32-43.3=9.7 mm` **before** shell margins, fasteners, connectors and lens. Therefore front projection alone is insufficient to prove fit: boards must be offset in depth, rotated, or head dimensions revised. Existing concept uses depth overlap; verify **3D collision** only after exact models.

For nominal 2.4-mm shell wall, cavity bounding box would be `100.2 × 80.2 × 55.2 mm`, before corner radii, bosses, removable panel, cabling and structural keepouts. A simple axis-aligned bounding box is not proof that a part clears rounded corners.

The P4 board in torso remains an **unmeasured stand-in** (95×70×18 mm in a prior SCAD). Do not use for mounting holes or final purchase.

## Required vendor measurements
- [ ] Get STEP archive; record download date, file names, revision and checksum; comply with vendor terms.
- [ ] Use STEP or dimensioned drawing to extract main PCB outline, all four mounting-hole coordinates, USB-A/USB-C/Ethernet heights and service connector keepouts.
- [ ] Obtain exact LCD PCB/glass/cable socket holes, alignment of active region, and screen-stack depth.
- [ ] Measure OV5647 lens center, lens barrel depth, PCB mounting points, mating FFC orientation.
- [ ] Obtain moving FFC *flex-rated* cable specification (minimum bend radius, cycle count, signal integrity), or redesign processor/camera location.

## Moving neck: three solutions to evaluate
1. **FFC in generous articulated loop:** lowest architectural change, but requires rated cable and repetitive movement tests; ordinary flat-flex is not proven for this purpose.
2. **Move P4 into head:** reduces relative CSI motion but increases neck torque, heat, head width and needs different high-current cable path; may exceed 15-cm target.
3. **Constrain neck movement / move camera independently:** possible fallback, but hurts intended face-tracking behavior.

**Recommendation:** do not choose any final solution before physical measurements and simple neck cycling rig. Use short travel and explicit mechanical hard stops.

## Required acceptance for issue #5
Exact manufacturer STEP/drawing available and revision recorded; interference-free complete head+torso volume study at all movement extremes; camera and display harness path proven at defined bend radius, plus explicit risk signoff. This document only completes the *source discovery and gap assessment* subtask.

## Handoff
Agent A owns `mechanics/`. Issue #5 remains open. Electrical work is in #6; firmware in #7.
