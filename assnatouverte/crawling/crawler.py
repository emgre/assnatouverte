from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database


class Crawler:

    def get_name(self) -> str:
        raise NotImplementedError

    def crawl(self, downloader: Downloader, database: Database):
        raise NotImplementedError
