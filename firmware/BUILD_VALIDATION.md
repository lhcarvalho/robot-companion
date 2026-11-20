# Continuous firmware compilation — issue #7

This workflow executes a **real cross-compilation** for the ESP32-P4 target using Espressif's supported GitHub Action: https://github.com/espressif/esp-idf-ci-action.

- Action: `espressif/esp-idf-ci-action@v1`
- ESP-IDF Docker toolchain requested: `v5.5` (CI will confirm availability and actual compiler versions).
- Target: `esp32p4`.
- Project path: `firmware/`.
- Scope: safe-idle project and pure-C motion safety component; no GPIOs are driven by this baseline.

## Passing CI does and does not prove
A passing workflow demonstrates that the code compiles/links with the selected toolchain in the runner. It **does not** prove CSI camera, ILI9341 SPI, onboard microphone, P4+C6 Wi-Fi bridge, real servo wiring or physical safety.

## Firmware acceptance evidence
- [ ] GitHub Actions ESP-IDF build successful with workflow-run URL and exact commit SHA.
- [ ] Repeat local `idf.py build` on a developer machine; compare configurations.
- [ ] Flash supported physical board revision and capture boot logs.
- [ ] Electrical lane #6 approves pinout and current budget before peripheral PWM or LCD wiring.
- [ ] Demonstrate a powered safe stop for servo controls and proper fault input logic.

The earlier `firmware/README.md` suggested v6.1.1 as an untested candidate. This workflow intentionally starts with tagged **v5.5** for compatibility qualification; do not assume equivalence until both are tested.
