"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""

my_str = str(input("Введите строку: "))
print(f'Введенная вами строка имеет длину: {len(my_str)}')

subs_set = set()

for i in range(len(my_str)):
    for j in range(len(my_str) - 1 if i == 0 else len(my_str), i, -1):
        subs_set.add(hash(my_str[i:j]))

print(f'Количество подстрок: {len(subs_set)}')
