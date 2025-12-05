# IT-140 Introduction to Scripting

This repository contains course work and milestone projects completed for **IT-140 Introduction to Scripting** at Southern New Hampshire University. The focus of the course is learning core scripting and programming concepts using Python, including variables, control flow, functions, loops, dictionaries, and basic problem solving.

At the moment this repository includes the **Module Six Milestone**, which is a simplified text adventure game that prepares for the larger Project Two game.

---

## Repository Structure


IT140/
├── module_six/
│   ├── module_six_assignment_lyback.py   # Module Six Milestone game
│   └── .gitignore                        # Local environment and system file ignores
└── README.md                             # Course and project overview

Additional modules and projects will be added to this structure as the course progresses.

Module Six Milestone
Simplified Dragon Text Adventure
The Module Six Milestone is a small text based game that uses a simplified version of the classic “dragon” map. The goal of this milestone is to practice:
-Using Python dictionaries to represent rooms and valid movement
-Building a gameplay loop that continues until the player chooses to exit
-Implementing decision branching with if / elif / else
-Performing basic input validation and feedback to the player
-Organizing logic into functions for clarity and reuse
The game does not yet include inventory or a full win / lose condition. Instead, it focuses on correct navigation and robust handling of player commands. This lays the foundation for the more complex Project One and Project Two designs.

Game Design Summary
-The player starts in the Great Hall.
-Rooms are connected in a small map:

Great Hall
   ↓ South
Bedroom ←→ East
           ↓
         Cellar
         
-Valid commands follow the pattern:
  go North
  go South
  go East
  go West
-The player may also type Exit to end the game.
-Room connections are defined with a Python dictionary:
rooms = {
    "Great Hall": {"South": "Bedroom"},
    "Bedroom": {"North": "Great Hall", "East": "Cellar"},
    "Cellar": {"West": "Bedroom"}
}
This structure allows the program to look up the next room based on the current room and direction.

How to Run the Game
Prerequisites
-Python 3 installed on your system
-A terminal or command prompt
Steps
1. Clone the repository:
-git clone https://github.com/YOUR-GITHUB-USERNAME/IT140.git
-cd IT140/module_six
2. Run the game script:
-python module_six_assignment_lyback.py
3. Follow the on screen instructions.
-Use go <direction> for movement.
-Use Exit to quit the game.

Example Session:
  Dragon Text Adventure Game - Simplified Version
  Move commands: go North, go South, go East, go West
  Type 'exit' to leave the game.
  You are in the Great Hall
  Enter your move: go South
  You go South and enter the Bedroom.
  You are in the Bedroom
  Enter your move: go East
  You go East and enter the Cellar.

Skills Demonstrated:
-Core Python syntax and scripting
-Use of dictionaries as data structures
-Loop control for repeated gameplay
-Branching logic for command handling
-Input validation and user feedback
-Basic code organization and documentation
These skills align with the learning outcomes of IT-140 Introduction to Scripting and serve as preparation for more complex projects later in the program.

Future Enhancements:
Planned improvements as the course progresses may include:
-Adding inventory and item collection
-Implementing a true win / lose condition
-Expanding the room map and narrative
-Refactoring into multiple modules for better organization
-Adding unit tests for core game functions

Author
Bailey Lyback
Student, IT-140 Introduction to Scripting
Southern New Hampshire University
