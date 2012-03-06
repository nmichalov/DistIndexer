#!/usr/bin/env python

import os
import re
from gensim import utils
from simserver import SessionsServer


class SearchServer:

    def __init__(self):
        self.service = SessionServer('SearchServer/')
    

    def generate_index(self):
        def page_text():
            for page_file in os.listdir('CrawlData'):
                content = open('CrawlData/'+page_file, 'r')
                page_content = content.read()
                content.close()
                page_url = re.sub('\s', '\/', page_file)
                yield page_url, page_content
        corpus = [{'id': '%s' % url, 'tokens': utils.simple_preprocess(text)}
                for url, text in page_text()]
        self.service.train(corpus, method='lsi')
        self.service.index(corpus)

    def Query(self):
        user_string = raw_input('Enter query: ')
        doc = {'tokens': utils.simple_preprocess(user_string)}
        print service.find_similar(doc, min_score=0.4, max_results=50)
