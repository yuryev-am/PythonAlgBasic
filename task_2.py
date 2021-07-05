"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 10  # Размер массива


def merge_sort(array_for_sort, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array_for_sort, start, mid)
        merge_sort(array_for_sort, mid, end)
        merge_list(array_for_sort, start, mid, end)


def merge_list(array_for_sort, start, mid, end):
    left = array_for_sort[start:mid]
    right = array_for_sort[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            array_for_sort[k] = left[i]
            i = i + 1
        else:
            array_for_sort[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array_for_sort[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array_for_sort[k] = right[j]
            j = j + 1
            k = k + 1


array = [random.randint(0, 50) for _ in range(size)]  # Генерируем массив рандомных значений
print(f'Исходный массив: {array}')
merge_sort(array, 0, len(array))
print(f'Отсортированный массив: {array}')
