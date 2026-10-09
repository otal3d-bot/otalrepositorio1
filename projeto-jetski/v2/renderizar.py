"""Renderiza a geometria real do protótipo, sem simular validação física."""
import bpy
import struct
from pathlib import Path
from mathutils import Vector

root = Path(__file__).parent
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def mesh(name, file, color, location=(0, 0, 0), flip=False):
    data = (root / 'stl' / file).read_bytes()
    vertices, faces = [], []
    for i in range(struct.unpack_from('<I', data, 80)[0]):
        d = struct.unpack_from('<12fH', data, 84 + 50*i)
        faces.append(tuple(range(len(vertices), len(vertices)+3)))
        vertices.extend([d[3:6], d[6:9], d[9:12]])
    geometry = bpy.data.meshes.new(name)
    geometry.from_pydata(vertices, [], faces)
    geometry.update()
    obj = bpy.data.objects.new(name, geometry)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    if flip:
        obj.rotation_euler[0] = 3.141592653589793
    obj.color = (*color, 1)
    return obj

mesh('Base', 'base.stl', (0.15, 0.19, 0.23))
mesh('Guarda-sol', 'guarda_sol.stl', (0.92, 0.36, 0.08), (0, -27, 10))
mesh('Porta-vara direito 25 graus', 'porta_vara_direita.stl', (0.10, 0.39, 0.58), (34, 28, 10))
mesh('Bucha 28 mm', 'bucha_28mm.stl', (0.98, 0.73, 0.16), (0, -27, 163), True)
from math import sin, cos, radians, pi
insert = mesh('Bucha porta-vara 25 mm', 'bucha_25mm.stl', (0.98, 0.73, 0.16),
              (34+153*sin(radians(25)),28,10+153*cos(radians(25))), True)
insert.rotation_euler[1] = radians(25)
knob = mesh('Borboleta guarda-sol', 'borboleta.stl', (0.98, 0.73, 0.16), (0, 30, 120))
knob.rotation_euler[0] = -pi/2

def parafuso_aperto(name, head_plane):
    # Ferragem metálica ilustrativa, excluída dos arquivos de impressão.
    x, y, z = head_plane
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=3, depth=45,
                                      location=(x, y-22.5, z), rotation=(-pi/2,0,0))
    bpy.context.object.name = name+' haste metalica M6'
    bpy.context.object.color = (0.65,0.68,0.72,1)
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=10/(2*cos(pi/6)), depth=4,
                                      location=(x,y+2,z), rotation=(-pi/2,0,0))
    bpy.context.object.name = name+' cabeca sextavada'
    bpy.context.object.color = (0.65,0.68,0.72,1)

parafuso_aperto('Guarda-sol', (0, -27+57+5.2, 120))
parafuso_aperto('Porta-vara', (34+110*sin(radians(25)),28+57+5.2,10+110*cos(radians(25))))
knob = mesh('Borboleta porta-vara', 'borboleta.stl', (0.98, 0.73, 0.16),
            (34+110*sin(radians(25)), 85, 10+110*cos(radians(25))))
knob.rotation_euler[0] = -pi/2

scene = bpy.context.scene
scene.render.engine = 'BLENDER_WORKBENCH'
scene.display.shading.light = 'STUDIO'
scene.display.shading.color_type = 'OBJECT'
scene.display.shading.show_shadows = True
scene.display.shading.show_cavity = True
scene.display.shading.cavity_type = 'BOTH'
scene.display.shading.background_type = 'WORLD'
scene.world.color = (0.92, 0.94, 0.96)
scene.view_settings.view_transform = 'Standard'
bpy.ops.object.camera_add(location=(310, 430, 310))
camera = bpy.context.object
camera.rotation_euler = (Vector((0, 0, 75))-camera.location).to_track_quat('-Z', 'Y').to_euler()
camera.data.type = 'ORTHO'
camera.data.ortho_scale = 300
scene.camera = camera
scene.render.resolution_x = 1200
scene.render.resolution_y = 1000
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = str(root / 'montagem-prototipo.png')
bpy.ops.wm.save_as_mainfile(filepath=str(root / 'montagem-prototipo.blend'))
bpy.ops.render.render(write_still=True)
