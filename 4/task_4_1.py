"""
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.
"""

from ipaddress import IPv4Network

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



try:
    network = IPv4Network(input('Введите сеть в формате: 10.1.1.0/24: '))
except ValueError:
    print("Не удалось распознать сеть.")
    exit()

print_network(network.network_address)

print('\nMask:\n{}'.format(network.prefixlen))
print_network(network.netmask)

