from sklearn.feature_extraction.text import CountVectorizer

text = ["Build search engines"]
vectorizer = CountVectorizer(analyzer='char_wb', ngram_range = (5, 5))
vectorizer.fit(text)
print(vectorizer.vocabulary_)
vector = vectorizer.transform(text)
print(vector.shape)
print(vector.toarray())





