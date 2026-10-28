def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	output = []
	for row in matrix:
		list = []
		for element in row:
			list.append(element*scalar)
		output.append(list)
	return output
	