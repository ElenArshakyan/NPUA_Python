import random
def generate_random_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix
def get_column_sum(matrix, column_index):
    column_sum = sum(row[column_index] for row in matrix)
    return column_sum
def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
random_matrix = generate_random_matrix(rows, cols)
print("Random Matrix:")
for row in random_matrix:
    print(row)
column_index = int(input("Enter the column index to calculate its sum: "))
row_index = int(input("Enter the row index to calculate its average: "))
column_sum = get_column_sum(random_matrix, column_index)
row_average = get_row_average(random_matrix, row_index)

print(f"Sum of column {column_index}: {column_sum}")
print(f"Average of row {row_index}: {row_average}")
