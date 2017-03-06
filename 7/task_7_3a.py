'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

    В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
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
                    line = f.readline().strip()
                    if line.startswith('switchport') and line.endswith('access'):
                        line = f.readline().split()
                        if line[0] == 'switchport':
                            dict_access[intf] = int(line[-1])
                        else:
                            dict_access[intf] = 1
                    elif line.startswith('switchport') and line.endswith('dot1q'):
                        line = f.readline().split()
                        dict_trunk[intf] = [int(i) for i in line[-1].split(',')]
    except OSError:
        print('Не найден файл конфигурации')
        exit()
    return (dict_access, dict_trunk)


print(get_int_vlan_map('config_sw2.txt'))
