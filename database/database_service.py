from database.database import Database


class DatabaseService:

    def __init__(self, database: Database):
        self._db = database

    def init_db(self, overwrite=False) -> None:
        if overwrite:
            self._db.drop_tables()

        self._db.create_tables()
