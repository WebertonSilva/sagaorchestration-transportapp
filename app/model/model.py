import uuid
from typing import List

from pydantic import BaseModel, Field

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


