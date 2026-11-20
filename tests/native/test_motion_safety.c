#include "motion_safety.h"
#include <assert.h>
#include <stdio.h>
#include <stdint.h>
int main(void) {
  motion_safety_t s;
  motion_safety_init(&s);
  assert(!s.armed && !motion_safety_command(&s, 100, 200, 200, 100));
  motion_safety_update_inputs(&s, true, true, true);
  assert(!motion_safety_command(&s, 100, 301, 100, 100));
  assert(!motion_safety_command(&s, 100, 100, 100, 1001));
  assert(!motion_safety_command(&s, 100, 100, 100, 0));
  assert(motion_safety_command(&s, 100, 200, -200, 250));
  motion_safety_tick(&s, 349); assert(s.armed);
  motion_safety_tick(&s, 350); assert(!s.armed && s.left_permille == 0);
  assert(motion_safety_command(&s, 400, 100, 100, 500));
  motion_safety_update_inputs(&s, true, false, true);
  assert(s.fault_latched && !s.armed);
  assert(!motion_safety_reset_fault(&s));
  motion_safety_update_inputs(&s, true, true, true);
  assert(!motion_safety_command(&s, 400, 100, 100, 100));
  assert(motion_safety_reset_fault(&s));
  assert(motion_safety_command(&s, 500, 100, 100, 100));
  motion_safety_emergency_stop(&s); assert(!s.armed && s.fault_latched);
  assert(motion_safety_reset_fault(&s));
  assert(motion_safety_command(&s, UINT32_MAX - 40, -150, 150, 100));
  motion_safety_tick(&s, 40); assert(s.armed);
  motion_safety_tick(&s, 58); assert(s.armed);
  motion_safety_tick(&s, 59); assert(!s.armed);
  puts("motion_safety: all 18 checks passed");
  return 0;
}
