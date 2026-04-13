"""
Workday Dungeon: L&D Edition

You are a Training & Documentation Specialist navigating five high-pressure
workplace challenges. Your goal is to manage your energy (health), collect
helpful resources, and make it through the workday.

--- Enhancements Added ---
- Workplace-themed treasures and traps
- Reframed dungeon into a corporate L&D environment
- Added healing events as a stretch goal
- Added score calculation based on treasure value and remaining health
"""

import random


def main():
    def setup_player():
        """
        Prompts the user to create their player profile.
        Returns a dictionary with name, health, and inventory.
        """
        name = input("Enter your name: ")
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }
        return player

    def create_treasures():
        """
        Creates a dictionary of workplace-themed treasures with random values.
        """
        items = [
            "Updated SOP",
            "Clear Instructions",
            "Focus Time Block",
            "Knowledge Base Article",
            "Manager Support",
            "Successful Training Launch",
            "Task Organization Board",
            "Quiet Work Session"
        ]
        return {item: random.randint(10, 40) for item in items}

    def create_traps():
        """
        Creates a dictionary of workplace traps with damage values.
        """
        return {
            "Last-Minute Change": 2,
            "Unclear Instructions": 3,
            "Meeting Overload": 2,
            "System Issue": 4,
            "Priority Shift": 3,
            "Message Flood": 2
        }

    def create_healing_events():
        """
        Creates a dictionary of healing events with recovery values.
        """
        return {
            "Quiet Lunch Break": 2,
            "Helpful Coworker": 3,
            "Clear Priorities": 2,
            "Unexpected Free Time": 4
        }

    def display_options(room_number):
        """
        Displays player options for the current room.
        """
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for resources")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")

    def search_room(player, treasures, traps, healing_events):
        """
        Randomly triggers a treasure, trap, or healing event.
        """
        outcome = random.choice(["treasure", "trap", "healing"])

        if outcome == "treasure":
            found = random.choice(list(treasures.keys()))
            player["inventory"].append(found)
            print(f"You found: {found} (value {treasures[found]})")

        elif outcome == "trap":
            trap = random.choice(list(traps.keys()))
            damage = traps[trap]
            player["health"] -= damage
            print(f"You hit a workplace trap: {trap}! -{damage} health.")

        else:
            healing = random.choice(list(healing_events.keys()))
            recovery = healing_events[healing]
            player["health"] += recovery
            print(f"You got a boost from {healing}! +{recovery} health.")

    def check_status(player):
        """
        Displays current player health and inventory.
        """
        print(f"Health: {player['health']}")
        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")

    def end_game(player, treasures):
        """
        Displays final game summary.
        """
        total_treasure_value = sum(treasures.get(item, 0) for item in player["inventory"])
        final_score = total_treasure_value + player["health"]

        print("\n--- Game Summary ---")
        print(f"Player: {player['name']}")
        print(f"Final Health: {player['health']}")

        if player["inventory"]:
            print("Items:", ", ".join(player["inventory"]))
        else:
            print("Items: None")

        print(f"Total Treasure Value: {total_treasure_value}")
        print(f"Final Score: {final_score}")
        print("Game Over! Thanks for playing.")

    def run_game_loop(player, treasures, traps, healing_events):
        """
        Runs the 5-room game loop.
        """
        for room in range(1, 6):
            while True:
                if player["health"] < 1:
                    print("\nYou've run out of energy.")
                    end_game(player, treasures)
                    return

                display_options(room)
                choice = input("Choose 1-4: ").strip()

                if choice == "1":
                    search_room(player, treasures, traps, healing_events)
                elif choice == "2":
                    print("Moving to the next room...")
                    break
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("Quitting the game...")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid choice. Enter 1, 2, 3, or 4.")

        print("\nYou made it through all 5 rooms!")
        end_game(player, treasures)

    # -----------------------------------------------------
    # GAME ENTRY POINT
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    traps = create_traps()
    healing_events = create_healing_events()

    run_game_loop(player, treasures, traps, healing_events)


if __name__ == "__main__":
    main()
player = {
        "name": name,
        "health": 10,
        "inventory": []
    }
pass
"""Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        """
    name = input("Enter your name: ")
    player = {
            "name": name,
            "health": 10,
            "inventory": []
        }
    return player
    dict: Example:
    {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
    Tip:
    You can customize treasures or randomize the values using random.randint(3, 12).
    """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary
        # NOTE: Using workplace-themed "treasures" like tools, support, and wins
        

    def display_options(room_number):
    """
    Displays available options for the player in the current room.

    Args:
    room_number (int): The current room number.

    Output Example:
    You are in room 3.
    What would you like to do?
    1. Search for treasure
    2. Move to next room
    3. Check health and inventory
    4. Quit the game
    """
    # TODO: Print the room number and the 4 menu options listed above


    def search_room(player, treasures):
        """
    Simulates searching the current room.

    If the outcome is 'treasure', the player gains an item from treasures.
    If the outcome is 'trap', the player loses 2 health points.

    Args:
    player (dict): The player's current stats.
    treasures (dict): Dictionary of available treasures.

    Behavior:
    - Randomly choose outcome = "treasure" or "trap"
    - If treasure: choose a random treasure, add to player's inventory,
    and print what was found.
    - If trap: subtract 2 from player's health and print a warning.
 """
   # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
        # NOTE: "treasure" represents helpful tools/resources
        # # NOTE: "trap" represents workplace stressors (meetings, unclear tasks, etc.)


    def check_status(player):
        """
Displays the player’s current health and inventory.

Args:
player (dict): Player stats including health and inventory.

Example Output:
Health: 8
Inventory: ruby, gold coin
or:
Health: 10
Inventory: You have no items yet.
"""
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”


    def end_game(player, treasures):
        """
Ends the game and displays a summary.

Args:
player (dict): Player stats.
treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."


    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
