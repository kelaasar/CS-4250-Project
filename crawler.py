import re
import mongo_manager
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

class WebCrawler:
    
    def __init__(self, seed_URL):
        self.frontier = [seed_URL]
        self.visited_URL = []
        
    def retrieveURL(url):
        try:
            html = urlopen(url)
            return html
        except HTTPError as e:
            print("HTTPError: " + e)
        except URLError as e:
            print("URLError: " + e)
        else:
            return None
            
    def crawlerThread(frontier, num_targets):
        targets_found = 0
            while frontier:
                url = frontier.pop()
                html = retrieveURL(url)
                storePage(url, html)
                if target_page (html):
                    targets_found = targets_found + 1
                if targets_found == num_targets:
                    clear_frontier()
                else:
                    for each not visited url in parse (html):
                        frontier.addURL(url)