
from core.map import Map


class Player(Map):
    """
    A class representing the player in the game.

    Args:
        name (str): The name of the player.
        character_class (str): The character class of the player.
        health (int, optional): The player's health (default is 100).
        inventory (list, optional): A list containing the player's inventory (default is an empty list).
        current_room (str, optional): The name of the room where the player is currently located (default is "Starting Room").
        score (int, optional): The player's score (default is 0).
    """

    def __init__(
        self,
        name: str,
        character_class: str,
        health: int = 100,
        inventory: list = [],
        current_room: str = "Starting Room",
        score: int = 0,
    ):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.inventory = inventory
        self.current_room: Room = self.load_room[current_room]
        self.score = score

    def display_stats(self):
        """
        Display the player's statistics, including name,
        character class, score, health, current room, and inventory.
        """
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Score: {self.score}")
        print(f"Health: {self.health}")
        print(f"Current Room: {self.current_room.name}")
        print("Inventory:")
        if self.inventory:
            for item in self.inventory:
                print(f"  - {item}")
        else:
            print("  Empty")

    def add_item_to_inventory(self, item: str):
        """
        Add an item to the player's inventory and increase the player's score.

        Args:
            item (str): The name of the item to add to the inventory.
        """
        self.score += 2
        self.inventory.append(item)

    def move_player(self, direction: str):
        """
        Move the player to a different room based on the specified direction. Handle dangers and item availability.

        Args:
            direction (str): The direction in which the player wants to move.
        """
        # Check if the desired direction is available from the current room
        if direction.lower() not in ("north", "east", "south", "west"):
            print(
                "\n----------WARNING!----------\nInvalid direction! Avilable directions are: north, south, east, and west\n"
            )
            return

        if self.map[self.current_room.name][direction]:
            self.current_room = self.load_room[
                self.map[self.current_room.name][direction]
            ]
            self.score += 5
            print(self.current_room.description)

            if self.items[self.current_room.name]:
                key = list(self.items[self.current_room.name].keys())[0]
                print(f"Item available in this room: {key}")

            if self.danger_levels[self.current_room.name] > 0:
                print(self.room_danger_message[self.current_room.name])
                self.health -= self.danger_levels[self.current_room.name]

                if self.health < 0:
                    print("You are dead!")
                    return
                print(f"Your health is now {self.health}")
        else:
            print("\nThere is nothing in that direction! Try a different direction.")

    def use_item(self, item_name: str):
        """
        Use a specific item from the player's inventory and handle its effects.

        Args:
            item_name (str): The name of the item to use.
        """
        # Check if the item exists in the player's inventory
        if item_name not in self.inventory:
            print(f"You don't have {item_name} in your inventory.")
            return

        # Handle using the "Medicine" item to heal the player
        if item_name == "Medicine":
            if self.health == 100:
                print("Your health is already full. No need to use the Medicine.")
            else:
                # Increase the player's health by 20 points, capped at 100
                self.health = min(self.health + 40, 100)
                print(f"You used the Medicine. Your health is now {self.health}.")
                # Remove the used item from the player's inventory
                self.inventory.remove(item_name)

        # Add more cases for handling other items as needed
        elif item_name == "Sword":
            if self.room_enemy[self.current_room.name] in ("Zombie"):
                self.score += 10
                print(
                    f"You used {item_name} to defeat {self.room_enemy[self.current_room.name]}!!"
                )

            else:
                print(
                    f"No point of using {item_name} on {self.room_enemy[self.current_room.name]}"
                )

        elif item_name == "Wand":
            if self.room_enemy[self.current_room.name] in ("Witch"):
                self.score += 10
                print(
                    f"You used {item_name} to defeat {self.room_enemy[self.current_room.name]}!!"
                )
            else:
                print(
                    f"No point of using {item_name} on {self.room_enemy[self.current_room.name]}"
                )
        elif item_name == "Key":
            if self.current_room.name == "Hidden Room":
                print("You found a invaluable gem!! You win!")
                self.score += 50
        else:
            print(f"{item_name} cannot be used.")

    
