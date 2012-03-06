#!/usr/bin/env python

from gensim import utils
from simserver import SessionServer


def main():
    service = SessionServer('/tmp/my_server/')
    user_string = raw_input('Enter query: ')
    doc = {'tokens': utils.simple_preprocess(user_string)}
    print service.find_similar(doc, min_score=0.4, max_results=50)

if __name__ == '__main__':
    main()
