'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
Скрипт не должен выводить команды, в которых содержатся слова,
которые указаны в списке ignore.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

if len(argv) != 2:
    print('Обработка файла с конфигурацией.')
    print(argv[0][2:] + ' <имя файла конфигурации>')
    exit()

try:
    with open(argv[1], 'r') as f:
        for line in f:
            if line[0] != '!':
                if list(line.count(i) for i in ignore) == [0] * len(ignore):
                    print(line.rstrip())
except FileNotFoundError:
    print('Указанный файл не найден.')
