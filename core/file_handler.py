import json
import os

from core.player import Player


def save_game(player: Player):
    """
    Save the player's data into a JSON file named "save_game.json".

    Args:
        player (Player): The player object containing the player's data to be saved.
    """
    # Get the path to the game_files folder
    game_files_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "game_files"
    )
    file_path = os.path.join(game_files_folder, "save_game.json")

    player_data = {
        "name": player.name,
        "character_class": player.character_class,
        "health": player.health,
        "inventory": player.inventory,
        "current_room": player.current_room.name,
        "score": player.score,
    }
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[player.name] = player_data

    with open(file_path, "w") as file:
        json.dump(data, file)


def load_game(player_name: str) -> Player:
    """
    Load a player's saved game from the JSON file "save_game.json".

    Args:
        player_name (str): The name of the player whose saved game should be loaded.

    Returns:
        Player: The Player object representing the loaded player's data.
    """
    # Get the path to the game_files folder
    game_files_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "game_files"
    )
    file_path = os.path.join(game_files_folder, "save_game.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            player_data = data[player_name]

            if player_data:
                player = Player(
                    player_data["name"],
                    player_data["character_class"],
                    player_data["health"],
                    player_data["inventory"],
                    player_data["current_room"],
                    player_data["score"],
                )

                print("\n------Saved game loaded successfully!------\n")
                return player
            else:
                print("Player not found!")
                return
    except FileNotFoundError:
        print("No saved game found.")
        return


def get_leaderboard():
    """
    Display the leaderboard showing the names and scores of all players.
    """
    
    # Get the path to the game_files folder
    game_files_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "game_files")
    file_path = os.path.join(game_files_folder, "save_game.json")


    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No save game found.")
        return

    # Create a list to store player information (name and score)
    leaderboard = []

    # Loop through each player's data in the JSON file
    for player_data in data.values():
        # Check if the player has a 'score' attribute
        if "score" in player_data:
            # Extract the player's name and score
            name = player_data["name"]
            score = player_data["score"]

            # Append the player's information to the leaderboard list as a tuple
            leaderboard.append((name, score))

    # Sort the players based on their scores in descending order
    leaderboard.sort(key=lambda x: x[1], reverse=True)

    # Print the leaderboard
    print("\n--- Leaderboard ---")
    for idx, (name, score) in enumerate(leaderboard, start=1):
        print(f"{idx}. {name}: {score}")


def create_game(player_name: str, player_class: str):
    """
    Create a new game for the player.

    Args:
        player_name (str): The name of the player.
        player_class (str): The character class chosen by the player.

    Returns:
        Player: The Player object representing the newly created game.
    """
    player = Player(player_name, player_class)
    return player
