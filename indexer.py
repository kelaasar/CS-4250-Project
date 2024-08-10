import mongodb

import re
import nltk
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Format of the "Indices" collection
# {'dog': {
#          'occurrence': 5,
#          'tfidf': 235465,
#          'weight': 32543,
#          }}

def rank():
    # Ranks Docs based on Query
    query = input("Input search query: ")
    query_vector = vectorizer.transform([vector])

    similarity_scores = cosine_similarity(query_vector, vector).flatten()
    ranked_docs = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)
    
# Returns the number of times a word appears in the document
def get_indices(content):
    vectorizer = CountVectorizer()
    vector = vectorizer.fit_transform(content)
    
    return (vector.toarray(), vectorizer.get_feature_names_out())

# Calculates tf-idf,  
def get_weights(content):
    vectorizer = TfidfVectorizer()
    vector = vectorizer.fit_transform(content)
    
    return (vector.toarray(), vectorizer.get_feature_names_out())
        
def index():
    docs = mongodb.retrieve_docs("Faculties")

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    raw_contents = [doc['content'] for doc in docs]
    urls = [doc['url'] for doc in docs]
    contents = []
    contents_tokens = []
    for content in raw_contents:
        tokens = word_tokenize(content)
        stopped = [word.lower() for word in tokens if word.lower() not in stop_words]
        lemmatized = [lemmatizer.lemmatize(word) for word in stopped]
        filtered = [word for word in lemmatized if re.compile(r'^[\w-]+$').match(word)]
        contents_tokens.append(filtered)
        content = ' '.join(filtered)
        contents.append(content)
        
    indices = get_indices(contents)
    tfidf = get_weights(contents)
    
    all_tokens = tfidf[1]
    
    indices = indices[0]
    tfidf = tfidf[0]
    
    entry_doc = {}
    for tokens in contents_tokens:
        entry = {}
        for token in tokens:
            i = all_tokens.index(token)
            entry[token] = {"occurrences": indices[i], "tf-idf": tfidf[i]}
        entry_doc[urls.pop(0)] = entry
        
    mongodb.store_doc("Indices", entry_doc)