#ifndef ROBOT_MOTION_SAFETY_H
#define ROBOT_MOTION_SAFETY_H
#include <stdbool.h>
#include <stdint.h>

typedef struct {
    bool armed;
    bool fault_latched;
    bool bumper_clear;
    bool cliff_clear;
    bool supply_ok;
    uint32_t expires_at_ms;
    int16_t left_permille;
    int16_t right_permille;
} motion_safety_t;

void motion_safety_init(motion_safety_t *s);
void motion_safety_update_inputs(motion_safety_t *s, bool bumper_clear, bool cliff_clear, bool supply_ok);
bool motion_safety_command(motion_safety_t *s, uint32_t now_ms, int16_t left, int16_t right, uint16_t duration_ms);
void motion_safety_tick(motion_safety_t *s, uint32_t now_ms);
void motion_safety_emergency_stop(motion_safety_t *s);
bool motion_safety_reset_fault(motion_safety_t *s);
#endif
