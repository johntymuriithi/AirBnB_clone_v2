#!/usr/bin/python3

"""This module initializes the models package
"""

from os import getenv
from models.engine import db_storage
from models.engine import file_storage


db_storage_type = getenv('HBNB_TYPE_STORAGE')

if db_storage_type == 'db':
    storage = db_storage.DBStorage()
    storage.reload()
else:
    storage = file_storage.FileStorage()
    storage.reload()
