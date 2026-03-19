def saddle_points(matrix):
    if not matrix:
        return []
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    n, m = len(matrix), len(matrix[0])
    result = []
    
    row_maxes = [max(row) for row in matrix]
    
    col_mins = []
    for col in range(m):
        col_values = [matrix[row][col] for row in range(n)]
        col_mins.append(min(col_values))
    
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == row_maxes[row] and matrix[row][col] == col_mins[col]:
                result.append({"row": row + 1, "column": col + 1})
    
    return sorted(result, key=lambda x: (x["row"], x["column"]))
