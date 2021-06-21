"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

arr = [random.randint(0, 100) for _ in range(10)]

print(f'Исходный массив чисел: {arr}')

max_idx = 0
min_idx = 0

for i, val in enumerate(arr):
    if val > arr[max_idx]:
        max_idx = i
    elif val < arr[min_idx]:
        min_idx = i
print('\n')
print(f'Индекс минимального значения {min_idx}. Само значение равно: {arr[min_idx]}')
print(f'Индекс максимального значения {max_idx}. Само значение равно: {arr[max_idx]}')
print('\n')

summa = 0
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

for i in range(min_idx + 1, max_idx):
    summa += arr[i]

print(f'Сумма значений между минимальным и максимальным элементами: {summa}')
