"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

# Строим словарь с числами от 2 до 9 в качестве ключей и нулевыми значениями.
numbers_dic = {i: 0 for i in range(2, 10)}
# print(numbers_dic)

for number in range(2, 100):
    for key in numbers_dic.keys():
        if number % key == 0:
            numbers_dic[key] += 1

for item in numbers_dic.items():
    print(f'Количество чисел кратных {item[0]} равно {item[1]}')
