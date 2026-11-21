# ILI9341 SPI display adapter (issue #7)

This component wraps Espressif's official `esp_lcd_ili9341` **2.1.0** for the ESP32-P4, using SPI and RGB565. Pins are runtime-configurable and **NO GPIO is enabled or connected during safe-idle app boot**.

Reference:
- https://components.espressif.com/components/espressif/esp_lcd_ili9341
- https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32p4/api-reference/peripherals/lcd/spi_lcd.html

**Important blockers:** 
- actual Waveshare P6 pin1 orientation, module revision, GPIO conflicts not fully checked;
- BL module topology/current and PWM capability not validated;
- actual CSI camera/audio/Wi-Fi simultaneous operation unknown.

Only after electrical #6 and real board checks should a bench test call `robot_display_init` with validated GPIOs. Initial SPI clock <=10 MHz recommended; this is a test starting value, not proven limit. Use 3.3V logic and check screen supply/current before wiring. Current code has no touch, animation engine or hardware smoke test.

**Build goal:** compile component in CI via ESP-IDF; do not confuse compilation with working LCD.
