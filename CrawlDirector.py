#!/usr/bin/env python

import sys
import Pyro4
import os
from DistCrawler import Crawler

class Director:
    
    def __init__(self):
        self.target_urls = []
        self.visited_urls = []

    def add_new(self, url_list):
        for url in url_list:
            if url not in self.visited_urls:
                self.target_urls.append(url)
        
    def new_urls(self):
        return self.target_urls

    def update_record(self, visited_url):
        self.visited_urls.append(self.target_urls)
        self.target_urls = []

def main():
    director = Director()
    daemon = Pyro4.Daemon()
    daemon.register(director)
    crawler = Pyro4.Proxy('PYRONAME:indexer.crawler')
    #open and read a file
    director.add_new()
    current_batch = director.new_urls()
    crawler = Crawler()
    for link in current_batch:
        print crawler.crawl(link)

if __name__ == "__main__":
    main()
