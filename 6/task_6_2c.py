'''
Задание 6.2c

Переделать скрипт из задания 6.2b:
* передавать как аргументы:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И затем записать оставшиеся строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

if len(argv) != 3:
    print('Обработка файла с конфигурацией.')
    print(argv[0][2:] + ' <имя файла конфигурации> <итоговый файл>')
    exit()

try:
    with open(argv[1], 'r') as f, open(argv[2], 'w') as out:
        for line in f:
            if list(line.count(i) for i in ignore) == [0] * len(ignore):
                out.write(line)
except FileNotFoundError:
    print('Указанный файл не найден.')
except OSError:
    print('Неподдерживаемое имя файла')
    