'''
Глава 4. Пример access_template.py
'''

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spaning-tree portfast',
                   'spaning-tree bpduguard enable']
print('Конфигурация интерфейса в режиме access:')
print('\n'.join(access_template).format(5))
