from crawler import WebCrawler
import parser
import mongo
import indexer

mongo.init()

# Obtains crawler obj
crawler = WebCrawler()
target_links = crawler.crawlerThread("https://www.cpp.edu/engineering/ce/index.shtml", 10) # unordered target links




# ░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
# ░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
# ░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
# ░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
# ░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
# █▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
# █▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
# ░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
# ░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
# ░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
# ░░░░█░░░▀▀▄░█░░░█░███████░█
# ░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
# ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
# ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
# ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░
