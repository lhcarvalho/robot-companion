# Mobile base option M01 — differential drive (2WD + passive support)

**Date:** 2026-11-23  
**Status:** **CANDIDATE OPTION**, not selected as sole future mobile architecture. **No fit, motor, or sensor hardware validated.**

## Goal
Develop the **first option** for an interchangeable moving base that can attach to the same rounded-square head + P4 electronics core used by the stationary desk base. Preserve ADR-001 (power/battery and mobility hardware live inside the base) and the slide cradle/latch concept in [base coupling V01](BASE_COUPLING_CONCEPT_V01.md).

## Architecture

- Two independent **geared DC wheel motors with quadrature encoders** (left and right) drive two rubber wheels.
- One passive **low-friction ball caster or caster wheel** supports the base at a third ground point (position front/rear TBD after CG analysis). Avoid poor carpet thresholds and debris ingestion in the sphere.
- **Protected base-local energy system** feeds motor driver and separately regulated core/servos; wheels never draw traction power from an ESP32-P4 GPIO or core-side regulator.
- A **dual-channel H-bridge** is required with PWM/direction and current rating at worst-case motor stall plus protection; TB6612FNG is a **candidate only**, not approved until chosen motor stall current and voltage are known.
- Prefer independent **base-local safety controller + watchdog** for motor-drive enable, encoders, bumper and cliff sensors, so loss of UART/core power/network causes a physical motor-off/safe-stop command. This controller may communicate with P4 over a future validated, level-compatible bus; **no pin allocation approved**.
- Base identification reports `base.type=mobile.diffdrive.v1` or equivalent (wire protocol TBD); unrecognized base = **no mobility**. Fixed desk base never accepts `motion.drive`.

## Kinematics and behaviors

Let `vL` and `vR` be left/right signed wheel linear speeds, `b` the measured distance between wheel contact centers. Body speed `v=(vR+vL)/2`; yaw rate `omega=(vR-vL)/b`.

| Command | Left wheel | Right wheel | Result |
|---|---|---|---|
| Straight | +v | +v | Forward |
| Gentle left | +small | +large | Left curve |
| Gentle right | +large | +small | Right curve |
| Pivot left | -v | +v | Rotate near center |
| Stop | zero/controlled braking | zero/controlled braking | Safe stop |

Use a velocity controller with encoder feedback, speed ramp/acceleration limits and independent motor-fault cutoff. Wheel slip and caster friction mean commanded turn angle is NOT guaranteed; calibrate experimentally. No autonomous roam without obstacle/cliff tests.

## Dimensions: deliberately *unfrozen*

Previous design nominal whole robot height ~150 mm, electronics torso nominal footprint ~125×100 mm; these are **concept values**, not approved mating measurements. Visual target: discreet, smooth base, concealed wheels, rounded shell.

Study these **parametric envelopes only** during first CAD:
- Wheel diameter *candidate study range*: **35–55 mm**; test indoor floor friction and threshold clearance.
- Wheel-center lateral spacing *candidate study range*: **85–115 mm**, subject to shell/interference, stability and motor gearbox envelopes.
- Base external footprint *candidate study range*: **140–170 mm wide, 120–155 mm deep**; battery, protected supplies, motor/gearbox, center of mass and tipping need volumetric proof.
- Base height *candidate study range*: **45–75 mm** including wheel protrusion; must assess whether **overall 150 mm goal must increase**. These are initial studies, not source-of-truth specifications.

**Critical:** a 125×100 mm core footprint should not be silently treated as a mating surface size. Future CAD must independently establish the adapter plate, rail stops and safe latch access. No mechanical load on the electrical plug; base swap is power-off.

## Safety design gates for family and children

| ID | Requirement / test before free navigation |
|---|---|
| M-S01 | Low starting speed; measured braking distance and gentle speed/acceleration limits |
| M-S02 | At least forward obstacle sensing + **physical bumper**; threshold and soft-object false negatives tested |
| M-S03 | **Downward cliff sensing** tested on the actual floor colors, gloss, edges and heights; no unsupervised tabletop driving |
| M-S04 | Wheel stall/over-current and tilt/fall safeties; monitor pack undervoltage and thermal risk |
| M-S05 | Base watchdog: loss of core/base data link or heartbeat, invalid command and detected safety fault **disable traction independently** |
| M-S06 | Enclosed wheels/gears/battery and no pinch access at head and docking latch; retention resists lifting/tipping |
| M-S07 | Unknown base cannot drive; desk/bench base safe idle |
| M-S08 | Battery/BMS/charger and protected rails qualified; no live base swapping |
| M-S09 | Emergency stop mechanism reachable by adult and timeout enforced even when cloud/server disconnected |

Sensors: forward ToF (VL53L0X/VL53L1X candidates), downward IR/ToF for cliffs, mechanical bumper switches; quantity/field of view unknown. A single forward ranging sensor is **not** a proven anti-collision system, and typical HC-SR04 has 5 V echo requiring logic protection. IMU optional; odometry needs encoders. No SLAM/LiDAR in M01 MVP.

## Component plan: no models final yet

| Count | Part | Selection criteria |
|---|---|---|
| 2 | Brushed DC gear motor with quadrature encoder | Voltage, no-load and stall current, gearbox efficiency/noise, encoder resolution, output torque |
| 2 | Rubber wheels | Matched gearbox shaft/hub; traction; gentle tread and low noise |
| 1 | Passive ball caster / caster wheel | Low drag, does not jam, load-bearing |
| 1 | Dual H-bridge motor driver | Peak stall current, thermal margin, PWM control, electrical protection |
| 1 | Base microcontroller/safety watchdog (candidate) | Deterministic motor cutoff, base ID/telemetry and sensor interfaces |
| 1+ | Protected battery pack, charger and power distribution | Base-located, chemistry-specific, mechanically contained; current budget pending |
| 1+ | Forward ranging + bumper | Real test-based coverage |
| 2+ | Downward edge/cliff detectors | Actual floor and threshold tests; more channels if blind spots |
| 1 | Interface rails + latch + electrical harness | Uses shared [base/core coupling](BASE_COUPLING_CONCEPT_V01.md), without carrying wheel load electrically |

Current component pricing and SKU procurement **not part of this design**, and no parts have been marked purchased.

## Integration and sequencing

1. **Bench baseline**: P4, display, camera and servo powers measured (G1/G2); confirm chosen P4/NANO board model before specific CAD redesign. Preserve core visual language: white rounded enclosure, black continuous face, large expressive eyes.
2. **Non-driving fit**: shell, axle, motors, caster and battery proxies, CG and tipping analysis, external footprint study. Do not call concept CAD print-ready.
3. **Motor bench rig with wheels off ground**: driver, encoder direction/counts, watchdog faults, current stalls, cutoff and brownout.
4. **Restrained floor rig**: speed calibration, soft bumper, cliff sensor accuracy, emergency stop, sensor blind spots, children proximity safety.
5. **Controlled indoor driving**: slow manual movement and scripted trajectories after safety gates. Navigation autonomy is later optional G8.

## Acceptance checklist

- [ ] Confirm actual board/camera/speaker/servo configuration and measured core+head mass and center of gravity
- [ ] Pick gearbox/wheels/driver from measured motor loads and published drawings
- [ ] Demonstrate stable physical coupling with the same core as desk base
- [ ] Demonstrate safe stop with command loss, servo interference, battery low and obstacle/edge
- [ ] Measure speed, yaw calibration, battery life, noise, heat, tip stability and collision clearances
- [ ] Produce **new** `_vNN.scad` CAD sources and matching PNG/STL/GLB (after parametric fit study), without overwriting older models

## Concept diagram
[Mobile base differential V01 SVG](../docs/diagrams/mobile-base-differential-v01.svg) — 2D illustration, **not to scale**, not manufacturing geometry.
