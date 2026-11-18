import numpy as np

def rref(matrix):
    row, col = np.shape(matrix)
    matrix = np.array(matrix, dtype=float)

    for i in range(row):
        pivot = matrix[i]
        pivot_col = None

        for j in range(col):
            if matrix[i][j] != 0:
                pivot_col = j
                break
        if pivot_col is None:
            continue

        pivot_val = matrix[i][pivot_col]
        matrix[i] = matrix[i]/pivot_val
        pivot = matrix[i]

        
        for j in range(row):

            if i == j:
                continue

            factor = matrix[j][pivot_col]/pivot[pivot_col]
            matrix[j] = matrix[j] - [x*factor for x in pivot]
    result = []
    for row in matrix:
        pivot_col = len(row)
        for idx, val in enumerate(row):
            if val != 0:
                pivot_col = idx
                break
        result.append((pivot_col, row))

    result.sort()

    return [val for _, val in result]

