"""
Bailey Lyback
IT 140 Module Six Milestone

Simplified text based game using the provided dragon map.
Focus: dictionaries, gameplay loop, decicion branching, and input validation.
"""

#Dictionary of the rooms for the simplified dragon game

rooms = {
    "Great Hall": {"South": "Bedroom"},
    "Bedroom": {"North": "Great Hall", "East": "Cellar"},
    "Cellar": {"West": "Bedroom"}
}

def show_instructions():
    """Display game instructions to the player."""
    print("Dragon Text Adventure Game - Simplified Version")
    print("Move commands: go North, go South, go East, go West")
    print("Type 'exit' to leave the game. \n")

def show_status(current_room):
    """Show the room that the player is currently in."""
    print("You are in the ", current_room)

def get_command():
    """Prompt the player for a command and return it."""
    command = input("Enter your move: ")
    return command.strip()

def main():
    """Main game loop that follows the milestone flowchart."""
    # Place player in start room
    current_room = "Great Hall"

    # Show instructions once at the beginning
    show_instructions()

    # Game loop continues until current room is 'Exit'
    while current_room != "Exit":

        # Show player status
        show_status(current_room)

        # Get command from the player
        command = get_command()

        # Decision branch: what is the command
        if command.lower() == "exit":
            # Set current room to 'Exit' so the loop will end
            current_room = "Exit"

        elif command.lower().startswith("go "):
            # Extract the direction of the word after 'go'
            direction = command[3:].strip().title()

            # Validate direction
            if direction not in ["North", "South", "East", "West"]:
                print("That is not a valid direction. "
                      "Use North, South, East, or West.\n")
                
            else:

                # Decision branching for move between rooms
                if direction in rooms[current_room]:
                    new_room = rooms[current_room][direction]
                    print("You go", direction, "and enter the", new_room + ".\n")
                    current_room = new_room
                    
                else:
                    print("You cannot go that way from the", current_room + ".\n")

        else:
            # Other (invalid) command
            print("Invalid move. Use 'go <direction>' or 'exit' .\n")

    # Exit path after loop ends
    print("Thanks for playing the game. Hope you enjoyed it.")

if __name__ == "__main__":
    main()
