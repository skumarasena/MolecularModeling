

class Atom(object):
	"""Represents an atom with bonds and electron pairs."""
	def __init__(self, elem = '', name = '', bonds = None, color):
		"""Initializes instance of the Atom class. 

		elem: string (element, ex. C, N, O)
		name: string (name of atom, ex. C1, C2, N3)
		bonds: list of strings/atoms... given our data structure, is this really necessary?
		"""
		self.elem = elem
		self.name = name
		self.bonds = bonds
		self.color = color

	def __str__(self):
		return '%s: %s, %s' % (self.elem, self.name, str(self.bonds))

#I have a feeling there is a way to combine these classes with the atom class above,
# but I'm not sure how. Especially with the bonds area, there should be a way to
# make this more elegant. Ideas?

class Hydrogen(Atom):
	"""Creates an H atom class with properties used to graph"""
		self.radius = 1
		self.color = (1,0,0) #makes it red in blender
	def __init__(self, bonds = []):
		self.bonds = bonds

class Nitrogen(Atom):
	"""Creates an N atom class with properties used to graph"""
		self.color = (0,1,0) #makes it green in blender
		self.bonds = bonds
	def __init__(self,bonds = ['e']):
		self.radius = 3

class Carbon(Atom):
	"""Creates a C atom class with properties used to graph"""
		self.radius = 2
		self.color = (1,1,1) #gray in blender
	def __init__(self,bonds = []):
		self.bonds = bonds

class Phosphorous(Atom):
	"""Creates a P atom class with properties used to graph"""
		self.radius = 4
		self.color = (2,0,2) #makes it purple
	def __init__(self,bonds = ['e']):
		self.bonds = bonds

class Oxygen(Atom):
		self.radius = 2
		self.color = (1,1,1) #gray in blender
	def __init__(self,bonds = ['e', 'e']):
		self.bonds = bonds

class Sulfur(Atom):
		self.radius = 2
		self.color = (1,1,1) #gray in blender
	def __init__(self,bonds = ['e', 'e']):
		self.bonds = bonds

import bpy
 
def makeMaterial(name, diffuse, specular, alpha):
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
    me = ob.data
    me.materials.append(mat)
 
def make_atom(origin,atom):
    atom_mat = makeMaterial(atom.name, atom.color, (0.5,0.5,0), 0.5)
    bpy.ops.mesh.primitive_uv_sphere_add(location=origin,size=atom.radius)
    bpy.ops.transform.translate(value=(0,0,0))
    setMaterial(bpy.context.object, atom_mat)
 
if __name__ == "__main__":
    run((0,0,0))


def main():
	#If no bonds are given...
	atom1 = Atom('N', 'N1')
	print atom1

	#If bonds are specified...
	atom2 = Atom('N', 'N2', ['C1', 'C2'])
	print atom2

if __name__ == '__main__':
	main()