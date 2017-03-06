'''
Задание 7.2a

Сделать копию скрипта задания 7.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.
'''

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    result = {}
    for intf in trunk:
        result[intf] = ['interface {}'.format(intf)]
        for line in trunk_template:
            if line.endswith('vlan'):
                result[intf].append('{} {}'.format(line, ','.join(str(i) for i in trunk[intf])))
            else:
                result[intf].append(line)
    return result




trunk_dict = {'FastEthernet0/1':[10, 20, 30],
              'FastEthernet0/2':[11, 30],
              'FastEthernet0/4':[17]}

print(generate_trunk_config(trunk_dict))
