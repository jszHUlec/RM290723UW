import os

plik = "ipconfig.txt"

os.system(f"ifconfig > {plik}")
    # wersja z plikiem
with open(plik,"r") as my_file:
    for wiersz in my_file:
        if "inet " in wiersz:
            print(wiersz.strip()) # "         asdf " trim()


#wersja bez pliku:
for wiersz in os.popen('ifconfig').readlines():
    if "inet " in wiersz:
        print(wiersz.strip())