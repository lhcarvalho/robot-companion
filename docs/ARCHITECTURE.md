# System architecture — conceptual v1

## Logical domains
1. **Hardware P4** (ESP-IDF): CSI camera, SPI ILI9341, audio I/O, microcontroller peripherals; protected servo actuation, local behavior/state and watchdogs.
2. **Connectivity C6** (on Waveshare board): Wi-Fi 6/BLE communications to optional home backend. P4 remains locally functional in disconnected mode.
3. **Desk body**: P4 mounted fixed in torso, OV5647 and LCD in moving head, 2-axis servo candidate, speaker and power; same head and control protocol should remain usable with mobile base.
4. **Optional home AI server**: Python gateway, PC RTX 3080 to handle richer ASR, LLM and vision; cloud API optional. Never on movement safety critical path.
5. **Future mobile base**: differential-drive motor driver, wheel encoders, bumper, front ToF, downward cliff sensors, protected battery and power; LiDAR/SLAM only when assessed.

## High-level data flows
```mermaid
flowchart TB
  Camera[OV5647 CSI camera] --> P4[ESP32-P4 / ESP-IDF]
  LCD[ILI9341 SPI LCD] <-- P4
  Audio[Microphone and speaker] <--> P4
  Sensors[Safety sensors] --> Safety[Deterministic safety controller]
  Safety --> Motion[Servo / later wheel motor drivers]
  P4 --> Safety
  P4 <--> C6[ESP32-C6 wireless link]
  C6 <--> Server[Optional local RTX 3080 / remote AI]
```

## Decisions / constraints
- No autonomous high-level model issues arbitrary motor PWM; permitted actions are sanitized by local controller.
- On link drop, motion commands time out to stop. Low-voltage faults also stop movement.
- Local vision model support must be tested on chosen P4 firmware, not assumed.
- Webcam-like stream and speech can be sent to external AI only under explicit configuration/privacy controls.
- Design modular capabilities: `face.detect`, `face.identify`, `display.expression`, `head.pan_tilt`, `motion.drive` (mobile only), `safety.stop`.

## Interface notes
- P4 has CSI and SPI peripherals, but **full GPIO map has not been verified** against Waveshare board schematics. An earlier hypothetical pinmap was discussed; it is **not approved wiring**.
- Camera cable through neck is an unsolved mechanical/electrical integration risk.
- Servo regulated supply must be isolated from MCU 3.3V; specifics still open.
- Internal placement: fixed P4 in torso, moving LCD/OV5647 in head is a preferred **candidate** that may change due to cable reliability.
- No final API schema or message protocol established yet. A future issue must specify compatibility/versioning.

## Diagram
See [system architecture SVG](diagrams/system-architecture.svg) and [mechanical concept SVG](diagrams/mechanical-envelope.svg). Diagrams are conceptual, not validated engineering drawings.
