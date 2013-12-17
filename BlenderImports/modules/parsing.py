import string
import Atom
import ast

i = 0


def remove_h(formula):
	"""Takes standard structural chemical formula, and removes all hydrogens from the formula.

	TODO: loops

	formula: string
	Returns: string
	"""
	#Just in case someone decides to enter non-capital letters...I've made that mistake before :P
	s = formula.upper()

	#Replaces all possible combinations of hydrogens with the empty string. Important: this function call replaces 'H' last!
	res = s.replace('H4','').replace('H3','').replace('H2','').replace('H','')

	return res

def make_list(formula):
	"""Takes stripped formula (i.e. a structural formula which has gone through remove_h()) and converts it to a nested list.

	TODO: handle formulas with parenthetical multiplicity, ex. C(CH3)3

	TODO: make this function less gross-string-manipulation-ish.

	formula: string
	Returns: list
	"""
	t = list(formula)

	#Puts spaces between each character, then concatenates list into a string.The spaces are important here because I'm using the split() method to split the string into elements of a list in the eval() function call.
	t2 = ''.join([c + ' ' for c in t])

	#Splits the string into elements by spaces, replaces parentheses with brackets, then evaluates the resulting expression as a Python expression. The result is a list. 
	return eval(str(t2.split()).replace("'(',", '[').replace("')'",']'))

# def make_list(formula):
# 	"""Takes stripped formula (i.e. a structural formula which has gone through remove_h()) and converts it to a nested list.

# 	TODO: handle formulas with parenthetical multiplicity, ex. C(CH3)3

# 	formula: string
# 	Returns: list
# 	"""
# 	#replaces parentheses with brackets
# 	s = formula.replace('(', '[').replace(')', ']')
	
# 	#puts spaces between each character of the string
# 	t = list(s)
# 	t2 = ''.join([c + ' ' for c in t])
# 	print t2

# 	print ast.literal_eval(str(t2.split()))






# def number_list(t):
# 	"""Takes a nested list that represents a chemical formula (returned by the function make_list()), makes an analogous list of atoms, and numbers the atoms in order.

# 	t: list of str
# 	Returns: list of Atoms
# 	"""	
# 	global i
# 	res = []
# 	for elem in t:
# 		if type(elem)==str:
# 			#res.append(elem + str(i))		#appends string
# 			if elem == 'C':
# 				res.append(Atom.Carbon(elem + str(i)))	#appends atom
# 			if elem == 'N':
# 				res.append(Atom.Nitrogen(elem + str(i)))	#appends atom
# 			if elem == 'O':
# 				res.append(Atom.Oxygen(elem + str(i)))	#appends atom
# 			if elem == 'P':
# 				res.append(Atom.Phosphorus(elem + str(i)))	#appends atom	
# 			if elem == 'S':
# 				res.append(Atom.Sulfur(elem + str(i)))	#appends atom	
# 			i +=1
# 		if type(elem)==list:
# 			res.append(number_list(elem))
# 	return res

class Parser(object):
	"""Traverses a chemical formula, creates analogous atoms, and assigns them names."""
	def __init__(self):
		"""Initializes instance of the Parser class."""
		self.i = 0
	def __str__(self):
		return 'Count: %d' % self.i

	def incr(self):
		"""Increments the counter."""
		self.i += 1

def parse_list(t, p):
	"""Takes a nested list that represents a chemical formula (returned by the function make_list()), makes an analogous list of atoms, and numbers the atoms in order.

	t: list of str
	p: Parser object
	Returns: list of Atoms
	"""	
	res = []
	for elem in t:
		if type(elem)==str:
			#res.append(elem + str(i))		#appends string
			if elem == 'C':
				res.append(Atom.Carbon(elem + str(p.i)))	#appends atom
			if elem == 'N':
				res.append(Atom.Nitrogen(elem + str(p.i)))	#appends atom
			if elem == 'O':
				res.append(Atom.Oxygen(elem + str(p.i)))	#appends atom
			if elem == 'P':
				res.append(Atom.Phosphorus(elem + str(p.i)))	#appends atom	
			if elem == 'S':
				res.append(Atom.Sulfur(elem + str(p.i)))	#appends atom	
			p.incr()
		if type(elem)==list:
			res.append(parse_list(elem, p))
	return res

def number_list(t):
	"""Takes a nested list that represents a chemical formula (returned by the function make_list()), uses parse_list() and a Parser object to number the atoms in order. 

	t: list of str
	Returns: list of Atoms"""
	
	p = Parser()
	res = parse_list(t, p)
	return res


def main():

	#I attempted to test number_list()
	i = 0
	x = number_list(['C', 'C', 'C'])
	print(x[0])		#should print representation of an Atom object

	#weirdly enough, even when I try to reset i, this will still start at C3!
	i = 0
	print(number_list(['C', 'N', 'O', ['C', 'P', ['C']], 'S', 'C']))


	#the basics
	s1 = 'CH3CH2CH3'
	print('s1: '+ remove_h(s1))

	#test case for mixed upper/lowercase letters
	s2 = 'Ch3Ch2cH3'
	print('s2: '+ remove_h(s2))

	#different types of central atoms
	s3 = 'CH3CH2NH2'
	print('s3: ' + remove_h(s3))

	#ooh! nesting!
	s4 = 'CH3CH2CH(CH3)CH2CH3'
	print('s4: ' + remove_h(s4))
	print(make_list(remove_h(s4)))

	#hard mode
	s5 = 'CH3CH2CH(CH3CH(CH3)CH3)CH2CH3'
	print('s5: ' + remove_h(s5))
	print(make_list(remove_h(s5)))

	#EXTREEEEEME!
	s6 = 'HOCH2(CH3CH2CH(CH2CH3)CH2CH3)CH(CH3)CH2NH2'
	print('s6: ' + remove_h(s6))
	print(make_list(remove_h(s6)))


if __name__ == '__main__':
	main()