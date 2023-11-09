import uuid
from typing import List

from pydantic import BaseModel, Field


class Adress(BaseModel):
    street: str = Field(...)
    number : int = Field(...)
    distrit : str = Field(...)
    city : str = Field(...)
    state : str = Field(...)
    cep: int = Field(...)


class Produto(BaseModel):
    id: str = Field(...)
    quantidade : int = Field(...)
    descricao : str = Field(...)


class Transport(BaseModel):

    # transport_id: str
    transport_id: str = Field(default_factory=uuid.uuid4, alias="transport_id")
    orderid: str = Field(...)
    status : str = Field(...)
    transport_value : float = Field(...)
    list_produtos : List[Produto] = Field(...)
    adress : Adress

    # class Config:
    #     allow_population_by_field_name = True
    #     schema_extra = {
    #         "example": {
    #             "transport_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
    #             "orderid": "06621314-315465b30-bsd-646d-6456664e",
    #             "status" : "[ENVIADO, CANCELADO, RETORNADO]",
    #             "transport_value": "10,00",
    #             "list_produtos": "[Produto]",
    #             "adreess" : "Rua Joao Paulo 10, Bela Vista - SP"
    #         }
    #     }


