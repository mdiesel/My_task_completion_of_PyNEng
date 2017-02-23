'''
Глава 4. Пример access_template_input.py
'''

interface = input('Enter interface type and number: ')
vlan = int(input('Enter VLAN number: '))

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spaning-tree portfast',
                   'spaning-tree bpduguard enable']
print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
