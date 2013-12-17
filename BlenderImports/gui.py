bl_info = {
    "name": "Make Molecule",
    "category": "User"
}

import bpy
from bpy.props import *
import Atom
import parsing
import make_bonds2
   
class DefineMolecule(bpy.types.Panel):
    bl_idname = "define_molecule"        # unique identifier for buttons and menu items to reference.
    bl_label = "Define a Molecule"              # display name in the interface.
    bl_region_type = "TOOLS"                       # set location of panel (in UI region)
    bl_space_type = "VIEW_3D"                   # panel is used in VIEW_3D space

    def draw(self, context):        
        layout = self.layout
        scn = context.scene
        layout.label(text = "Input Molecule")
        layout.prop(scn, "my_molecule")
        layout.operator("make.moleculestring", text = "Make Molecule")
        

class MakeMolecule(bpy.types.Operator):
    bl_idname = "make.moleculestring"
    bl_label = "Create Molecule"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self,context):
        scn = context.scene
        molecule = scn.my_molecule
        parsed_molecule = parsing.number_list(parsing.make_list(parsing.remove_h(molecule)))
        molecule_with_set_bonds = make_bonds2.set_bonds(parsed_molecule)
        flattened_bonds = make_bonds2.flatten(molecule_with_set_bonds)
        return{'FINISHED'} 

def register():
    bpy.utils.register_class(DefineMolecule)
    bpy.utils.register_class(MakeMolecule)
    bpy.types.Scene.my_molecule = bpy.props.StringProperty(name = "",description = "User inputs a chemical formula",default = "CH3CH3")

def unregister():
    bpy.utils.unregister_class(DefineMolecule)
    bpy.utils.unregister_class(MakeMolecule)
    del bpy.types.Scene.my_molecule
    

if __name__ == "__main__":
    register()