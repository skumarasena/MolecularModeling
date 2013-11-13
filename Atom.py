

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
			#determines how many electron pairs an atom gets, based on which element it is
			if elem == 'C':
				self.bonds = []
			elif elem == 'N' or elem == 'P':
				self.bonds = ['e']
			elif elem == 'O' or elem == 'S':
				self.bonds = ['e', 'e']
		else:
			self.bonds = bonds

def print_atom(atom):
	print atom.elem + ':',
	print atom.name,
	print atom.bonds

def main():
	#If no bonds are given...
	atom1 = Atom('N', 'N1')
	print_atom(atom1)

	#If bonds are specified...
	atom2 = Atom('N', 'N2', ['C1', 'C2'])
	print_atom(atom2)

if __name__ == '__main__':
	main()