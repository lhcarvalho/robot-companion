// RC-MECH-003: DESK ASSEMBLY / PACKAGING STUDY V0.2
// Units: mm. PLACEHOLDER dimensions are deliberately exposed below.
// NOT READY FOR PRINTING. Component volumes are NOT vendor STEP models.
$fn=48;
show_shell=true;
show_parts=true;
show_assembly=true;
// Approved / documented module outlines:
head_w=105; head_h=85; head_depth=60;
lcd_w=70.5; lcd_h=43.3;
camera_w=32; camera_h=32;
// STEP assembly extents measured by CadQuery/OCP from Waveshare model 20250427;\n// axis order and origin of conceptual torso placement remain assumptions:
board_w=88.3591; board_d=57.0910; board_stack_h=20.1000; // official STEP whole-assembly bounding extents, NOT bare PCB outline
torso_w=125; torso_depth=100; torso_h=61; // design allowance, NOT approved dimensions
wall=2.4; foot_d=113; foot_h=14;
pcb_z=34; head_center_z=107.5; // bbox center is assumed placement, not manufacturer mounting plane
neck_pan_z=65; neck_tilt_z=77; // proxies only
speaker_d=40; speaker_depth=14; // placeholder 8 ohm 2W driver
power_space_w=36; power_space_d=25; power_space_h=18; // PSU/connector allowance
// Overall envelope: desk bottom z=0, head top z=150.
// NOTE: head bottom z=65, torso top z=75; intentional proxy intersection,
// not a real mechanical mechanism.

module rbox(w,d,h,r=9) {
  hull() for (x=[-w/2+r,w/2-r], y=[-d/2+r,d/2-r], z=[-h/2+r,h/2-r])
    translate([x,y,z]) sphere(r=r);
}
module shell_proxy() {
  difference() {
    translate([0,0,44.5]) rbox(torso_w,torso_depth,torso_h,12);
    translate([0,0,44.5]) rbox(torso_w-2*wall,torso_depth-2*wall,torso_h-2*wall,12-wall);
  }
}
module electronics() {
  // Whole-board STEP extents measured; location and port orientation NOT yet aligned
  color([0.03,0.39,0.27,0.5])
   translate([0,0,pcb_z])
   cube([board_w,board_d,board_stack_h],center=true);
  // No mounting holes or real connectors yet. Bounding volume only.
  // speaker behind front grill at front (-Y); driver depth and mount unverified
  color([0.24,0.28,0.33])
    translate([0,-torso_depth/2+speaker_depth/2+wall,49])
      rotate([90,0,0]) cylinder(d=speaker_d,h=speaker_depth,center=true);
  // power connector/regulator *reservation* near rear; do not equate with battery
  color([0.93,0.53,0.11,0.55])
   translate([0,torso_depth/2-power_space_d/2-wall,20])
   cube([power_space_w,power_space_d,power_space_h],center=true);
}
module neck_proxy(){
  color([0.23,0.26,0.33])
   translate([0,0,neck_pan_z]) cylinder(d=28,h=14,center=true);
  color([0.52,0.56,0.6])
   for(x=[-49,49]) translate([x,0,neck_tilt_z])
     cube([4,24,23],center=true);
}
module head_proxy(){
  color([0.82,0.85,0.9,0.28])
    translate([0,0,head_center_z]) rbox(head_w,head_depth,head_h,14);
  // front = negative Y
  color([0.12,0.48,0.22])
    translate([0,-head_depth/2+7,head_center_z-15])
    cube([lcd_w,2, lcd_h],center=true);
  color([0.07,0.08,0.1])
    translate([0,-head_depth/2+5,head_center_z-15])
    cube([48.96,1.3,36.72],center=true);
  color([0.13,0.34,0.65])
    translate([0,-head_depth/2+17,head_center_z+22])
    cube([camera_w,2,camera_h],center=true);
  color([0.11,0.13,0.16])
    translate([0,-head_depth/2+7,head_center_z+22])
      rotate([90,0,0]) cylinder(d=14,h=11,center=true);
}
module foot(){
  color([0.65,0.68,0.73,0.55])
    translate([0,0,foot_h/2]) cylinder(d=foot_d,h=foot_h,center=true);
}
if(show_assembly){
 foot();
 if(show_shell) color([0.8,0.83,0.87,0.20]) shell_proxy();
 if(show_parts) electronics();
 neck_proxy();
 head_proxy();
}
// Test mechanical checks are intentionally NOT declared passed.
// P4 vendor STEP bounding box measured; but connector coordinates, mounting holes and front acoustic path,
// real head and servo mass/COM, cable flex and fasteners are missing.
