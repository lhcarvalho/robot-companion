# Host-side motion safety tests

These tests validate only deterministic **software gating logic**, not motor electrical safety, sensor wiring or physical motion. No motors are driven.

Run on Linux:
```sh
cc -std=c11 -Wall -Wextra -Werror -pedantic -fsanitize=undefined -fno-omit-frame-pointer \
  -I firmware/components/motion_safety/include \
  firmware/components/motion_safety/motion_safety.c tests/native/test_motion_safety.c \
  -o /tmp/test_motion_safety
/tmp/test_motion_safety
```

As of 2026-11-20, native test executed locally using GCC with AddressSanitizer and UBSan; **18 assertions passed**. CI runs UBSan by default. Full ESP-IDF build, hardware and real sensors have not been tested.

Guardrail API: all safety inputs start unknown/unready, requests are bounded to ±300/1000 in arbitrary per-mille units and <=1000 ms; every new request must be explicitly accepted; missing command/failed sensor supply/latching emergency stop outputs zero. `reset_fault` needs all safety inputs clear, and must not automatically start motion.

**Critical integration requirements:** application must call `motion_safety_tick` frequently using a monotonic millisecond clock; the actual motor output must default disabled on boot and on crash, watchdog or power fault. Sensor electrical faults must map to unsafe, not clear. Commands require real authenticated local authority. Choose calibrated output limits based on prototype measurements; current numerical caps are conservative placeholders, not child safety certification. This is a pure C module, **not wired to any ESP32 PWM GPIO yet**.
