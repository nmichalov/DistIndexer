DistCrawler
===========

Distributed web crawling and indexing with python and Pyro4.
------------------------------------------------------------

DistCrawler is divided into three parts.

*CrawlDirector* Which handles URL updating and delegation

*DistCrawler* the actual web crawler meant to be run on some set of remote servers

*DataReduce* currently inaccurately named, as it actually stores the data remotely on the servers running instances of DistCrawler



