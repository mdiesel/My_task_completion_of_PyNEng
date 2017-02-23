'''
Задание 3_7

    Преобразовать MAC-адрес в двоичную строку (без двоеточий).

    MAC = "AAAA:BBBB:CCCC"
'''

MAC = "AAAA:BBBB:CCCC"
MAC_BIN = bin(int(MAC.replace(':', ''), 16))[2:]
print(MAC_BIN)
