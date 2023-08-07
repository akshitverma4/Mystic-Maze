from enum import Enum


class RoomItems:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ItemEnum(Enum):
    """
    An enumeration representing different room items.
    """

    MEDICINE = RoomItems("Medicine", "A small vial containing a healing potion.")
    SWORD = RoomItems("Sword", "A sharp and sturdy sword.")
    WAND = RoomItems("Wand", "You can cast spells with it!")
    KEY = RoomItems("Key", "A rusty key that might unlock something.")
