# Electrical purchasing and first-power verification — issue #6

**State: no physical parts received; wiring and power budget NOT approved.**

## Purchase default
The Waveshare **ESP32-P4-Module-DEV-KIT-A (SKU 30772)** includes:
- P4+C6 board,
- OV5647 RPi Camera (B),
- matching FFC 15-pin camera cable,
- 8-ohm 2-watt speaker,
- two SH1.0 4-pin interface cables.

Manufacturer product source:
https://www.waveshare.com/product/mcu-tools/esp32-p4-module-dev-kit.htm

The LCD Waveshare ILI9341 2.4-inch SPI SKU 18366, servos MG90S and regulated servo power are **not** included in that kit. Speaker maker/dimensions and harness type must be checked against real kit revision.

## Before first power (mandatory)
1. Record photographed PCB model, revision, silkscreen, board power supply input and kit contents.
2. Identify the **physical** pin-1 of connector P6 and verify candidate pinout against the exact board schematic; do not infer Raspberry Pi header layout.
3. With all supplies disconnected, inspect for shorts between 5V, 3V3 and GND; verify connector polarity and physical clearance.
4. Measure the 3.3V rail and current capacity, choose display supply and validate logic-level thresholds. **BL/backlight pin current and topology still unknown**; do not drive BL until circuit inspection.
5. Power servos via a dedicated current-limited protected nominal 5V rail, never the MCU 3.3V pin. Common reference ground required.
6. Test board+camera+LCD idle current and peak supply drop separately before servo power; instrument inrush and supply heating.
7. Verify both servo output signals and safe state with no mechanical load. Keep head and moving camera cable disconnected for initial tests.
8. Only after mechanical and electrical checks, test pan/tilt physical stops and camera FFC strain relief.
9. No unattended use with children until cliff/bumper/power failsafe is physically verified.

## Bundle accounting
BOM row `HW-001` is for the KIT, while rows `HW-003` and `HW-005` are the **components inside it**, not additional orders. Do not sum quantities as if all three were separate purchase lines.

## No electrical approval yet
`electronics/PINOUT_PROPOSAL_V02.md` is provisional. Supply current, GPIO boot state, speaker enclosure, physical orientation and backlight driver require tests.
