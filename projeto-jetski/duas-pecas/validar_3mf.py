"""Verifica o projeto entregue, seus dois objetos e o G-code efetivamente gerado."""
from pathlib import Path
import hashlib,json,re,sys,xml.etree.ElementTree as ET,zipfile
root=Path(__file__).resolve().parent
path=Path(sys.argv[1]) if len(sys.argv)>1 else root/'completo_duas_pecas_facetado.3mf'
report={'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
with zipfile.ZipFile(path) as z:
    assert z.testzip() is None, 'Falha de integridade ZIP'
    model=ET.fromstring(z.read('3D/3dmodel.model'))
    objects=model.findall('./{*}resources/{*}object')
    items=model.findall('./{*}build/{*}item')
    assert len(objects)==len(items)==2, 'Esperadas exatamente duas peças'
    config=json.loads(z.read('Metadata/project_settings.config'))
    assert config['wall_loops']=='3'
    assert config['sparse_infill_density']=='15%'
    assert config['sparse_infill_pattern']=='gyroid'
    assert config['enable_support']=='0', 'O arquivo final deve abrir com suportes desligados'
    report.update(objects=2,wall_loops=3,infill='15% gyroid',layer_height_mm=config['layer_height'],enable_support=False,plates=[])
    for name in z.namelist():
        if not name.endswith('.gcode'):continue
        g=z.read(name).decode()
        assert 'G1 ' in g, 'G-code sem movimentos'
        features=set(re.findall(r'^; FEATURE: ([^\r\n]+)',g,re.M))
        assert not any('support' in v.lower() for v in features), 'Há trajetórias de suporte'
        lines=[l for l in g.splitlines() if 'total estimated time:' in l or 'total filament weight' in l]
        assert len(lines)==2, 'Estimativas não encontradas'
        report['plates'].append({'gcode':name,'support_features':0,'statistics':lines})
    assert report['plates'], 'Nenhuma mesa foi fatiada'
    settings=ET.fromstring(z.read('Metadata/model_settings.config'))
    stats=[v.attrib for v in settings.findall('.//mesh_stat')]
    assert len(stats)==2
    assert all(int(s.get('edges_fixed',0))==int(s.get('facets_removed',0))==int(s.get('facets_reversed',0))==0 for s in stats), 'O fatiador precisou reparar malhas'
    report['mesh_statistics']=stats
report['stl_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'stl').glob('*.stl')}
(root/'validacao-3mf.json').write_text(json.dumps(report,indent=2)+'\n')
(root/'estimativas.json').write_text(json.dumps({'source':'Bambu Studio 02.08.02.61','estimated_not_measured':True,'plates':report['plates']},indent=2)+'\n')
print(json.dumps(report,indent=2))
