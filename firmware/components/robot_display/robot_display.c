#include "robot_display.h"
#include "esp_lcd_panel_io.h"
#include "esp_lcd_panel_vendor.h"
#include "esp_lcd_ili9341.h"
#include "driver/spi_master.h"
#include "driver/gpio.h"
#include "esp_log.h"

static const char *TAG = "robot_display";

static bool pins_valid(const robot_display_config_t *c)
{
    if (!c || c->spi_clock_hz < 100000 || c->spi_clock_hz > 40000000) return false;
    const int pins[5] = {c->sclk_gpio,c->mosi_gpio,c->cs_gpio,c->dc_gpio,c->rst_gpio};
    for (int i=0;i<5;i++) {
        if (!GPIO_IS_VALID_OUTPUT_GPIO(pins[i])) return false;
        for(int j=0;j<i;j++) if(pins[j]==pins[i]) return false;
    }
    if (c->backlight_gpio >= 0) {
        if(!GPIO_IS_VALID_OUTPUT_GPIO(c->backlight_gpio)) return false;
        for(int i=0;i<5;i++) if(pins[i]==c->backlight_gpio) return false;
    }
    return true;
}

esp_err_t robot_display_init(const robot_display_config_t *c,
                             esp_lcd_panel_handle_t *panel_out)
{
    if (!panel_out || !pins_valid(c)) return ESP_ERR_INVALID_ARG;
    *panel_out = NULL;
    spi_bus_config_t bus = {
        .sclk_io_num = c->sclk_gpio,
        .mosi_io_num = c->mosi_gpio,
        .miso_io_num = -1,
        .quadwp_io_num = -1,
        .quadhd_io_num = -1,
        .max_transfer_sz = 320*20*2,
    };
    esp_err_t err=spi_bus_initialize(SPI2_HOST,&bus,SPI_DMA_CH_AUTO);
    if(err!=ESP_OK)return err;

    esp_lcd_panel_io_handle_t io=NULL;
    esp_lcd_panel_io_spi_config_t io_cfg={
        .dc_gpio_num=c->dc_gpio,
        .cs_gpio_num=c->cs_gpio,
        .pclk_hz=c->spi_clock_hz,
        .lcd_cmd_bits=8,
        .lcd_param_bits=8,
        .spi_mode=0,
        .trans_queue_depth=10,
    };
    err=esp_lcd_new_panel_io_spi((esp_lcd_spi_bus_handle_t)SPI2_HOST,&io_cfg,&io);
    if(err!=ESP_OK){spi_bus_free(SPI2_HOST);return err;}
    esp_lcd_panel_dev_config_t panel_cfg={
        .reset_gpio_num=c->rst_gpio,
        .rgb_ele_order=LCD_RGB_ELEMENT_ORDER_RGB,
        .bits_per_pixel=16,
    };
    esp_lcd_panel_handle_t panel=NULL;
    err=esp_lcd_new_panel_ili9341(io,&panel_cfg,&panel);
    if(err==ESP_OK) err=esp_lcd_panel_reset(panel);
    if(err==ESP_OK) err=esp_lcd_panel_init(panel);
    if(err==ESP_OK) err=esp_lcd_panel_disp_on_off(panel,true);
    if(err!=ESP_OK){
        if(panel)esp_lcd_panel_del(panel);
        esp_lcd_panel_io_del(io);
        spi_bus_free(SPI2_HOST);
        return err;
    }
    if(c->backlight_gpio>=0){
        /* Only digital on/off; do not claim PWM/dimming. Check module BL electronics first. */
        gpio_config_t cfg={
            .pin_bit_mask=(1ULL<<c->backlight_gpio),
            .mode=GPIO_MODE_OUTPUT,
        };
        err=gpio_config(&cfg);
        if(err==ESP_OK) err=gpio_set_level(c->backlight_gpio,c->backlight_active_high?1:0);
        if(err!=ESP_OK){
            ESP_LOGW(TAG,"Backlight GPIO failed (%s)",esp_err_to_name(err));
            /* Keep panel accessible; caller must handle power/backlight fault. */
        }
    }
    *panel_out=panel;
    ESP_LOGI(TAG,"ILI9341 initialized (hardware and wiring acceptance still required)");
    return ESP_OK;
}
