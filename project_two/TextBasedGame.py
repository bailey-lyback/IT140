"""
Bailey Lyback
IT 140 Project Two

BMW Dealership Escape Game
The goal is to collect all items in the dealership before
entering the Salesperson Desk. This prevents the long sales pitch.
"""


def show_instructions():
    """
    Display the introduction and list of main commands.
    This helps the player understand what they can do.
    """
    print("==============================================")
    print("         Welcome to BMW Dealership Escape")
    print("==============================================")
    print("Move between departments and collect all six items.")
    print("If you reach the Salesperson Desk before collecting")
    print("every item, the salesperson traps you in a long pitch.")
    print()
    print("Move commands: go North, go South, go East, go West")
    print("Item command:  get 'item name'")
    print("==============================================\n")


def show_status(current_room, inventory, rooms, villain_name, villain_room):
    """
    Show the player's current location, their inventory,
    and any item available in the current room.
    """
    print("\n----------------------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    room_item = rooms[current_room].get("Item")

    # The villain room has a unique message to build tension
    if current_room == villain_room:
        print("You see the", villain_name, "waiting at the desk.")
    elif room_item is None or room_item == "None":
        print("You do not see any useful item here.")
    else:
        print("You see a", room_item)

    print("----------------------------------------")


def get_player_command():
    """
    Prompt the player for their next move and return
    their typed command as clean text.
    """
    command = input("Enter your move: ")
    return command.strip()


def main():
    """
    Main game logic:
    - Store the dealership layout and items using a dictionary
    - Track the player's location and inventory
    - Allow valid room movement and item collection
    - End the game with a win or loss after reaching the villain

    I applied the concepts learned over the last several weeks
    to structure the rooms, validate user input, and control
    the flow of the game using loops, decisions, and functions.
    """

    # Dictionary representing the dealership map.
    # Each room links to other rooms and may contain one item.
    # This layout matches my visual room design from the map.
    rooms = {
        "Showroom": {
            "North": "Service Garage",
            "South": "Lounge",
            "East": "Accessory Display",
            "West": "Parts Counter",
            "Item": "None"
        },

        "Service Garage": {
            "South": "Showroom",
            "East": "Finance Office",
            "Item": "Oil Filter"
        },

        "Finance Office": {
            "West": "Service Garage",
            "Item": "Credit Report"
        },

        "Parts Counter": {
            "East": "Showroom",
            "Item": "Wiper Blade"
        },

        "Accessory Display": {
            "West": "Showroom",
            "North": "Salesperson Desk",
            "Item": "Keychain"
        },

        # Villain room is only accessible from Accessory Display
        "Salesperson Desk": {
            "South": "Accessory Display",
            "Item": "None"
        },

        "Lounge": {
            "North": "Showroom",
            "East": "Manager Office",
            "Item": "Cup Of Coffee"
        },

        "Manager Office": {
            "West": "Lounge",
            "Item": "Complaint Form"
        }
    }

    # This defines the final room where the win or loss happens
    villain_room = "Salesperson Desk"
    villain_name = "Salesperson"

    # Total items needed for the win condition
    collectible_items = [
        "Oil Filter",
        "Credit Report",
        "Wiper Blade",
        "Keychain",
        "Cup Of Coffee",
        "Complaint Form"
    ]
    total_items_to_collect = len(collectible_items)

    # Starting state
    current_room = "Showroom"
    inventory = []

    # Show instructions at the beginning of the game
    show_instructions()

    # ----------------------- Main Gameplay Loop -----------------------
    while True:
        # Display the current status so the player can choose their next move
        show_status(current_room, inventory, rooms, villain_name, villain_room)

        command = get_player_command()

        # Player commands use two-part input such as "go North" or "get Keychain"
        parts = command.split(" ", 1)

        if len(parts) != 2:
            print("Invalid input. Use commands like 'go North' or 'get Keychain'.")
            continue

        action = parts[0].lower()
        target_text = parts[1].strip()

        # ------------------------- Player Movement -------------------------
        if action == "go":
            direction = target_text.title()

            # Validate the direction text
            if direction not in ["North", "South", "East", "West"]:
                print("That is not a valid direction. Use North, South, East, or West.")
                continue

            # Validate the move against the room layout
            if direction in rooms[current_room]:
                next_room = rooms[current_room][direction]
                print("You walk", direction, "and enter the", next_room + ".")
                current_room = next_room

                # If player enters the villain room, check win or loss
                if current_room == villain_room:
                    if len(inventory) == total_items_to_collect:
                        # Winning outcome
                        print("\nCongratulations!")
                        print("You collected all items necessary to avoid the extended sales pitch.")
                        print("You escape the dealership before the salesperson can trap you in financing talk.")
                        print("\nThanks for playing the game. Hope you enjoyed it.")
                    else:
                        # Losing outcome
                        print("\nGAME OVER")
                        print("You entered the Salesperson Desk without all the items.")
                        print("The salesperson launches into a long talk about financing and dealer fees.")
                        print("You are unable to escape the sales pitch.")
                        print("\nThanks for playing the game. Hope you enjoyed it.")
                    break

            else:
                print("You cannot go that way from the", current_room + ".")

        # ------------------------- Item Collection -------------------------
        elif action == "get":
            requested_item = target_text.title()
            room_item = rooms[current_room].get("Item")

            # No items in this room
            if room_item is None or room_item == "None":
                print("There is no item to pick up in this room.")

            # Wrong item name
            elif requested_item != room_item:
                print("You cannot get", requested_item + ".")
                print("The item in this room is", room_item + ".")

            # Already collected
            elif room_item in inventory:
                print("You already picked up the", room_item + ".")

            # Collect item
            else:
                inventory.append(room_item)
                rooms[current_room]["Item"] = "None"
                print("You picked up the", room_item, "and added it to your inventory.")
                items_remaining = total_items_to_collect - len(inventory)

                # Show how many items are left to gather
                if items_remaining > 0:
                    print("You still need", items_remaining, "more item(s).")

        # ------------------- Invalid Commands -------------------
        else:
            print("Invalid action. Use 'go' to move or 'get' to pick up an item.")

        # Loop continues until the player wins or loses by entering the Salesperson Desk


# Run the game
if __name__ == "__main__":
    main()
