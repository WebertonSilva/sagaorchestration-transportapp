import logging
from fastapi import FastAPI
from pymongo import MongoClient
#from dotenv import dotenv_values

app = FastAPI()

class Database:

    def __int__(self):
        self = self
    #
    # @app.on_event("startup")
    def startup_db_client(self):
        mongodb_client = MongoClient("mongodb+srv://admin:admin@transport-db.wzzh9qg.mongodb.net/?retryWrites=true&w=majority")
        database = mongodb_client["transport_database"]
        print("Connected to the MongoDB database!")
        return database

    @app.on_event("shutdown")
    def shutdown_db_client(self):
        app.mongodb_client.close()