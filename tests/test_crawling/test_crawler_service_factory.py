from unittest import TestCase
from unittest.mock import patch

from crawling.crawler_service import CrawlerService
from crawling.crawler_service_factory import CrawlerServiceFactory
from crawling.defaults import DEFAULT_DB_STR


class TestCrawlerServiceFactory(TestCase):

    def setUp(self):
        patcher = patch('crawling.crawler_service_factory.CrawlerRepository', autospec=True)
        self.crawler_repo = patcher.start()()
        self.addCleanup(patcher.stop)

        patcher = patch('crawling.crawler_service_factory.HttpDownloader', autospec=True)
        self.downloader = patcher.start()
        self.addCleanup(patcher.stop)

        patcher = patch('crawling.crawler_service_factory.Database', autospec=True)
        self.database = patcher.start()
        self.addCleanup(patcher.stop)

        self.factory = CrawlerServiceFactory()

    def test_default_values(self):
        crawler_service = self.factory.build()

        self.assertIsInstance(crawler_service, CrawlerService)
        self.crawler_repo.discover_crawlers.assert_called_once()
        self.downloader.assert_called_once()
        self.database.assert_called_once_with(DEFAULT_DB_STR, False)

    def test_set_db_str(self):
        db_str = 'sqlite:///test.sqlite'
        crawler_service = self.factory.with_db_str(db_str).build()

        self.assertIsInstance(crawler_service, CrawlerService)
        self.database.assert_called_once_with(db_str, False)

    def test_set_echo_sql(self):
        crawler_service = self.factory.echo_sql().build()

        self.assertIsInstance(crawler_service, CrawlerService)
        self.database.assert_called_once_with(DEFAULT_DB_STR, True)
