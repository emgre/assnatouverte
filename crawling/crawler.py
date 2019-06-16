from crawling.downloader.downloader import Downloader
from database.database import Database


class Crawler:

    def crawl(self, downloader: Downloader, db: Database):
        raise NotImplementedError
