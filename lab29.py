# przygotuj program, ktory
# wygeneruje pseudolosowy numer (1-100)
# i bedzie pytal uzytkownika o podanie liczby
# jezeli podana liczba pasuje do wylosowanej to wygrales
# jezeli oddalona jest o mniej niz 10 to goraco
# Jezeli oddalona jest o mniej niz 20 to ciplo
# jezeli oddalona jest o mniej niz 30 to zimno
# jezeli inaczej to lodowato
import random

wylosowana_liczba = 0
def generuj_liczbe():
    global wylosowana_liczba
    wylosowana_liczba = random.randint(1,100)

def sprawdz(wybor_uzytkownika):
    odleglosc = abs(wybor_uzytkownika - wylosowana_liczba)
    if wybor_uzytkownika == wylosowana_liczba:
        print("Gratulacje wygrales!!!")
        return True
    elif odleglosc <= 10:
        print("Goraco")
    elif odleglosc <= 20:
        print("Cieplo")
    elif odleglosc <= 30:
        print("Zimno")
    else:
        print("Lodowato")

    return False

def Main():

    print("Witaj w programi zimno/cieplo")

    wybor = ""
    while True:
        wybor = input("1.Gram\n2.Wyjscie\n==>")
        if wybor == "1":
            print("gram dalej")
            generuj_liczbe()

            # z = sprawdz(int(input("podaj twoj typ: ")))
            # while z is False : # False is False => True
            #     z = sprawdz(int(input("podaj twoj typ: ")))
            #     continue
            while sprawdz(int(input("podaj twoj typ: ")))  is False : # False is False => True
                continue

        elif wybor == "2":
            print("wychodze")
            break

    print("Koniec programu. Dzieki za gre!")

if __name__ == "__main__":
    Main()

