from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Downloads these packages 
# nltk.download('punkt')
# nltk.download('stopwords')

documents = [
    "I love cats and cats",
    "She loves her dog",
    "They love their dogs and cat"
]

stemmer = PorterStemmer()

# Tokenizer including stemming and stop word removal
def tokenizer(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]  # Remove punctuation
    tokens = [word.lower() for word in tokens if word.lower() not in stopwords.words('english')]  # Remove stopwords
    tokens = [stemmer.stem(word) for word in tokens]  # Apply stemming
    return tokens

# TF-IDF Vectorizer with tokenizer
vectorizer = TfidfVectorizer(tokenizer=tokenizer)
tfidf_matrix = vectorizer.fit_transform(documents)

# Query
query = "dogs"

# Vectorize the query using the same vectorizer
query_vector = vectorizer.transform([query])

# Compute cosine similarity between the query and all documents
similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

# Rank the documents by similarity score
ranked_documents = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)

# Display the ranking
print(f"Ranking for query '{query}':")
for doc_idx, score in ranked_documents:
    print(f"Document {doc_idx + 1}: Score {score:.4f}")