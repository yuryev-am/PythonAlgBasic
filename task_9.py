"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
его цифр.
"""

in_number = input('Введите натуральное число или END для выхода: ')
cur_max_sum = -1
cur_max_number = -1
while in_number != 'END':
    tmp_sum = 0
    tmp_number = in_number
    in_number = int(in_number)
    while in_number > 0:
        tmp_sum += in_number % 10
        in_number //= 10
    if tmp_sum > cur_max_sum:
        cur_max_sum = tmp_sum
        cur_max_number = tmp_number
    in_number = input('Введите натуральное число или END для выхода: ')
if cur_max_number != -1:
    print(f'У числа {cur_max_number} максимальная сумма, которая равна {cur_max_sum}')
