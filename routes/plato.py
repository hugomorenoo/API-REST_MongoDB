from fastapi import APIRouter, HTTPException, status
from config.bd import conn
from schemas.plato import platosEntity, platoEntity
from bson import ObjectId
from models.plato import Plato

plato = APIRouter()

@plato.get('/', response_model=list[Plato], tags=["platos"])
@plato.get('/platos', response_model=list[Plato], tags=["platos"])
def get_all_platos():
    return platosEntity(conn.hugomoreno.platos.find())

@plato.get('/platos/{id}', response_model=Plato, tags=["platos"])
async def find_plato(id: str):
    plato = conn.hugomoreno.platos.find_one({"_id": ObjectId(id)})
    if plato:
        return platoEntity(plato)
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

@plato.post('/platos', response_model=Plato, tags=["platos"])
def create_plato(plato: Plato):
    nuevo_plato = dict(plato)
    id = conn.hugomoreno.platos.insert_one(nuevo_plato).inserted_id
    plato = conn.hugomoreno.platos.find_one({"_id": id})
    return platoEntity(plato)

@plato.put('/platos/{id}', response_model=Plato, tags=["platos"])
def edit_plato(id: str, nuevoPlato: Plato):
    plato = conn.hugomoreno.platos.find_one({"_id": ObjectId(id)})
    if plato:
        conn.hugomoreno.platos.update_one(plato, {"$set": dict(nuevoPlato)})
        return platoEntity(conn.hugomoreno.platos.find_one({"_id": ObjectId(id)}))
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

@plato.delete('/platos/{id}', response_model=Plato, tags=["platos"])
def delete_plato(id: str):
    plato = conn.hugomoreno.platos.find_one({"_id": ObjectId(id)})
    if plato:
        platoEntity(conn.hugomoreno.platos.find_one_and_delete({"_id": ObjectId(id)}))
        return platoEntity(plato)
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)