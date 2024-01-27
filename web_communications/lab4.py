import requests

url2="http://hack-yourself-first.com/Account/Login"
payload = {"Email":"asdasda@gmail.com","Password":"123456"}
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

r = requests.post(url2, data=payload, headers=headers)
print(r.status_code)

