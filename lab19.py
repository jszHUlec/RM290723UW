# napisz funkcje, ktora przyjmuje od uzytkwonika pewien tekst (w petli)
# dodaj do tego tekstu 'ish'
# wyseitl tekst
# jesli wpiszemy 'exit' to konczymy program

# realizacja funckja z parametrami

#wersja v1
def rename(a):
    print(a+'ish')

name=input('Enter any word ')
rename(name)


#wersja v2
def ADDish(tekst):
    new_text = tekst+"ish"
    print(new_text.upper())
    # print(tekst, "ish", sep='')

print('Wpisuj teksty, jak napiszesz \'exit\' to zakończysz działąnie programu')
while True:
    x = input()
    if x == "exit":
        break
    ADDish(x)
