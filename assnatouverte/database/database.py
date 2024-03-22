from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session

from assnatouverte.database.base import Base


class Database:
    def __init__(self, db_str: str, echo_sql: bool = False):
        self._engine = create_engine(db_str, echo=echo_sql)
        self.session: Session = sessionmaker(bind=self._engine)()

    def create_tables(self):
        Base.metadata.create_all(self._engine)

    def drop_tables(self):
        meta = MetaData()
        # Find all tables and delete them
        meta.reflect(self._engine)
        meta.drop_all(self._engine)
