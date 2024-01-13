# napisz program, ktory:
# pobiera od uzytkownika 'marke' pojazdu i dodaje ja do listy
# program prosi o wprowadzenie 4 pojazdow
# po wprowadzeniu pojazdow, uzytkownik jest pytany
# czy wyswietlic liste wprowadzonych pojazdow
# jesli odpowie 'yes' (lub tak) to wyswietlamy utworzona liste

car_brands=[]
print('Enter car brands')
for i in range(4):
    car_brand = input()
    car_brands.append(car_brand)
answer = input('Do you want to see your answers? Enter Y or N ')
print("***",answer.upper(),"***") #.upper() zamienia tekst, na duze znaki
if answer.upper() == "Y":
    for i in car_brands:
       print (i)
else:
    print('Ok')