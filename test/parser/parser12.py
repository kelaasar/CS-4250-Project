from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

ids = bs.find_all(id='gift1')
print(ids)
for tag in ids:
    print(tag.get_text())
