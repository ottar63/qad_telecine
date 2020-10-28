$fn=120;
spindle_traction();
translate([30,0,0])
spindle_top();
module spindle_traction() {
        difference () {
            cylinder(d=24,h=12);
            cylinder(d=5,h=12);
        }
        translate([0,0,12])
        difference(){
            cylinder(d=16,h=9);
            translate([-2,-2,1])
            #cube([4,4,8]);
        }
        translate([-4,-3,0])cube([2.5, 6, 8]);    
        translate([1.5,-3,0])cube([2.5,6, 8]);
       
}
module spindle_top() {
    cylinder(d=24,h=4);
    translate([-2,-2,2])
    cube([4,4,7]);
}