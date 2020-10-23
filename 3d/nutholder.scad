$fn=60;
difference () {
    cylinder(d=16,h=10);
    cylinder(d=10,h=5,$fn=6);
    cylinder(d=5.1,h=10);
}
translate([1.5,-3,5])
    cube([3,6,5]);
translate([-1.5-3,-3,5])
    cube([3,6,5]);