# pylint: skip-file

from assnatouverte.crawling.crawler import Crawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database


class FirstCrawler(Crawler):
    def get_name(self) -> str:
        return 'first_crawler'

    def crawl(self, downloader: Downloader, db: Database):
        pass


class SecondCrawler(Crawler):

    def get_name(self) -> str:
        return 'second_crawler'

    def crawl(self, downloader: Downloader, db: Database):
        pass
