'''
Функции для задания 8.1
'''
def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    result = []
    for intf in access:
        result.append('interface {}'.format(intf))
        for line in access_template:
            if line.endswith('vlan'):
                result.append('{} {}'.format(line, access[intf]))
            else:
                result.append(line)
        if psecurity:
            for line in port_security:
                result.append(line)

    return result

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    result = []
    for intf in trunk:
        result.append('interface {}'.format(intf))
        for line in trunk_template:
            if line.endswith('vlan'):
                result.append('{} {}'.format(line, ','.join(str(i) for i in trunk[intf])))
            else:
                result.append(line)
    return result

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
        print('Не найден файл конфигурации {}.'.format(config))
        exit()
    return (dict_access, dict_trunk)

