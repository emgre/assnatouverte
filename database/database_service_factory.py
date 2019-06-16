from crawling.defaults import DEFAULT_DB_STR
from database.database import Database
from database.database_service import DatabaseService


class DatabaseServiceFactory:

    def __init__(self):
        self._db_str = DEFAULT_DB_STR

    def with_db_str(self, db_str: str):
        self._db_str = db_str
        return self

    def build(self) -> DatabaseService:
        database = Database(self._db_str, False)
        return DatabaseService(database)
