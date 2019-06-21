from typing import Iterable

from assnatouverte.crawling.crawler_repo import CrawlerRepository, CrawlerNotFoundException
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database


class CrawlerService:

    def __init__(self, crawler_repo: CrawlerRepository, downloader: Downloader, database: Database):
        self._crawler_repo = crawler_repo
        self._downloader = downloader
        self._database = database

    def check_valid_crawlers(self, crawler_names: Iterable[str]):
        for name in crawler_names:
            try:
                self._crawler_repo.get_crawler(name)
            except CrawlerNotFoundException:
                return False

        return True

    def execute_crawler(self, crawler_name: str) -> None:
        crawler = self._crawler_repo.get_crawler(crawler_name)
        crawler.crawl(self._downloader, self._database)
