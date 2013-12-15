
#import bpy

class Atom(object):
	"""Represents an atom with bonds and electron pairs."""
	def __init__(self, name = '', bonds = None, pos = None):
		"""Initializes instance of the Atom class. 

		name: string (name of atom, ex. C1, C2, N3)
		bonds: list of Atom objects
		"""
		self.name = name
		if bonds == None:
			self.bonds = []
		else: 
			self.bonds = bonds

		if pos is None:
			self.pos = [0,0,0]
		else:
			self.pos = pos

	def __str__(self):
		return '%s: %s: %s' % (self.name, str(self.bonds), str(self.pos))#, str(self.pos))

	def __repr__(self):
		"""Creates a more formal representation of an Atom object, with its name, element, and bonds.

		self: Atom
		Returns: str
		"""
		return '%s: %s' % (self.name, str(self.bonds))#, str(self.pos))


class Hydrogen(Atom):
	"""Creates an H atom class with properties used to graph"""
	def __init__(self,name,bonds=None, pos = None):

		super(Hydrogen,self).__init__(name,bonds, pos)

		self.radius = 1
		self.color = (1,1,1) #makes it white in blender


class Nitrogen(Atom):
	"""Creates an N atom class with properties used to graph"""
	def __init__(self,name,bonds=None, pos=None):

		super(Nitrogen,self).__init__(name,bonds,pos)

		
		self.bonds.append('e')
		self.color = (135/255,206/255,235/255) #makes it sky blue in blender
		self.radius = 3


class Carbon(Atom):
	"""Creates a C atom class with properties used to graph"""
	def __init__(self,name,bonds=None, pos=None):

		super(Carbon,self).__init__(name,bonds,pos)
		
		self.radius = 2
		self.color = (0,0,0) #black in blender


class Phosphorus(Atom):
	"""Creates a P atom class with properties used to graph"""
	def __init__(self,name,bonds=None, pos=None):

		super(Phosphorus,self).__init__(name,bonds,pos)
		
		self.bonds.append('e')
		self.radius = 4
		self.color = (139/255,0,139/255) #makes it purple


class Oxygen(Atom):
	def __init__(self,name,bonds=None, pos=None):
		
		super(Oxygen,self).__init__(name,bonds,pos)
		
		self.bonds.extend('e'*2)
		self.radius = 2
		self.color = (1,0,0) #red in blender


class Sulfur(Atom):
	def __init__(self,name,bonds=None, pos=None):

		super(Sulfur,self).__init__(name,bonds,pos)
		
		self.bonds.extend('e'*2)
		self.radius = 2
		self.color = (1,215/255,0) #gold in blender


def main():
	#initializing atoms with bonds, and without bonds
	atom1 = Hydrogen('H1',['bond1'], [1,2,3])
	atom2 = Oxygen('O2',['bondddd'])
	atom3 = Oxygen('O3')#,[1,2,3])

	#list of atoms -- can it print properly?
	#HINT: yes
	t = [atom1, atom2, atom3]

	#testing...
	# print(atom1)
	# print(atom2)
	# print(atom3)
	# print(t)

	#can we append bonds to atom objects that already have a bond list?
	# atom2.bonds.append('bond2.5')
	# print(atom2)

	#can we append bonds to atom objects that do not have a bond list yet?
	# atom3.bonds.append('bond3')
	# print(atom3)

	#can we append atoms to bond lists?
	# atom1.bonds.append(atom2)
	# print(atom1)

	#can positions be modified?
	# atom1.pos = [2,3,4]
	# print(atom1)

	#can position variables be created?
	# print atom3
	# atom3.pos = [3,4,5]
	# print(atom3)



if __name__ == '__main__':
	main()
