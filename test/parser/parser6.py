from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')

bs = BeautifulSoup(html, 'html.parser')

try:
   badContent = bs.nonExistentTag.someTag
except AttributeError as e:
   print('Tag was not found')

badContent = bs.find("nonExistentTag")
if badContent != None:
   print(badContent.someTag)
else:
    print('Tag was not found')


