#!/usr/bin/env python

import sys
import Pyro4
import os
import cPickle
from DistCrawler import Crawler 
from DataReduce import DataReduce

class Director:
    
    def __init__(self):
        self.target_urls = []
        if os.path.exists('Visited.pkl'):
            self.visited_urls = cPickle.load('Visited.pkl')
        else:
            self.visited_urls = []

    def add_new(self, url):
        if url not in self.visited_urls:
            self.target_urls.append(url)
        
    def new_urls(self):
        return self.target_urls

    def update_record(self):
        self.visited_urls.append(self.target_urls)
        visited_list = open('Visited.pkl', 'w')
        cPickle.dump(self.visited_urls, visited_list)
        visited_list.close()

def main():
    urls = []
    url_file = open('URLlist', 'r')
    for line in url_file:
        line = line.strip()
        director.add_new(line)
    target_urls = director.new_urls()
    crawler = Crawler()
    datareduce = DataReduce()
    for link in target_urls:
        data = crawler.crawl(link)
        datareduce.reduce_data(data)
    datareduce.return_urls()

if __name__ == "__main__":
    director = Director()
    daemon = Pyro4.Daemon()
    daemon.register(director)
    crawler = Pyro4.Proxy('PYRONAME:indexer.crawler')
    main()
    director.update_record()
