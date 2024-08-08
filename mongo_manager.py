import pymongo

client = None
db = None
collection = None

def init():
    client = pymongo.MongoClient()
    db = client["CS4250-WebCrawler"]
    collection = db["Faculties"]
    
def store_page(url, html):
    entry = {"url": url, "html": html}
    collection.insert_one(entry)