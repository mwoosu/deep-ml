
import numpy as np

def matrix_image(A):
	# Write your code here
	
	candidate = []
	selected = []

	for col in range(A.shape[1]):
		candidate = selected + [col]
		rank = np.linalg.matrix_rank(A[candidate])

		if rank > len(selected):
			selected.append(col)

	return A[:, selected]
