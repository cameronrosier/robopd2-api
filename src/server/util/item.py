import re
from typing import List


def requirement_calc(base_stat: str, stat_props: List[str]) -> int:
    """
    In order to make sure requirements for an item are given correctly, we need to make sure
    that any "Requirements" stat within the stat list is accounted for.  This function will take a
    base stat value and a list of stat properties and apply the "Requirements" amount to the base stat
    if it exists in the stat property list.

    Args:
      base_stat (str): The base stat (numeric) to be altered with a requirements stat
      stat_props (List[str]): A list of stat strings to search through for the "Requirements X%" property
    
    Returns:
      int: A number representing the factoring in of the requirements modifier into the base stat.
    """

    number = base_stat
    for stat in stat_props:
        if "Requirements" in stat:
            numexp = re.compile(r'[-]?\d[\d,]*[\.]?[\d{2}]*')
            number = numexp.findall(stat)    
            number = int(number[0].replace(',', ''))
    if number < 0:
        return int(base_stat - (base_stat * int(str(number).replace('-',''))) / 100)
    else:
        return int(base_stat + (base_stat * number / 100))


def unique_formatter(unique_item: dict) -> dict:
    """
    Since the entries in the database are much more verbose than a user typically needs, this function intends to
    format a dictionary using useful fields formatted in a useable way.

    Args:
      unique_item (dict): A dictionary representing a unique item from the database with key-value pairs representing the stats and properties.
    
    Returns:
      dict: A dictionary with unuseful fields scrubbed and others formatted to a more useable manner for front-end clients
    """
    item_stats = [prop_str['PropertyString'] for prop_str in unique_item['Properties']]
    stat_values = [
      {
        "stat": prop['Property']['Code'],
        "min_value": prop['Min'],
        "max_value": prop['Max'],
        "desc_str_positive": prop['ItemStatCost']['DescriptonStringPositive'],    # This spelling error is on purpose. It's how it is in the database.
        "desc_str_negative": prop['ItemStatCost']['DescriptionStringNegative'],
      }
      for prop in unique_item['Properties']
    ]
    return {
        "name": unique_item['Name'],
        "ilvl": unique_item['ItemLevel'],
        "lvl_req": unique_item['RequiredLevel'],
        "item_code": unique_item['Code'],
        "stat_values": stat_values,
        "properties": item_stats,
        "base": unique_item['Equipment']['Name'],
        "str_req": unique_item['Equipment']['RequiredStrength'],
        "dex_req": unique_item['Equipment']['RequiredDexterity']
    }

def runeword_formatter(runeword_item: dict) -> dict:
    """
    Since the entries in the database are much more verbose than a user typically needs, this function intends to
    format a dictionary representing a runeword item using useful fields formatted in a useable way.

    Args:
      runeword_item (dict): A dictionary representing a runeword item from the database with key-value pairs representing the stats and properties.
    
    Returns:
      dict: A dictionary with unuseful fields scrubbed and others formatted to a more useable manner for front-end clients
    """
    item_stats = [prop_str['PropertyString'] for prop_str in runeword_item['Properties']]
    stat_values = [
      {
        "stat": prop['Property']['Code'],
        "min_value": prop['Min'],
        "max_value": prop['Max'],
        "desc_str_positive": prop['ItemStatCost']['DescriptonStringPositive'],    # This spelling error is on purpose. It's how it is in the database.
        "desc_str_negative": prop['ItemStatCost']['DescriptionStringNegative'],
      }
      for prop in runeword_item['Properties']
    ]
    return {
        "name": runeword_item['Name'],
        "ilvl": runeword_item['ItemLevel'],
        "lvl_req": runeword_item['RequiredLevel'],
        "item_code": runeword_item['Code'],
        "stats": stat_values,
        "properties": item_stats,
        "bases": [item['Name'] for item in runeword_item['Types']],
        "runes": [item['Name'] for item in runeword_item['Runes']],
    }


def get_items_from_set(set: str) -> List[dict]:
    """
    Given the name of a set, this function will format and return a dictionary containing all of that set's items as well as their stats and modifiers.

    Args:
      set (dict): A dictionary representing a Diablo 2 set.
    
    Returns:
      List[dict]: A list of dictionaries containing useful information about the items found within a requested set.
    """
    set_items = []
    for item in set['SetItems']:
        item_stat_strings = [prop_str['PropertyString'] for prop_str in item['Properties']]
        item_stats = [
          {
            "prop_code": prop['Property']['Code'],
            "prop_stat": prop['Property']['Stat'],
            "prop_min": prop['Min'],
            "prop_max": prop['Max']
          }
          for prop in item['Properties']
        ]
        set_items.append({
            "name": item['Name'],
            "set_name": item['Set'],
            "ilvl": item['ItemLevel'],
            "lvl_req": item['RequiredLevel'],
            "item_code": item['Code'],
            "stats": item_stats,
            "stat_strings": item_stat_strings,
            "base": item['Equipment']['Name'],
            "str_req": item['Equipment']['RequiredStrength'],
            "dex_req": item['Equipment']['RequiredDexterity']
        })
    return set_items


def full_set_formatter(full_set: dict) -> dict:
    return {
        "name": full_set['Name'],
        "set_items": [f"{set_item['Name']} ({set_item['Equipment']['Name']})" for set_item in full_set['SetItems']],
        "full_set_properties": [
          {
            "prop_code": prop['Property']['Code'],
            "prop_stat": prop['Property']['Stat'],
            "prop_min": prop['Min'],
            "prop_max": prop['Max'],
            "prop_str": prop['PropertyString']
          }
          for prop in full_set['FullProperties']
        ],
        "partial_set_properties": [
          {
            "prop_code": prop['Property']['Code'],
            "prop_stat": prop['Property']['Stat'],
            "prop_min": prop['Min'],
            "prop_max": prop['Max'],
            "prop_str": prop['PropertyString']
          }
          for prop in full_set['PartialProperties']
        ]
    }