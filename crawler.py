# Arze: im keeping the prof's method names as it is for now

# Custom files
import mongo_manager as mongo
import parser

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

class WebCrawler:
    
    def __init__(self, seed_url):
        self.frontier = [seed_url]
        self.visited = []
        
    # Retrieve HTML content from a given url
    @staticmethod
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
            
    # Determines if the current page matches the faculty website HTML format
    @staticmethod
    def target_page(html):
        try:
            bs.find('div', attr={'class': 'fac-info'})
        except:
            return False
        return True
        
    # Clear the list of new unvisited links
    def clear_frontier(self):
        self.frontier = []
        return
        
    def crawlerThread(self, frontier, num_targets):
        targets_found = 0
            while self.frontier:
                url = self.frontier.pop()
                
                if url in visited:
                    continue
                else:
                    self.visited.append(url)
                    
                html = retrieveURL(url)
                mongo.storePage(url, html)
                
                if self.target_page(html):
                    targets_found = targets_found + 1
                if targets_found == num_targets:
                    self.clear_frontier()
                else:
                    for each not visited url in parser.parse(html):
                        self.frontier.append(url)