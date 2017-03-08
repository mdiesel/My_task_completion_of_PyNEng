'''
Найти индекс последнего вхождения элемента с конца.

Например, для списка num_list, индекс последнего вхождения элемента 10 - 4; для списка word_list, индекс последнего вхождения элемента 'ruby' - 6.

Сделать решение общим и проверить на разных списках и элементах.

Не использовать для решения циклы (for, while) и условия (if/else).
'''
num_list = [10, 2, 30, 100, 10, 50, 11, 30]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

what_to_find = 'perl'

try:
    print(len(num_list) - num_list[::-1].index(what_to_find) - 1)
except:
    pass
try:
    print(len(word_list) - word_list[::-1].index(what_to_find) - 1)
except:
    pass

