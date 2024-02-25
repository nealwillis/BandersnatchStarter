from os import getenv
import pandas as pd
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient

load_dotenv()

# Create a new client and connect to the server
client = MongoClient(getenv("DB_URL"), tlsCAFile=where())['Database']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

collection = client["Monsters"]


class Database:
    def seed(self, amount):
        """Inserts a new monster into the Monster collection based on input"""
        monsters = []
        for i in range(amount):
            monsters.append(Monster().to_dict())
        uid = collection.insert_many(monsters)

    def reset(self):
        """Removes all monsters from the Monster collection"""
        collection.delete_many({})

    def count(self) -> int:
        """Returns the number of monsters in the collection"""
        return collection.count_documents({})

    def dataframe(self) -> pd.DataFrame:
        """Turns the monster collection into a pandas dataframe"""
        return pd.DataFrame(list(collection.find({})))

    def html_table(self) -> str:
        """Turns monster collection into a html table"""
        return str(pd.DataFrame(list(collection.find({}))).drop(columns="_id").to_html())
