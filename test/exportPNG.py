from pydoc import render_doc
import bpy
import os

for scene in bpy.data.scenes:
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080


# import GLB
bpy.ops.import_scene.gltf(filepath=filename)

# bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
# save as the changes on the blend proyect
# bpy.ops.wm.save_as_mainfile(filepath=os.getcwd() + "\\test.blend")
