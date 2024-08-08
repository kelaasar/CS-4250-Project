from crawler import WebCrawler
import mongo_manager as mongo

mongo.init()
crawler = WebCrawler("https://www.cpp.edu/sci/biological-sciences/index.shtml")