import numpy as np

def inverse(matrix):

    n = len(matrix)
    aug = []
    for i, row in enumerate(matrix):
        identity_row = [0] * n
        identity_row[i] = 1
        aug.append(row + identity_row)

    return aug

def transform_basis(B, C):
    aug = inverse(C)
    n = len(aug)

    for i, row in enumerate(aug):
        pivot = None
        for r in range(i, n):
            if aug[r][i] != 0:
                pivot = r
                break
        if pivot is None:
            raise ValueError("")
        aug[i], aug[pivot] = aug[pivot], aug[i]
        pivot_val = aug[i][i]


        aug[i] = [x / pivot_val for x in aug[i]]
        factor = None
        for r in range(n):
            if r == i:
                continue

            
            factor = aug[r][i]
            
            for j in range(len(aug[r])):
                aug[r][j] = aug[r][j] - factor*aug[i][j]
    
    c_inv = [row[n:] for row in aug]
    b_cols = list(zip(*B))
    result = []

    for row in c_inv:
        result_row = []
        for col in b_cols:
            value = sum(x*y for x,y in zip(row, col))
            result_row.append(value)
        result.append(result_row)
        

    return result 
