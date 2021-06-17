"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

arr = [random.randint(-10, 10) for _ in range(10)]

print(f'Исходный массив:\n {arr}')

min_idx = -1

for i, item in enumerate(arr):
    if (item < 0 and min_idx == -1) or (arr[min_idx] < item < 0):
        min_idx = i

print(f'Индекс максимального отрицательного значения: {min_idx}. Значение: {arr[min_idx]}')
