'''
Задание 8.1

Создать отдельный файл my_func.py.

Перенести в него функции из заданий:
* 7.1 или 7.1a
* 7.2
* 7.3 или 7.3a

Создать файл main.py:
* По ходу задания импортировать нужные функции из файла my_func.
* Файл main.py должен ожидать как аргумент имя конфигурационного файла коммутатора.

* Имя конфигурационного файла передать как аргумент функции get_int_vlan_map (из задания 7.3-7.3a)
 * На выходе функции, мы должны получить кортеж двух словарей.

* Словари, соответственно, надо передать функциям:
 * generate_access_config (из задания 7.1-7.1a)
 * generate_trunk_config (из задания 7.2)

* Эти функции, в свою очередь, возвращают список со строками готовой конфигурации
которую надо записать в файл result.txt в виде стандартного конфига (то есть, строк)
'''
