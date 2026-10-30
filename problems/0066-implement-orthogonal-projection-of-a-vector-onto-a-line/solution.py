import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot = sum(i*j for (i,j) in zip(v, L))
	denominator = sum(j*j for j in L)

	return [dot / denominator * j for j in L]
	pass
