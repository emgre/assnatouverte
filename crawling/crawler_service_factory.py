from crawling.crawler_repo import CrawlerRepository
from crawling.crawler_service import CrawlerService
from crawling.defaults import DEFAULT_DB_STR
from crawling.downloader.http_downloader import HttpDownloader
from database.database import Database


class CrawlerServiceFactory:

    def __init__(self):
        self._db_str = DEFAULT_DB_STR
        self._echo_sql = False

    def with_db_str(self, db_str: str):
        self._db_str = db_str
        return self

    def echo_sql(self):
        self._echo_sql = True
        return self

    def build(self) -> CrawlerService:
        crawler_repo = CrawlerRepository()
        crawler_repo.discover_crawlers()
        downloader = HttpDownloader()
        database = Database(self._db_str, self._echo_sql)

        return CrawlerService(crawler_repo, downloader, database)
