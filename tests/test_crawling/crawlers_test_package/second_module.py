from crawling.crawler import Crawler
from crawling.downloader.downloader import Downloader
from database.database import Database


class ThirdCrawler(Crawler):
    name = 'third_crawler'

    def crawl(self, downloader: Downloader, db: Database):
        pass


class NotACrawler:
    pass
