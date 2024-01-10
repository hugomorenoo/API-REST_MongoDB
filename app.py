from fastapi import FastAPI
from routes.plato import plato

app = FastAPI(
    title="API-REST para proyecto DWES. Hugo Moreno y Hugo Pérez",
    version="0.0.1"
)

app.include_router(plato)