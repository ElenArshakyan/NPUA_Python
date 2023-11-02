class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is not None:
            if len(data) != rows or any(len(row) != columns for row in data):
                raise ValueError("Invalid data for matrix dimensions")
            self.data = data
        else:
            self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions do not match for addition")
        result = Matrix(self.rows, self.columns)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions do not match for subtraction")
        result = Matrix(self.rows, self.columns)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.columns))
        return result


if __name__ == "__main__":
   
    matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
    matrix2 = Matrix(2, 2, [[5, 6], [7, 8]])

   
    result_add = matrix1 + matrix2
    print("Matrix Addition:")
    print(result_add)

    
    result_sub = matrix1 - matrix2
    print("Matrix Subtraction:")
    print(result_sub)

  
    result_mul = matrix1 * matrix2
    print("Matrix Multiplication:")
    print(result_mul)