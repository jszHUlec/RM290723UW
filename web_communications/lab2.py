import requests
# req = requests.get(f"http://hack-yourself-first.com/")

with open("slownik.txt","r") as slownik:
    for x in slownik:
        print(x)
        req = requests.get(f"http://hack-yourself-first.com/{x.strip()}")
        if req.status_code == 200:
            print(req.status_code)
            print(req.text)
