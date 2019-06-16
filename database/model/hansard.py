from sqlalchemy.orm import relationship

from database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Hansard(Base):
    __tablename__ = "hansards"

    id = Column('id', Integer, primary_key=True)
    paragraphs = relationship("Paragraph")


class Paragraph(Base):
    __tablename__ = "paragraphs"

    id = Column('id', Integer, primary_key=True)
    speaker_name = Column('speaker_name', String)
    text = Column('text', String)
    hansard_id = Column(Integer, ForeignKey('hansards.id'))
