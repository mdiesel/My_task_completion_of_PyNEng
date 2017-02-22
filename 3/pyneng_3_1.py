'''
Задание 3.1
'''

OSPF_ROUTE = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

D_ROUTE_INFO = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

ROUTE_INFO = dict.fromkeys(D_ROUTE_INFO, None)



OSPF_ROUTE_SPLITED = OSPF_ROUTE.replace(',', '').split()

if OSPF_ROUTE_SPLITED[0] == 'O':
    ROUTE_INFO['Protocol'] = 'OSPF'
    ROUTE_INFO['Prefix'] = OSPF_ROUTE_SPLITED[1]
    ROUTE_INFO['AD/Metric'] = OSPF_ROUTE_SPLITED[2][1:-1]
    ROUTE_INFO['Next-Hop'] = OSPF_ROUTE_SPLITED[4]
    ROUTE_INFO['Last update'] = OSPF_ROUTE_SPLITED[5]
    ROUTE_INFO['Outbound Interface'] = OSPF_ROUTE_SPLITED[6]

for i in D_ROUTE_INFO:
    print('{0:25} {1}'.format(i + ':', ROUTE_INFO[i]))
