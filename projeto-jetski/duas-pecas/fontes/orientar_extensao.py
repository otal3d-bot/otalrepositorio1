import numpy as np,struct,json
from pathlib import Path
r=Path(__file__).resolve().parent
D=np.dtype([('normal','<f4',(3,)),('v','<f4',(3,3)),('attr','<u2')]);data=(r/'extensao_parametrica.stl').read_bytes();tri=np.frombuffer(data,offset=84,dtype=D)['v'].astype(float)
n=np.array([np.sin(np.deg2rad(3)),-np.cos(np.deg2rad(3)),0.]);x=np.cross([0,0,1],n);x/=np.linalg.norm(x);y=np.cross(n,x);M=np.stack((x,y,n));q=tri@M.T
lo=q.reshape(-1,3).min(axis=0);hi=q.reshape(-1,3).max(axis=0);cut=max(lo[2],hi[2]-254)
q-=np.array([0,0,cut]);out=np.zeros(len(q),dtype=D);out['v']=q
(r/'extensao_orientada_antes_bisel.stl').write_bytes(bytes(80)+struct.pack('<I',len(q))+out.tobytes())
T=np.eye(4);T[:3,:3]=M;T[2,3]=-cut
matrix='['+','.join('['+','.join(str(float(v)) for v in row)+']' for row in T)+']'
source=(r/'extensao_modelo.scad').read_text()
pos=source.index('difference() {\nunion()')
(r/'extensao_revisada.scad').write_text(source[:pos]+'\nintersection() {\n multmatrix('+matrix+') {\n'+source[pos:]+'\n}\n translate([-400,-400,0]) cube([800,800,300]);\n}\n')
report={'original_file':'completo.3mf','pieces':2,'extension_curve_deg':45,'extension_print_rotation':M.tolist(),'extension_print_translation_mm':T[:3,3].tolist(),'extension_before_foot_bevel_dimensions_mm':(hi-lo).tolist(),'non_mating_tip_bevel_max_depth_mm':float(cut-lo[2]),'target_height_mm':254,'protected_stem_original_y_max_mm':-5.03302,'extension_arm_length_before_tip_bevel_mm':190,'original_stem_outside_diameter_mm':59.69,'original_inner_diameter_mm':41.275}
(r/'alteracoes.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
