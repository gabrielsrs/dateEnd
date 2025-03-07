from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def create_conn():
    """Create database connection"""
    client = MongoClient(os.getenv("MONGO_CONNECTION"))
    db = client.dateEnd
    collection = db.dates

    return collection
