'''
Глава 4. Пример access_template_argv.py
'''
from sys import argv

interface, vlan = argv[1:]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spaning-tree portfast',
                   'spaning-tree bpduguard enable']
print('interface {}'.format(interface))
print('\n'.join(access_template).format(int(vlan)))
