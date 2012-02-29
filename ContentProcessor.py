#!/usr/bin/env python

import os
from gensim import corpora, models, similarities

class StoreContent:

    def __init__(self, site_key):
        self.page_key = 0
        self.page_hash = {}
        self.out_dir = '%s/%s' % (os.getcwd(), str(site_key))
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def write_content(self, page_content):
        for k in page_content:
            if k not in self.page_key:
                self.page_hash[k] = self.page_key
            out_file = '%s/%s' % (self.out_dir, str(self.page_key))
            page_file = open(out_file, 'a')
            page_file.write(page_content[k])
            page_file.close()
            self.page_key += 1

       
class ContentPro:
    def __iter__(self, page_content):
        yield dictionary.doc2bow(page_content.split())

#class ContentModel:
 #   def topic_model(self, corpus):
  #      lda = 

