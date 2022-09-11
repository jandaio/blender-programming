from pydoc import render_doc
import bpy
import os

dirname = os.path.dirname(__file__)

# Blend file where the GLB will be imported ( a sort of scene template)
filenameBlenderTemplate = os.path.join(dirname, 'blender\\cube.blend')
# Blend file save to save after python scrin runs
# filenameBlenderOutput = os.path.join(dirname, 'blender\\result2.blend')


bpy.ops.wm.open_mainfile(filepath=filenameBlenderTemplate)


obj = bpy.data.objects.get("Cube")

obj.color = (1, 0, 0, 1)


mat = bpy.data.materials.new("Red")
mat.use_nodes = True
principled = mat.node_tree.nodes['Principled BSDF']
principled.inputs['Base Color'].default_value = (1, 0, 0, 1)
obj.data.materials.clear()
obj.data.materials.append(mat)
obj.active_material = mat

# obj.active_material = bpy.data.materials.get("Blue")

# bpy.ops.wm.save_as_mainfile(filepath=filenameBlenderOutput)
