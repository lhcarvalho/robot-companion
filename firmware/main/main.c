#include <stdint.h>
#include <stdbool.h>
#include "esp_log.h"
#include "esp_chip_info.h"
#include "esp_idf_version.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

static const char *TAG = "robot_companion";

void app_main(void)
{
    esp_chip_info_t chip_info;
    esp_chip_info(&chip_info);
    ESP_LOGI(TAG, "Robot Companion P4 scaffold; ESP-IDF %s", esp_get_idf_version());
    ESP_LOGI(TAG, "Chip cores: %d", chip_info.cores);
    ESP_LOGW(TAG, "Motor outputs disabled. LCD, CSI, audio and wireless are NOT configured.");
    while (true) {
        ESP_LOGI(TAG, "Heartbeat; safe idle");
        vTaskDelay(pdMS_TO_TICKS(5000));
    }
}
