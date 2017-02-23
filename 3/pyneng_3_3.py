'''
Задание 3.2
    Получить из строки CONFIG список VLAN вида ['10', '20', '30'].

    CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
'''
CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"

VLANS = CONFIG[30:].split(',')

print(VLANS)
