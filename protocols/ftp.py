import ftplib

try:
    target = input("podaj IP")
    server = ftplib.FTP()
    server.connect(target, 21, timeout=2)
    username = input("podaj login")
    password = input("podaj haslo")
    server.login(username, password)

    server.dir()
except Exception as e:
    print(e)