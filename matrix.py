import numpy as np


class Matrix:
    def __init__(self, matrix, t=int):
        self.matrix = matrix
        self.type = t

    @staticmethod
    def random(rows: int, colums: int, seed: int = 0, t=int):
        if seed != 0:
            np.random.seed(seed)
        return Matrix(np.random.randint(0, 100, size=(rows, colums), dtype=t), t)

    def __str__(self):
        return f"{self.matrix}"

    def multiply(self, m):
        matrix_a = self.matrix
        matrix_b = m.matrix
        resultant = np.zeros((matrix_a.shape[0], matrix_b.shape[1]), dtype=self.type)
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ArithmeticError("Cannot multiply matrices because of mismatched sizes")

        for row in range(len(matrix_a)):
            for col in range(len(matrix_b[0])):
                for element in range(len(matrix_b)):
                    resultant[row, col] += matrix_a[row, element] * matrix_b[element, col]
        return resultant
