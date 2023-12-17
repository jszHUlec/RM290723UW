type(input("")) # zawsze zwroci text

x = int(float(input("podaj liczbe: ")))
print("rzutowanie float/int",x)

int_x = int(x)
str_x = str(x)
float_x = float(x)
bool_x = bool(int_x)

print(int_x)
print(str_x)
print(float_x)
print(bool_x)

print("float ",float_x," jako wartosc int:",int(float_x))

