#!/usr/bin/env python

import Pyro4


class LinkReducer:

    def __init__(self):
        self.unique_urls = []
        self.referrer_dict = {}
   
    def reduce_referrers(self, page_referrers):
        for k in page_referrers:
            if k not in self.referrer_dict:
                self.referrer_dict[k] = page_referrers[k]
            else:
                for v in page_referrers[k]:
                    if v not in self.referrer_dict[k]:
                        self.referrer_dict[k].append(v)
        return self.referrer_dict
    
    
    def reduce_externals(self, external_links):
        for link in external_links:
            if link not in self.unique_urls:
                self.unique_urls.append(link)
        return self.unique_urls
