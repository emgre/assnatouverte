from unittest import TestCase
from unittest.mock import call, create_autospec

from crawling.crawler import Crawler
from crawling.crawler_repo import CrawlerRepository, CrawlerNotFoundException
from crawling.crawler_service import CrawlerService
from crawling.downloader.downloader import Downloader
from database.database import Database


class TestCrawlerService(TestCase):

    def setUp(self):
        self.crawler_repo = create_autospec(CrawlerRepository)
        self.downloader = create_autospec(Downloader)
        self.database = create_autospec(Database)

        self.crawler_service = CrawlerService(self.crawler_repo, self.downloader, self.database)

    def test_check_valid_crawlers_all_exists(self):
        self.crawler_repo.get_crawler.side_effect = [create_autospec(Crawler), create_autospec(Crawler), create_autospec(Crawler)]

        result = self.crawler_service.check_valid_crawlers(['asdf', 'qwer', 'zxcv'])

        self.assertTrue(result)
        self.crawler_repo.get_crawler.assert_has_calls([call('asdf'), call('qwer'), call('zxcv')])

    def test_check_valid_crawlers_all_exists(self):
        self.crawler_repo.get_crawler.side_effect = [create_autospec(Crawler), create_autospec(Crawler), CrawlerNotFoundException()]

        result = self.crawler_service.check_valid_crawlers(['asdf', 'qwer', 'zxcv'])

        self.assertFalse(result)
        self.crawler_repo.get_crawler.assert_has_calls([call('asdf'), call('qwer'), call('zxcv')])

    def test_execute_crawler(self):
        crawler_name = 'asdf'
        mock_crawler = create_autospec(Crawler)
        self.crawler_repo.get_crawler.return_value = mock_crawler

        self.crawler_service.execute_crawler(crawler_name)

        self.crawler_repo.get_crawler.assert_called_once_with(crawler_name)
        mock_crawler.crawl.assert_called_once_with(self.downloader, self.database)
