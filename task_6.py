"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

symbols = 'abcdefghijklmnopqrstuvwxyz'

a = int(input('Номер буквы в алфавите: '))
if a <= 0 or a > len(symbols):
    print('Такой буквы не существует')
else:
    print(f'Буква с номером {a}: {symbols[a - 1]}')
