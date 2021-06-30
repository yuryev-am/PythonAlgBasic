"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Используем следующую задачу:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""
import sys


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)}, object={x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


def arr_sum(cnt):
    summa = 0
    sum_val = 1

    for i in range(cnt):
        summa += sum_val
        sum_val /= -2

    show_size(summa)
    show_size(sum_val)

    return summa


# type=<class 'float'>, size=24, object=0.666015625
# type=<class 'float'>, size=24, object=0.0009765625


def arr_sum1(val, cnt):
    if cnt == 1:
        show_size(val)
        return val
    show_size(val)
    show_size(cnt)
    return val + arr_sum1(val / -2, cnt - 1)


# type=<class 'int'>, size=28, object=1
# type=<class 'int'>, size=28, object=10
# type=<class 'float'>, size=24, object=-0.5
# type=<class 'int'>, size=28, object=9
# type=<class 'float'>, size=24, object=0.25
# type=<class 'int'>, size=28, object=8
# type=<class 'float'>, size=24, object=-0.125
# type=<class 'int'>, size=28, object=7
# type=<class 'float'>, size=24, object=0.0625
# type=<class 'int'>, size=28, object=6
# type=<class 'float'>, size=24, object=-0.03125
# type=<class 'int'>, size=28, object=5
# type=<class 'float'>, size=24, object=0.015625
# type=<class 'int'>, size=28, object=4
# type=<class 'float'>, size=24, object=-0.0078125
# type=<class 'int'>, size=28, object=3
# type=<class 'float'>, size=24, object=0.00390625
# type=<class 'int'>, size=28, object=2
# type=<class 'float'>, size=24, object=-0.001953125


def arr_sum2(cnt):
    arr_vals = [1]

    for i in range(1, cnt):
        arr_vals.append(arr_vals[i - 1] / -2)

    show_size(arr_vals)
    show_size(i)

    return sum(arr_vals)


# type=<class 'list'>, size=184, object=[1, -0.5, 0.25, -0.125, 0.0625, -0.03125, 0.015625, -0.0078125, 0.00390625, -0.001953125]
#  type=<class 'int'>, size=28, object=1
#  type=<class 'float'>, size=24, object=-0.5
#  type=<class 'float'>, size=24, object=0.25
#  type=<class 'float'>, size=24, object=-0.125
#  type=<class 'float'>, size=24, object=0.0625
#  type=<class 'float'>, size=24, object=-0.03125
#  type=<class 'float'>, size=24, object=0.015625
#  type=<class 'float'>, size=24, object=-0.0078125
#  type=<class 'float'>, size=24, object=0.00390625
#  type=<class 'float'>, size=24, object=-0.001953125

print(sys.version, sys.platform, '\n')

print(arr_sum(10))
print('\n')
print(arr_sum1(1, 10))
print('\n')
print(arr_sum2(10))

# Выводы.
# Как видно из результатов теста для 10 значенией последовательности по объему используемой памяти самой
# оптимальной является функция arr_sum, т.к в ней используются всего 2 переменные не зависимо от количества значений
# последовательности и занимает все это 48 байт памяти.
# Во втором случае с функцией arr_sum1 мы имеем рекурсию и в каждом вызове две переменные размером 28 и 24 байта на
# каждый вызов функции. Итого для вычисления 10 значений мы тратим 496 байт
# Третий случай arr_sum2 показывает нам количество памяти 244 байт.
# Надо сказать, что последние 2 варианта зависят от количества элементов последовательности.
