import os
# with open("log.txt") as plik_logu:
rezult = os.popen("sudo dmesg | tail ")
for wiersz in rezult:
    nowy_wiersz = wiersz.split()
    # if nowy_wiersz[2].lower() == "error":
    print(nowy_wiersz[2],nowy_wiersz[0], nowy_wiersz[3:])

