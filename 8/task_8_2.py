"""
Задание 8.2

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

"""

from sys import argv

def parse_cdp_neighbors(filename):
    '''
    Функция парсинга вывода команды show cdp neighbors
    '''
    result = {}
    try:
        with open(filename) as f:
            line = f.readline()
            hostname = line[:line.index('>')]
            line = f.readline()
            start = True
            while start:
                line = f.readline().split()
                if len(line) > 0:
                    if line[0] == 'Device':
                        start = False
            line = f.readline().split()
            while len(line) > 0:
                result[(hostname, line[1] + line[2])] = (line[0], line[-2] + line[-1])
                line = f.readline().split()
    except OSError:
        print('Файл {} не найден'.format(filename))
        exit()
    return result

if __name__ == '__main__':
    if len(argv) != 2:
        print('Программа ожидает на входе 1 параметр - имя файла с выводом комманды show cdp neighbors.\nНеверное число параметров.')
        exit()

    print(parse_cdp_neighbors(argv[1]))

