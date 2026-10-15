from pathlib import Path
import math,struct,json,collections
r=Path(__file__).resolve().parent
report={}
for p in sorted((r/'stl').glob('*.stl')):
 b=p.read_bytes();n=struct.unpack_from('<I',b,80)[0];assert len(b)==84+50*n
 edges=collections.Counter(); verts=[];volume=0;bad=[]
 for i in range(n):
  t=struct.unpack_from('<12fH',b,84+50*i);a,c,d=[tuple(t[j:j+3]) for j in [3,6,9]];vs=[a,c,d];verts+=vs
  for j in range(3):edges[tuple(sorted((vs[j],vs[(j+1)%3])))]+=1
  u=[c[k]-a[k] for k in range(3)];v=[d[k]-a[k] for k in range(3)]
  cross=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
  norm=math.sqrt(sum(x*x for x in cross))
  volume+=sum(a[k]*[c[1]*d[2]-c[2]*d[1],c[2]*d[0]-c[0]*d[2],c[0]*d[1]-c[1]*d[0]][k] for k in range(3))/6
  if norm and cross[2]/norm < -math.sqrt(.5)-1e-4 and max(q[2] for q in vs)>.25:
   bad.append({'area_mm2':norm/2,'center_mm':[sum(q[k] for q in vs)/3 for k in range(3)],'down_normal_z':cross[2]/norm})
 non=sum(v!=2 for v in edges.values())
 assert non==0,(p,non)
 report[p.name]={'triangles':n,'nonmanifold_edges':non,'dimensions_mm':[round(max(q[k] for q in verts)-min(q[k] for q in verts),3) for k in range(3)],'volume_cm3':round(abs(volume)/1000,3),'overhang_above_45_degrees_from_vertical_area_mm2':round(sum(f['area_mm2'] for f in bad),3),'flagged_faces':bad}
 print(p.name,'volume cm3',report[p.name]['volume_cm3'],'steep downward area',report[p.name]['overhang_above_45_degrees_from_vertical_area_mm2'])
 for f in sorted(bad,key=lambda f:-f['area_mm2'])[:5]:print(' ',f)
assert len(report)==9, 'Esperadas nove malhas STL'
assert all(d['overhang_above_45_degrees_from_vertical_area_mm2']==0 for d in report.values()), 'Há faces inferiores acima do limite de 45 graus'
(r/'validacao-malhas.json').write_text(json.dumps(report,indent=2)+'\n')
