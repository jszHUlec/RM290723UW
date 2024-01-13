# napisz program, ktory pobiera od uzytkownika tekst do momentu wpisania 'exit'
# pobrany tekst przekaz do funkcji
# funkcja powinna policzyc dlugosc tekstu
# dlugosc tekstu powinna byc dodana do globalnego licznika

counter = 0

def policz(txt):
    global counter
    counter = counter + len(txt)

def Main():
    while True:
        tekst = input("Podaj tekst:")
        if tekst.lower() == "exit":
            break
        else:
            policz(tekst)

    print("licznik =",counter)
    print("koniec programu")

if __name__ == "__main__":
    Main()