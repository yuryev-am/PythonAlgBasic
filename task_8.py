"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

matrix = []

for i in range(4):
    row = []
    summa = 0
    for j in range(4):
        in_number = int(input(f'Введите элемент {i} строки и {j} столбца: '))
        summa += in_number
        row.append(in_number)

    row.append(summa)
    matrix.append(row)

for el in matrix:
    print(el)
