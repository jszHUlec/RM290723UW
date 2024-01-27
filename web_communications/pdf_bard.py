import requests
from bs4 import BeautifulSoup

def pobierz_plik_pdf(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, "html.parser")

    # Znajdź element <a> z atrybutem href wskazujący na plik PDF
    link = soup.find("a", attrs={"href": True})

    # Pobierz link do pliku PDF
    pdf_url = link["href"]

    # Pobierz plik PDF
    response = requests.get(pdf_url)

    # Zapisz plik PDF
    with open("plik.pdf", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    url = "https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania/Prawda_i_mity_na_temat_grypy.pdf"
    pobierz_plik_pdf(url)