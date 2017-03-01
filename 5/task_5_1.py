'''
Задание 5.1

1. Запросить у пользователя ввод IP-адреса в десятично-точечном формате.
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239
'''

from ipaddress import IPv4Address

address = input("Введите IP адрес в десятично-точечном формате: ")
try:
    ipv4_addr = IPv4Address(address)
except ValueError:
    print("Не удалось распознать адрес")
    exit()

first = int(str(ipv4_addr).split('.')[0])

if ipv4_addr.is_multicast:
    print('multicast')
elif str(ipv4_addr) == '255.255.255.255':
    print('local broadcast')
elif str(ipv4_addr) == '0.0.0.0':
    print('unassigned')
elif first >= 0 and first < 224:
    print('unicast')
else:
    print('unused')

