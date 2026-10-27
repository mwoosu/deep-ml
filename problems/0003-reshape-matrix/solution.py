import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	r, c = np.shape(a)
	row, col = new_shape
	if r*c != row*col:
		return []
	
	reshaped = []
	b = []

	for i in a:
		for j in i:
			b.append(j)
	k = 0
	for i in range(row):
		line = []
		for j in range(col):
			line.append(b[k])
			k+=1
		reshaped.append(line)
			
	return reshaped