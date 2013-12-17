bl_info = {
    "name": "Make Molecule",
    "category": "User"
}

import bpy
from bpy.props import *
import Atom
import get_locations
import make_bonds
import make_bonds2
import parsing
import to_cartesian
   
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
        s1 = get_data("MyString",scn)
        return{'FINISHED'} 

def get_data(key, scn):
    val = scn[key]

def register():
    bpy.utils.register_class(DefineMolecule)
    bpy.utils.register_class(MakeMolecule)

def unregister():
    bpy.utils.unregister_class(DefineMolecule)
    bpy.utils.unregister_class(MakeMolecule)


if __name__ == "__main__":
    register()