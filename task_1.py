"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        # print(array)
    return array


# Данный вариант сортировки во внутреннем цикле проверяет, если при проходе по оставшимся элементам перестановок больше
# не было, то значит уже все отсортировано и можно возвращать массив.
def bubble_sort_optimize(array):
    n = 1
    while n < len(array):
        no_swap = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                no_swap = False
        # print(array)
        if no_swap:
            return array
        n += 1

    return array


size = 10  # Размер массива

# Создадим рандомный массив и скопируем его, чтобы потом передать одинаковые массивы в обе функции для проверки
array1 = [random.randint(-100, 100) for _ in range(size)]  # Генерируем массив рандомных значений
array2 = array1.copy()

print(f'Исходный массив: {array1}')
print(f'Отсортированный массив (bubble_sort):          {bubble_sort(array1)}')
print(f'Отсортированный массив (bubble_sort_optimize): {bubble_sort_optimize(array2)}')
