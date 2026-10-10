def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    b = []
    for i in range(len(a[0])):
        b.append([])

    for row in a:
        for i in range(len(row)):
            b[i].append(row[i])

    return b
    pass