import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a_row, a_col = np.shape(a)
    b_row, b_col = np.shape(b)

    if a_col != b_row:
        return -1
    b_t = list(zip(*b))
    result = []
    for row in a:
        result_row = []
        for col in b_t:
            result_row.append(sum(x*y for x,y in zip(row,col)))
        result.append(result_row)

    return result