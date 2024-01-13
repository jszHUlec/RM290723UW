# napisz program, ktory ma 3 funkcje
# pierwsza funkcja zapisuje dane wprowadzone przez uzytkownika do zmiennej globalnej
#   w formacie dzien.miesiac.rok::godzina:minuta
# druga funkcja wyswietla zawartosc zmiennej globalnej
# wyswietla menu i posiada obsluge wyboru menu przez uzytkownika
# 1. wprowadz wartosc, 2. wyswielt zmienna db, 3. quit

import datetime

db = []

def wprowadzLog():
    global db
    now = datetime.datetime.now()
    log = input("podaj log/text: ")
    db.append(f"{now.year}.{now.month}.{now.day}::{now.hour}:{now.minute} - {log}")


def wysweitlLog():
    global db
    print("##### poczatek logu #####")
    for wiersz in db:
        print(wiersz)
    print("##### koniec logu #####")

def menu():
    print("1. Wprowadz log")
    print("2. Wyswietl logi")
    print("3. quit")
    wybor = input("podaj wybor:")
    return wybor


def Main():
    while True:
        wybor = menu()
        if wybor == "1":
            wprowadzLog()
        elif wybor == "2":
            wysweitlLog()
        elif wybor == "3":
            print("bye bye")
            return
        else:
            "zly wybor!"

if __name__ == "__main__":
    Main()

