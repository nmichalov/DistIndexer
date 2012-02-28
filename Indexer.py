#!/usr/bin/env python

import Pyro4
from CrawlDirector import Director
from DistCrawler import Crawler
from LinkMapper import LinkMapper
from LinkReducer import LinkReducer
from gensim import corpora, models, utils

class Indexer:

    def __init__(self):
        self.director = Director()
        self.crawler = Crawler()
        self.LinkMapper = LinkMapper()
        self.LinkReducer = LinkReducer()


    def index(self, url_list):
        self.director.add_new(url_list)
        batch_urls = director.new_urls
        self.director.update_record()
        for url in batch_urls:
            links, content = self.crawler.crawl(url)
            self.LinkMapper.proc_links(links)
            self.#content processing here
        batch_referrers = self.LinkMapper.referrers()
        refererrs_reduced = self.LinkReducer.proc_links(batch_referrers)
        found_links = self.LinkReducer.unique_urls()
        #self.index(found_links)

if __name__ == '__main__':
    start_urls = ['http://www.hackerschool.com']
    indexer = Indexer()
    indexer.index(start_urls)

