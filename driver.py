from crawler import WebCrawler
import mongodb
import parser
import indexer

mongodb.init()

# Obtains crawler obj
crawler = WebCrawler(max_depth = 10)
seed = "https://www.cpp.edu/faculty/ysalem/"
target_links = crawler.crawlerThread(seed, num_targets=2) # unordered target links

#"https://www.cpp.edu/engineering/ce/index.shtml"
#"https://www.cpp.edu/engineering/ce/faculty.shtml"
#"https://www.cpp.edu/faculty/ysalem/"


# ░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
# ░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
# ░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
# ░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
# ░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
# █▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
# █▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
# ░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
# ░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
# ░░░█░░██░░▀█▄▄▄█▄▄█▄████░2
# ░░░░█░░░▀▀▄░█░░░█░███████░█
# ░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
# ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
# ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
# ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░
