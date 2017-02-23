"""
Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом, чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
"""

from ipaddress import ip_interface
from sys import argv

def print_network(_network):
    '''
    Печатает сеть в десятичном и двоичном форматах
    '''
    network_splited = str(_network).split('.')
    for i in network_splited:
        print('{:10}'.format(i), end='')
    print('')
    for i in network_splited:
        print('{:10}'.format('0' * (8 - len(bin(int(i))[2:])) + bin(int(i))[2:]), end='')
    print('')

if len(argv) != 2:
    print("В качестве аргумента приниматеся адрес вида: 10.1.1.1/24")
    exit()

try:
    ip_address = ip_interface(str(argv[1]))
except ValueError:
    print("Не удалось распознать сеть.")
    exit()

if ip_address.version == 6:
    print("Скрипт не рассчитан на работу с IPv6")
    exit()

print_network(ip_address.network.network_address)

print('\nMask:\n{}'.format(ip_address.network.prefixlen))
print_network(ip_address.network.netmask)
