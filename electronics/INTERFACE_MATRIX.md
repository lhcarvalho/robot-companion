# Electrical interface allocation — issue #6 (review 0.1)

**Board:** Waveshare ESP32-P4-Module-DEV-KIT, ESP32-C6 on the module. **Status:** physical header pin mapping and exact GPIO signal allocations NOT YET VERIFIED. This is a no-assumption interface plan, not a wiring diagram.

## Sources
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT
- https://files.waveshare.com/wiki/ESP32-P4-Module-DEV-KIT/ESP32-P4-Module-DEV-KIT.pdf (manufacturer schematic, 3 pages; inspect at original resolution)
- https://docs.espressif.com/projects/esp-idf/en/stable/esp32p4/api-reference/peripherals/lcd/index.html

## Interfaces
| Module | Bus | Expected connection | Physical J6/P6 pin | Conflict status |
|---|---|---|---|---|
| Camera Waveshare RPi Camera (B) | MIPI CSI-2 + control I²C | Dedicated CSI socket | not via free general pin allocation | connector orientation not tested |
| LCD Waveshare ILI9341 | SPI MOSI, SCLK, CS, DC, RST, BL, 3V3, GND | Exposed user GPIOs and 3.3V supply | **TBD from official J6/P6 sheet** | **NOT CLEAR** |
| Pan MG90S | MCPWM output | User GPIO + protected regulated supply | TBD | **NOT CLEAR** |
| Tilt MG90S | MCPWM output | User GPIO + protected regulated supply | TBD | **NOT CLEAR** |
| Mic | Board onboard microphone/codec path | Fixed onboard nets | PCB routing | Source-supported feature; software integration pending |
| Speaker | 8Ω 2W via board amp | MX1.25 2P port | PCB connector | exact speaker part and mating connector TBD |
| Wi-Fi | SDIO to onboard C6 | Fixed module connection | PCB routing | don't allocate shared pads without checking |
| Safety inputs | future bumpers/cliff sensors | GPIO/I²C | TBD | reserve interrupts and safe states |

### Previously proposed pin numbers are NOT approved
Old conversational guesses GPIO4, GPIO5, GPIO6, GPIO20, GPIO21, GPIO22 for SPI/backlight are **not verified J6 assignments**. This document deliberately leaves physical pin numbers unassigned. Next action is to extract and independently cross-check all P6 header pin numbers from the manufacturer PDF and board revision.

### LCD power and backlight
The Waveshare 2.4in module accepts a module supply described as 3.3V/5V in the vendor docs, but **logic-level, regulator, backlight driver topology/current and BL pin electrical behavior require per-SKU board inspection**. Don't assume PWM directly drives a bare LED. `esp_lcd_panel_disp_on_off` does not dim backlight (Espressif documentation).

### Safety
- Servo power: independent current-rated **nominal 5V** rail with fuse/current limiting; share ground with P4; **not MCU 3.3V**.
- Confirm MG90S command-signal 3.3V-high interoperability with exact servo sample.
- E-stop / watchdog command timeout / mechanical stops independent of cloud or AI.
- If supply droops or overcurrent is detected, disable motor signals or power safely.

## Acceptance remains open
No physical pin mapping signed off, no voltage/current measurements, no powered servo tests, no tested concurrent camera/audio/LCD/wireless integration. The source schematic has been located, but a complete traceable J6 allocation is still to be extracted.
