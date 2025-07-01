# AI slop
I wrote this as an interactive experiment with Gemini CLI. I made sure it asked me a bunch of questions to clarify the PRD. By having the agent refer back to the PRD I was able to get working code in the first iteration. The second interation broke much of the functionality which made me create a reference in the gemini.md file to refer to the PRD before making any major changes.

# URL
https://github.com/pleabargain/elevator-simulator


# Elevator Simulator

This is a command-line based elevator simulation game written in Python. The player manages an elevator in a building to transport passengers efficiently.

## How to Play

### Goal
The primary goal is to reach a score of 100 by transporting passengers to their destinations.

### Game Flow
The game is turn-based. In each turn, you will:
1.  See the current status of the building, including the elevator's position and waiting passengers.
2.  Be prompted to enter a target floor for the elevator.
3.  The game will then simulate the elevator's movement, passenger drop-offs, and pick-ups for that turn.

### Controls
-   When prompted, enter a floor number to send the elevator to that floor.
-   Enter 'q' to quit the game.

### Win/Loss Conditions
-   **Win:** Reach a score of 100.
-   **Lose:** 
    - The average passenger wait time exceeds 15 turns.
    - More than 20 passengers are waiting in the building.

## How to Run the Game
To play the game, simply run the `main.py` file from your terminal:
```bash
python main.py
```

## Code Overview

The project is contained within a single file, `main.py`, and is structured into three main classes:

-   `Passenger`: Represents a person with a start floor and a destination floor.
-   `Elevator`: Represents an elevator with a current floor, capacity, and a list of passengers.
-   `Building`: Represents the building itself, containing the elevator and the lists of waiting passengers for each floor.