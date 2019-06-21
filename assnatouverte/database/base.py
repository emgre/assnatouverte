from sqlalchemy.ext.declarative import declarative_base

# Declarative base model
Base = declarative_base() # pylint: disable=invalid-name

# pylint: disable=wildcard-import, wrong-import-position
from assnatouverte.database.model import *
