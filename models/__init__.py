#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""

import os

# Conditionally import either DBStorage or FileStorage based on the environment variable
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage instance after instantiation
storage.reload()
