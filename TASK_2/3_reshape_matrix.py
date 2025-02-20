import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    flat_list = []

    for row in a:
        for num in row:
            flat_list.append(num)

    new_rows, new_cols = new_shape

    if len(flat_list) != new_rows * new_cols:
        return []  

    reshaped_matrix = []
    index = 0
    for i in range(new_rows):
        row = []
        for j in range(new_cols):
            row.append(flat_list[index])
            index += 1
        reshaped_matrix.append(row)

    return reshaped_matrix
