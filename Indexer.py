#!/usr/bin/env python

import os
import Pyro4
from CrawlDirector import Director
from DistCrawler import Crawler
from LinkMapper import LinkMapper
from LinkReducer import LinkReducer
from ContentProcessor import StoreContent, ContentPro#, ContentModel

class Indexer:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.site_key = 0
        self.site_hash = {}
        self.director = Director()
        self.crawler = Crawler()
        self.linkmapper = LinkMapper()
        self.linkreducer = LinkReducer()

    def index(self, url_list):
        self.director.add_new(url_list)
        batch_urls = director.new_urls
        self.director.update_record()
        for url in batch_urls:
            self.site_hash[url] = self.site_key
            links, content = self.crawler.crawl(url)
            self.linkmapper.proc_links(links)
            self.contentprocessinghere
        batch_referrers = self.linkmapper.referrers()
        refererrs_reduced = self.linkreducer.proc_links(batch_referrers)
        found_links = self.linkreducer.unique_urls()
        #self.index(found_links)

if __name__ == '__main__':
    start_urls = ['http://www.hackerschool.com']
    indexer = Indexer()
    indexer.index(start_urls)

