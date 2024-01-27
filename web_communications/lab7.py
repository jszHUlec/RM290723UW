import requests

response = requests.get("https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania", verify=False)

print(response.text)