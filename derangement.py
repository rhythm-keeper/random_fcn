#!/usr/bin/env



def num_permutations(n):
	"""
	Returns the exact number of permutations
	for a given number of n objects
	with n items where it is not 
	permissible for object i to 
	to be assigned item i
	
	https://en.wikipedia.org/w/index.php?title=Derangement

	!n = (n-1)( !(n-1) + !(n-2) )
	"""

	if n < 0:
		print("Input must be >= 0")
		exit(1)
	if n == 1: return 0
	elif n == 0: return 1
	else: return (n-1)*( num_permutations(n-1)+num_permutations(n-2) ) # recursive call 

def factorial(n):
	if n < 0: 
	     print("Input must be >= 0")
	     exit(1)
	if n == 0:   # base case
	    return 1
	else:
	    return n * factorial(n-1)  # recursive call

def est_num_permutations(n):
	"""
	An alternative to calculating
	the number of derangements using the 
	factorial function

	[n!/e]

	where n is the nearest integer function

	round function returns integer
	"""
	from math import e

	return round( factorial(n) / e  )
	


def examples():		

	print("### def num_permutations ###")
	for i in range(5):
		print("N objects, items: ",i,"  num permuations: ",num_permutations(i))

	print("### def est_num_permutations ###")
	for i in range(5):
		print("N objects, items: ",i,"  num permuations: ",est_num_permutations(i))



