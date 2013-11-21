

class Atom(object):
	"""Represents an atom with bonds and electron pairs."""
	
	def __init__(self, elem = '', name = '', bonds = None, size = 0, color = None):
		"""Initializes instance of the Atom class. 

		elem: string (element, ex. C, N, O)
		name: string (name of atom, ex. C1, C2, N3)
		bonds: list of strings/atoms... given our data structure, is this really necessary?
		size: Radius of sphere that represents each Atom
		color: Color of sphere that represents each Atom

		TODO: Figure out which sizes and colors to use for each element!
		"""
		self.elem = elem
		self.name = name

		if elem == 'C':
			self.size = 2
			self.color = 'GRAY'
			if bonds == None:
				self.bonds = []
			else:
				self.bonds = bonds

		elif elem == 'N' or elem == 'P':
			if bonds == None:
				self.bonds = ['e']
			else:
				self.bonds = bonds

			if elem == 'N':	
				self.size = 3
				self.color = 'GREEN'
			else:					#if it is a phosphorus atom
				self.size = 4
				self.color = 'PURPLE'

		elif elem == 'O' or elem == 'S':
			if bonds == None:
				self.bonds = ['e', 'e']
			else:
				self.bonds = bonds

			if elem == 'O':
				self.size = 2
				self.color = 'GRAY'
			else:					#if it is a sulfur atom
				self.size = 2
				self.color = 'GRAY'

	def __str__(self):
		"""Creates an informal string representation of an Atom object, with its name, element, and bonds, when the print function is called.

		self: Atom
		Returns: str
		"""

		return '%s: %s, %s' % (self.elem, self.name, str(self.bonds))
		#eturn '%s: %s, %s, %s' % (self.elem, self.name, str(self.bonds), self.color)

	def __repr__(self):
		"""Creates a more formal representation of an Atom object, with its name, element, and bonds.

		self: Atom
		Returns: str
		"""
		return '%s: %s, %s' % (self.elem, self.name, str(self.bonds))


def main():
	#If no bonds are given...
	atom1 = Atom('N', 'N1')
	print atom1

	#If bonds are specified...
	atom2 = Atom('N', 'N2', ['C1', 'C2'])
	print atom2

	#Can we print datastructures?
	#HINT: yes
	t = [atom1, atom2]
	print t

if __name__ == '__main__':
	main()