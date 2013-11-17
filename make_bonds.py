from Atom import *

def set_bonds(t):
    
    for i in range(1,len(t)):

        if type(t[i]) == Atom and type(t[i-1])==Atom:
            t[i-1].bonds.append(t[i].name)
            t[i].bonds.append(t[i-1].name)

        elif type(t[i]) ==Atom and type(t[i-1]) == list:
            t[i-2].bonds.append(t[i].name)
            t[i].bonds.append(t[i-2].name)

        elif type(t[i]) == list and type(t[i-1]) == Atom:
            sub = t[i]
            print sub[0]
            t[i-1].bonds.append(sub[0].name)
            sub[0].bonds.append(t[i-1].name)
            set_bonds(sub)


    for atom in t:
        if isinstance(atom,Atom.Atom):
            print atom.bonds





