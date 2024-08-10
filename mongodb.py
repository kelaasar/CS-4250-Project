import pymongo

_client = None
_db = None

def init():
    global _client, _db
    
    if not _client:
        _client = pymongo.MongoClient()
        _db = _client["CS4250-WebCrawler"]
    return _db
    
def store_doc(collection, doc):
    global _db

    _db[collection].insert_one(doc)
   
    return
    
def retrieve_docs(collection):
    global _db
    
    return _db[collection].find()