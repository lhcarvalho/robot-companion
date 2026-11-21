# Robot Companion — Product brief (v1)

**Mission:** Build an affordable, open, modular hobby companion robot for an adult's desk and for supervised interaction with children at home. The robot should express personality through a digital face, recognize familiar people, listen and speak, move its head, and eventually navigate slowly on the floor. The same central electronics/software should be reused across desk and mobile configurations.

**Product owner:** repository owner. **Source of truth:** this repository; past chats are not required to continue.

## Intended experience
- **Desk v1:** small friendly robot; face animations on LCD, camera above display, audio, two-axis neck; powered from a safe external supply. It can recognize enrolled faces with compact offline vision models and react with preprogrammed greetings. Natural open-ended conversation uses optional local PC (RTX 3080) or cloud API.
- **Mobile v2:** same shared module attached to wheeled base; encoders, obstacle and cliff sensors, safe limited-speed driving; future mapping/navigation if extra compute/sensors are justified.
- **Offline principle:** physical control, safety stop, expressions and supported lightweight perception should work without cloud connectivity. **Do not promise offline LLM-level conversations or full-house SLAM on P4 alone.**

## Priorities
1. Fit and electrical integrity of P4+C6, camera, LCD, audio and moving neck.
2. Produce demonstrable bench prototype before final 3D printed cosmetics.
3. Real-time motor/servo safety independent of LLM/cloud/network.
4. Modular software, body/base connectors and maintainable build documentation.
5. Privacy-first local enrollment/deletion for children's face biometrics.

## Current product decisions (not necessarily validated hardware)
- ESP32-P4 plus ESP32-C6 Waveshare ESP32-P4-Module-DEV-KIT; consider official kit A with OV5647 camera and cable.
- Nominal robot height 150 mm; acceptable conceptual range 120–180 mm.
- Rounded-square head, proposed 105 W × 85 H × 60 D mm.
- Waveshare 2.4inch LCD Module, ILI9341, SPI, SKU 18366.
- Waveshare RPi Camera (B), OV5647, CSI-2.
- Pan/tilt concept using two MG90S *candidate* servos, pan ±45°, tilt ±20° *targets only*.
- ESP-IDF; ESP-DL/ESP-WHO for supported vision, LVGL for animations, C6 for connectivity, optional server for advanced AI.
- Desktop torso dimensions and PCB fit remain OPEN; existing CAD dimensions are mockups.

## Non-goals for current milestone
- Selling or certifying a consumer product; unattended play with children.
- Physical mobility or autonomous navigation in first desk prototype.
- Designing an entire custom PCB or replacing the manufacturer dev board.
- Finalizing shell STL from estimated PCB/cable/servo dimensions.
- Assuming every offline vision model is supported or recognizing a specific child without training, enrollment and real-world testing.

## Success criteria for first physical MVP
- Board boots reproducibly and can be programmed/documented.
- LCD displays animated face using supported SPI GPIOs and frame-rate measurement.
- Camera captures images and is interoperable with LCD/audio/Wi-Fi.
- Local person/face detection demonstrably operates on this board; identity enrollment evaluated with permission/privacy protections.
- Two-axis movement only after mechanical clearances, servo torque and cable flex are verified.
- Power protection, physical stops and communications-loss safety tested.
- Complete BOM, reproducible build instructions and annotated CAD updated with actual measurements.

See [STATUS](STATUS.md), [ROADMAP](ROADMAP.md), [DECISIONS](DECISIONS.md), [OPEN_QUESTIONS](OPEN_QUESTIONS.md), [ARCHITECTURE](ARCHITECTURE.md).

## Modular power / base architecture (decision 2026-11-21)
The shared head+P4 electronics assembly must operate from an externally powered bench stand for prototyping. Main energy storage belongs exclusively in the interchangeable desk/mobile base, not in the shared core. Different bases may have different batteries, with the same protected regulated output and a defined mechanical connector. Live swapping is not part of the first prototype. See [ADR-001](adr/ADR-001-modular-base-power.md).
