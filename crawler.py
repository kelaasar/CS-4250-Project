# Custom files
import mongo
import parser

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError
from urllib.error import URLError

class WebCrawler:
    def __init__(self, seed_url, depth):
        self.frontier = [seed_url]
        self.depth = 0
        self.visited = []
        
    # Retrieve HTML content from a given url
    @staticmethod
    def retrieveURL(url):
        try:
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            html = str(bs)
            html = "<!--" + url + "-->\n" + html
            return html
        except HTTPError as e:
            print("HTTPError: " + e)
        except URLError as e:
            print("URLError: " + e)
        else:
            return None
            
    # Determines if the current page matches the faculty website HTML format
    def target_page(self, html):
        try:
            bs = BeautifulSoup(html, 'html.parser')
            bs.find('div', attr={'class': 'fac-info'})
        except:
            self.depth += 1
            if self.depth >= 10:
                self.frontier = self.seed_url
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

            if url in self.visited:
                continue
            else:
                self.visited.append(url)
                
            html = self.retrieveURL(url)
            mongo.store_page(url, html)
            
            if self.target_page(html):
                targets_found = targets_found + 1
                
            if targets_found == num_targets:
                self.clear_frontier()
                return
            else:
                for url in parser.parse(html):
                    if url not in self.visited:
                        self.frontier.append(url)