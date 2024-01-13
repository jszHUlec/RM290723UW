# napisz program, ktory:
# pobiera od uzytkownika 'marke' pojazdu i dodaje ja do listy
# program prosi o wprowadzenie 4 pojazdow
# po wprowadzeniu pojazdow, uzytkownik jest pytany
# czy wyswietlic liste wprowadzonych pojazdow
# jesli odpowie 'yes' (lub tak) to wyswietlamy utworzona liste

car_brands=[]
print('Enter four car brands. Enter exit if you want to finish')
while True:
    car_brand = input()
    if car_brand.lower() == 'exit':
        break
    car_brands.append(car_brand)
while True:
    answer = input('Do you want to see your answers? Enter Y or N ')
    if answer.upper() == "Y":
        for i in car_brands:
            print(i)
        break
    elif answer.upper() == "N":
        print('bye-bye')
        break
    else:
        print('Error! Enter Y or N')