
# Napisz program, ktora pobiera od uzytkownika login i haslo
# przekazuje te dane do funkcji uwierzytelniajacej
# funkcja sprawdza, czy taki uzytkownika istnieje w bazie danych
# jesli istnieje, to zwracamy wartosc True
# jesli nieistnije to zwaracamy wartosc False


# Napisz program, ktora pobiera od uzytkownika login i haslo
# przekazuje te dane do funkcji uwierzytelniajacej
# funkcja sprawdza, czy taki uzytkownika istnieje w bazie danych
# jesli istnieje, to zwracamy wartosc True
# jesli nieistnije to zwaracamy wartosc False

data_base = {
    'admin':'admin',
    'kali':'kali',
    'john':'123456',
    'max':'password'
}

def auth(user, pw, db):
    for i in db:
        if i == user:
            if db[user] == pw:
                return True
            else:
                return False



counter = 0
while counter < 3:
    user_name=input('Enter your username: ')
    password=input('Enter your password: ')
    # print('Authentication is successful' if auth(user_name, password, data_base) == True else 'Authentication failed')
    if auth(user_name, password, data_base) == True:
        print("Authentication is successful")
        break
    else:
        print("Authentication failed")
    counter += 1
else:
    print('Authentication failed 3 times. Try later')

