from core.item import ItemEnum


class Room:
    """
    A class representing a room in the map.

    Args:
        name (str): The name of the room.
        description (str): The description of the room.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Map:
    """
    A class representing the game map.
    """

    map = {
        "Starting Room": {
            "north": "North Hallway",
            "south": None,
            "east": None,
            "west": None,
        },
        "North Hallway": {
            "north": None,
            "south": "Starting Room",
            "east": "North East Wing",
            "west": "North West Wing",
        },
        "North West Wing": {
            "north": None,
            "south": None,
            "east": "North Hallway",
            "west": None,
        },
        "North East Wing": {
            "north": None,
            "south": "Hidden Room",
            "east": None,
            "west": "North Hallway",
        },
        "Hidden Room": {
            "north": "North East Wing",
            "south": None,
            "east": None,
            "west": None,
        },
    }

    danger_levels = {
        "Starting Room": 0,  # No danger
        "North Hallway": 0,  # No danger
        "North West Wing": 20,  # Moderate danger
        "North East Wing": 50,  # High danger
        "Hidden Room": 80,  # Singnificantly High danger
    }

    room_danger_message = {
        "Starting Room": "There is no danger here.",
        "North Hallway": "There is no danger here.",
        "North West Wing": "\nThere is poisonous gas here, and you inhaled it. Now your health is significantly reduced.",  # Moderate danger
        "North East Wing": "\nA zombie appeared out of nowhere! He's attacking you, do something!",  # High danger
        "Hidden Room": "\nA witch is here! She cast a spell on you, which is making your skin burn!!",  # Singnificantly High danger
    }

    room_enemy = {
        "Starting Room": None,
        "North Hallway": None,
        "North West Wing": "Poisonous gas",
        "North East Wing": "Zombie",
        "Hidden Room": "Witch",
    }

    items = {
        "North Hallway": {"Medicine": ItemEnum.MEDICINE},
        "North West Wing": {"Sword": ItemEnum.SWORD},
        "North East Wing": {"Wand": ItemEnum.WAND},
        "Hidden Room": {"Key": ItemEnum.KEY},
    }

    load_room = {
        "Starting Room": Room(
            "Starting Room", "You find yourself in a dimly lit room."
        ),
        "North Hallway": Room(
            "North Hallway",
            "You are in a long hallway with doors to the west and east.",
        ),
        "North East Wing": Room(
            "North East Wing", "You sense something mysterious in this room."
        ),
        "Hidden Room": Room(
            "Hidden Room", "Congratulations! You found the hidden treasure room!"
        ),
        "North West Wing": Room(
            "North West Wing", "This room seems to be abandoned and dusty."
        ),
    }
