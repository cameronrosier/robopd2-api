import os
import motor.motor_asyncio
from typing import List

from server.util.item import (
    unique_formatter,
    runeword_formatter,
    get_items_from_set,
    full_set_formatter
)

# No colon (':') between host and port because the MONGO_PORT env var already has it
MONGO_CONN = f"mongodb://{os.getenv('ROBOPD2_MONGO_USER')}:{os.getenv('ROBOPD2_MONGO_PASS')}@{os.getenv('ROBOPD2_MONGO_HOST')}:{os.getenv('ROBOPD2_MONGO_PORT')}" 
print(f"Connecting to MongoDB at {MONGO_CONN}")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONN, authSource="admin")
database = client[f"robopd2"]

unique_item_collection = database.get_collection("unique_items")
runes_collection = database.get_collection("runes")
runeword_collection = database.get_collection("runeword_items")

async def get_unique_item(name: str) -> dict:
    query = {'$text': {'$search': name}}
    cursor = unique_item_collection.find(query).sort([('score', {'$meta': 'textScore'})])
    unique_items = await cursor.to_list(None)
    if len(unique_items) > 0:
        return unique_formatter(unique_items[0])
    else:
        return {}

async def get_unique_items() -> List[dict]:
    all_unique_items = []
    async for item in unique_item_collection.find():
        all_unique_items.append(unique_formatter(item))
    
    return all_unique_items

async def get_runeword_item(name: str) -> dict:
    query = {'$text': {'$search': name}}
    cursor = runeword_collection.find(query).sort([('score', {'$meta': 'textScore'})])
    runeword_items = await cursor.to_list(None)
    if len(runeword_items) > 0:
        return runeword_formatter(runeword_items[0])
    else:
        return {}
