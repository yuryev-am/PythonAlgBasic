"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def hex_summa(x, y):
    hex_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = hex_numbers[x.pop()] + hex_numbers[y.pop()] + transfer
        else:
            res = hex_numbers[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(hex_numbers[res])
        else:
            result.appendleft(hex_numbers[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')

    return list(result)


def hex_multiply(x, y):
    hex_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    tmp = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = hex_numbers[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            tmp[i].appendleft(m * hex_numbers[x[j]])

        for _ in range(i):
            tmp[i].append(0)

    transfer = 0

    for _ in range(len(tmp[-1])):
        res = transfer

        for i in range(len(tmp)):
            if tmp[i]:
                res += tmp[i].pop()

        if res < 16:
            result.appendleft(hex_numbers[res])
        else:
            result.appendleft(hex_numbers[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(hex_numbers[transfer])

    return list(result)


a = list(input('Введите первое шестнадцатиричное число: ').upper())
b = list(input('Введите второе шестнадцатиричное число: ').upper())
# print(a, b)

print(f'{"".join(a)} + {"".join(b)} = {"".join(hex_summa(a, b))}')
print(f'{"".join(a)} * {"".join(b)} = {"".join(hex_multiply(a, b))}')
