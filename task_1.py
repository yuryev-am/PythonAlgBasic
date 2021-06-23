"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
уроков.

Возьмем для примера следующую задачу:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""
import cProfile


def arr_sum(cnt):
    summa = 0
    sum_val = 1

    for i in range(cnt):
        summa += sum_val
        sum_val /= -2

    return summa


# "task_1.arr_sum(100)"
# 10 loops, best of 5: 6.18 usec per loop

# "task_1.arr_sum(200)"
# 10 loops, best of 5: 12.4 usec per loop

# "task_1.arr_sum(400)"
# 10 loops, best of 5: 25.1 usec per loop

# "task_1.arr_sum(800)"
# 10 loops, best of 5: 58.2 usec per loop

# "task_1.arr_sum(1000)"
# 10 loops, best of 5: 66.8 usec per loop

# "task_1.arr_sum(2000)"
# 10 loops, best of 5: 134 usec per loop


# cProfile.run('arr_sum(900)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:7(arr_sum)

# cProfile.run('arr_sum(100000)')
# 4 function calls in 0.009 seconds
# 1    0.009    0.009    0.009    0.009 task_1.py:7(arr_sum)

def arr_sum1(val, cnt):
    if cnt == 1:
        return val
    return val + arr_sum1(val / -2, cnt - 1)


# "task_1.arr_sum1(1, 100)"
# 10 loops, best of 5: 11.8 usec per loop

# "task_1.arr_sum1(1, 200)"
# 10 loops, best of 5: 25.9 usec per loop

# "task_1.arr_sum1(1, 400)"
# 10 loops, best of 5: 61.6 usec per loop

# "task_1.arr_sum1(1, 800)"
# 10 loops, best of 5: 130 usec per loop

# "task_1.arr_sum1(1, 1000)"
# RecursionError: maximum recursion depth exceeded in comparison

# cProfile.run('arr_sum1(1, 900)')
# 903 function calls (4 primitive calls) in 0.001 seconds
# 900/1    0.001    0.000    0.001    0.001 task_1.py:34(arr_sum1)

# cProfile.run('arr_sum1(1, 100000)')
# RecursionError: maximum recursion depth exceeded in comparison

def arr_sum2(cnt):
    arr_vals = [1]

    for i in range(1, cnt):
        arr_vals.append(arr_vals[i - 1] / -2)

    return sum(arr_vals)

# "task_1.arr_sum2(100)"
# 10 loops, best of 5: 12 usec per loop

# "task_1.arr_sum2(200)"
# 10 loops, best of 5: 20.7 usec per loop

# "task_1.arr_sum2(400)"
# 10 loops, best of 5: 44.2 usec per loop

# "task_1.arr_sum2(800)"
# 10 loops, best of 5: 93.2 usec per loop

# "task_1.arr_sum2(1000)"
# 10 loops, best of 5: 115 usec per loop

# cProfile.run('arr_sum2(900)')
# 904 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_1.py:55(arr_sum2)

# cProfile.run('arr_sum2(100000)')
# 100004 function calls in 0.029 seconds
# 1    0.021    0.021    0.029    0.029 task_1.py:55(arr_sum2)

# print(arr_sum(10))
# print(arr_sum1(1, 10))
# print(arr_sum2(10))

# Итого. Лучшим алгоритмом оказался обычный цикл в функции arr_sum. Сложность линейная O(n).
