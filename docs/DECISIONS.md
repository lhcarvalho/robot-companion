# Decision register — architecture decision records (ADR-lite)

Status meanings: **DECIDED** product/strategy choice; **CANDIDATE** provisional engineering selection; **OPEN** undecided; **VALIDATED** verified by specified physical/test evidence. Product decisions do not imply engineering validation.

| ID | Status | Decision | Why | Revisit when |
|---|---|---|---|---|
| D-001 | DECIDED | Use ESP32-P4 + C6 as central platform, not Pi5 or ESP32-S3+Grove | Offline lightweight vision and rich I/O without Raspberry Pi price/power | Specific board fails functional tests |
| D-002 | DECIDED | Modular shared head/electronics; removable desk and wheeled bases | Reuse electronics and software | Interface design proves infeasible |
| D-003 | DECIDED | Medium robot; nominal 150 mm, conceptual 120–180 mm | Desk-scale but permits camera/audio/mechanics | Accurate component models prove size insufficient |
| D-004 | DECIDED | Rounded-square head | Room for front expressive display; approachable look | Structural packaging study |
| D-005 | CANDIDATE | Waveshare 2.4-inch ILI9341 SPI LCD SKU 18366 | Compact dimensions and ESP-IDF driver | GPIO/driver/optical/fit benchmarks |
| D-006 | CANDIDATE | Waveshare RPi Camera (B) OV5647 CSI-2, ideally P4-A kit | Vendor-supported camera/cable pair | Mechanical and on-board validation |
| D-007 | CANDIDATE | Two MG90S servos, pan ±45°, tilt ±20° | Economical two-axis head mechanism | Measured moving mass, fatigue and torque |
| D-008 | DECIDED | P4 in fixed torso, camera and LCD in moving head as initial layout | Reduced servo moving mass | Moving FFC proves unsuitable |
| D-009 | DECIDED | Offline physical safety; RTX 3080/cloud optional for advanced conversations | Reliability and cost | Never relax safety dependency |
| D-010 | OPEN | Exact torso footprint/USB access, speaker SKU, power topology, mobile base coupling | Need STEP, BOM and measurements | Packaging/electrical proof |
| D-011 | OPEN | Exact GPIO assignments / backlight PWM / CSI+LCD concurrency | No full pin and electrical conflict matrix yet | Firmware and schematic verification |

**Change policy:** For a materially different product/architecture choice add a dated ADR in `docs/adr/`, update this register and cite evidence. Never silently change CAD parameters or claim a candidate is final.
