from unittest import TestCase
from unittest.mock import patch

from assnatouverte.crawling.defaults import DEFAULT_DB_STR
from assnatouverte.database.database_service import DatabaseService
from assnatouverte.database.database_service_factory import DatabaseServiceFactory


class TestDatabaseServiceFactory(TestCase):

    def setUp(self):
        patcher = patch('assnatouverte.database.database_service_factory.Database', autospec=True)
        self.database = patcher.start()
        self.addCleanup(patcher.stop)

        self.factory = DatabaseServiceFactory()

    def test_default_values(self):
        db_service = self.factory.build()

        self.assertIsInstance(db_service, DatabaseService)
        self.database.assert_called_once_with(DEFAULT_DB_STR, False)

    def test_set_db_str(self):
        db_str = 'sqlite:///test.sqlite'
        db_service = self.factory.with_db_str(db_str).build()

        self.assertIsInstance(db_service, DatabaseService)
        self.database.assert_called_once_with(db_str, False)
