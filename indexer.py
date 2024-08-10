import re
import mongo
import nltk
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

    # {'dog': {
    #          'occurrence': 5,
    #          'tfidf': 235465,
    #          'weight': 32543,
    #          }}

# Record the number of times a word appears in the document
def index(url, content):
    stop_words = set(stopwords.words('englsh'))
    lemmatizer = WordNetLemmatizer()
    vectorizer = CountVectorizer()
    tokenizer = vectorizer.build_tokenizer()

    tokens = word_tokenize(content)

    stopped = [word.lower() for word in tokens if word.lower() not in stop_words]
    lemmatized = [lemmatizer.lemmatize(word) for word in stopped]
    filtered = [word for word in lemmatized if re.compile(r'^[\w-]+$').match(word)]

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

def weight(content):

def rank():
    # Ranks Docs based on Query
    query = input("Input search query: ")
    query_vector = vectorizer.transform([vector])

    similarity_scores = cosine_similarity(query_vector, vector).flatten()
    ranked_docs = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)