from pydoc import render_doc
import bpy
import os

# for scene in bpy.data.scenes:
#     scene.render.resolution_x = 1920
#     scene.render.resolution_y = 1080

dirname = os.path.dirname(__file__)

filenameTemplate = os.path.join(dirname, 'blender\\cube.blend')
print(filenameTemplate)
bpy.ops.wm.open_mainfile(filepath=filenameTemplate)

#  import GLB
# filenameGLB = os.path.join(dirname, 'glbs\\model.glb')
# bpy.ops.import_scene.gltf(filepath=filenameGLB)

# bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
#  save as the changes on the blend proyect
# filenameOutput = os.path.join(dirname, 'blender\\result.blender')
# bpy.ops.wm.save_as_mainfile(filenameOutput)
