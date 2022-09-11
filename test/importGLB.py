from pydoc import render_doc
import bpy
import os

dirname = os.path.dirname(__file__)

# Blend file where the GLB will be imported ( a sort of scene template)
filenameBlenderTemplate = os.path.join(dirname, 'blender\\default_scene.blend')
# Blend file save to save after python scrin runs
filenameBlenderOutput = os.path.join(dirname, 'blender\\result2.blend')
# GLB file to import
filenameToImportGLB = os.path.join(dirname, 'glbs\\model.glb')


bpy.ops.wm.open_mainfile(filepath=filenameBlenderTemplate)
bpy.ops.import_scene.gltf(filepath=filenameToImportGLB)
bpy.ops.wm.save_as_mainfile(filepath=filenameBlenderOutput)
