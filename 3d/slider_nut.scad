$fn=60;
w=40;
slider_nut_holder();
translate([-5,10,0])
    rotate([0,0,180])
    slider_nut_cover();
module slider_nut_holder () 
{
    
    difference() {
    cube([w,10,44]);
    translate([0,0,32])
        cube([w,8,10]);
    translate([w/2,0,10]){
        rotate([-90,0,0]){
            cylinder(d=6.2,10);
            cylinder(d=11.8,5.5,$fn=6);
            }
        }
    
    translate([5,0,5])
        rotate([-90,0,0])
        cylinder(d=3,h=10);
    translate([w-5,0,5])
        rotate([-90,0,0])
        cylinder(d=3,h=10);
    translate([5,0,27])
        rotate([-90,0,0])
        cylinder(d=3,h=10);
    translate([w-5,0,27])
        rotate([-90,0,0])
        cylinder(d=3,h=10);
    }
}
module slider_nut_cover () {
    difference() {
        cube([w,4,44]);
        
        translate([0,2,32])
            cube([w,2,10]);
        translate([5,0,5])
            rotate([-90,0,0])
            cylinder(d=3,h=10);
        translate([w-5,0,5])
            rotate([-90,0,0])
            cylinder(d=3,h=10);
        translate([5,0,27])
            rotate([-90,0,0])
            cylinder(d=3,h=10);
        translate([w-5,0,27])
            rotate([-90,0,0])
            cylinder(d=3,h=10);
        translate([w/2,0,10])
            rotate([-90,0,0])
                cylinder(d=6.2,10);
        
    }
}