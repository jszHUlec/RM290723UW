# from WlasnyException import BledyWyborUzytkownikError
# w pliku WlasnyExcepiton.py mozna dodac ponizsze dwie linijki

class BledyWyborUzytkownikError(Exception):
    pass

num1 = 10
num2 = 0

try:

    x = input("podaj liczbe")
    print(num1/num2) #blad dzielenia przez zero
    raise BledyWyborUzytkownikError #wlasny blad w aplikacji

except BledyWyborUzytkownikError as e: # blad szczegolny w aplikacji
    print("moj wlasny blad w aplikacji",e)
except Exception as e: # blad ogolny w palikacji
    print("blad ogolny w aplikacji",e)
else: #dziala tylko gdy nie ma bledu w aplikacji
    print("jestem w else")
finally: #zawsze uruchamia. Obojetne czy byl blad czy nie
    print("jestem w finaly")

