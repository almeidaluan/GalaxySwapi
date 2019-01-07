import os

from pymongo import MongoClient

class Mongo(object):
    def __init__(self):
        mongo_connection = os.environ.get("MONGO_CONNECTION")
        self.client = MongoClient(mongo_connection)
        self.galaxy_db = self.client.galaxy_db
        self.planets_collection = self.galaxy_db.planets