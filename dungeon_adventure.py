"""
Workday Dungeon: L&D Edition

This program simulates a workplace-themed adventure game where the player
navigates five "rooms" representing common workplace challenges.

The player must manage their health (energy), collect helpful resources,
and make decisions that impact their ability to successfully complete the workday.

Core Concepts Demonstrated:
- Functions and modular design
- Dictionaries and lists for data storage
- Loops and conditionals for game flow
- Randomized events for variability
- User input handling

Enhancements:
- Role-based gameplay (Trainer, Knowledge Manager, Project Coordinator)
- Workplace-themed treasures, traps, and recovery events
- Score calculation based on performance and remaining energy
"""

import random


def setup_player():
    """Prompts the user to create their player profile.

    This function initializes the player by collecting their name and allowing
    them to select a role. The selected role influences gameplay outcomes,
    introducing basic strategy and replayability.

    Roles:
    - Trainer: Gains additional health from recovery events
    - Knowledge Manager: Higher chance of finding useful resources
    - Project Coordinator: Takes reduced damage from workplace challenges

    Returns:
        dict: A dictionary containing player attributes including name, role,
        starting health, and an empty inventory.
    """

    name = input("Enter your name: ")

    print("\nChoose your role:")
    print("1. Trainer")
    print("2. Knowledge Manager")
    print("3. Project Coordinator")

    role_choice = input("Enter 1-3: ").strip()

    if role_choice == "1":
        role = "Trainer"
    elif role_choice == "2":
        role = "Knowledge Manager"
    elif role_choice == "3":
        role = "Project Coordinator"
    else:
        print("Invalid choice. Defaulting to Trainer.")
        role = "Trainer"

    player = {
        "name": name,
        "role": role,
        "health": 10,
        "inventory": []
    }

    return player


def create_treasures():
    """Creates a dictionary of workplace-themed resources.

    Each item represents a helpful tool or successful outcome in a workplace
    environment. Values are randomized to introduce variability.
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
    """Creates a dictionary of workplace challenges.

    Each trap represents a productivity barrier.
    Values represent health (energy) loss.
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
    """Creates a dictionary of recovery opportunities.

    These events restore player health.
    """

    return {
        "Quiet Lunch Break": 2,
        "Helpful Coworker": 3,
        "Clear Priorities": 2,
        "Unexpected Free Time": 4
    }


def display_options(room_number):
    """Displays available player actions in the current room."""

    print(f"\nYou are in room {room_number}.")
    print("What would you like to do?")
    print("1. Search for resources")
    print("2. Move to next room")
    print("3. Check health and inventory")
    print("4. Quit the game")


def search_room(player, treasures, traps, healing_events):
    """Simulates searching a room.

    Randomly triggers a treasure, trap, or healing event.
    Outcomes are slightly influenced by player role.
    """

    role = player["role"]

    # Knowledge Manager has higher chance of finding resources
    if role == "Knowledge Manager":
        outcome_pool = ["treasure", "treasure", "trap", "healing"]
    else:
        outcome_pool = ["treasure", "trap", "healing"]

    # Randomly determine outcome
    outcome = random.choice(outcome_pool)

    if outcome == "treasure":
        found = random.choice(list(treasures.keys()))
        player["inventory"].append(found)
        print(f"You found: {found} (value {treasures[found]})")

    elif outcome == "trap":
        trap = random.choice(list(traps.keys()))
        damage = traps[trap]

        # Project Coordinator takes reduced damage
        if role == "Project Coordinator":
            damage = max(1, damage - 1)

        player["health"] -= damage
        print(f"You hit a workplace trap: {trap}! -{damage} health.")

    else:
        healing = random.choice(list(healing_events.keys()))
        recovery = healing_events[healing]

        # Trainer gets bonus healing
        if role == "Trainer":
            recovery += 1

        player["health"] += recovery
        print(f"You got a boost from {healing}! +{recovery} health.")


def check_status(player):
    """Displays the player’s current status."""

    print(f"\nName: {player['name']}")
    print(f"Role: {player['role']}")
    print(f"Health: {player['health']}")

    if player["inventory"]:
        print("Inventory:", ", ".join(player["inventory"]))
    else:
        print("Inventory: You have no items yet.")


def end_game(player, treasures):
    """Displays final game summary, score, and achievement outcome.

    The final result evaluates player performance based on:
    - Remaining health (energy management)
    - Total resource value collected (productivity)

    This adds a performance interpretation layer to the game,
    similar to real-world performance evaluation in L&D contexts.
    """

    # Calculate total value of all collected resources
    total_treasure_value = sum(
        treasures.get(item, 0) for item in player["inventory"]
    )

    # Final score combines collected resources and remaining energy
    final_score = total_treasure_value + player["health"]

    print("\n--- Game Summary ---")
    print(f"Player: {player['name']}")
    print(f"Role: {player['role']}")
    print(f"Final Health: {player['health']}")

    if player["inventory"]:
        print("Items:", ", ".join(player["inventory"]))
    else:
        print("Items: None")

    print(f"Total Resource Value: {total_treasure_value}")
    print(f"Final Score: {final_score}")

    # Determine achievement based on final performance
    if player["health"] >= 8 and total_treasure_value >= 80:
        achievement = "Thriving Employee"
        message = "You balanced productivity and well-being exceptionally well."
    elif total_treasure_value >= 80:
        achievement = "Overachiever"
        message = "You delivered strong results, but at a personal cost."
    elif player["health"] <= 2:
        achievement = "Burnout"
        message = "You pushed too hard and ran out of energy."
    else:
        achievement = "Steady Contributor"
        message = "You maintained a balanced but moderate performance."

    # Display achievement outcome as part of the final summary
    print(f"\nAchievement Unlocked: {achievement}")
    print(message)

    print("\nGame Over. Thanks for playing.")


def run_game_loop(player, treasures, traps, healing_events):
    """Controls the main game flow across 5 rooms."""

    for room in range(1, 6):
        while True:
            # End the game early if the player runs out of energy
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


def main():
    """Game entry point with replay option.

    Runs the full game loop and allows the player to restart
    without rerunning the program.
    """

    # Outer loop allows the full game to restart
    while True:
        # Create a fresh game state for each new playthrough
        player = setup_player()
        treasures = create_treasures()
        traps = create_traps()
        healing_events = create_healing_events()

        # Run one full game session
        run_game_loop(player, treasures, traps, healing_events)

        # Inner loop validates replay input before continuing
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

            if play_again == "y":
                # Restart the game by returning to the top of the outer loop
                break
            elif play_again == "n":
                # End the program completely
                print("Thanks for playing Workday Dungeon: L&D Edition!")
                return
            else:
                print("Invalid choice. Please enter y or n.")


if __name__ == "__main__":
    main()