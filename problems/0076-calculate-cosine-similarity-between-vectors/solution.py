import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	v1_norm = 0 
	v2_norm = 0

	for i in v1:
		v1_norm += (i*i)

	for j in v2:
		v2_norm += (j*j)

	return np.dot(v1, v2)/((v1_norm**0.5)*(v2_norm**0.5))