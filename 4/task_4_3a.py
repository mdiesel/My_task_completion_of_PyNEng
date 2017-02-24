"""
Задание 4.3a

В этой задаче нельзя использовать условие if.

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'
"""

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

dict_template = {'access':access_template, 'trunk':trunk_template}
vlan_template = {'access':'Enter VLAN number: ', 'trunk':'Enter allowed VLANs: '}


interface_mode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface type and number: ')
vlan = input(vlan_template[interface_mode])

print('\ninterface {}'.format(interface))
print('\n'.join(dict_template[interface_mode]).format(vlan))
