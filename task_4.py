"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

arr = [random.randint(0, 20) for _ in range(50)]

print(f'Исходный массив:\n{arr}')

numb_cnt_dic = {}
max_numb = None
max_numb_cnt = 0

for item in arr:
    if numb_cnt_dic.get(item):
        numb_cnt_dic[item] += 1
    else:
        numb_cnt_dic[item] = 1
    if numb_cnt_dic[item] > max_numb_cnt:
        max_numb_cnt = numb_cnt_dic[item]
        max_numb = item

print(f'Словарь чисел и сколько раз они встречаются в исходном массиве:\n {numb_cnt_dic}')

print(f'Число {max_numb} встретилось максимальное число раз: {max_numb_cnt}')
