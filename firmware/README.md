# ESP32-P4 firmware scaffold (issue #7)

**Phase:** safe-idle scaffold **compiled successfully for ESP32-P4 in GitHub Actions** using ESP-IDF v5.5 (PR #16; run [44801017376](https://github.com/lhcarvalho/robot-companion/actions/runs/44801017376)). **Not flashed or bench-tested:** no camera, display, motor, audio or C6 integration is proven.

## Target
- Board: Waveshare ESP32-P4-Module-DEV-KIT / P4+C6.
- Toolchain candidate: **ESP-IDF v6.1.1** (current stable P4 docs as consulted 2026-11-20); treat as a pinned version for initial evaluation, but board vendor sample compatibility remains to be tested.
- This stage has no external managed dependencies. Later add reviewed versions for ILI9341 driver, camera pipeline and ESP-SR/ESP-DL only after verified sample support.

Official sources:
- https://docs.espressif.com/projects/esp-idf/en/stable/esp32p4/get-started/index.html
- https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT
- https://github.com/waveshareteam/ESP32-P4-Platform

## Build steps (not executed here)
Install ESP-IDF **v6.1.1** and its RISC-V toolchain, then:
```bash
. $HOME/esp/esp-idf/export.sh
cd firmware
idf.py set-target esp32p4
idf.py build
# after verifying USB/board/cable and power:
idf.py -p /dev/ttyUSB0 flash monitor
```
Replace port with actual device. Capture host tool version, `idf.py --version`, build exit code/log and serial monitor output into `tests/evidence/`.

## Expected behavior
The program initializes ESP-IDF logging and emits a 5-second heartbeat in a safe idle loop. **All motors remain disabled and no GPIO is manipulated.** Successful compilation is not claimed.

## Hardware test sequence (each requires a separate evidence record)
1. Basic boot / serial log, flash and watchdog.
2. ILI9341 SPI using **approved** pin map from electrical lane (#6), proper backlight circuit; log display init.
3. OV5647 camera CSI with manufacturer example and actual matching FFC; log frame success.
4. Board microphone, amplifier and speaker volume; measure feedback/noise and current.
5. Wi-Fi/C6 integration.
6. Concurrent camera + display + audio + Wi-Fi; measure RAM, latency, CPU and power.
7. Motion *only after* safety circuitry and neck torque/cable mechanics are verified.

Do not initialize motor PWM with unverified pin assignments. Review `docs/ARCHITECTURE.md` and `AGENTS.md` before changing controls.
