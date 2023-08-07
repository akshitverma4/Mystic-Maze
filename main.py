from core.file_handler import (create_game, get_leaderboard, load_game,
                               save_game)
from core.player import Player


def main():
    """
    The main function that runs the text-based dungeon adventure game.
    It handles user input and interactions with the game world.
    """
    player = None

    print("Welcome to the 'Mystic Maze', A Text-based Dungeon Adventure!")
    print("1. Start New Game")
    print("2. Load Saved Game")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        player_name = input("Enter your name: ")
        player_class = input(
            "Choose your character class (Warrior, Magician, Archer): "
        )
        if player_class in ("Warrior", "Magician", "Archer"):
            player = create_game(player_name, player_class)
        else:
            print("Invalid character class. Exiting")
            return
    elif choice == "2":
        player_name = input("Enter player name: ")
        player = load_game(player_name)
    else:
        print("Invalid choice. Exiting.")
        return

    player.display_stats()
    print(player.current_room.description)
    print(
        f"Item available in this room: {list(player.items[player.current_room.name].keys())[-1] if player.current_room.name in player.items.keys() else 'Nothing'}"
    )

    while True:

        command = input("\nEnter your command (Type 'help' for options): ").lower()

        if command == "help":
            print("\nList of commands:")
            print("\t- go <direction> - Move to a different room (e.g., go north)")
            print("\t- take <item> - Pick up an item from the room")
            print("\t- use <item> - Pick up an item from the room")
            print("\t- health - to see the current health")
            print("\t- score - to see the current score")
            print("\t- location - to see the current location")
            print("\t- inventory - View your inventory")
            print("\t- leaderboard - View leaderboard")
            print("\t- save - Save the game")
            print("\t- exit - Exit the game")
        elif command.startswith("go "):
            # moving the player to another room
            direction = command.split(" ")[1]
            player.move_player(direction)
            continue
        elif command.startswith("take "):
            # taking the item and adding to the player's inventory
            item = command.split(" ")[1].capitalize()
            if (
                player.items[player.current_room.name][item].value.name.lower()
                == item.lower()
            ):
                player.add_item_to_inventory(item)
            else:
                print(f"There is no {item}.")
            continue
        elif command.startswith("use "):
            item = command.split(" ")[1].capitalize()
            player.use_item(item)

        elif command == "location":
            print(player.current_room.name)

        elif command == "health":
            print(player.health)

        elif command == "score":
            print(player.score)

        elif command == "inventory":
            print(f"{player.inventory if player.inventory else 'Empty'}")

        elif command == "leaderboard":
            get_leaderboard()

        elif command == "save":
            save_game(player)
            print("Game saved successfully.")

        elif command == "exit":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid command. Type 'help' for options.")


if __name__ == "__main__":
    main()
