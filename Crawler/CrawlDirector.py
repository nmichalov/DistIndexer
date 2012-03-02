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

    def add_new(self):
        url_file = open('URLlist', 'r')
        for line in url_file:
            line = line.strip()
            if line not in self.visited_urls:
                self.target_urls.append(line)
        
    def new_urls(self):
        return self.target_urls

    def update_record(self):
        self.visited_urls.append(self.target_urls)
        self.target_urls = []

def main():
    site_index = 0
    director = Director()
    daemon = Pyro4.Daemon()
    daemon.register(director)
    crawler = Pyro4.Proxy('PYRONAME:indexer.crawler')
    director.add_new()
    current_batch = director.new_urls()
    crawler = Crawler()
    for link in current_batch:
        savedata = SaveData(site_index)
        content, links = crawler.crawl(link)
        savedata.save_content(content)
        savedata.save_links(links)
        site_index += 1

if __name__ == "__main__":
        main()
