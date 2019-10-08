from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from assnatouverte.database.base import Base


class Member(Base):
    __tablename__ = "members"

    id = Column('id', String, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    name_details = Column('name_details', String)
    electoral_division = Column('electoral_division', String)
    political_affiliation = Column('political_affiliation', String)
    email = Column('email', String)

    roles = relationship('Role', back_populates='member')


class Role(Base):
    __tablename__ = "roles"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    description = Column('description', String)
    start_date = Column('start_date', Date)
    end_date = Column('end_date', Date)
    member_id = Column(String, ForeignKey(Member.id))

    member = relationship('Member', back_populates='roles')
