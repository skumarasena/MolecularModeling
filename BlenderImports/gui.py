import bpy
from bpy.props import *
import Atom

def init_scene_properties(scn):
    bpy.types.Scene.MyString = StringProperty(
        name = "Input a Molecule")
    scn['MyString'] = "Lorem ipsum dolor sit amet"
    return

init_scene_properties(bpy.context.scene)
   
class DefineMolecule(bpy.types.Panel):
    #def __init__(self):
        
    bl_idname = "object.define_molecule"        # unique identifier for buttons and menu items to reference.
    bl_label = "Define a Molecule"              # display name in the interface.
    bl_region_type = "UI"                       # set location of panel (in UI region)
    bl_space_type = "VIEW_3D"                   # panel is used in VIEW_3D space

    def draw(self, context):        
        layout = self.layout
        scn = context.scene
        layout.prop(scn,"MyString")
        layout.operator("input.moleculestring")

class MakeMolecule(bpy.types.Operator):
    bl_idname = "input.moleculestring"
    bl_label = "Create Molecule"
    
    def execute(self,context):
        scn = context.scene
        return{'FINISHED'} 

#    Registration
bpy.utils.register_module(__name__)