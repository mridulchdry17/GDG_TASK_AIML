def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    if not matrix:  
        return []
    
    if mode == "row":
        return [sum(row) / len(row) for row in matrix]

    elif mode == "column":
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        means = []
        for j in range(num_cols): 
            col_sum = sum(matrix[i][j] for i in range(num_rows))
            means.append(col_sum / num_rows)
        return means
