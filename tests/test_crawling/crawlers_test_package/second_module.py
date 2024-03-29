# pylint: skip-file

from assnatouverte.crawling.crawler import Crawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database


class ThirdCrawler(Crawler):

    def get_name(self) -> str:
        return 'third_crawler'

    def crawl(self, downloader: Downloader, db: Database):
        pass


class NotACrawler:
    pass
