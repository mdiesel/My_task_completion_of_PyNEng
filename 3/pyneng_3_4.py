'''
Задание 3.4
'''

command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"

VLANS = set(command1[30:].split(',') + command2[30:].split(','))

print(VLANS)
