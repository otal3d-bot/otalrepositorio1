"""Regenera as duas peças a partir das malhas originais e dos parâmetros."""
import os,subprocess,sys,shutil
from pathlib import Path
here=Path(__file__).resolve().parent
out=here.parent/'stl'
out.mkdir(exist_ok=True)
env=os.environ|{'QT_QPA_PLATFORM':'offscreen'}
def run(*args):subprocess.run(args,cwd=here,env=env,check=True)
run('openscad','--export-format','binstl','-o',str(out/'corpo_revisado.stl'),str(here/'corpo_revisado.scad'))
run(sys.executable,str(here/'gerar_curva_facetada.py'))
run('openscad','--export-format','binstl','-o',str(here/'extensao_parametrica.stl'),str(here/'extensao_modelo.scad'))
run(sys.executable,str(here/'orientar_extensao.py'))
run('openscad','--export-format','binstl','-o',str(out/'extensao_revisada.stl'),str(here/'extensao_revisada.scad'))

for name in ['alteracoes.json','curva-parametros.json']:
    shutil.copy2(here/name,here.parent/name)
