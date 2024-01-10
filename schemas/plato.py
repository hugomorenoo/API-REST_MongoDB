def platoEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "nombre": item["nombre"],
        "precio": item["precio"],
        "tipo": item["tipo"],
    }

def platosEntity(entity) -> list:
    return [platoEntity(item) for item in entity]