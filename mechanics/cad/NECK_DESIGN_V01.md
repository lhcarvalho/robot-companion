# RC-MECH-002 — Pan/tilt neck V0.1

**State: concept selected for prototyping, NOT ready for print or purchase.**

## Mechanism
Two position servos: vertical yaw (pan) at torso interface, horizontal pitch (tilt) through a two-sided yoke. Tentative software travel pan **±45°**, tilt **±20°**. These are design targets, not validated clearances. No slip ring; keep moving cable path short with hard end stops.

## Servo candidate
**TowerPro MG90S** metal gear servo ×2. Manufacturer https://towerpro.com.tw/product/mg90s-3/

| Parameter | Manufacturer specification |
|---|---|
| Body | 22.8 × 12.2 × 28.5 mm |
| Mass | 13.4 g |
| Stall torque | 1.8 kgf·cm at 4.8V; 2.2 kgf·cm at upper specified voltage |
| Speed | 0.10 sec/60° at 4.8V |
| Connector | 3-wire hobby servo |

Stall rating is NOT a continuous torque rating. Genuine maker and clone dimensions may vary. FEETECH FS90MG is a possible alternate but requires a separate dimensional review.

## First-order pitch torque sensitivity
Gravitational torque in kgf·cm ≈ moving head mass in kg × horizontal COM offset in cm.

| Assumed moving mass | COM offset | Gravity torque | 3× provisional margin |
|---|---|---|---|
| 0.15 kg | 1 cm | 0.15 kgf·cm | 0.45 kgf·cm |
| 0.25 kg | 2 cm | 0.50 kgf·cm | 1.50 kgf·cm |
| 0.35 kg | 3 cm | 1.05 kgf·cm | 3.15 kgf·cm |

The last case exceeds nominal MG90S stall torque. The pitch axis should be near the assembly COM and supported on the opposite side by an idler/bearing. Measure actual complete moving mass before committing to MG90S.

## Electrical
- Power servos from an **independent, fused/protected ~5V rail**, NOT the P4 3.3V rail. Share ground with controller. A dedicated regulator rated >= 2 A is a **starting design allowance**, not a measurement or approved final supply.
- Generate positional servo pulses with P4 ESP-IDF **MCPWM**. Choose final GPIOs after checking the ILI9341 SPI, camera controls and other peripheral pin allocation. A 3.3V PWM-high signal's acceptance by the specific servo must be tested.
- Apply acceleration limits, soft and physical stops, emergency disable, and safe behavior on disconnect.
- MCPWM official documentation: https://docs.espressif.com/projects/esp-idf/en/stable/esp32p4/api-reference/peripherals/mcpwm.html
- Servo power guidance: https://www.pololu.com/docs/0J40/all

## Critical cable risk
The camera's **15-pin MIPI-CSI flat-flex cable** must cross two moving axes, plus the display SPI harness. Ordinary FFC is NOT automatically cyclic-flex rated. Reserve a guided cable loop near pivots with strain relief, confirm minimum bending radius, tension, twist, and lifetime; do not route high-speed MIPI via generic slip ring. Potential alternative: mount the processing board with the head or constrain camera movement if cable reliability cannot be demonstrated.

## CAD model
`mechanics/cad/neck_kinematics_v01.scad` shows 105×85×60 mm head, two servo-sized proxies, pan/tilt geometry and a cable keepout. Set `pan_angle` and `pitch_angle` to inspect poses. **It is not a fit-checked mechanical assembly, nor a printable servo bracket.**

## Validation gates
- [ ] Real servo envelope including horns, tabs, output axis, bearings, and mounting-hole pitch.
- [ ] Real P4 board and camera STEP/drawings, FFC connector orientation and cable limits.
- [ ] Dynamic interference check at pan ±45°, tilt ±20°.
- [ ] Head BOM-derived mass and CAD center-of-mass analysis, servo torque and stability margin.
- [ ] Cable routing/strain relief with cyclic motion durability test.
- [ ] Bench servo load current, regulator voltage droop, noise on camera/LCD.
- [ ] Physical hard stops, safe supply protection and rounded/guarded pinch points.
- [ ] Verify pin and power allocation and build a test jig before a final shell.
