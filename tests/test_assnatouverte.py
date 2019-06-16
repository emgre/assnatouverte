import sys
from unittest import TestCase
from unittest.mock import patch, create_autospec, call

import assnatouverte
from crawling.crawler_service import CrawlerService
from crawling.defaults import DEFAULT_DB_STR
from database.database_service import DatabaseService


class TestAssNatOuverte(TestCase):

    def setUp(self):
        self.mock_crawler_service = create_autospec(CrawlerService)
        patcher = patch('assnatouverte.CrawlerServiceFactory', autospec=True)
        self.mock_crawler_service_factory = patcher.start()()
        self.addCleanup(patcher.stop)
        self.mock_crawler_service_factory.with_db_str.return_value = self.mock_crawler_service_factory
        self.mock_crawler_service_factory.echo_sql.return_value = self.mock_crawler_service_factory
        self.mock_crawler_service_factory.build.return_value = self.mock_crawler_service

        self.mock_database_service = create_autospec(DatabaseService)
        patcher = patch('assnatouverte.DatabaseServiceFactory', autospec=True)
        self.mock_database_service_factory = patcher.start()()
        self.addCleanup(patcher.stop)
        self.mock_database_service_factory.with_db_str.return_value = self.mock_database_service_factory
        self.mock_database_service_factory.build.return_value = self.mock_database_service

    def test_unknown_command(self):
        with self.assertRaises(SystemExit):
            self.run_with_args('unknown')

    def test_crawl_defaults(self):
        self.run_with_args('crawl', 'first_crawler', 'second_crawler')

        self.mock_crawler_service_factory.with_db_str.assert_called_once_with(DEFAULT_DB_STR)
        self.mock_crawler_service_factory.echo_sql.assert_not_called()

        self.mock_crawler_service.execute_crawler.assert_has_calls([call('first_crawler'), call('second_crawler')])

    def test_crawl_custom_db_str(self):
        db_str = 'asdf'

        self.run_with_args('-db', db_str, 'crawl', 'all')

        self.mock_crawler_service_factory.with_db_str.assert_called_once_with(db_str)

    def test_crawl_print_sql(self):
        self.run_with_args('crawl', '--print-sql', 'all')

        self.mock_crawler_service_factory.echo_sql.assert_called_once_with()

    def test_db_init_no_overwrite(self):
        self.run_with_args('init_db')

        self.mock_database_service_factory.with_db_str.assert_called_once_with(DEFAULT_DB_STR)

        self.mock_database_service.init_db.assert_called_once_with(False)

    def test_db_init_overwrite(self):
        self.run_with_args('init_db', '-x')

        self.mock_database_service_factory.with_db_str.assert_called_once_with(DEFAULT_DB_STR)

        self.mock_database_service.init_db.assert_called_once_with(True)

    def run_with_args(self, *args: str):
        with patch.object(sys, 'argv', ['assnatouverte'] + list(args)):
            assnatouverte.main()
