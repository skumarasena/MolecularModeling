from parsing import remove_h,make_list,number_list
import math
import imp
from Atom import Atom, Hydrogen,Carbon
from make_bonds2 import set_bonds,flatten, fill_hydrogens
import copy
import bpy
from to_cartesian import to_cartesian
from math import pi, cos, sin, sqrt
from mathutils import Vector, Matrix

def set_pos(t,b):
    """Sets the positions of all atoms in or bonded to atoms in t.
    
    t: list of Atom objects
    b: bond length
    """
    
    #Toggles when atom is supposed to rotate
    rotate = False
  
    #Checks if atom is not a hydrogen, then uses it as starting point for positions of all bonded atoms
    for item in t:
      if isinstance(item,Atom):
          if not isinstance(item,Hydrogen):
                set_bonded(item,rotate,b)
                rotate = not rotate
      else:
        set_pos(item)

def set_bonded(atom,rotate,b):
    """Sets the positions of all atoms bonded to atom.
    
    atom: Atom object
    rotate: Boolean defining whether or not to rotate tetrahedron around the z-axis
    b: bond length
    """
    
    x = 0
    y = 0
    z = 0
    b = b*sqrt(atom.radius)
    
    bonds = atom.bonds
    
    #Differences in position between central atom and bonded atom
    for item in bonds:
        if isinstance(item, Atom):
            x = atom.pos[0] - item.pos[0]
            y = atom.pos[1] - item.pos[1]
            z = atom.pos[2] - item.pos[2]
            break

    #Angles between various atoms
    n = math.radians(109.5)
    n2 = 2*pi/3
    
    #Angle between existing bond and y-axis
    y_angle = math.atan2(x,z)+pi
   
    #Represents tetrahedron base centered at (0,0,0)
    v1 = Vector((b*sin(n),0,b*cos(n)))
    v2 = Vector((b*cos(n2),b*sin(n2),b*cos(n)))
    v3 = Vector((b*cos(2*n2),b*sin(2*n2),b*cos(n)))
    
    cy= cos(y_angle)
    sy = sin(y_angle)
    
    #Rotates tetrahedron around y-axis to match initial bond position
    my = Matrix(((cy,0,-sy),(0,1,0),(sy,0,cy)))
 
    #Rotates every other atom around z
    if (rotate):
        a1 = pi-math.atan2(x,y)
        c1 = cos(a1)
        s1 = sin(a1)
        m_base = Matrix(((c1,s1,0),(-s1,c1,0),(0,0,1)))
    else:
        m_base = Matrix()
    
    offset = (Vector((atom.pos)))
    
    #Rotates the tetrahedron base to align itself with the starting vector
    v1 = v1*my*m_base
    v2 = v2*my*m_base
    v3 = v3*my*m_base
    
    #Sets the positions of bonded atoms to locations in the tetrahedron, scales bond lengths and moves tetrahedron
    if isinstance(bonds[1], Atom):
        bonds[1].pos = v1*sqrt(bonds[1].radius)+offset
    if isinstance(bonds[2], Atom):
        bonds[2].pos = v2*sqrt(bonds[2].radius)+offset
    if isinstance(bonds[3], Atom):
        bonds[3].pos = v3*sqrt(bonds[3].radius)+offset

def makeMaterial(name, diffuse, specular, alpha):
    """Creates a material that defines the appearance of a mesh.
    
    name: identifier of material
    diffuse: base color of material, specified as a tuple of fractions in (R,G,B) format
    specular: tuple defining reflection color, intensity and rate of transtion between base color and highlight
    alpha: numeric between 0-1 defining object transparency
    
    Return: material
    """
    #Creates material and sets various properties
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT'
    mat.diffuse_intensity = 1.0
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    """Sets the material of object ob to mat.
    
    ob: Blender object
    mat: Material
    """
    me = ob.data
    me.materials.append(mat)
    
           

def makeMolecule(formula):    
    
    #Creates list of atoms with appropriate bonds
    t = fill_hydrogens(set_bonds(number_list(make_list(remove_h(formula)))))
    
    #Base bond length
    b = 3

    #Sets position of first atom for use in rotation
    t[0].pos = (0,0,b*sqrt(t[0].radius)*sqrt(t[1].radius))
    set_pos(t,b)
    t2 = flatten(t)
  
    bpy.ops.scene.delete()
    bpy.ops.scene.new(type = 'NEW')
    
    colors = {}
    
    #Draws atom with appropriate color and size
    for atom in t2:
        elem = (atom.name[0:1])
        
        #maps element to an appropriate material
        colors[elem] = colors.get(elem, makeMaterial(elem,tuple(atom.color), (1,1,1),1))
        
        #Draws atom and sets its material
        bpy.ops.mesh.primitive_uv_sphere_add(location = atom.pos, size = atom.radius*1)
        setMaterial(bpy.context.object, colors[(atom.name[0:1])])
        bonds = atom.bonds
        
        #Draws cylinders between atoms
        for i in range(0, len(bonds)):
            if isinstance(bonds[i], Atom):
                list = [atom, bonds[i]]
                
                # Create curve 
                draw_curve = bpy.data.curves.new('draw_curve','CURVE')
                draw_curve.dimensions = '3D'
                spline = draw_curve.splines.new('BEZIER')
                spline.bezier_points.add(len(list)-1)
                curve = bpy.data.objects.new('curve',draw_curve)
                bpy.context.scene.objects.link(curve)
            
                # Curve settings for new curve
                draw_curve.resolution_u = 64
                draw_curve.fill_mode = 'FULL'
                draw_curve.bevel_depth = 0.3
                draw_curve.bevel_resolution = 5
        
                # Assign bezier points to selection object locations
                for i in range(len(list)):
                    p = spline.bezier_points[i]
                    p.co = list[i].pos
                    p.handle_right_type="VECTOR"
                    p.handle_left_type="VECTOR"
                
                bpy.context.scene.objects.active = curve
                bpy.ops.object.mode_set(mode='OBJECT')
                
if __name__ =="__main__":
    formula = input("Enter a molecular formula.")
    makeMolecule(formula) 
                
            
            
    
    
    
        
    