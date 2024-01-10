from typing import Optional
from pydantic import BaseModel

class Plato(BaseModel):
    id: Optional[str] = None
    nombre: str
    precio: float
    tipo: str