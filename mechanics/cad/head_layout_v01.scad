// Robot Companion - head layout / envelope feasibility model v0.1
// Dimensions in mm. NOT a manufacturing-ready shell.
// Reference dimensions: Waveshare LCD 2.4in 70.5x43.3; RPi Camera (B) 32x32.
// Unverified proxies: PCB thickness, active-area placement, lens offsets/length,
// fastener locations, connector envelopes, cable bend radius and servo geometry.
$fn = 48;
head_w = 105;
head_h = 85;
head_d = 60;
corner_r = 14;
wall = 2.4;
lcd_w = 70.5;
lcd_h = 43.3;
lcd_thick = 1.6; // placeholder, measure actual PCB
lcd_active_w = 48.96;
lcd_active_h = 36.72;
lcd_y = -15;
lcd_z = 23;
cam_w = 32;
cam_h = 32;
cam_thick = 1.6; // placeholder
cam_y = 22;
cam_z = 10;
lens_d = 14; // NOT measured: design allowance only
lens_to_front = 19; // NOT measured: proxy, actual lens geometry is required
front_z = head_d/2;
show_shell = true;
show_components = true;
show_clearance = true;

module rounded_2d(w,h,r) {
    offset(r=r) square([w-2*r,h-2*r],center=true);
}
module rounded_box(w,h,d,r) {
    linear_extrude(height=d,center=true) rounded_2d(w,h,r);
}
module head_shell() {
    // Representative empty shell to visualize volumes, not printable geometry.
    difference() {
        rounded_box(head_w,head_h,head_d,corner_r);
        rounded_box(head_w-2*wall,head_h-2*wall,head_d-2*wall,corner_r-wall);
        // Front LCD viewport, size based on *active area* only. Alignment TBD.
        translate([0,lcd_y,front_z-wall/2])
            cube([lcd_active_w+1,lcd_active_h+1,wall+3],center=true);
        // Camera lens clearance (diameter provisional).
        translate([0,cam_y,front_z-wall/2])
            cylinder(h=wall+3,d=lens_d+2,center=true);
    }
}
module components() {
    // Front surface is +Z, vertical coordinate +Y.
    color([0.10,0.50,0.25])
        translate([0,lcd_y,lcd_z])
            cube([lcd_w,lcd_h,lcd_thick],center=true);
    color([0.04,0.07,0.11])
        translate([0,lcd_y,lcd_z+lcd_thick/2+0.2])
            cube([lcd_active_w,lcd_active_h,0.4],center=true);
    color([0.18,0.42,0.75])
        translate([0,cam_y,cam_z])
            cube([cam_w,cam_h,cam_thick],center=true);
    color([0.10,0.12,0.15])
        translate([0,cam_y,cam_z+cam_thick/2])
            cylinder(h=lens_to_front,d=lens_d);
}
if (show_shell) color([0.8,0.82,0.84],0.28) head_shell();
if (show_components) components();
// Debug volumes: optional cable exit / neck keepout (not a designed joint)
if (show_clearance) {
    color([1,0.4,0.1],0.25)
    translate([0,-head_h/2+9,-3]) cube([20,12,head_d-12],center=true);
}
