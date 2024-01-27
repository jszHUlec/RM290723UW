import socket

target = input("podaj adres komputera:")

for port in range(20,200):
    try:
        sock = socket.socket()

        sock.connect((target, port))
        sock.send("who are you ?".encode())
        socket.setdefaulttimeout(4)
        ret = sock.recv(2048).decode()
        print(port, ret)

    except Exception as e:
        continue
    finally:
        sock.close()


# target = input('Enter PC address: ')
# while True:
#     sock=socket.socket()
#     port = int(input("Enter port: "))
#     # if "exit" in port:
#     #     break
#     sock.connect((target, port))
#     sock.send('whoare you?'.encode())
#     ret = sock.recv(2048).decode()
#     print(ret)
#     sock.close()