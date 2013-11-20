
#import bpy

class Atom(object):
	"""Represents an atom with bonds and electron pairs."""
	def __init__(self, name = '', bonds = None):
		"""Initializes instance of the Atom class. 

		name: string (name of atom, ex. C1, C2, N3)
		bonds: list of Atom objects
		"""
		self.name = name
		self.bonds = bonds

	def __str__(self):
		return '%s: %s, %s' % (self.name, str(self.bonds), str(self.color))

	def __repr__(self):
		"""Creates a more formal representation of an Atom object, with its name, element, and bonds.

		self: Atom
		Returns: str
		"""
		return '%s: %s' % (self.name, str(self.bonds))



class Hydrogen(Atom):
	"""Creates an H atom class with properties used to graph"""
	def __init__(self,name,bonds):
		atom = Atom(name,bonds)
		self.name = atom.name
		if atom.bonds == None:
			bonds = []
		else:
			self.bonds = atom.bonds
		self.radius = 1
		self.color = (1,0,0) #makes it red in blender


	# def __str__(self):
	# 	return '%s,%s' % (self.name, str(self.bonds))


class Nitrogen(Atom):
	"""Creates an N atom class with properties used to graph"""
	def __init__(self,name,bonds):
		atom = Atom(name,bonds)
		self.name = atom.name
		if atom.bonds == None:
			bonds = []
		else:
			self.bonds = atom.bonds
		self.color = (0,1,0) #makes it green in blender
		self.radius = 3


class Carbon(Atom):
	"""Creates a C atom class with properties used to graph"""
	def __init__(self,name,bonds):
		atom = Atom(name,bonds)
		self.name = atom.name
		if atom.bonds == None:
			bonds = []
		else:
			self.bonds = atom.bonds
		self.radius = 2
		self.color = (1,1,1) #gray in blender


class Phosphorus(Atom):
	"""Creates a P atom class with properties used to graph"""
	def __init__(self,name,bonds):
		atom = Atom(name,bonds)
		self.name = atom.name
		if atom.bonds == None:
			bonds = []
		else:
			self.bonds = atom.bonds
		self.radius = 4
		self.color = (2,0,2) #makes it purple


class Oxygen(Atom):
	def __init__(self,name,bonds):
		atom = Atom(name,bonds)
		self.name = atom.name
		if atom.bonds == None:
			bonds = []
		else:
			self.bonds = atom.bonds
		self.radius = 2
		self.color = (1,1,1) #gray in blender


class Sulfur(Atom):
	def __init__(self,name,bonds):
		atom = Atom(name,bonds)
		self.name = atom.name
		if atom.bonds == None:
			bonds = []
		else:
			self.bonds = atom.bonds
		self.radius = 2
		self.color = (1,1,1) #gray in blender


 
# def makeMaterial(name, diffuse, specular, alpha):
#     mat = bpy.data.materials.new(name)
#     mat.diffuse_color = diffuse
#     mat.diffuse_shader = 'LAMBERT' S
#     mat.diffuse_intensity = 1.0 
#     mat.specular_color = specular
#     mat.specular_shader = 'COOKTORR'
#     mat.specular_intensity = 0.5
#     mat.alpha = alpha
#     mat.ambient = 1
#     return mat
 
# def setMaterial(ob, mat):
#     me = ob.data
#     me.materials.append(mat)
 
# def make_atom(origin,atom):
#     atom_mat = makeMaterial(atom.name, atom.color, (0.5,0.5,0), 0.5)
#     bpy.ops.mesh.primitive_uv_sphere_add(location=origin,size=atom.radius)
#     bpy.ops.transform.translate(value=(0,0,0))
#     setMaterial(bpy.context.object, atom_mat)
 
# if __name__ == "__main__":
#     run((0,0,0))


def main():
	atom = Hydrogen('H1',['bond1'])
	atom2 = Hydrogen('H2',['bond2'])
	print atom
	print atom2



if __name__ == '__main__':
	main()