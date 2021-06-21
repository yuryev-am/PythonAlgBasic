"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random as rnd

M = 5
N = 5

matrix = [[rnd.randint(0, 50) for _ in range(M)] for _ in range(N)]

for el in matrix:
    print(el)

max_val = 0

for j in range(N):
    min_val = matrix[0][j]

    for i in range(M):
        if min_val > matrix[i][j]:
            min_val = matrix[i][j]
    #  print(min_val)
    if min_val > max_val:
        max_val = min_val

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_val}')
