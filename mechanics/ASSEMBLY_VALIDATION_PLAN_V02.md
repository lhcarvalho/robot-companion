# Assembly validation gate V0.2 (Issue #5)

**No manufacturer STEP imported. No collision-free 3D assembly or print-ready part claimed.**

The proposed 105×85×60 mm rounded-square head has a **2.1 mm nominal** clearance from top of 32×32 mm OV5647 board to inside shell in the prior 2D placement. LCD/camera nominal board silhouettes overlap by **0.65 mm vertically over 32 mm horizontal width**. That makes a depth-staggered layout necessary, not proven: connector, lens, screw and cable keepouts remain unknown.

## Verified references
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT/Resources-And-Documents — Waveshare publishes **mechanical drawings/STEP archive**.
- https://www.waveshare.com/2.4inch-lcd-module.htm — LCD board nominal dimensions.
- https://www.waveshare.com/rpi-camera-b.htm — OV5647 camera candidate.
- Existing `mechanics/cad/*.scad` are **mockup envelopes**, and coordinate systems between sketches differ; read `docs/MECHANICAL_INDEX.md`.

## Dimensional check
Run `python3 mechanics/fit_gate_v02.py`. This passes/proves only 2D nominal bounding-box arithmetic. Do not use it as a physical validation.

## Critical unsolved flex problem
The CSI camera and SPI LCD are on the tilting/panning head, but P4 mainboard is fixed in body. Unrated flat-flex cable is not inherently suitable for thousands of moving cycles. Before printed yoke, obtain a cable drawing and minimum dynamic bend radius, or choose a verified flexible alternative. Do not force a generic FFC around a sharp 90° elbow. Ensure full pan/tilt range, clips and anchor positions are mechanically checked.

## Checklist for first meaningful CAD assembly
- [ ] Original STEP ZIP obtained. Record archive URL, filename, SHA256, manufacturer and board revision. **The ZIP could not be imported into this environment; archive is not committed.**
- [ ] Extract accurate motherboard envelope/ports, mounting holes, and connector axes.
- [ ] Camera lens and cable connector positions, screw mounts and cable exit clearance.
- [ ] LCD mount holes, glass stack thickness, PCB socket, light/visible offsets.
- [ ] Servo shaft location, horn mounting plane, support bearing, head mass/centre of gravity.
- [ ] 3D assembly interference sweep at yaw ±45° and pitch ±20° with actual parts.
- [ ] Cable fatigue test plan at full travel and after vendor-confirmed radius.
- [ ] Full serviceable fasteners, ventilation and pinch-point guards.

## Alternatives requiring evaluation
1. Keep board in body and use **verified flex-rated** high-speed camera harness with large protected loops.
2. Move P4 board into head and evaluate added mass/torque/thermal envelope.
3. Constrain tilt/pan or move camera independently if cable rating cannot be achieved.

**Exit gate:** no final printable shell until detailed board STEP + cables, moving-part collisions and service access are validated. This PR addresses calculations and procedural readiness, not the STEP/cable blocker.
