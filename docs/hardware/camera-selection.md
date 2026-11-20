# Camera selection — RC-CAM-001 (revision 0.1)

**Status:** selected for prototype; mechanical and electrical integration awaiting physical validation.

## Selected hardware

- Host: **Waveshare ESP32-P4-Module-DEV-KIT** (base SKU 30560), with built-in ESP32-C6.
- Camera: **Waveshare RPi Camera (B)**, OV5647, 5 megapixels, MIPI CSI-2.
- Recommended purchasing route when possible: **ESP32-P4-Module-DEV-KIT-A**, SKU **30772**, which includes the host board, RPi Camera (B), and matching 15-pin FFC.
- Screen (existing decision): **Waveshare 2.4inch LCD Module**, ILI9341, SPI, nominal PCB 70.5 × 43.3 mm.
- Proposed head envelope (not frozen): **105 W × 85 H × 60 D mm**, target robot height 150 mm.

## Verified from vendor sources

| Property | Value | Evidence |
|---|---|---|
| Camera sensor | OV5647, 5 MP | Waveshare RPi Camera (B) product selection guide |
| Camera PCB outline | 32 × 32 mm | Waveshare camera selection guide |
| Lens diagonal angle of view | about 43 degrees | Waveshare camera selection guide |
| Interface | 2-lane MIPI-CSI on P4 host | Waveshare ESP32-P4-Module-DEV-KIT documentation |
| Physical cable supplied in P4-A | 15-pin FFC cable | Waveshare P4-A kit contents |
| Vendor sample | camera preview / OV5647 pipeline | Waveshare ESP32-P4-Platform examples |
| Camera control I2C | SDA GPIO7; SCL GPIO8 in vendor example | Waveshare ESP-IDF video examples |

Sources:
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT
- https://www.waveshare.com/product/mcu-tools/esp32-p4-module-dev-kit.htm
- https://github.com/waveshareteam/ESP32-P4-Platform/blob/main/examples/esp-idf/16_video_lcd_display/README.md
- https://www.waveshare.com/rpi-camera-b.htm
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT/Resources-And-Documents

## Design implications

1. Mount the lens on the head front, **centered above the LCD visible area**, but permit the **32 × 32 mm camera PCB to overlap the display PCB in the depth direction**. Otherwise a 32 mm high camera PCB plus a 43.3 mm high display PCB leaves only 9.7 mm vertically before margins, cable clearances and separation.
2. Place the P4 dev board in the torso/base rather than the articulated head where practical. The CSI cable must therefore pass through the neck; its connector orientation, available length, minimum bend radius, twisting and strain relief remain unverified.
3. Preserve access to focus adjustment and clearance for the protruding lens.
4. Create an opaque black face mask hiding LCD inactive areas and separate lens aperture; the mask must not obstruct the camera field of view.
5. A 43° diagonal field of view is relatively narrow for a roving robot. Evaluate a wide-angle OV5647 variant only after compatibility validation.
6. Camera uses CSI differential lanes and shared control I2C; the selected ILI9341 uses SPI. This avoids direct bus-sharing but **does not yet prove** that all GPIO assignments, power rails, or runtime combinations are conflict-free.

## Validation gates before final CAD or purchase

- [ ] Verify exact host-board revision and identify 15-pin CSI connector orientation from mechanical drawings and the actual board.
- [ ] Verify exact camera module mechanical drawing (holes, lens position/height, lens field-of-view cone).
- [ ] Verify supplied FFC cable length, pin contact orientation, bend constraints and clearance through pan/tilt neck mechanism.
- [ ] Confirm camera electrical initialization using Waveshare reference firmware and the board revision actually purchased.
- [ ] Verify simultaneous camera capture, LCD SPI updates, Wi-Fi and audio under realistic load.
- [ ] Verify heat, current consumption and achievable frame rate with the intended vision model.
- [ ] Validate head envelope against camera, LCD, mounts and service access in parametric CAD.
- [ ] Confirm face identification reliability across normal home lighting with appropriate local biometric data handling.

## Decisions and exclusions

- Selected camera for first prototype: **RPi Camera (B) / OV5647**.
- Do **not** substitute a generic Raspberry Pi camera or a 22-pin CSI cable merely because the sensor is also OV5647; physical pinout and cable orientation must be verified.
- Do **not** assume the proposed head can be manufactured at 105 × 85 × 60 mm without a 3D assembly check.
- No requirement to store children's face images remotely: consent, local storage and deletion controls should be built into the later software spec.
