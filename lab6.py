# pobierz od uzytkownika dwie wartosci
# przekonwertuj jes do liczb
# wyswietl wieksza wartosc

var_1 = int(input("Podaj pierwsza liczbe:"))
var_2 = int(input("Podaj druga liczbe:"))

if var_1 > var_2:
    print(var_1, "jest wieksze")
elif var_1 == var_2:
    print("obie wartosci sa rowne")
else:
    print(var_2, "jest wieksze")