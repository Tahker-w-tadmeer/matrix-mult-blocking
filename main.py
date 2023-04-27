import matplotlib.pyplot as plt
from matrix import Matrix
from calculate_time import CalculateTime
import sqlite3

con = sqlite3.connect("calculations.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS calculations")
cur.execute("""CREATE TABLE calculations(
    size int,
    blocks int,
    time int
)""")

matrices_sizes = [
    3, 10, 25, 50, 75, 100, 500, 1000
]

blocks = [
    1, 20, 100, 600, 1000, 1500
]
x = blocks

for matrix in matrices_sizes:
    A = Matrix.random(matrix)
    B = Matrix.random(matrix)
    y = []
    data = []
    for block in blocks:
        calc = CalculateTime(lambda: A.multiply(B, block))
        time = calc.execute()
        y.append(time / 10**6)
        data.append((matrix, block, time))

    cur.executemany("INSERT INTO calculations VALUES (?, ?, ?)", data)
    con.commit()

    plt.plot(x, y, label=f"{matrix}x{matrix}", marker="o")

cur.close()

plt.legend()
plt.xlabel("Block size")
plt.ylabel("Execution time (ms)")
plt.show()
