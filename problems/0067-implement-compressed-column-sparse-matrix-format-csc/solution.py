import numpy as np
def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	row, col = np.shape(dense_matrix)
	values = []
	row_indices = []
	column_pointer = []
	ptr = 0
	for i in range(col):
		idx = 0
		column_pointer.append(ptr)
		for j in range(row):
			if dense_matrix[j][i] != 0:
				row_indices.append(idx)
				values.append(dense_matrix[j][i])
				ptr += 1
			idx += 1
	column_pointer.append(ptr)
	return values, row_indices, column_pointer
