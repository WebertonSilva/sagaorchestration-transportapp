import uuid
from typing import List

from pydantic import BaseModel, SerializeAsAny, Field







# class Produto :
#     def __init__(id, quantidade, descricao):
#         id: str = Field(...)
#         quantidade : int = Field(...)
#         descricao : str = Field(...)
#
# class Transport :
#     def __init__(transport_id, orderid, status, transport_value, list_of_products):
#         transport_id: str = Field(default_factory=uuid.uuid4, alias="transport_id")
#         orderid: str = Field(...)
#         status: str = Field(...)
#         transport_value: float = Field(...)
#         list_of_products = list_of_products



class Produto(BaseModel):
    id: str = Field(...)
    quantidade : int = Field(...)
    descricao : str = Field(...)

class Adress(BaseModel):
    street: str = Field(...)
    number : int = Field(...)
    distrit : str = Field(...)
    city : str = Field(...)
    state : str = Field(...)
    cep: int = Field(...)

class Transport(BaseModel):

    transport_id: str = Field(default_factory=uuid.uuid4, alias="transport_id")
    orderid: str = Field(...)
    status: str = Field(...)
    transport_value: float = Field(...)
    list_id_products: List[str] = []
    #list_produtos: SerializeAsAny == List[Produto] = Field(...)

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


