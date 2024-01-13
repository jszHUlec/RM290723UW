
print("2","3",end=' ')
wypisz = False
start = 3
while True:  # można ograniczyć ilość warunkiem wyjścia, np. start < 100
    start+=1
    for x in range(2,start,1):
        wypisz = True # tryb verose
        if not bool(start%x):
            wypisz = False
            break
    if wypisz:
        print(start,end=' ')