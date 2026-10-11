import numpy as np

def make_diagonal(x):
	# Your code here
	n = len(x)
	matrix = [[0]*n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			if i == j:
				matrix[i][j] = x[i]
	return matrix
	pass