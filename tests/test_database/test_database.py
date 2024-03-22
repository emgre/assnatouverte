from unittest import TestCase
from sqlalchemy import inspect

from assnatouverte.database.database import Database


class TestDatabase(TestCase):
    # pylint: disable=protected-access

    def setUp(self):
        self.database = Database('sqlite://')

    def test_create_tables(self):
        self.database.create_tables()

        inspector = inspect(self.database._engine)
        self.assertGreater(len(inspector.get_table_names()), 0)

    def test_drop_tables(self):
        self.database.create_tables()

        self.database.drop_tables()

        inspector = inspect(self.database._engine)
        self.assertEqual(len(inspector.get_table_names()), 0)
