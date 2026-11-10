import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    
    if np.linalg.det(A) == 0 or np.linalg.det(S) == 0:
        return -1
    

    return np.dot(np.dot(np.linalg.inv(T), A), S)