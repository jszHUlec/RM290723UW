import requests
import re
from bs4 import BeautifulSoup
def pobierz_pliki(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Znajdź wszystkie linki do plików PDF
    linki = soup.find_all("a", attrs={"href": re.compile(".*pdf")})

    # Pobierz każdy plik PDF
    for link in linki:
        url = link["href"]
        nazwa_pliku = url.split("/")[-1]

        # Pobierz plik
        response = requests.get(url)
        with open("/tmp/" + nazwa_pliku, "wb") as f:
            f.write(response.content)

if __name__ == "__main__":
    url = "https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania/"
    pobierz_pliki(url)