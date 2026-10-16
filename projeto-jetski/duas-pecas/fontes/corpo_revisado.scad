// Revisão local sobre a malha original do usuário: continua uma única peça.
$fn=96;
module apoio_copo(cx,cy) {
    // Só adiciona material sob os fundos; mantém o volume interno do pedestal.
    difference() {
        hull() {
            translate([0,cy>0?34:-34,20]) cylinder(r=3,h=.1,$fn=8);
            translate([cx,cy,73.17]) cylinder(r=37.25,h=15.68,$fn=8);
        }
        translate([0.03268,1.25774,-1]) cylinder(r=44,h=91);
    }
}
module capa_tubo(cx,cy) {
    translate([cx,cy,0]) difference() {
        union() {
            hull() {
                translate([0,0,88.65]) cylinder(r=33.5,h=.1,$fn=12);
                translate([0,0,93]) cylinder(r=35.7,h=.1,$fn=12);
            }
            translate([0,0,93]) cylinder(r=35.7,h=120.8,$fn=12);
        }
        translate([0,0,88]) cylinder(r=33.4,h=128);
    }
}
module capa_pedestal() {
    translate([0.03268,1.25774,0]) difference() {
        union() {
            hull() {
                translate([0,0,9.9]) cylinder(r=44,h=.1,$fn=12);
                translate([0,0,15.5]) cylinder(r=46.9,h=.1,$fn=12);
            }
            translate([0,0,15.5]) cylinder(r=46.9,h=62.5,$fn=12);
        }
        translate([0,0,8]) cylinder(r=44.5,h=71);
    }
}
module arco_ligacao(z) {
    // Duas rampas formando um arco sob cada ligação entre os tubos.
    translate([-10.179,0,z]) rotate([0,0,7.05]) rotate([90,0,90])
        linear_extrude(height=8.5,center=true)
            polygon([[-6,-6*sqrt(3)],[-6,.15],[6,.15],[6,-6*sqrt(3)],[0,0]]);
}
union() {
    translate([0,0,107.950005]) union() {
        import("original_corpo_shell_0.stl");
        import("original_corpo_shell_1.stl");
    }
    capa_tubo(-5.3233,-39.26);
    capa_tubo(-15.0345,39.26);
    capa_pedestal();
    apoio_copo(-5.3233,-39.26);
    apoio_copo(-15.0345,39.26);
    arco_ligacao(142.365);
    arco_ligacao(199.515);
    // Três pequenos ressaltos diagonais, sem tocar furos ou encaixes.
    for(y=[-12,0,12]) translate([0,y,0]) rotate([90,0,0])
        linear_extrude(height=3,center=true)
            polygon([[41,30],[41.1,30],[47,37],[47,57],[43,62],[41,62]]);
}
