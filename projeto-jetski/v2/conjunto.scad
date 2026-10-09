// Protótipo V2: somente base circular, porta-varas inclinados.
// Interface de fixação candidata e resistência SEM validação física.
$fn=96;
peca="base";
diametro_bucha=28;
angulo_vara=25; // em graus, em relação à vertical, abertura para fora
folga_diametral=0.6;
furos_oem=[[58.10935,-1.01371],[-16.06119,-55.94250],[-14.63087,56.77056]];
centro_guarda=[0,-27];
centro_vara=[34,28];
fixacoes_vara=[[-22,22],[-18,-22]];

module prisma_hex(af,h) { cylinder(d=af/cos(30),h=h,$fn=6); }
module furo_gota(d,comprimento) {
    rotate([90,0,90]) linear_extrude(height=comprimento,center=true)
        union() {
            circle(d=d,$fn=48);
            polygon([[-d/2*sqrt(0.5),d/2*sqrt(0.5)],
                     [0,d/2*sqrt(2)],
                     [d/2*sqrt(0.5),d/2*sqrt(0.5)]]);
        }
}

module boss_aperto(raio,z=110) {
    // A porca metálica entra por cima; o reforço inferior cresce gradualmente.
    hull() {
        translate([-9,raio-4,z-32]) cube([18,4,1]);
        translate([-9,raio-2,z-7]) cube([18,42-(raio-2),14]);
    }
}
module cortes_aperto(z=110,compensacao=0) {
    translate([0,30,z]) rotate([0,-compensacao,0]) rotate([0,0,90]) furo_gota(6.6,34);
    // Porca M6 normal, AF 10 mm, espessura nominal 5 mm.
    translate([-5.3,32,z-6.2]) cube([10.6,5.6,25]);
}

module base() {
    difference() {
        union() {
            cylinder(d=140,h=10); // contorno circular, sem abas
            translate([centro_guarda[0],centro_guarda[1],10]) prisma_hex(44,28);
        }
        for(p=furos_oem) {
            translate([p[0],p[1],-1]) cylinder(d=7,h=12);
            translate([p[0],p[1],4]) cylinder(d=14,h=7);
        }
        for(p=fixacoes_vara)
            translate([centro_vara[0]+p[0],centro_vara[1]+p[1],-1])
                cylinder(d=6.6,h=12);
        translate([centro_guarda[0],centro_guarda[1],28]) furo_gota(6.6,65);
    }
}

module pe_vara() {
    // O pé segue a seção elíptica da raiz, com duas fixações compactas.
    // Recorte limita o seu contorno ao disco da base; não cria abas externas.
    intersection() {
        hull() {
            scale([1/cos(angulo_vara),1,1]) cylinder(d=46,h=8);
            for(p=fixacoes_vara) translate([p[0],p[1],0]) cylinder(d=16,h=8);
        }
        translate([-centro_vara[0],-centro_vara[1],0]) cylinder(d=140,h=8);
    }
}

module corpo_vara() {
    difference() {
        union() {
            pe_vara();
            // Tubo começa abaixo da mesa e é cortado no plano z=0.
            // Cada camada da parede inclinada se apoia na camada anterior.
            intersection() {
                rotate([0,angulo_vara,0]) translate([0,0,-40]) cylinder(d=46,h=190);
                translate([-100,-100,0]) cube([250,200,180]);
            }
            rotate([0,angulo_vara,0]) boss_aperto(23);
        }
        // Fundo maciço inclinado; abertura interna de 36 mm.
        rotate([0,angulo_vara,0]) translate([0,0,24]) cylinder(d=36,h=150);
        translate([0,0,-1]) cylinder(d=8,h=40);
        for(p=fixacoes_vara) translate([p[0],p[1],-1]) cylinder(d=6.6,h=10);
        rotate([0,angulo_vara,0]) cortes_aperto(compensacao=angulo_vara);
    }
}

module porta_vara_direita() { corpo_vara(); }

module guarda_sol() {
    difference() {
        union() {
            cylinder(d=56,h=150);
            boss_aperto(28);
        }
        translate([0,0,-1]) prisma_hex(44+folga_diametral,30);
        hull() {
            translate([0,0,28]) prisma_hex(44+folga_diametral,0.1);
            translate([0,0,39]) cylinder(d=36,h=0.1);
        }
        translate([0,0,38.9]) cylinder(d=36,h=112);
        translate([0,0,18]) furo_gota(6.6,80);
        cortes_aperto();
    }
}

module bucha(d=28) {
    difference() {
        union() {
            cylinder(d=40,h=3);
            translate([0,0,3]) cylinder(d=35.5,h=60);
        }
        translate([0,0,-1]) cylinder(d=d+0.5,h=65);
        translate([-0.8,0,-1]) cube([1.6,25,65]);
        // Janela para a sapata do parafuso. Teto inclinado a 45°, sem suporte.
        translate([0,12.5,0]) rotate([90,0,0])
            linear_extrude(height=25,center=true)
                polygon([[-7,31],[7,31],[7,51],[0,58],[-7,51]]);
    }
}

module borboleta() {
    difference() {
        hull() {
            cylinder(d=20,h=10);
            for(x=[-18,18]) translate([x,0,0]) cylinder(d=12,h=10);
        }
        translate([0,0,-1]) cylinder(d=6.6,h=12);
        translate([0,0,5.2]) prisma_hex(10.4,6);
    }
}
module sapata() {
    difference() {
        hull() for(x=[-3,3],y=[-3,3]) translate([x,y,0]) cylinder(d=6,h=5);
        translate([0,0,2.5]) cylinder(d=6.4,h=3.5);
    }
}

module central_montado() { translate([centro_guarda[0],centro_guarda[1],10]) guarda_sol(); }
module direita_montada() { translate([centro_vara[0],centro_vara[1],10]) porta_vara_direita(); }
module montagem() {
    color("SlateGray") base();
    color("DarkOrange") central_montado();
    color("RoyalBlue") direita_montada();
    color("Gold") translate([centro_guarda[0],centro_guarda[1],163]) rotate([180,0,0]) bucha(28);
    color("Gold") translate([34+153*sin(angulo_vara),28,10+153*cos(angulo_vara)])
        rotate([0,angulo_vara,0]) rotate([180,0,0]) bucha(25);
    color("Gold") translate([0,-27+57,120]) rotate([-90,0,0]) borboleta();
    color("Gold") translate([34+110*sin(angulo_vara),28+57,10+110*cos(angulo_vara)])
        rotate([-90,0,0]) borboleta();
}

if(peca=="base") base();
if(peca=="porta_vara_direita") porta_vara_direita();
if(peca=="guarda_sol") guarda_sol();
if(peca=="bucha") bucha(diametro_bucha);
if(peca=="borboleta") borboleta();
if(peca=="sapata") sapata();
if(peca=="montagem") montagem();
if(peca=="colisao_central_direita") intersection() { central_montado(); direita_montada(); }
if(peca=="colisao_base_central") intersection() { base(); central_montado(); }
if(peca=="pe_fora_base") difference() {
    translate([centro_vara[0],centro_vara[1],0]) pe_vara();
    translate([0,0,-1]) cylinder(d=140,h=10);
}
