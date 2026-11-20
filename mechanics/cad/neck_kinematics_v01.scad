// Robot Companion V0.1: pan/tilt kinematic envelope only.
// NOT a final printable bracket. All units mm.
$fn=36;
pan_angle=0; pitch_angle=0; // target +/-45 and +/-20 degrees (unvalidated)
head_w=105; head_d=60; head_h=85; head_r=14;
head_z=107; pan_z=64; pitch_z=99;
servo_l=22.8; servo_w=12.2; servo_h=28.5; // TowerPro MG90S nominal dimensions
module rounded_box(w,d,h,r) {
 hull() for (x=[-w/2+r,w/2-r],y=[-d/2+r,d/2-r],z=[-h/2+r,h/2-r])
 translate([x,y,z]) sphere(r=r);
}
module head_proxy(){
 color([0.86,0.88,0.91,0.24]) rounded_box(head_w,head_d,head_h,head_r);
 // LCD and camera are nominal bounding volumes, not vendor STEP.
 color([0.08,0.35,0.16]) translate([0,-head_d/2+7,-15])
 cube([70.5,1.6,43.3],center=true);
 color([0.05,0.06,0.08]) translate([0,-head_d/2-0.6,-15])
 cube([48.96,0.6,36.72],center=true);
 color([0.13,0.32,0.7]) translate([0,-head_d/2+18,22])
 cube([32,1.6,32],center=true);
 color([0.06,0.08,0.1]) translate([0,-head_d/2+7,22])
 rotate([90,0,0]) cylinder(d=14,h=12,center=true);
}
module yoke(){
 color([0.52,0.55,0.61]){
  for(x=[-49,49]) translate([x,0,(pitch_z-pan_z)/2])
   cube([5,22,pitch_z-pan_z],center=true);
  translate([0,0,-1]) cylinder(d=40,h=7,center=true);
 }
 color([0.14,0.18,0.24]) translate([0,0,pitch_z-pan_z])
 rotate([0,90,0]) cylinder(d=8,h=106,center=true);
 // Tilt actuator body only; actual mounting shaft, horn and bearing TBD.
 color([0.19,0.24,0.31]) translate([-54,0,pitch_z-pan_z])
 rotate([0,90,0]) cube([servo_h,servo_l,servo_w],center=true);
}
module torso_proxy(){
 color([0.81,0.84,0.87,0.30]) translate([0,0,36])
 cylinder(h=54,d1=95,d2=85,center=true);
 color([0.19,0.24,0.31]) translate([0,0,47])
 cube([servo_l,servo_w,servo_h],center=true);
 color([0.52,0.56,0.62]) translate([0,0,pan_z-3])
 cylinder(h=8,d=28,center=true);
}
torso_proxy();
translate([0,0,pan_z]) rotate([0,0,pan_angle]){
 yoke();
 translate([0,0,pitch_z-pan_z]) rotate([pitch_angle,0,0])
 translate([0,0,head_z-pitch_z]) head_proxy();
}
color([1,0.55,0.08,0.25]) translate([0,17,pan_z+10])
 cylinder(h=25,d=15,center=true); // cable keepout, NOT cable bend design
