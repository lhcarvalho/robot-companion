idf_component_register(SRCS "robot_display.c"
    INCLUDE_DIRS "include"
    REQUIRES esp_lcd esp_driver_spi esp_driver_gpio
    PRIV_REQUIRES esp_lcd_ili9341)
