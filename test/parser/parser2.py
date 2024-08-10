from bs4 import BeautifulSoup

bs = BeautifulSoup("<HTML><body><h1>Trash</h1><h1>Title</h1></body><HTML>", 'html.parser')
print(bs.find_all('h1')[0].get_text())

