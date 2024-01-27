import requests
from bs4 import BeautifulSoup

req = requests.get("http://hack-yourself-first.com/")

html_page = BeautifulSoup(req.text, 'html.parser')

for line in html_page.find_all('a'):
    print( line.get('href') )
