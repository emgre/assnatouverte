from unittest import TestCase
from unittest.mock import call, create_autospec

from database.database import Database
from database.database_service import DatabaseService


class TestDatabaseService(TestCase):

    def setUp(self):
        self.mock_database = create_autospec(Database)

        self.db_service = DatabaseService(self.mock_database)

    def test_init_db_no_overwrite(self):
        self.db_service.init_db(False)

        # assert_has_calls fails due to this bug: https://bugs.python.org/issue36871
        self.assertEqual(self.mock_database.mock_calls, [call.create_tables()])

    def test_init_db_overwrite(self):
        self.db_service.init_db(True)

        # assert_has_calls fails due to this bug: https://bugs.python.org/issue36871
        self.assertEqual(self.mock_database.mock_calls, [call.drop_tables(), call.create_tables()])
