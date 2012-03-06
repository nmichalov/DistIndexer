#!/usr/bin/env python

import os
import re
from gensim import utils 
from simserver import SessionServer

def page_text():
    for page_file in os.listdir('CrawlData'):
        content = open('CrawlData/'+page_file, 'r')
        page_content = content.read()
        content.close()
        page_url = re.sub('\s', '\/', page_file)
        yield page_url, page_content


if __name__ == '__main__':
    service = SessionServer('/tmp/my_server/')
    corpus = [{'id': '%s' % url, 'tokens': utils.simple_preprocess(text)}
            for url, text in page_text()]
    service.train(corpus, method='lsi')
    service.index(corpus)
