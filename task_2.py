"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, code_list=None, code=''):
    if code_list is None:
        code_list = dict()
    if root is None:
        return

    if isinstance(root.value, str):
        code_list[root.value] = code
        return code_list

    get_code(root.left, code_list, code + '0')
    get_code(root.right, code_list, code + '1')

    return code_list


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]
    return [key for key in string_count][0]


def coding(string, code_list):
    res = ''
    for symbol in string:
        res += code_list[symbol]
    return res


def decoding(string, code_list):
    res = ''
    i = 0

    while i < len(string):
        for code in code_list:
            if string[i:].find(code_list[code]) == 0:
                res += code
                i += len(code_list[code])

    return res


my_string = input('Введите строку: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр кодирования: {codes}')

coding_str = coding(my_string, codes)
print('Закодированная строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)
