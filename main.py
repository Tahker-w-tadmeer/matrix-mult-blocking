import time
import pyautogui
from matrix import SquareMatrix
from calculate_time import CalculateTime

seed = round(time.time())
A = SquareMatrix.random(100, round(time.time()))
B = SquareMatrix.random(100, round(time.time()) + 15)

# print(f"Matrix A:\n {A}\n")
# print(f"Matrix B:\n {B}\n")

blocks = [
    1, 8, 16, 24, 32, 48, 64
]

for block in blocks:
    calc = CalculateTime(lambda: A.multiply(B, block))
    time = calc.execute() / 10**6
    print(f"Time with {block} blocks: {time}ms")
