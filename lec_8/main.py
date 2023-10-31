import random

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[random.randint(1, 30) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

    def calculate_mean(self):
        total = sum(sum(row) for row in self.matrix)
        return total / (self.n * self.m)

    def calculate_row_sum(self, row_idx):
        if 0 <= row_idx < self.n:
            return sum(self.matrix[row_idx])
        return None

    def calculate_column_average(self, col_idx):
        if 0 <= col_idx < self.m:
            total = sum(row[col_idx] for row in self.matrix)
            return total / self.n
        return None

    def print_submatrix(self, col1, col2, row1, row2):
        if 0 <= col1 <= col2 < self.m and 0 <= row1 <= row2 < self.n:
            for i in range(row1, row2 + 1):
                sub_row = self.matrix[i][col1:col2 + 1]
                print(' '.join(map(str, sub_row))
            )
        else:
            print("Invalid submatrix coordinates.")

n = 3
m = 4
matrix = Matrix(n, m)

matrix.print_matrix()
print("Mean of the matrix:", matrix.calculate_mean())
print("Sum of row 1:", matrix.calculate_row_sum(1))
print("Average of column 2:", matrix.calculate_column_average(2))
print("Submatrix:")
matrix.print_submatrix(1, 3, 0, 2)
