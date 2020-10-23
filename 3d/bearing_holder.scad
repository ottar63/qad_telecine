$fn=60;
bearing_holder();

module bearing_holder() {
    difference () {
        cube([40,20,40]);
        translate([0,0,27.8])
            cube([40,17.8,10.2]);
        translate([5,0,27.8+(10.2/2)])
            rotate([-90,0,0])
            cylinder(d=3,h=20);
        translate([35,0,27.8+(10.2/2)])
            rotate([-90,0,0])
            cylinder(d=3,h=20);
        translate([(40/2)-(22/2),0,40-2-9-22])
            cube([22,5,22]);
        translate([40/2,0,40-2-9-(22/2)])
            rotate([-90,0,0])
            cylinder(d=12,h=20);
    }
}
    