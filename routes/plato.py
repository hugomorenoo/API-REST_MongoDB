from fastapi import APIRouter, Response, status
from config.bd import conn
from schemas.plato import platosEntity, platoEntity
from bson import ObjectId
from models.plato import Plato
from starlette.status import HTTP_204_NO_CONTENT

plato = APIRouter()

@plato.get('/', response_model=list[Plato], tags=["users"])
def get_all_platos():
    return platosEntity(conn.hugomoreno.platos.find())

@plato.post('/platos', response_model=Plato, tags=["users"])
def create_plato(plato: Plato):
    nuevo_plato = dict(plato)
    id = conn.hugomoreno.platos.insert_one(nuevo_plato).inserted_id
    plato = conn.hugomoreno.platos.find_one({"_id": id})
    return platoEntity(plato)

@plato.get('/platos/{id}', response_model=Plato, tags=["users"])
async def find_plato(id: str):
    plato = conn.hugomoreno.platos.find_one({"_id": ObjectId(id)})
    if plato:
        return platoEntity(plato)
    else:
        return {"error": "Plato no encontrado"}

@plato.put('/platos/{id}', response_model=Plato, tags=["users"])
def edit_plato(id: str, plato: Plato):
    conn.hugomoreno.platos.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(plato)})
    return platoEntity(conn.hugomoreno.platos.find_one({"_id": ObjectId(id)}))

@plato.delete('/platos/{id}', response_model=Plato, tags=["users"])
def delete_plato(id: str):
    plato = conn.hugomoreno.platos.find_one({"_id": ObjectId(id)})
    platoEntity(conn.hugomoreno.platos.find_one_and_delete({"_id": ObjectId(id)}))
    if plato:
        return platoEntity(plato)
    else:
        return {"error": "Plato no encontrado"}