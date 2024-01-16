from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
usuario = os.environ.get("USUARIO")
password = os.environ.get("PASSWORD")

uri = f"mongodb+srv://{usuario}:{password}@cluster0.76rx93h.mongodb.net/"

conn = MongoClient(uri, server_api=ServerApi("1"))


