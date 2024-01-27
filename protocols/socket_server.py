import socket

while True:
    try:
        my_socket = socket.socket()
        my_socket.bind(("0.0.0.0",1342))
        my_socket.listen(1)

        conn, addr = my_socket.accept()

        while True:
            data = conn.recv(2048).decode()
            if data == "exit":
                break
            else:
                print(data)

            odpowiedz = input("Podaj odpoweidz: ")
            conn.send(odpowiedz.encode())
    finally:
        my_socket.close()