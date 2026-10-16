"""Loft exterior facetado e interior circular para a extensão de 45°."""
import numpy as np,struct,json
from pathlib import Path
r=Path(__file__).resolve().parent
cx=76.20766448;cy=1.18;curve_radius=45.;L=190.
sections=[]
for th in np.linspace(0,np.pi/4,25):
 p=np.array([cx-curve_radius*(1-np.cos(th)),cy+curve_radius*np.sin(th),0])
 tangent=np.array([-np.sin(th),np.cos(th),0]);bx=np.array([-np.cos(th),-np.sin(th),0])
 outer=34.3
 sections.append((p,tangent,bx,outer))
p0=sections[-1][0];a=sections[-1][1];b=sections[-1][2]
for t in np.linspace(5,L,38):sections.append((p0+t*a,a,b,34.3-min(t/140,1)*4.455))
def loft(name,inner=False):
 n=96 if inner else 12;vertices=[]
 for j,(p,tangent,bx,outer) in enumerate(sections):
  # Sobreposição de 0,1 mm na entrada para não deixar uma película no encaixe.
  if inner and j==0:p=p-tangent*.15
  if inner and j==len(sections)-1:p=p+tangent*2
  radius=20.6375 if inner else outer/np.cos(np.pi/12)
  for phi in np.linspace(0,2*np.pi,n,endpoint=False)+(np.pi/12 if not inner else 0):
   vertices.append(p+bx*radius*np.cos(phi)+np.array([0,0,(.77709086 if inner else 0)+radius*np.sin(phi)]))
 vertices=np.array(vertices);faces=[]
 for k in range(len(sections)-1):
  for j in range(n):
   a0=k*n+j;b0=k*n+(j+1)%n;c0=(k+1)*n+(j+1)%n;d0=(k+1)*n+j
   faces.extend([(a0,b0,c0),(a0,c0,d0)])
 for j in range(1,n-1):faces.append((0,j+1,j));last=(len(sections)-1)*n;faces.append((last,last+j,last+j+1))
 with (r/name).open('wb') as f:
  f.write(bytes(80));f.write(struct.pack('<I',len(faces)))
  for t in faces:
   v=vertices[list(t)];N=np.cross(v[1]-v[0],v[2]-v[0]);norm=np.linalg.norm(N)
   if norm:N/=norm
   f.write(struct.pack('<12fH',*N,*v.reshape(-1),0))
loft('curva_exterior.stl');loft('curva_interior.stl',True)
M=np.column_stack((b,np.array([0,0,1]),a))
config={'arc_radius_mm':curve_radius,'curve_angle_deg':45,'arm_length_before_tip_bevel_mm':L,'inner_radius_mm':20.6375,'inner_center_offset_mm':.77709086,'straight_start':p0.tolist(),'straight_a':a.tolist(),'straight_b':b.tolist(),'local_matrix':[[*M[i],float(p0[i])] for i in range(3)]+[[0,0,0,1]]}
(r/'curva-parametros.json').write_text(json.dumps(config,indent=2)+'\n')
# Abertura em U e entalhe com entradas inclinadas, sem tetos perpendiculares ao braço.
ms='['+','.join('['+','.join(str(float(v)) for v in row)+']' for row in config['local_matrix'])+']'
(r/'extensao_modelo.scad').write_text('''$fn=96;
module encaixe_original() {
    intersection() {
        import("original_2.stl");
        translate([-300,-300,-300]) cube([600,301.3174,600]);
    }
}
module corte_u() {
    // A janela termina em arco pontudo, apoiado nas duas paredes laterais.
    // Perfil no plano YZ, extrudido somente na metade aberta X<0.
    translate([-100,0,0]) rotate([90,0,90]) linear_extrude(height=100)
        polygon([[-60,25+60*4],[0,25],[60,25+60*4],
                 [60,400],[-60,400]]);
}
module entalhe() {
    rotate([90,0,0]) linear_extrude(height=100,center=true)
        polygon([[-25,155],[8,141.8],[8,155]]);
}
module limite_ponta() {
    rotate([90,0,0]) linear_extrude(height=200,center=true)
        polygon([[-100,-100],[100,-100],[100,400],[-100,400]]);
}
difference() {
union() {
    encaixe_original();
    intersection() {
        difference() {
            import("curva_exterior.stl");
            import("curva_interior.stl");
            multmatrix('''+ms+''') corte_u();
            // Bordas do berço contínuas: elimina abas que começariam suspensas.
        }
        multmatrix('''+ms+''') limite_ponta();
    }
}
    // Alívio de décimos na saída interna; não alcança a zona de encaixe Y<-5.
    translate([76.20766448,-4.5,.77709086]) rotate([-90,0,0])
        cylinder(r1=20.60,r2=20.66,h=6,$fn=96);
}
''')
print(config)
