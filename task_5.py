"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

symbols = 'abcdefghijklmnopqrstuvwxyz'
a = input('Введите первую букву: ').lower()
b = input('Введите вторую букву: ').lower()

print(f'Индекс символа {a} = {symbols.find(a) + 1}')
print(f'Индекс символа {b} = {symbols.find(b) + 1}')

if a == b:
    c = 0
else:
    c = abs(symbols.find(b) - symbols.find(a)) - 1

print(f'Между символами {a} и {b} находится {c} символов')
