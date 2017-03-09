'''
Задание 7.4a

Задача такая же, как и задании 7.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Теперь, если уровня 3, то самый вложенный должен быть списком, а остальные - словарями.

На примере interface Ethernet0/3.100
{'interface Ethernet0/3.100':{
                    'encapsulation dot1Q 100':[],
                    'xconnect 10.2.2.2 12100 encapsulation mpls':
                        ['backup peer 10.4.4.4 14100',
                         'backup delay 1 1']}}


'''

ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    """
    ignore_command = False

    for word in ignore:
        if word in command:
            ignore_command = True
    return ignore_command


def config_to_dict(config):
    """
    config - имя конфигурационного файла
    """
    depth = 1
    temp_data = []
    temp_key = None
    temp_key_2 = None

    result = {}
    try:
        with open(config, 'r') as f:
            for line in f:
                if not (line.strip().startswith('!') or check_ignore(line, ignore) or line.strip() == ''):
                    if not line.startswith(' '):
                        result[line.strip()] = []
                        if depth == 2:
                            depth = 1
                            for i in temp_data:
                                result[temp_key].append(i.strip())
                        elif depth == 3:
                            depth = 1
                            result[temp_key] = {}
                            for i in temp_data:
                                if len(i) - len(i.lstrip()) == 1:
                                    temp_key_2 = i.strip()
                                    result[temp_key][temp_key_2] = []
                                else:
                                    result[temp_key][temp_key_2].append(i.strip())

                        temp_key = line.strip()
                        temp_key_2 = []
                        temp_data = []
                    else:
                        depth = max(depth, len(line)-len(line.lstrip()) + 1)
                        temp_data.append(line)
    except OSError:
        print('Файл конфигурации не найден')
    return result

#a = config_to_dict('config_r1.txt')
print(config_to_dict('config_r1.txt'))

for key, value in config_to_dict('config_r1.txt').items():
    print('{} {}'.format(key, value))
