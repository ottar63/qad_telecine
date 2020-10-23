$fn=60;
w=30;
d=10;
h=30;
difference () {
    
    cube([w,d,h]);
   
    translate([w/2-22/2,2,2])
        cube([22,20,40]);
    
    translate([w/2-8/2,0,10])
        cube([10,5,25]);
        //#cylinder(d=4,h=10);
    translate([w/2-24.4/2,5+2,2])
        cube([24.4,1.5,h]);
     translate([-10,0,15])
        rotate([-90,0,0])
        cylinder(d=3,h=2);
     translate([40,0,15])   
       rotate([-90,0,0])
       cylinder(d=3,h=2);
     
 }
 difference() {
 translate([w,8,0])
    cube([10,2,20]);
 translate([w+5,8,15])
     rotate([-90,0,0])
     #cylinder(d=3,h=2);
 }
 difference() {
 translate([-10,8,0])
     cube([10,2,20]);
 translate([-5,8,15])
     rotate([-90,0,0])
     #cylinder(d=3,h=2);
 }
//difference(){
//    translate([-20,0,0])
//        cube([20,2,30]);
//    translate([-10,0,20])
//        rotate([-90,0,0])
//        cylinder(d=3,h=2);
//}
//difference(){
//        translate([30,0,0])
//            cube([20,2,30]);
//        translate([40,0,20])
//            rotate([-90,0,0])
//            #cylinder(d=3,h=2);
//}