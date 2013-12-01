import Atom
import parsing
from parsing import remove_h,make_list,number_list
import make_bonds
import math
import imp
imp.reload(Atom)
from Atom import Atom
from make_bonds2 import set_bonds,flatten
import copy


def set_pos(t):
   
    for item in t:
      if type(item) != list:
        set_bonded(item)
      else:
        set_pos(item)

def set_bonded(atom):
    b = 5
    bonds = atom.bonds

    x = atom.pos[0] - bonds[0].pos[0]
    y = atom.pos[1] - bonds[0].pos[1]
    z = atom.pos[2] - bonds[0].pos[2]
    
    theta = math.atan(float(y)/x)
    print theta
    
    if len(bonds) ==2:
        phi = theta+math.pi
        if isinstance(bonds[1],Atom):
            atom.bonds[1].pos = [atom.pos[0] -b*math.cos(phi),atom.pos[1]-b*math.sin(phi),atom.pos[2]]
    
    if len(bonds) == 3:
        phi = theta + (2*math.pi/3)
        phi2 = phi + (2*math.pi/3)
        if isinstance(bonds[1],Atom):
            atom.bonds[1].pos = [atom.pos[0] - b*math.cos(phi),atom.pos[1] - b*math.sin(phi),atom.pos[2]]
        if isinstance(bonds[2],Atom):
            atom.bonds[2].pos = [atom.pos[0] - b*math.cos(phi2),atom.pos[1]-b*math.sin(phi2), atom.pos[2]]
    
    if len(bonds) ==4:
        print ("fix this")
        
if __name__ == "__main__":
    s1 = 'CH3CH2CH(CH2CH3)CH2CH3'

    t = set_bonds(number_list(make_list(remove_h(s1))))
    t[1].pos = [2,3,0]
    set_pos(t)

    t2 = flatten(t)
    
    for atom in t2:
        print atom
        print atom.pos
        
    
    
    
        
    
