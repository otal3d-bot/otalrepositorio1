"""Gera perfis completos a partir dos perfis oficiais e fatia no Bambu Studio."""
import json
import os
import subprocess
import time
from pathlib import Path

root = Path(__file__).parent
tools = Path(os.environ.get('JETSKI_TOOLS', '/workspace/onboarding'))
profiles = tools / 'squashfs-root/resources/profiles/BBL'
out = root / 'perfis'
out.mkdir(exist_ok=True)
index = {}
for path in sorted(profiles.rglob('*.json')):
    try:
        data = json.loads(path.read_text())
        if 'name' in data:
            index[data['name']] = data
    except (ValueError, UnicodeDecodeError):
        continue

def resolve(name):
    data = index[name]
    result = resolve(data['inherits']) if data.get('inherits') else {}
    for include in data.get('include', []):
        result.update(resolve(include))
    result.update(data)
    result.pop('include', None)
    result.pop('inherits', None)
    return result

machine = resolve('Bambu Lab A1 0.4 nozzle')
process = resolve('0.24mm Draft @BBL A1')
process.update({
    'name': 'Jetski prototipo PETG V3 0.24mm 3 paredes 15% gyroid',
    'from': 'User', 'print_settings_id': 'Jetski prototipo PETG V3 0.24mm 3 paredes 15% gyroid',
    'layer_height': '0.24', 'initial_layer_print_height': '0.24',
    'wall_loops': '3', 'top_shell_layers': '6', 'bottom_shell_layers': '6',
    'sparse_infill_density': '15%', 'sparse_infill_pattern': 'gyroid',
    'enable_support': '0', 'brim_type': 'outer_only', 'brim_width': '6',
    'brim_object_gap': '0.15', 'outer_wall_speed': '45',
    'inner_wall_speed': '70', 'sparse_infill_speed': '80',
    'internal_solid_infill_speed': '70', 'top_surface_speed': '40',
    'initial_layer_speed': '25', 'initial_layer_infill_speed': '35',
    'curr_bed_type': 'Textured PEI Plate',
    'bridge_speed': '25', 'default_acceleration': ['2000'],
    'outer_wall_acceleration': '1000', 'print_sequence': 'by layer',
})
filament = resolve('Generic PETG @BBL A1')
filament.update({
    'name': 'Jetski PETG generico A1 8mm3s', 'from': 'User',
    'filament_settings_id': ['Jetski PETG generico A1 8mm3s'],
    'filament_max_volumetric_speed': ['8'],
})
for name, data in [('A1-0.4', machine), ('processo-PETG', process), ('filamento-PETG', filament)]:
    (out / f'{name}.json').write_text(json.dumps(data, indent=2)+'\n')

env = dict(os.environ)
env['LD_LIBRARY_PATH'] = ':'.join(map(str, [
    tools/'apt/root/usr/lib/x86_64-linux-gnu', tools/'squashfs-root/bin'
]))
env['XDG_CONFIG_HOME'] = str(tools/'config')
env['XDG_CACHE_HOME'] = str(tools/'cache')
runtime = tools/'runtime'
runtime.mkdir(exist_ok=True, mode=0o700)
env['XDG_RUNTIME_DIR'] = str(runtime)
env['DISPLAY'] = ':197'
env['GDK_BACKEND'] = 'x11'
env['XDG_SESSION_TYPE'] = 'x11'
command = [str(tools/'squashfs-root/bin/bambu-studio'),
    '--datadir', str(tools/'bambu-data'), '--debug', '2',
    '--load-settings', f'{out}/A1-0.4.json;{out}/processo-PETG.json',
    '--load-filaments', str(out/'filamento-PETG.json'),
    '--orient', '0', '--arrange', '1', '--ensure-on-bed',
    '--slice', '0', '--export-3mf', 'Jetski_A1_PETG_V3_FACETADO_25GRAUS.3mf',
    '--outputdir', str(root/'fatiamento'),
]
(root/'fatiamento').mkdir(exist_ok=True)
files = ['base', 'guarda_sol', 'porta_vara_direita', 'bucha_28mm', 'bucha_25mm',
         'borboleta', 'borboleta', 'sapata', 'sapata']
command.extend(str(root/'stl'/f'{name}.stl') for name in files)
display = subprocess.Popen([str(tools/'apt/root/usr/bin/Xvfb'), ':197',
                           '-screen', '0', '1280x1024x24', '-nolisten', 'tcp'],
                          env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    time.sleep(0.5)
    if display.poll() is not None:
        raise RuntimeError('O display virtual não iniciou')
    with (root/'bambu-studio.log').open('w') as log:
        result = subprocess.run(command, env=env, stdout=log, stderr=subprocess.STDOUT)
finally:
    display.terminate()
    display.wait()
if result.returncode == 0:
    import shutil
    shutil.copy2(root/'fatiamento/Jetski_A1_PETG_V3_FACETADO_25GRAUS.3mf', root/'Jetski_A1_PETG_V3_FACETADO_25GRAUS.3mf')
print('Bambu Studio exit:', result.returncode)
print((root/'bambu-studio.log').read_text()[-7000:])
raise SystemExit(result.returncode)
