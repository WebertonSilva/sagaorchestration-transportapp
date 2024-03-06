import logging

from dotenv import dotenv_values
from fastapi import FastAPI
from pymongo import MongoClient
#from dotenv import dotenv_values

app = FastAPI()

logger = logging.getLogger(__name__)
config = dotenv_values("db.env")

class Database:

    def __int__(self):
        self = self
    #
    # @app.on_event("startup")
    def startup_db_client(self):
        logger.info("logging from the startup_db_client")
        client = MongoClient(config["DB_URI"])
        database = client[config["DB_NAME"]]
        print("Connected to the MongoDB database!")
        return database

    @app.on_event("shutdown")
    def shutdown_db_client(self):
        app.mongodb_client.close()