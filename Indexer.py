#!/usr/bin/env python

import Pyro4
import os
from CrawlDirector import Director
from DistCrawler import Crawler
from LinkMapper import LinkMapper
from LinkReducer import LinkReducer
from ContentProcessor import StoreContent


class Indexer:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.site_key = 0
        self.site_hash = {}
        self.director = Director()

    def get_batch(self, url_list):
        self.director.add_new(url_list)
        batch_urls = self.director.new_urls()
     #needs a list of visited   self.director.update_record()
        return batch_urls

    def crawl_batch(self, batch_urls):
        crawler = Crawler()
        for url in batch_urls:
            storecontent = StoreContent(self.site_key)
            self.site_hash[url] = self.site_key
            content, links = crawler.crawl(url)
        storecontent.write_content(content)
        return links

    def link_map(self, returned_links):
        linkmapper = LinkMapper()
        return linkmapper.map_links(returned_links)
    
    def link_reduce(self, external_urls, referrer_dict):
        linkreducer = LinkReducer()
        next_batch = linkreducer.reduce_externals
        referrer_dict = linkreducer.reduce_externals


if __name__ == '__main__':
    start_urls = ['http://www.hackerschool.com']
    indexer = Indexer()
    batch0 = indexer.get_batch(start_urls)
    page_links = indexer.crawl_batch(batch0)
    externals, refs = indexer.link_map(page_links)
    indexer.link_reduce(externals, refs)
