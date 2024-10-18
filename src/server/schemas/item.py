from typing import List

from pydantic import BaseModel, Field


class UniqueItemSchema(BaseModel):
    name: str = Field(...)
    ilvl: int = Field(...)
    lvl_req: int = Field(...)
    item_code: str = Field(...)
    stats: List[str] = Field(...)
    base: str = Field(...)
    str_req: int = Field(...)
    dex_req: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "The Oculus",
                "ilvl": 50,
                "lvl_req": 42,
                "item_code": "oba",
                "stats": [
                    "2% Chance to Cast Level 1  Teleport when Struck",
                    "+[2-3] to All Skills (varies)",
                    "+30% Faster Cast Rate"
                ],
                "base": "Swirling Crystal",
                "str_req": 0,
                "dex_req": 0
            }
        }

class RunewordItemSchema(BaseModel):
    name: str = Field(...)
    ilvl: int = Field(...)
    lvl_req: int = Field(...)
    item_code: str = Field(...)
    stats: List[str] = Field(...)
    bases: List[str] = Field(...)
    runes: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Insight",
                "ilvl": 27,
                "lvl_req": 27,
                "item_code": "Runeword62",
                "stats": [
                    "Level 12-17 Meditation Aura When Equipped",
                    "+140-180% Enhanced Damage",
                    "+35% Faster Cast Rate (Staves Only)"
                ],
                "bases": [
                    "Polearm",
                    "Staff",
                    "Spear",
                    "Scepter"
                ],
                "Runes": [
                    "Ral Rune",
                    "Tir Rune",
                    "Tal Rune",
                    "Sol Rune"
                ]
            }
        }

def ItemResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }

def AllItemsResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }
