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
        mongodb_client = MongoClient("STRING DE CONEXÃO")
        database = mongodb_client["CLIENT DB"]
        print("Connected to the MongoDB database!")
        return database

    @app.on_event("shutdown")
    def shutdown_db_client(self):
        app.mongodb_client.close()