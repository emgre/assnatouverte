from database.base import Base
from sqlalchemy import Column, Integer, String


class Member(Base):
    __tablename__ = "members"

    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    electoral_division = Column('electoral_division', String)
    political_affiliation = Column('political_affiliation', String)
    email = Column('email', String)
