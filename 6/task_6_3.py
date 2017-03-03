'''
Задание 6.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
- считывались строки, в которых указаны MAC-адреса
- каждая строка, где есть MAC-адрес, должна обрабатываться таким образом,
  чтобы на стандартный поток вывода была выведена таблица вида:

 100    aabb.cc80.7000     Gi0/1
 200    aabb.cc80.7000     Gi0/2
 300    aabb.cc80.7000     Gi0/3
 100    aabb.cc80.7000     Gi0/4
 500    aabb.cc80.7000     Gi0/5
 200    aabb.cc80.7000     Gi0/6
 300    aabb.cc80.7000     Gi0/7
'''

try:
    with open('CAM_table.txt') as f:
        for line in f:
            splited = line.split()
            if len(splited) == 4:
                if len(splited[1]) == 14:
                    print('{:7}{:19}{}'.format(splited[0], splited[1], splited[3]))
except FileNotFoundError:
    print('Файл не найден')
