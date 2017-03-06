'''
Задание 7.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt
'''

def get_int_vlan_map(config):
    """
    config - имя конфигурационного файла коммутатора

    Возвращает кортеж словарей:
    - первый словарь: порты в режиме access
      { 'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17  }
    - второй словарь: порты в режиме trunk
      { 'FastEthernet0/1':[10, 20],
        'FastEthernet0/2':[11, 30],
        'FastEthernet0/4':[17] }

    """
    dict_access = {}
    dict_trunk = {}

    try:
        with open(config, 'r') as f:
            for line in f:
                if line.startswith('interface F'):
                    intf = line.split()[1]
                    print(intf)
                    line = f.readline().strip()
                    if line.startswith('switchport') and line.endswith('access'):
                        line = f.readline().split()
                        dict_access[intf] = int(line[-1])
                    elif line.startswith('switchport') and line.endswith('dot1q'):
                        line = f.readline().split()
                        dict_trunk[intf] = [int(i) for i in line[-1].split(',')]
                pass
    except OSError:
        print('Не найден файл конфигурации')
        exit()
    return (dict_access, dict_trunk)


print(get_int_vlan_map('config_sw1.txt'))
