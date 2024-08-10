from crawler import WebCrawler

import mongo

mongo.init()

# Obtains crawler obj
crawler = WebCrawler("https://www.cpp.edu/engineering/ce/index.shtml")
crawler.

done = False

while not done:
    input = input("Enter query: ")
    links = mongo.query(input)

    print("Relevant links:\n")
    for link in links:
        print(link)

