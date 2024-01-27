from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://www.google.com/search?q=cats')
links = r.html.links

for l in links:
    if l.startswith("https"):
        print(l)
