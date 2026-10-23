
import numpy as np

def matrix_image(A):
	# Write your code here
	B = A.astype(float).copy()
	rows, cols = B.shape

	pivot_row = 0
	pivot_cols = []
	for col in range(cols):
		if pivot_row >= rows:
			break

		if B[pivot_row, col] == 0:
			continue

		pivot_cols.append(col)

		for i in range(pivot_row+1, rows):
			factor = B[i, col] / B[pivot_row, col]
			B[i, : ] -= factor*B[pivot_row, :]
			
		pivot_row += 1

	return A[:, pivot_cols]
