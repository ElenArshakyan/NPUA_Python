def vector_matrix_product(vector, matrix):
    if len(matrix[0]) != len(vector):
        print("Error: Cannot multiply matrix and vector")
        return None

    result = []
    for row in matrix:
        dot_product = sum(vector[i] * row[i] for i in range(len(vector)))
        result.append(dot_product)

    return result

def save_result_to_file(result, filename):
    with open(filename, 'w') as file:
        for value in result:
            file.write(str(value) + '\n')

# Example usage:
vector = [1, 0, -6]
matrix = [
    [-2, 0, -13],
    [7, -3, 8],
    [1, 12, -21]
]

result = vector_matrix_product(vector, matrix)

if result is not None:
    print("Vector - Matrix Product is:")
    print(result)
    save_result_to_file(result, 'result.txt')