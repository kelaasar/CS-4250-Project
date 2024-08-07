# Arze: im keeping the prof's method names as it is for now

# Custom files
import mongo_manager
import parser

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

class WebCrawler:
    
    def __init__(self, seed_url):
        self.frontier = [seed_url]
        self.visited_url = []
        
    # Retrieve HTML content from a given url    
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
    def target_page(html):
    
    def clear_frontier():
        frontier = []
        return
        
    def crawlerThread(frontier, num_targets):
        targets_found = 0
            while frontier:
                url = frontier.pop()
                
                if url in visited_url:
                    continue
                else:
                    visited_url.append(url)
                    
                html = retrieveURL(url)
                storePage(url, html)
                
                if target_page(html):
                    targets_found = targets_found + 1
                if targets_found == num_targets:
                    clear_frontier()
                else:
                    for each not visited url in parse(html):
                        frontier.addURL(url)