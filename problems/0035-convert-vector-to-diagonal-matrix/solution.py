import numpy as np

def make_diagonal(x):
	# Your code here
	return [[x[i] if i==j else 0 for i in range(len(x))]for j in range(len(x))]
	pass