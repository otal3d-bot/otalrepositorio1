import numpy as np,json
from pathlib import Path

def audit(path):
 p=Path(path);data=p.read_bytes();n=int.from_bytes(data[80:84],'little');assert len(data)==84+50*n
 dtype=np.dtype([('normal','<f4',(3,)),('v','<f4',(3,3)),('attr','<u2')]);tri=np.frombuffer(data,offset=84,dtype=dtype,count=n)['v'].astype(float)
 normal=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);area=np.linalg.norm(normal,axis=1)/2;nz=np.divide(normal[:,2],area*2,out=np.zeros(n),where=area>1e-10)
 steep=(nz<-.7072)&(np.max(tri[:,:,2],axis=1)>.25)
 unique,idx=np.unique(tri.reshape(-1,3),axis=0,return_inverse=True);f=idx.reshape(-1,3);edges=np.sort(np.vstack((f[:,[0,1]],f[:,[1,2]],f[:,[2,0]])),axis=1);e,cnt=np.unique(edges,axis=0,return_counts=True)
 parent=list(range(len(unique)))
 def root(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 for a,b in e:parent[root(int(a))]=root(int(b))
 components=len({root(i) for i in range(len(unique))})
 report={'file':p.name,'triangles':n,'nonmanifold_edges':int(np.count_nonzero(cnt!=2)),'connected_components':components,'bbox_min_mm':np.min(unique,axis=0).tolist(),'bbox_max_mm':np.max(unique,axis=0).tolist(),'dimensions_mm':np.ptp(unique,axis=0).tolist(),'steep_downward_area_mm2':float(area[steep].sum()),'steep_faces':int(steep.sum())}
 print(report)
 ids=np.where(steep)[0];ids=ids[np.argsort(-area[ids])]
 for i in ids[:15]:print('  ',float(area[i]),tri[i].mean(axis=0).tolist(),float(nz[i]))
 return report,tri,normal,area,steep
if __name__=='__main__':
 import sys
 reports=[audit(p)[0] for p in sys.argv[1:]]
 (Path(__file__).resolve().parent/'validacao-malhas.json').write_text(json.dumps(reports,indent=2)+'\n')
