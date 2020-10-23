$fn=60;
gate_w=80;
gate();
translate([0,30,0])

// rotate([180,0,0])
cover();
module gate() {
    difference(){
        cube([gate_w,10,4]);
        translate([0,1,3])
            cube([gate_w,8,2]);
        translate([gate_w/2-(8/2),1.5])
            cube([8,7,4]);
    }
    difference (){
        union() {
            translate([0,10,0])
                cube([gate_w,15,2]);
            translate([0,-15,0])
                cube([gate_w,15,2]);
        }
        translate([5,17.5,0])
            cylinder(r=1.6,h=2);
        translate([gate_w-5,17.5,0])
            cylinder(r=1.6,h=2);
        translate([5,-7.5,0])
            cylinder(r=1.6,h=2);
        translate([gate_w-5,-7.5,0])
            cylinder(r=1.6,h=2);
    }
}

module cover() {
    difference(){
        cube([gate_w,40,4]);
        translate([gate_w/2-(8/2),20-5])
            cube([8,10,4]);
        translate([0,14.5,2])
            cube([gate_w,11,2]);
        translate([5,7.5,0])
            cylinder(r=1.6,h=4);
        translate([gate_w-5,7.5,0])
            cylinder(r=1.6,h=4);
        translate([5,32.5,0])
            cylinder(r=1.6,h=4);
        translate([gate_w-5,32.5,0])
            cylinder(r=1.6,h=4);
    }
        
    }
