from string import *
import ast

def remove_h(formula):
	"""Takes standard structural chemical formula, and removes all hydrogens from the formula.

	formula: string
	Returns: string
	"""
	s = formula.upper()
	# s1 = s.replace('H4', '')
	# s2 = s1.replace('H3', '')
	# s3 = s2.replace('H2', '')
	# s4 = s3.replace('H', '')
	res = s.replace('H4','').replace('H3','').replace('H2','').replace('H','')

	return res

def make_list(formula):
	"""Takes stripped formula (i.e. a structural formula which has gone through remove_h()) and converts it to a nested list.

	formula: string
	Returns: list
	"""
	t = list(formula)
	t2 = ''.join([c + ' ' for c in t])
	return eval(str(t2.split()).replace("'(',", '[').replace("')'",']'))



def main():
	s1 = 'CH3CH2CH3'
	print 's1:',
	print remove_h(s1)

	s2 = 'Ch3Ch2cH3'
	print 's2:',
	print remove_h(s2)

	s3 = 'CH3CH2NH2'
	print 's3:',
	print remove_h(s3)

	s4 = 'CH3CH2CH(CH3)CH2CH3'
	print 's4:',
	print remove_h(s4)

	s5 = 'CH2(CH3CH2CH(CH3)CH2CH3)CH(CH3)CH2CH3'
	print 's5:',
	print remove_h(s5)
	print make_list(remove_h(s5))

if __name__ == '__main__':
	main()