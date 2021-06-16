"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

numbers_cnt = int(input('Введите количество вводимых чисел: '))
digit = input('Введите искомую цифру: ')

digit_cnt = 0
for i in range(numbers_cnt):
    tmp_number = input(f'Введите {i + 1} число: ')
    digit_cnt += tmp_number.count(digit)

print(f'Цифра {digit} встречается {digit_cnt} раз.')
