

import urllib3

http = urllib3.PoolManager() # polaczenie internetwo

r = http.request("GET","http://hack-yourself-first.com/")
print("status: ", r.status)

with open("index.html","w") as plik:
    plik.write(r.data.decode('UTF-8'))

