'''
Решение задачи 8.1
'''
from sys import argv
from my_func import generate_access_config, generate_trunk_config, get_int_vlan_map

if len(argv) != 2:
    print('Неверное число аргументов. Укажите в качестве аргумента конфигурационный файл.')
    exit()

d_access, d_trunk = get_int_vlan_map(argv[1])
access_config = [x + '\n' for x in generate_access_config(d_access)]
trunk_config = [x + '\n' for x in generate_trunk_config(d_trunk)]

with open('result.txt', 'w') as f:
    f.writelines(access_config)
    f.writelines(trunk_config)

print('Файл result.txt сформирован.')
