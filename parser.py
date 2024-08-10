import mongo
import re
import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def index(base, content):
    stop_words = set(stopwords.words('englsh'))
    lemmatizer = WordNetLemmatizer()
    vectorizer = CountVectorizer()
    tokenizer = vectorizer.build_tokenizer()

    tokens = word_tokenize(content)

    stopped = [word.lower() for word in tokens if word.lower() not in stop_words]
    lemmatized = [lemmatizer.lemmatize(word) for word in stopped]
    filtered = [word for word in lemmatized if word.isalpha()]

    content = [' '.join(filtered)]

    vector = vectorizer.fit_transform(content)

    tokens = vectorizer.get_feature_names_out()
    occurrences = vector.toarray()[0]
    size = len(tokens)
    indices = {}

    indices['URL'] = base

    for i in range(size):
        indices[tokens[i]] = occurrences[i]

    mongo.store_indices(indices)
    
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

    index(content)

    # do vector here
    
    

    return links

