from pathlib import Path
from unittest import TestCase
from unittest.mock import create_autospec

from crawling.crawler import Crawler
from crawling.crawler_repo import CrawlerRepository, CrawlerNotFoundException, CrawlerWithSameIdAlreadyExistsException


class TestCrawlerRepository(TestCase):

    def setUp(self):
        self.crawler_name = 'asdf'
        self.mock_crawler = create_autospec(Crawler)
        self.mock_crawler.name = self.crawler_name

        self.filled_crawler_repo = CrawlerRepository()
        self.filled_crawler_repo.add_crawler(self.mock_crawler)

        self.empty_crawler_repo = CrawlerRepository()

    def test_add_crawler(self):
        second_mock_crawler = create_autospec(Crawler)
        second_mock_crawler.name = 'qwer'

        self.filled_crawler_repo.add_crawler(second_mock_crawler)

        self.assertCountEqual(self.filled_crawler_repo.get_all_crawlers(), [self.mock_crawler, second_mock_crawler])

    def test_add_crawler_with_same_name(self):
        second_mock_crawler = create_autospec(Crawler)
        second_mock_crawler.name = self.crawler_name

        with self.assertRaises(CrawlerWithSameIdAlreadyExistsException):
            self.filled_crawler_repo.add_crawler(second_mock_crawler)

        self.assertCountEqual(self.filled_crawler_repo.get_all_crawlers(), [self.mock_crawler])

    def test_get_crawler(self):
        crawler = self.filled_crawler_repo.get_crawler(self.crawler_name)

        self.assertEqual(crawler, self.mock_crawler)

    def test_get_unknown_crawler(self):
        with self.assertRaises(CrawlerNotFoundException):
            self.filled_crawler_repo.get_crawler('unknown')

    def test_discover_crawlers(self):
        self.empty_crawler_repo.discover_crawlers(Path(__file__).parent / 'crawlers_test_package')

        crawler_names = [crawler.name for crawler in self.empty_crawler_repo.get_all_crawlers()]
        self.assertCountEqual(crawler_names, ['first_crawler', 'second_crawler', 'third_crawler'])
