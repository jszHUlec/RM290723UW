# pobierz od uzytkownika tekst # input()
# przekonwertuj wprowadzony tekst na liczbe # int()
#
# sprawdz czy wartosc wprowadzona przez uzytkownika jest wieksza niz 18
#   jeze tak, to wyswietl komunikat "Hura, jestes dorosly"
#   jezeli nie, to wyswietl komunikat "Jeste za mlody"

wiek = int(input("Podaj swoj wiek"))

if wiek >= 18:
    print("Gratulacje mozesz leganie kupic alkohol")
else:
    print("Przykro mi, musisz poczekac jeszcze:", 18-wiek ,"lat")


