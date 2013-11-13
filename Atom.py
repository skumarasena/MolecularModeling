

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
			self.bonds = []
		else:
			self.bonds = bonds

def print_atom(atom):
	print atom.elem + ':',
	print atom.name,
	print atom.bonds

def main():
	#Simple test case
	atom = Atom('N', 'N1', ['C1', 'C2'])
	print_atom(atom)

if __name__ == '__main__':
	main()