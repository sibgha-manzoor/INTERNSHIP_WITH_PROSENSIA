class MatrixDimensionError(Exception):
    pass

class MatrixValueError(Exception):
    pass

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise MatrixDimensionError("Matrices are not of the same dimensions.")
    
    for matrix in (matrix1, matrix2):
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixValueError("Matrices must contain only numbers.")
    
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result.append([element1 + element2 for element1, element2 in zip(row1, row2)])
    
    return result

try:
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    sum_matrix = add_matrices(matrix_a, matrix_b)
    print(sum_matrix) 
except (MatrixDimensionError, MatrixValueError) as e:
    print(e)