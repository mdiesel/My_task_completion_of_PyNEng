'''
Задание 6.1

Аналогично заданию 3.1 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:				OSPF
Prefix:					10.0.24.0/24
AD/Metric:				110/41
Next-Hop:				10.0.13.3
Last update:			3d18h
Outbound Interface:		FastEthernet0/0

Так как это первое задание с открытием файла, заготовка для открытия файла уже сделана.
'''

def print_route(route_line):
    '''
    Печатаем инфомацию о маршруте
    '''
    d_route_info = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update',
                    'Outbound Interface']

    route_info = dict.fromkeys(d_route_info, None)

    route_splited = route_line.replace(',', '').split()

    if route_splited[0] == 'O':
        route_info['Protocol'] = 'OSPF'
        route_info['Prefix'] = route_splited[1]
        route_info['AD/Metric'] = route_splited[2][1:-1]
        route_info['Next-Hop'] = route_splited[4]
        route_info['Last update'] = route_splited[5]
        route_info['Outbound Interface'] = route_splited[6]

    for i in d_route_info:
        print('{0:25} {1}'.format(i + ':', route_info[i]))


with open('ospf.txt', 'r') as f:
    for line in f:
        print_route(line)
        print()
