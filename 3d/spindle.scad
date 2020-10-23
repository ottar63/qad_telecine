$fn=120;
spindle_base();
translate([0,0,12])
    spindle();
//spindle_guide();

module spindle() {
    difference(){
    cylinder(d=12.7,h=14);
    cylinder(d=8,h=10);
    }
    translate([0,0,14])
        sphere(d=12.7);
    for (f=[0:120:360])
        rotate([0,0,f])
            translate([12.7/2-0.5,0,0])
                cube([2,1.4,10]);
       
}


module spindle_base() {
    difference(){
        cylinder(d=26,h=12);
        cylinder(d=13.1,h=5);
        translate([0,0,5])
            sphere(d=13.1);
        //cylinder(d=13.3,h=5);
        cylinder(d=8,h=12);
    }
}

module spindle_guide () {
  difference() {
        union () {
        cylinder(d=26,h=1.5);
        cylinder(d=12,h=10);
        }
        cylinder(d=8,h=8);
    }
}