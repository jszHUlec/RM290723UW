def utworz_i_zainicjalizuj_plik():
    moj_plik = open("brak.txt", "a")
    moj_plik.write("\nKolejna linijka")
    moj_plik.write("\nKolejna linijka")
    moj_plik.write("\nKolejna linijka")
    moj_plik.close()


try:
    moj_plik = open("brak.txt","r")
    print("program glowny:")
    print(moj_plik.read())

except FileNotFoundError as e:
    print("Nie ma takiego pliku.",e)
    utworz_i_zainicjalizuj_plik()

    moj_plik = open("brak.txt", "r")  # plik czytany od poczatku
    print(moj_plik.read())




