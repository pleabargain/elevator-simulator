# Product Requirements Document: Elevator Simulator

## 1. Problem Statement
Users want a simple yet engaging simulation game that challenges their strategic thinking. The core problem is to efficiently manage an elevator to transport passengers between different floors in a building, balancing speed and capacity to achieve a high score.

## 2. Goals and Objectives
The primary goal is to create a command-line based elevator simulation game that is easy to understand but challenging to master.
- **Objective for the Player:** Reach a score of 100 points by successfully transporting passengers.
- **Objective for the Game:** Provide a clear and responsive interface, fair game mechanics, and clear win/loss conditions.

## 3. Target Users
- Players who enjoy casual simulation and strategy games.
- Individuals interested in simple algorithmic or logistical challenges.
- Students or developers looking for a small, understandable project to analyze or modify.

## 4. Functional Requirements

### 4.1. Core Gameplay
- The game is turn-based.
- The simulation displays the building status each turn, including elevator position, waiting passengers, and their desired directions.
- A new passenger is randomly generated on a floor in any given turn.
- The player provides a target floor for the elevator.
- The elevator moves to the target floor, drops off passengers for that floor, and picks up waiting passengers (up to its capacity).

### 4.2. Objective and Scoring
- The primary objective is to reach a score of 100 points.
- Points are awarded for each passenger successfully transported to their destination.

### 4.3. Win/Loss Conditions
- **Win:** The player wins by reaching a score of 100.
- **Lose:** The game ends if:
    - The average passenger wait time exceeds 15 turns.
    - More than 20 passengers are waiting in the building.

### 4.4. User Interface
- The simulation is presented in a command-line interface.
- The UI displays the building's floors, the elevator's current position, and passenger information.
- **Waiting Passengers:** Indicated by their desired direction (e.g., `^` for up, `v` for down).
- **Onboard Passengers:** Indicated by their specific destination floor (e.g., `[E1: 5,0]`).

## 5. Non-functional Requirements
- **Platform:** The application must run on any system with a standard command-line interface.
- **Language:** The application is to be written in Python 3.x.
- **Performance:** The game must run smoothly with no noticeable delay between turns. State updates and user input processing should be instantaneous.
- **Scalability:** The simulation must handle the maximum defined number of passengers and floors without degradation in performance.

## 6. Success Metrics
- **Primary Metric:** The player is able to complete the game by reaching the win condition (100 points).
- **Secondary Metrics:**
    - The average passenger wait time is consistently kept below the 15-turn limit by a skilled player.
    - The total number of waiting passengers is kept below the 20-passenger limit by a skilled player.

## 7. Timeline and Milestones
- **Milestone 1:** Development of core simulation logic (elevator movement, passenger generation).
- **Milestone 2:** Implementation of scoring, win/loss conditions, and UI.
- **Milestone 3:** Testing and bug fixing.
- **Delivery:** TBD.

## 8. How to Build and Run
### 8.1. Prerequisites
- Python 3.x
### 8.2. Running the Simulation
To run the simulation, execute the following command in your terminal:
```bash
python main.py
```
