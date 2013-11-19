from Atom import *

def set_bonds(t):
    """Takes a nested list of empty Atom objects, and gives each atom a list of Atom objects to which it is directly bonded.

    t: nested list of Atom objects
    Returns: None
    """
    
    for i in range(1,len(t)):

        if type(t[i]) == Atom and type(t[i-1])==Atom:
            t[i-1].bonds.append(t[i])
            t[i].bonds.append(t[i-1])

        elif type(t[i]) ==Atom and type(t[i-1]) == list:
            t[i-2].bonds.append(t[i])
            t[i].bonds.append(t[i-2])

        elif type(t[i]) == list and type(t[i-1]) == Atom:
            sub = t[i]
            print sub[0]
            t[i-1].bonds.append(sub[0])
            sub[0].bonds.append(t[i-1])
            set_bonds(sub)


    for atom in t:
        if isinstance(atom,Atom.Atom):
            print atom.bonds



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
    t = [1,2,3,[4,5],[],[6]]
    print flatten(t)



if __name__ == '__main__':
    main()