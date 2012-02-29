#!/usr/bin/env python

import os
import cPickle

class SaveData:

    def __init__(self, site_key):
        self.page_key = 0
        self.page_hash = {}
        self.out_dir = '%s/%s' % (os.getcwd(), str(site_key))
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def save_content(self, page_content):
        for k in page_content:
            if not self.page_hash.has_key(k):
                self.page_hash[k] = self.page_key
            page_file = open('%s/%s', 'a')  % (self.out_dir, str(self.page_key))
            for p_tag in page_content[k]:
                page_file.write(p_tag.strip())
            page_file.close()
            self.page_key += 1

    def save_links(self, page_links):
        link_file = open('%s/%s', 'w') % (self.out_dir, 'links')
        cPickle.dump(page_links, link_file)
        link_file.close()


