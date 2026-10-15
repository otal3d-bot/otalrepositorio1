"""Exporta os nove STL com as orientações de impressão do CAD."""
import concurrent.futures
import os
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
(root / 'stl').mkdir(exist_ok=True)
parts = [(p, p, None) for p in ['base', 'guarda_sol', 'porta_vara_direita', 'borboleta', 'sapata']]
parts += [(f'bucha_{d}mm', 'bucha', d) for d in [22, 25, 28, 32]]

def export(part):
    name, selector, diameter = part
    command = ['openscad', '--export-format', 'binstl', '-o', str(root/'stl'/f'{name}.stl'), '-D', f'peca="{selector}"']
    if diameter:
        command += ['-D', f'diametro_bucha={diameter}']
    command += [str(root/'conjunto.scad')]
    subprocess.run(command, check=True, env=os.environ | {'QT_QPA_PLATFORM': 'offscreen'})
    print(name, 'OK', flush=True)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    list(pool.map(export, parts))
