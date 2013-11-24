import Atom
import parsing
import copy
#from Atom import *

def set_bonds(t):
    """Takes a nested list of empty Atom objects, and gives each atom a list of Atom objects to which it is directly bonded.

    TODO: make this function work for nested lists.
    t: nested list of Atom objects
    Returns: None
    """
    res = copy.copy(t)#Not a typo. DO NOT change this to deepcopy!  
    
    for i in range(1,len(t)):

        #if current element and previous element of the list are both part of the same chain, bond both atoms to each other.
        if isinstance(t[i],Atom.Atom) and isinstance(t[i-1],Atom.Atom):
            res[i-1].bonds.append(t[i])
            res[i].bonds.append(t[i-1])

        #if current element is an Atom and the previous element represents a subchain, bond the current Atom to the Atom before the subchain.
        elif isinstance(t[i],Atom.Atom) and isinstance(t[i-1],list):
            res[i-2].bonds.append(t[i])
            res[i].bonds.append(t[i-2])

        #If current element is a subchain and the previous element is an Atom, bond the first Atom in the subchain to the previous Atom, then evaluate the subchain recursively. 
        elif isinstance(t[i],list) and isinstance(t[i-1],Atom.Atom):
            sub = t[i]
            res[i-1].bonds.append(sub[0])
            sub[0].bonds.append(t[i-1])
            set_bonds(sub)
	
    return (res)

def flatten(t):
    """Takes a nested list of Atom objects (from the function set_bonds()) and flattens it, so that the collapsed list can be passed to our drawing functions.

    t: nested list of Atom objects
    Returns: flattened list of Atoms
    """
    res = []
    for elem in t:
        if isinstance(elem, list):
            res.extend(flatten(elem))
        else:
            res.append(elem)
    return res


def main():
    #t = [1,2,3,[4,5],[],[6]]
    #print(flatten(t))

    s1 = 'CH3NH2SH'
    t1 = set_bonds(parsing.number_list(parsing.make_list(parsing.remove_h(s1))))

    s2 = 'CH3NH(CHNHOH)SH'

    t2 = set_bonds(parsing.number_list(parsing.make_list(parsing.remove_h(s2))))

    for item in flatten(t2):
        bonds = item.bonds
        print item.name+":",
        for thing in bonds:
            if isinstance(thing,Atom.Atom):
                print thing.name,
        print ""

if __name__ == '__main__':
    main()
