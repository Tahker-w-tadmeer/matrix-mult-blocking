import time
import pyautogui
from matrix import Matrix

seed = round(time.time())
A = Matrix.random(3, 9, seed)
B = Matrix.random(10, 2, seed)

print(f"Matrix A:\n {A}\n")
print(f"Matrix B:\n {B}\n")

print(f"A x B:\n {A.multiply(B)}\n")
