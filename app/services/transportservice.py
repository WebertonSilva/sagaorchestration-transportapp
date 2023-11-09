import logging
import random

from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from model.model import Transport
from database.transportdatabase import Database

router = APIRouter()
db = Database()
logger = logging.getLogger(__name__)

class TransportService:
    def __init__(self): self = self

    def creat_envio(self, transport : Transport):
        transport.status='enviado'
        tr = jsonable_encoder(transport)
        db.startup_db_client()["transport_table"].insert_one(tr)
        return transport.transport_id

    def getTransportById(self, transport_id):
        transport = db.startup_db_client()["transport_table"].find_one(
             {"transport_id": transport_id}
        )
        return transport

    def calculator(self, cep):
        return random.uniform(0.0, 100.0)  # Generates a random float between 0.0 and 1.0


    def canceltransport(self, transport_id):
        transport = db.startup_db_client()["transport_table"].find_one(
             {"transport_id": transport_id}
        )
        transport['status'] = 'cancelado'
        update_result = db.startup_db_client()["transport_table"].update_one(
             {"_id": transport.get('_id', None)}, {"$set":transport}
        )
        return 'Envio cancelado com sucesso !!'
