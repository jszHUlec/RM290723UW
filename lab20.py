
# pobierz od uzytkownika dwie liczby
# pomnoz kazda liczbe przez 2
# tak pomnozone liczby dodaj do siebie
# i wyswietl na ekranie

def TimesAndAdd(a, b):
    return ((a * 2) + (b * 2))


x = float(input("Podaj x "))
y = float(input("Podaj y "))

rezultat = TimesAndAdd(x, y)
print(rezultat)