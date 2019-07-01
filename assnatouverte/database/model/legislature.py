from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from assnatouverte.database.base import Base


class Legislature(Base):
    __tablename__ = 'legislatures'

    id = Column('id', Integer, primary_key=True)

    sessions = relationship('Session', back_populates='legislature')


class Session(Base):
    __tablename__ = 'sessions'

    legislature_id = Column('legislature_id', ForeignKey(Legislature.id), primary_key=True)
    session_id = Column('session_id', Integer, primary_key=True)
    start_date = Column('start_date', Date)
    prorogation_date = Column('prorogation_date', Date)
    dissolution_date = Column('dissolution_date', Date)
    num_sittings = Column('num_sittings', Integer)

    legislature = relationship('Legislature', back_populates='sessions')
