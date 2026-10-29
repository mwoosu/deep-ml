import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	num = 0
	vals = []
	col_idx = []
	row_ptr = []
	for row in dense_matrix:
		idx = 0
		row_ptr.append(num)
		for ele in row:
			if ele != 0:
				vals.append(ele)
				col_idx.append(idx)
				num += 1
			idx += 1
	row_ptr.append(num)
	return vals, col_idx, row_ptr
