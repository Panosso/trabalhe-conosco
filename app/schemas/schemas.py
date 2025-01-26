from pydantic import BaseModel, validator
from typing import List
import re

class PropertyCreate(BaseModel):
    name: str
    city: str
    state: str
    total_area: float
    agricultural_area: float
    vegetation_area: float

    @validator("total_area")
    def check_area(cls, value):
        if value <= 0:
            raise ValueError("Total area must be positive.")
        return value

    @validator("agricultural_area", "vegetation_area")
    def check_positive_area(cls, value):
        if value < 0:
            raise ValueError("Areas must be non-negative.")
        return value

    @validator("vegetation_area")
    def validate_total_area(cls, value, values):
        if "agricultural_area" in values and "total_area" in values:
            if (values["agricultural_area"] + value) > values["total_area"]:
                raise ValueError("Sum of agricultural and vegetation areas exceeds total area.")
        return value

class ProducerCreate(BaseModel):
    name: str
    cpf_cnpj: str
    hash_password: str

    @validator("cpf_cnpj")
    def validate_cpf_cnpj(cls, value):
        if not re.match(r"^\d{11}$|^\d{14}$", value):
            raise ValueError("Invalid CPF/CNPJ format.")
        return value

class ProducerResponse(ProducerCreate):
    id: int
    properties: List[PropertyCreate] = []

    class Config:
        orm_mode = True