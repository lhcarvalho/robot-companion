# Smoke-test matrix — issue #7

No hardware tests have been run. This checklist is deliberately NOT a pass report.

| Test ID | Required evidence | Status |
|---|---|---|
| T-001 | ESP-IDF version + successful P4 build log | NOT RUN |
| T-002 | Safe idle boot/heartbeat serial log | NOT RUN |
| T-003 | SPI ILI9341 init/image/frame rate, electrical pinmap approved | BLOCKED by #6 and hardware |
| T-004 | CSI OV5647 still frame, cable/revision verified | BLOCKED by hardware |
| T-005 | Speaker/microphone playback/recording | BLOCKED by hardware |
| T-006 | C6 Wi-Fi connectivity | BLOCKED by hardware |
| T-007 | Concurrent peripherals and supply voltage measurement | BLOCKED |
| T-008 | Two servos with physical stops, power-fault stop and cable bend test | BLOCKED by #5/#6 |
| T-009 | Face detection and local enrollment benchmark with opt-in/privacy | NOT STARTED |

For each completion: attach reproducible command, board/revision, configuration, commit SHA, measured data and raw log; never just check the box.
