#!/usr/bin/env python

import Pyro4
import os
import urlparse
import sys

class LinkMapper:

    def __init__(self):
        self.referrers = {}
        self.external_links = []
        
    def proc_links(self, link_dict):
        for k in link_dict:
            for v in link_dict[k]:
                if not self.referrers.has_key(v):
                    self.referrers[v] = [k,]
                else:
                    self.referrers[v].append(k)
                    link_site = urlparse.urlparse(v).netloc
                    if 'http://'+link_site not in self.external_urls:
                        self.external_links.append('http://'+link_site)
    
    def externals(self):
        return self.external_links

    def referrers(self):
        return self.referrers
