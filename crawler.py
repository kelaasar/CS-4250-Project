# Custom files
import mongodb
import parser

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError
from urllib.error import URLError

class WebCrawler:
    def __init__(self, max_depth=10):
        self.visited = []
        self.depth = 0
        self.max_depth = max_depth
        
    # Retrieve HTML content from a given url
    @staticmethod
    def _retrieveURL(url):
        try:
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            html = str(bs)
            html = "<!--" + url + "-->\n" + html
            return html
        except HTTPError as e:
            error = "HTTPError: " + str(e) + "\n"
            error_log = open("error_log.txt", "a")
            error_log.write("HTTPError: " + str(e) + "\n")
            error_log.close()
            return "<!--" + url + "-->\n" + error
        except URLError as e:
            error = "URLError: " + str(e) + "\n"
            error_log = open("error_log.txt", "a")
            error_log.write(error)
            error_log.close()
            return "<!--" + url + "-->\n" + error
            
    # Determines if the current page matches the faculty website HTML format
    def _target_page(self, html):
        bs = BeautifulSoup(html, 'html.parser')
        
        if bs.find('div', attr={'class': 'fac-info'}) is None:
            self.depth += 1
            if self.depth >= self.max_depth:
                self.frontier = [self.seed_url]
                
            return False

        return True

    # Clear the list of new unvisited links
    def _clear_frontier(self):
        self.frontier = []
        return
        
    def crawlerThread(self, frontier, num_targets):
        self.seed_url = frontier
        self.frontier = [frontier]

        targets_found = 0
        while self.frontier:
            url = self.frontier.pop(0)

            if url in self.visited:
                continue
            else:
                self.visited.append(url)
                
            html = self._retrieveURL(url)
            doc = {"url": url, "html": html}
            mongodb.store_doc("Pages", doc)
            
            if self._target_page(html):
                targets_found = targets_found + 1
                
            if targets_found >= num_targets:
                self._clear_frontier()
                return
            else:
                for url in parser.parse(html):
                    if url not in self.visited:
                        self.frontier.append(url)