# RC-MECH-003 — Desk internal packaging / V0.1

**State:** first *parametric volume study*, not a fit-checked or printable assembly. Design target **150 mm total height**, with 105×85×60 mm rounded rectangular head.

## Confirmed hardware
| Part | Evidence | Known fact |
|---|---|---|
| Host | Waveshare ESP32-P4-Module-DEV-KIT, SKU 30560 or kit A 30772 | Onboard ESP32-C6 Wi-Fi, microphone, MX1.25 2-pin speaker interface (8Ω 2W), USB, Ethernet, 40-pin header, CSI camera |
| Screen | Waveshare 2.4inch LCD Module, SKU 18366 | SPI ILI9341, overall module 70.5 × 43.3 mm, active region 48.96 × 36.72 mm, PH2.0 8-pin cable |
| Camera | Waveshare RPi Camera (B), OV5647 | 32 × 32 mm camera PCB; 15-pin CSI cable included in P4-A kit |
| Neck candidate | TowerPro MG90S ×2 | Nominal servo body 22.8 × 12.2 × 28.5 mm; subject to torque and cable tests |

Sources:
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT/Resources-And-Documents
- https://www.waveshare.com/2.4inch-lcd-module.htm
- https://www.waveshare.com/rpi-camera-b.htm
- https://towerpro.com.tw/product/mg90s-3/

## Proposed volume study (all unverified unless marked above)
| Element | Proposed envelope / location | Status |
|---|---|---|
| Head shell | 105 W × 60 D × 85 H mm; center Z = 107.5 mm | Concept |
| Desk torso | 125 W × 100 D × 61 H mm; center Z = 44.5 mm | **Not frozen** |
| Host board + protruding connectors | **95 W × 70 D × 18 H mm** placeholder; PCB Z=29 mm | **NOT MEASURED**; must replace with Waveshare STEP |
| Speaker | Ø40 × 14 mm provisional; facing forward | **NOT SELECTED**; must verify specific 8Ω 2W speaker |
| Power + connectors keepout | 36 × 25 × 18 mm provisional | Does NOT dimension real regulator or protections |
| Desk foot | Ø113 × 14 mm | Concept |
| Head / torso assembly | Target overall height 150 mm | Needs head, neck, fastener fit check |

The torso is intentionally wider than the head because the development board includes bulky ports (RJ45/USB). A **125 mm torso width is NOT proof the board fits**. Do not order a final enclosure until the manufacturer STEP is imported, connectors are measured and ventilation/USB access is considered.

## Mechanical architecture
- LCD and camera remain in **moving head**.
- P4 DEV-KIT and speaker in **fixed torso**; speaker points through a front acoustic grille.
- Pan and tilt servo assembly at neck, no unconstrained 360° swivel.
- Provide rear service door for flashing, USB, cable replacement, and board access.
- **No final removable lower coupling design yet.** Preserve independent interface to future wheel base.
- Desktop is mains/USB powered first; no battery is implied by reserved regulator/connector volume.

## Main risks / actions
1. **CRITICAL: board dimensions missing.** Official STEP ZIP linked by manufacturer; direct download/import not possible in this run. Obtain exact assembly and connector outlines before final CAD.
2. **CRITICAL: moving FFC camera cable.** 15-pin CSI FFC durability, twist radius, retention and strain relief unknown. Design cable loop, test cycles, or reconsider processor/head placement.
3. **HIGH: power.** Use appropriate regulated 5V with current budget for board + servos + LCD + speaker; servo spikes must not brown out camera/MCU.
4. **HIGH: neck/head weight.** Obtain parts mass and calculate real center of gravity/servo torque.
5. **HIGH: desk stability.** Check tipping moment at pan/tilt extremes and cable loads. A fixed foot of Ø113 mm is only a candidate.
6. **HIGH: EMI/thermal/acoustics.** Separate servo power wiring from camera and speaker signal lines; do not block microphone with the loudspeaker or chassis.
7. **HIGH: LCD connection.** SPI cable supplied is 20 cm PH2.0 8 pin; check route through neck and wire strain.
8. **HIGH: safety.** Rounded edges, finger pinch guards, mechanical stops, grounded power design, no exposed battery contacts.

## Acceptance gates before printable pieces
- [ ] Import original Waveshare board STEP and assess fit, connector clearance and service port access.
- [ ] Specify exact speaker SKU and physical/acoustic envelope.
- [ ] Verify mounting holes, screws and board standoffs for all modules.
- [ ] Confirm safe FFC + LCD cable route across ±45° yaw, ±20° pitch with lifecycle test.
- [ ] Measure assembled mass / center of mass, check pitch torque and desk tip resistance.
- [ ] Freeze body envelope and select snap/bolt split scheme with tolerances.
- [ ] Only then produce printable STEP/STL and detailed assembly drawing.

## CAD
`mechanics/cad/desk_internal_layout_v01.scad`

Shows *proxy* solids for head, torso, board, speaker, power clearance, foot and neck. The axes are X=width, Y=depth, Z=height, with front at -Y. Default values are exposed for revisions. Use OpenSCAD to inspect shape; do NOT assume its bodies are printable or geometrically collision-free.
