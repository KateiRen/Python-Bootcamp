#from  crawler import *
#fetcher = ArticleFetcher()

import crawler
fetcher = crawler.ArticleFetcher()


for element in fetcher.fetch():
    print(element.title)

