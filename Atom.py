

class Atom(object):
	"""Represents an atom with bonds and electron pairs."""
	def __init__(self, elem = '', name = '', bonds = None):
		"""Initializes instance of the Atom class. 

		elem: string (element, ex. C, N, O)
		name: string (name of atom, ex. C1, C2, N3)
		bonds: list of strings/atoms... given our data structure, is this really necessary?
		"""
		self.elem = elem
		self.name = name
		if bonds == None:
			if elem == 'C':
				self.bonds = []
			elif elem == 'N' or elem == 'P':
				self.bonds = ['e']
			elif elem == 'O' or elem == 'S':
				self.bonds = ['e', 'e']
		else:
			self.bonds = bonds

	def __str__(self):
		"""Creates an informal string representation of an Atom object, with its name, element, and bonds, when the print function is called.

		self: Atom
		Returns: str
		"""
		return '%s: %s, %s' % (self.elem, self.name, str(self.bonds))

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

	t = [atom1, atom2]
	print t

if __name__ == '__main__':
	main()