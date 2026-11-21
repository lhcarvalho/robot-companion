#pragma once
#include <stdbool.h>
#include <stdint.h>
#include "esp_err.h"
#include "esp_lcd_panel_ops.h"

/* No GPIOs are enabled by this library until explicitly called.
 * Supply a board-verified pin allocation — do not rely on provisional schematic pins.
 */
typedef struct {
    int sclk_gpio;
    int mosi_gpio;
    int cs_gpio;
    int dc_gpio;
    int rst_gpio;
    int backlight_gpio; /* -1 disables any backlight GPIO toggling. */
    uint32_t spi_clock_hz; /* Start at 10 MHz for bench validation. */
    bool backlight_active_high;
} robot_display_config_t;

esp_err_t robot_display_init(const robot_display_config_t *config,
                             esp_lcd_panel_handle_t *panel_out);
