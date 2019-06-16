from crawling.crawler import Crawler
from crawling.downloader.downloader import Downloader
from database.database import Database


class FirstCrawler(Crawler):
    name = 'first_crawler'

    def crawl(self, downloader: Downloader, db: Database):
        pass


class SecondCrawler(Crawler):
    name = 'second_crawler'

    def crawl(self, downloader: Downloader, db: Database):
        pass
