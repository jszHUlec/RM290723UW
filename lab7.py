# Pobierz od uzytkownika dwie wartosci
# przekonwertoj je do wartosci numerycznej
# pobierz od uzytkownika operacje do wykonania: + - / *
# wykonaj operacje na wartosciach pobranych od uzytkownika
# wyswietl wynik

a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
operator = input ("Enter operator: ")

if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    if b == 0:
        print('error! no devision by 0')
    else:
        print(a/b)
else:
    print('error! enter operator +, -, * or /')