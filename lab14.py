        # 0         1      2          3
colors = ["RED", "BLUE", "YELLOW", "PURPLE"]

print("pierwsza petla")
for x in colors[1:4]:
    print(x)

print("druga petla:")
for x in colors[0:-2]:
    print(x)

print("trzecia petla:")
for x in colors[1:]:
    print(x)

print("pelna lista:")
for x in colors:
    print(x)