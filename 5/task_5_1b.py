'''
Задание 5.1b

Сделать копию скрипта задания 5.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
'''
from ipaddress import IPv4Address

ipv4_addr = False

while not ipv4_addr:
    address = input("Введите IP адрес в десятично-точечном формате: ")
    try:
        ipv4_addr = IPv4Address(address)
    except ValueError:
        print('Incorrect IPv4 address.')

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

