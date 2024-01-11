import uuid

from fastapi import FastAPI, Body, Request
from fastapi import APIRouter
from pydantic import BaseModel
import logging

from model.model import Transport
from services.transportservice import TransportService
from fastapi.encoders import jsonable_encoder

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/transport",
    tags=["transport"],
    responses={404: {"description": "Not found"}},
)
transportservice = TransportService()

@router.post("/send", response_description="Pedido enviado", status_code=201)
async def create_envio_transport(request: Request, transport: Transport = Body(...)):
    logger.info("create a send order")
    return {"Pedido enviado com sucesso, id " : transportservice.creat_envio(transport)}


@router.get("/{transport_id}", status_code=200, response_model=Transport)
async def get_status_transport(transport_id: str):
    return transportservice.getTransportById(transport_id)

#calcularfrete
@router.get("/calculator/{cep}", status_code=200)
async def get_transport_calculator(cep: str):
    return transportservice.calculator(cep)


#cancelar envio
@router.put("/cancel/{transport_id}", status_code=200)
async def get_status_transport(transport_id: str):
    return transportservice.canceltransport(transport_id)