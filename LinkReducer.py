#!/usr/bin/env python

import Pyro4


class LinkReducer:

    def __init__(self):
        self.unique_urls = []
        self.referrer_dict = {}
   
    def proc_links(self, page_referrers):
        for k in page_referrers:
            if k not in self.referrer_dict:
                self.referrer_dict[k] = page_referrers[k]
            else:
                for v in page_referrers[k]:
                    if v not in self.referrer_dict[k]:
                        self.referrer_dict[k].append(v)

    def unique_urls(self):
        return self.unique_urls

    def referrer_dict(self):
        return self.referrer_dict
