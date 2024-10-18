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
MONGO_CONN = f"mongodb://{os.getenv('ROBOPD2_MONGO_USER')}:{os.getenv('ROBOPD2_MONGO_PASS')}@{os.getenv('ROBOPD2_MONGO_HOST')}{os.getenv('ROBOPD2_MONGO_PORT')}" 
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONN)
database = client[f"robopd2"]

unique_item_collection = database.get_collection("uniques")
set_item_collection = database.get_collection("sets")
runeword_collection = database.get_collection("runewords")
cube_recipe_collection = database.get_collection("cube_recipes")

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

async def _get_full_set(name: str) -> dict:
    query = {'$text': {'$search': name}}
    cursor = set_item_collection.find(query).sort([('score', {'$meta': 'textScore'})])
    full_sets = await cursor.to_list(None)
    if len(full_sets) > 0:
        return full_set_formatter(full_sets[0])
    else:
        return {}


#### TODO: Make getting a single set item cleaner
async def get_set_item(name: str) -> dict:
    all_set_items = []
    async for _set in set_item_collection.find():
        all_set_items.extend(get_items_from_set(_set))

    for set_item in all_set_items:
        if set_item['name'].lower() == name.lower():
            return set_item
    return {}
