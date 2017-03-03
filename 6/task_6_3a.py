'''
Задание 6.3a

Сделать копию скрипта задания 6.3.

Дополнить скрипт:
  Отсортировать вывод по номеру VLAN
'''

mac_list = []
try:
    with open('CAM_table.txt') as f:
        for line in f:
            splited = line.split()
            if len(splited) == 4:
                if len(splited[1]) == 14:
                    mac_list.append('{:7}{:19}{}'.format(splited[0], splited[1], splited[3]))
    for i in sorted(mac_list):
        print(i)
except FileNotFoundError:
    print('Файл не найден')
