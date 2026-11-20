#include "motion_safety.h"
#include <stddef.h>

#define MAX_ABS_SPEED_PERMILLE 300
#define MAX_COMMAND_MS 1000

static bool ready(const motion_safety_t *s) {
    return s && !s->fault_latched && s->bumper_clear && s->cliff_clear && s->supply_ok;
}
static void stop(motion_safety_t *s) {
    s->armed = false;
    s->left_permille = 0;
    s->right_permille = 0;
}
void motion_safety_init(motion_safety_t *s) {
    if (!s) return;
    *s = (motion_safety_t){0}; /* Power-on: all safety inputs unknown -> STOP. */
}
void motion_safety_update_inputs(motion_safety_t *s, bool bumper_clear, bool cliff_clear, bool supply_ok) {
    if (!s) return;
    s->bumper_clear = bumper_clear;
    s->cliff_clear = cliff_clear;
    s->supply_ok = supply_ok;
    if (!bumper_clear || !cliff_clear || !supply_ok) {
        s->fault_latched = true;
        stop(s);
    }
}
bool motion_safety_command(motion_safety_t *s, uint32_t now_ms, int16_t left, int16_t right, uint16_t duration_ms) {
    if (!ready(s) || duration_ms == 0 || duration_ms > MAX_COMMAND_MS ||
        left > MAX_ABS_SPEED_PERMILLE || left < -MAX_ABS_SPEED_PERMILLE ||
        right > MAX_ABS_SPEED_PERMILLE || right < -MAX_ABS_SPEED_PERMILLE) return false;
    s->expires_at_ms = now_ms + duration_ms;
    s->left_permille = left;
    s->right_permille = right;
    s->armed = true;
    return true;
}
void motion_safety_tick(motion_safety_t *s, uint32_t now_ms) {
    if (!s) return;
    if (!ready(s) || (s->armed && (int32_t)(now_ms - s->expires_at_ms) >= 0)) stop(s);
}
void motion_safety_emergency_stop(motion_safety_t *s) {
    if (!s) return;
    s->fault_latched = true;
    stop(s);
}
bool motion_safety_reset_fault(motion_safety_t *s) {
    if (!s || !s->bumper_clear || !s->cliff_clear || !s->supply_ok) return false;
    stop(s);
    s->fault_latched = false;
    return true;
}
