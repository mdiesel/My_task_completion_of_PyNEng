'''
Задание 5.1a

Сделать копию скрипта задания 5.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'
'''

from ipaddress import IPv4Address

address = input("Введите IP адрес в десятично-точечном формате: ")
try:
    ipv4_addr = IPv4Address(address)
except ValueError:
    print('Incorrect IPv4 address')
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

