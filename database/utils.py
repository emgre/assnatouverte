import os
from database.base import DB_PATH, Base


def flush_database():
    try:
        os.remove(DB_PATH)
        Base.metadata.create_all()
    except:
        pass
