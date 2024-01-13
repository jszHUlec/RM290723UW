# Napisz program, ktory uzupelnia 'slownik'
# zapytaj uzytkownika ile produktow chce dodac
# do slownika dodawaj produkty wraz z cena
# na koncu wyswietl podsumowanie slownika
# oraz wartosc zgromadoznych produktow

def main():
    slownik_produktow = {}

    ilosc_produktow = int(input("Ile produktów chcesz dodać do słownika? "))

    for _ in range(ilosc_produktow):
        produkt = input("Podaj nazwę produktu: ")
        cena = float(input(f"Podaj cenę produktu {produkt}: "))
        slownik_produktow[produkt] = cena

    print("\nPodsumowanie słownika:")
    for produkt, cena in slownik_produktow.items():
        print(f"{produkt}: {cena} zł")

    suma_wartosci = sum(slownik_produktow.values())
    print(f"\nWartość zgromadzonych produktów: {suma_wartosci} Zl")

if __name__ == "__main__":
    main()




