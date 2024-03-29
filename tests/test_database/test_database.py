from unittest import TestCase

from assnatouverte.database.database import Database


class TestDatabase(TestCase):
    # pylint: disable=protected-access

    def setUp(self):
        self.database = Database('sqlite://')

    def test_create_tables(self):
        self.database.create_tables()

        self.assertGreater(len(self.database._engine.table_names()), 0)

    def test_drop_tables(self):
        self.database.create_tables()

        self.database.drop_tables()

        self.assertEqual(len(self.database._engine.table_names()), 0)
