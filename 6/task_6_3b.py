'''
Задание 6.3b

Сделать копию скрипта задания 6.3a.

Дополнить скрипт:
  Запросить у пользователя ввод номера VLAN.
  Выводить информацию только по указанному VLAN.

'''

mac_list = []
vlan = -1
try:
    with open('CAM_table.txt') as f:
        while vlan == -1:
            try:
                vlan = int(input('Input VLAN number: '))
                if vlan < 1 or vlan > 4094:
                    vlan = -1
                    print('Vlan numbe must be an integer between 1 and 4094. Please, try again: ')
            except ValueError:
                print('Vlan numbe must be an integer between 1 and 4094. Please, try again: ')
        for line in f:
            splited = line.split()
            if len(splited) == 4:
                if len(splited[1]) == 14:
                    if splited[0] == str(vlan):
                        mac_list.append('{:7}{:19}{}'.format(splited[0], splited[1], splited[3]))
    for i in sorted(mac_list):
        print(i)
except FileNotFoundError:
    print('Файл не найден')
