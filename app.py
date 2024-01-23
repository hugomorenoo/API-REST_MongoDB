from fastapi import FastAPI
from routes.plato import plato
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API-REST para proyecto DWES. Hugo Moreno y Hugo Pérez",
    version="0.0.1"
)

app.include_router(plato)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
