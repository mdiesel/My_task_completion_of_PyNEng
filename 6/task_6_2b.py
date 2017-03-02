'''
Задание 6.2b

Дополнить скрипт из задания 6.2a:
* вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.

Строки, которые начинаются на '!' отфильтровывать не нужно.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

if len(argv) != 2:
    print('Обработка файла с конфигурацией.')
    print(argv[0][2:] + ' <имя файла конфигурации>')
    exit()

try:
    with open(argv[1], 'r') as f, open('config_sw1_cleared.txt', 'w') as out:
        for line in f:
            if list(line.count(i) for i in ignore) == [0] * len(ignore):
                out.write(line)
except FileNotFoundError:
    print('Указанный файл не найден.')
