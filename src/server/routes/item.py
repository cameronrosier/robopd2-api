from fastapi import APIRouter
from typing import List

from server.controller.mongo import (
    get_unique_item,
    get_unique_items,
    get_runeword_item
)

unique_router = APIRouter()
runeword_router = APIRouter()
set_item_router = APIRouter()


@unique_router.get("/", response_description="All unique items fetched", status_code=200)
async def get_all_unique_items() -> List[dict]:
    all_unique_items = await get_unique_items()
    if all_unique_items:
        return all_unique_items
    else:
        return []


@unique_router.get("/{name}", response_description="Item fetched", status_code=200)
async def get_single_unique_item(name: str) -> dict:
    unique_item = await get_unique_item(name)
    if unique_item:
        return {
            "item_type": "unique",
            "item_data": unique_item
        }
    else:
        return {}
    
@unique_router.get("/", response_description="All unique items fetched", status_code=200)
async def get_all_unique_items() -> dict:
    unique_items = await get_unique_items()
    return {
        "item_type": "unique",
        "item_data": unique_items
    }

@runeword_router.get("/{name}", response_description="Item fetched", status_code=200)
async def get_single_runeword_item(name: str) -> str:
    runeword_item = await get_runeword_item(name)
    if runeword_item:
        return {
            "item_type": "runeword",
            "item_data": runeword_item
        }
    else:
        return {}
