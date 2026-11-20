# Provisional ESP32-P4 module DEV KIT GPIO allocation — ISSUE #6

**Status: electrical design candidate only. DO NOT WIRE WITHOUT VERIFYING ACTUAL PCB PIN-1 / POWER PINS / REVISION.**

## Sources
- Original board schematic: https://files.waveshare.com/wiki/ESP32-P4-Module-DEV-KIT/ESP32-P4-Module-DEV-KIT.pdf (Interface section; see PDF screenshot and reference)
- Manufacturer: https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT
- Independent transcription for corroboration only (different board/revision risks): https://github.com/Mcgee1704/waveshare-esp32-p4-wifi6-poe-eth/blob/main/docs/02-pinout.md

`electronics/p6_schematic_pinmap.csv` lists all 40 contacts of schematic **P6**. **Schematic contact order is NOT equivalent to left/right physical positioning without identifying P6 pin 1**. Photos from different revisions show reversed headers. Even a visually matching 40-pin header is not a Raspberry Pi BCM pinout.

## Proposed functional allocation, NOT committed to firmware
| Signal | P4 GPIO | Schematic P6 contact | Status |
|---|---:|---:|---|
| ILI9341 SPI CLK | 5 | 15 | CANDIDATE |
| ILI9341 SPI MOSI/DIN | 4 | 17 | CANDIDATE |
| ILI9341 CS | 20 | 14 | CANDIDATE |
| ILI9341 DC | 21 | 12 | CANDIDATE |
| ILI9341 RESET | 22 | 11 | CANDIDATE |
| ILI9341 BL | 3 | 20 | **ELECTRICAL DRIVER UNKNOWN — not direct PWM approved** |
| Neck pan PWM | 2 | 22 | CANDIDATE |
| Neck tilt PWM | 23 | 8 | CANDIDATE |

**Not an approved wiring diagram.** SPI peripheral route through GPIO matrix, board peripherals, pin level and boot state must be tested. The above allocation is provisional until a physical sample and manufacturer PDF revision are checked.

## Avoid or reserve on this board
- GPIO7/8: shared I²C camera/codec/connector.
- GPIO6: connected to ESP32-C6 control net; do not reuse.
- GPIO53: audio amplifier enable; GPIO54: C6 chip-enable/reset control.
- GPIO37/38: board UART/USB-to-UART path; avoid for production peripherals.
- GPIO0/1: optional 32-kHz crystal nets; avoid without verifying solder population.
- GPIO24/25: USB full-speed signals; avoid without PCB/revision verification.
- GPIO45: microSD power selection.
- GPIO36: boot-related / strapping. Additional strapping signals and multiplexing must be checked from actual silicon revision and current datasheet.
- The board's fixed audio, SD, Wi-Fi SDIO and Ethernet nets must not be repurposed based on exposed header alone.

## Power
ILI9341 board accepts VCC 3.3V or 5V per module guide; **logic thresholds, BL current and module backlight topology remain to be checked against the exact assembled PCB**. Power MG90S servos from independently protected regulated nominal 5V supply, not the ESP_3V3 pin. Tie signal reference grounds. No servo stall currents have been measured. Never infer regulator size from the 8Ω/2W speaker's output rating.

## Next verification gate
1. Inspect owner P4 module board PCB revision and mark physical P6 pin 1, GND and rails with a multimeter **before external power**.
2. Compare P6 schematic to actual PCB revision, establish 3.3V current availability and backlight current.
3. Bench test LCD initialization at low SPI clock, safely boot and monitor C6/audio/CSI.
4. Test servo output with **no mechanical load** and independent supply, instrument current.
5. Lock electrical map only after conflicts, pin states, and owner-board orientation are proven.

Other open scope: CSI FFC cyclic stress in mechanical Issue #5; audio and MCU/current budget remaining in #6.
