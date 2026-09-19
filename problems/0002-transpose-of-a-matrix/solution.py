def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    
    rows = len(a)
    cols = len(a[0])

    result = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(a[i][j])
        result.append(row)

    return result