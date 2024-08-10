import mongo
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

# Filters given HTML content,
# then store the raw text data of target pages in MongoDB
def parse(html):
    bs = BeautifulSoup(html, 'html.parser')
    html = str(bs)
    match = re.compile(r'<!--(.*)-->').search(html)   
    base = match.group(1).strip()

    links = []
    link_pattern = '^https://.*$|^http://.*$' 

    for a in bs.find_all('a', href=True):
        link = a['href']
        if re.match(link_pattern, link):
            links.append(link)
        else:
            new_link = urljoin(base, link)
            try:
                urlopen(new_link)
                links.append(new_link)
            except:
                continue

    try:
        bs.find('div', attr={'class': 'fac-info'})
    except:
        return links

    content = bs.find('div', attrs={'class', 'fac-staff'}).get_text()
    content += bs.find('div', attrs={'class', 'accolades'}).get_text()
    doc = {'content': content}
    mongo.store_target_page(doc) 

    return links

