"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках
"""

import random


def find_median(array, first, last):
    array = array.copy()
    idx = len(array) // 2

    if first >= last:
        return array[idx]

    half_idx = array[idx]
    i = first
    j = last

    while i <= j:
        while array[i] < half_idx:
            i += 1
        while array[j] > half_idx:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if idx < i:
        array[idx] = find_median(array, first, j)
    elif j < idx:
        array[idx] = find_median(array, i, last)

    return array[idx]


m = 5  # Изменить при необходимости
size = 2 * m + 1  # Размер массива

my_array = [random.randint(-50, 50) for _ in range(size)]  # Генерируем массив рандомных значений
print(f'Исходный массив: {my_array}')
print(f'Медиана: {find_median(my_array, 0, len(my_array) - 1)}')
