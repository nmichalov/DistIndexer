#!/usr/bin/env python

import sys
import Pyro4
import os
from DistCrawler import Crawler
from SaveData import SaveData

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

    def update_record(self):
        self.visited_urls.append(self.target_urls)
        self.target_urls = []

def main(start_url):
    director = Director()
    daemon = Pyro4.Daemon()
    daemon.register(director)
    crawler = Pyro4.Proxy('PYRONAME:indexer.crawler')
    director.add_new(start_url)
    current_batch = director.new_urls()
    crawler = Crawler()
    for link in current_batch:
        savedata = SaveData(0)
        links, content = crawler.crawl(link)
        savedata.save_content(content)
        savedata.save_links(links)

if __name__ == "__main__":
    target_url = raw_input('Enter a URL to crawl: ')
    url = [target_url]
    main(url)
