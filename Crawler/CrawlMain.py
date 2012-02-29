#!/usr/bin/env python

import Pyro4
import os
from CrawlDirector import Director
from DistCrawler import Crawler
from LinkMapper import LinkMapper
from LinkReducer import LinkReducer
from SaveData import SaveData


def main(url_list, site_number):
    current_dir = os.getcwd()
    site_key = site_number
    site_hash = {}
    director = Director()
    director.add_new(url_list)
    batch_urls = director.new_urls()
    crawler = Crawler()
    for url in batch_urls:
        savedata = SaveData(site_key)
        site_hash[url] = site_key
        content, links = crawler.crawl(url)
        savedata.write_content(content)
        savedate.save_links(links)
        site_key += 1
    director.update_record()


if __name__ == '__main__':
    start_urls = ['http://www.hackerschool.com']
    main(start_urls)
