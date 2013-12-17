bl_info = {
    "name": "Make Molecule",
    "category": "User"
}

import bpy
from bpy.props import *
import Atom

# def init_scene_properties(scn):
#     bpy.types.Scene.MyString = StringProperty(
#         name = "Input a Molecule")
#     scn['MyString'] = "Lorem ipsum dolor sit amet"
#     return

# init_scene_properties(bpy.context.scene)
   
class DefineMolecule(bpy.types.Panel):
    bl_idname = "define_molecule"        # unique identifier for buttons and menu items to reference.
    bl_label = "Define a Molecule"              # display name in the interface.
    bl_region_type = "TOOLS"                       # set location of panel (in UI region)
    bl_space_type = "VIEW_3D"                   # panel is used in VIEW_3D space

    def draw(self, context):        
        layout = self.layout
        scn = context.scene
        layout.prop(scn,"MyString")
        layout.operator("input.moleculestring", text = "Make Molecule")

class MakeMolecule(bpy.types.Operator):
    bl_idname = "input.moleculestring"
    bl_label = "Create Molecule"
    bl_options = {'REGISTER', 'UNDO'}

    # molecule = bpy.props.StringProperty(name="Input Molecule", default = "",  options={'ANIMATABLE'})
    
    def execute(self,context):
        scn = context.scene
        return{'FINISHED'} 

# def menu_func(self, context):
#     self.layout.operator(MakeMolecule.bl_idname)

# # store keymaps here to access after registration
# addon_keymaps = []

def register():
    bpy.utils.register_class(DefineMolecule)
    bpy.utils.register_class(MakeMolecule)

    # bpy.types.VIEW3D_MT_object.append(menu_func)

    # # handle the keymap
    # wm = bpy.context.window_manager
    # km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    # kmi = km.keymap_items.new(MakeMolecule.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
    # kmi.properties.molecule = 'Input molecule here'
    # addon_keymaps.append(km)

def unregister():
    bpy.utils.unregister_class(DefineMolecule)
    bpy.utils.unregister_class(MakeMolecule)
    # bpy.types.VIEW3D_MT_object.remove(menu_func)

    # # handle the keymap
    # wm = bpy.context.window_manager
    # for km in addon_keymaps:
    #     wm.keyconfigs.addon.keymaps.remove(km)
    # # clear the list
    # del addon_keymaps[:]


if __name__ == "__main__":
    register()