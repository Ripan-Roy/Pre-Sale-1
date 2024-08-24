from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")


def connect_db():
    try:
        client = MongoClient(MONGO_URL)
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        client = None

    return client
