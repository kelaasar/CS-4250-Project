import pymongo

client = None
db = None
pages = None
faculties = None
indices = None

def init():
    client = pymongo.MongoClient()
    db = client["CS4250-WebCrawler"]
    pages = db["Pages"]
    faculties = db["Faculties"]
    indices = db["Indices"]
    
def store_page(url, html):
    doc = {"url": url, "html": html}
    pages.insert_one(doc)

def store_target_page(doc):
    pages.insert_one(doc)

def store_indices(doc):
    indices.insert_one(doc)