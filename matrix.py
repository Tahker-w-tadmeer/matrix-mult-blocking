import numpy as np


class Matrix:
    def __init__(self, matrix, t=int):
        self.matrix = matrix
        self.type = t

    @staticmethod
    def random(n: int, seed: int = 0, t=int):
        if seed != 0:
            np.random.seed(seed)
        return Matrix(np.random.randint(0, 100, size=(n, n), dtype=t), t)

    def __str__(self):
        return f"{self.matrix}"

    def multiply(self, m, block_size=0):
        if block_size < 1:
            block_size = 1
        matrix_a = self.matrix
        matrix_b = m.matrix
        n = matrix_a.shape[0]
        en = block_size * (matrix_a.shape[0] // block_size)

        resultant = np.zeros((matrix_a.shape[0], matrix_b.shape[1]), dtype=self.type)
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ArithmeticError("Cannot multiply matrices because of mismatched sizes")

        for kk in range(0, en, block_size):
            for jj in range(0, en, block_size):
                for i in range(n):
                    for j in range(jj, jj + block_size):
                        for k in range(kk, kk+block_size):
                            resultant[i, j] += matrix_a[i, k] * matrix_b[k, j]
        return resultant
