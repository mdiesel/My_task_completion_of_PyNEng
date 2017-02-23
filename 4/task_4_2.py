"""
Задание 4.2

В этой задаче нельзя использовать условие if и нельзя изменять словарь london_co.

В задании создан словарь, с информацией и разных устройствах.

Вам нужно запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве на стандартный поток вывода
(информация будет в виде словаря).


Пример выполнения скрипта (у вас в выводе все элементы словаря будут в одну строку):
$ python task_4_2.py
Enter device name: r1
{'ios': '15.4', 'model': '4451', 'vendor': 'Cisco',
'location': '21 New Globe Walk', 'ip': '10.255.0.1'}

"""

london_co = {
    'r1' : {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
        },
    'r2' : {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
        },
    'sw1' : {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
        }
}

ask_device = input("Введите имя устройства: ")
try:
    print(london_co[ask_device])
except KeyError:
    print("Устройство не найдено")
