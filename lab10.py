

hello = "Jakub Szepielak"
lista = hello.split()

print(f"imie: {lista[0]}, nazwisko: {lista[1]}, moje inicjaly to:")
print(lista[0][0]+"."+lista[1][0]+".")


hello = "Oksana Marusiak"
print(f"imie: {hello.split()[0]}, nazwisko: {hello.split()[1]}, moje inicjaly to:")
print(hello.split(" ")[0][0], hello.split(" ")[1][0], sep='.', end='.')

