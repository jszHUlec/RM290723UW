#funkcje.py
def ADDish(tekst):
    new_text = tekst+"ish"
    print(new_text.upper())
    # print(tekst, "ish", sep='')

def addTwoParameters(x, y):
    newx = 2 * float(x)
    newy = 2 * float(y)
    result = newx + newy
    print(result)

def Main():
    print("jakies tesyty dla funckji addTwoParameters")


print("jestem w pliku funckje.py. Zmienna __name__ ma wartosc",__name__)
print("jestem w pliku funckje.py. Zmienna __name__ ma wartosc",__name__)
print("jestem w pliku funckje.py. Zmienna __name__ ma wartosc",__name__)
print("jestem w pliku funckje.py. Zmienna __name__ ma wartosc",__name__)
print("jestem w pliku funckje.py. Zmienna __name__ ma wartosc",__name__)

if __name__ == "__main__":
    Main()