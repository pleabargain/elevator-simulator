import time
import random

class Passenger:
    """Represents a person waiting for an elevator."""
    def __init__(self, start_floor, destination_floor):
        self.start_floor = start_floor
        self.destination_floor = destination_floor
        self.wait_time = 0

class Elevator:
    """Represents an elevator."""
    def __init__(self, capacity, start_floor=0):
        self.floor = start_floor
        self.capacity = capacity
        self.passengers = []
        self.destination_floors = set()
        self.direction = 0  # 0 for idle, 1 for up, -1 for down

class Building:
    """Represents the building with floors and elevators."""
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.elevators = [Elevator(capacity=10) for _ in range(num_elevators)]
        self.waiting_passengers = [[] for _ in range(num_floors)]
        self.score = 0
        self.total_wait_time = 0
        self.passengers_transported = 0

def display_state(building):
    """
    Displays the current state of the building and elevator.
    """
    print("\n--- Current State ---")
    print(f"Score: {building.score}")

    WAITING_WIDTH = 15
    ELEVATOR_WIDTH = 20

    # --- Header ---
    header = f"| Floor | {'Waiting'.ljust(WAITING_WIDTH)} |"
    for j in range(len(building.elevators)):
        header += f" Elevator {j+1}".ljust(ELEVATOR_WIDTH) + "|"
    print(header)
    print("-" * len(header))

    # --- Floors ---
    for i in range(building.num_floors - 1, -1, -1):
        # Waiting passengers display
        waiting_passengers = building.waiting_passengers[i]
        if waiting_passengers:
            directions = "".join(["^" if p.destination_floor > p.start_floor else "v" for p in waiting_passengers])
            waiting_str = f"[{directions}]"
        else:
            waiting_str = "[ ]"
        
        floor_str = f"| {i:2d}    | {waiting_str.ljust(WAITING_WIDTH)} |"

        # Elevators display
        for j, elevator in enumerate(building.elevators):
            elevator_display = ""
            if elevator.floor == i:
                passenger_dests = ",".join(str(p.destination_floor) for p in elevator.passengers)
                if elevator.passengers:
                    elevator_display = f"[E{j+1}: {passenger_dests}]"
                else:
                    elevator_display = f"[E{j+1}]"
            
            floor_str += elevator_display.ljust(ELEVATOR_WIDTH) + "|"
        
        print(floor_str)
    
    print("-" * len(header))

def main():
    """
    Main function to run the elevator simulator game.
    """
    print("Welcome to the Elevator Simulator!")

    # Create the building
    building = Building(num_floors=10, num_elevators=1)
    elevator = building.elevators[0] # We'll work with one elevator for now

    # Game loop
    turn = 0
    while True:
        turn += 1
        print(f"\n--- Turn {turn} ---")

        # 1. Generate new passengers
        if random.random() < 0.5: # 50% chance of new passenger each turn
            start_floor = random.randint(0, building.num_floors - 1)
            destination_floor = random.randint(0, building.num_floors - 1)
            if start_floor != destination_floor:
                passenger = Passenger(start_floor, destination_floor)
                building.waiting_passengers[start_floor].append(passenger)
                print(f"A new passenger has appeared on floor {start_floor}, going to floor {destination_floor}.")

        # 2. Print game state
        display_state(building)

        # 3. Get user input
        print("\n--- Your Turn ---")
        try:
            target_floor_input = input(f"Enter target floor for the elevator (0-{building.num_floors - 1}), or 'q' to quit: ")
            if target_floor_input.lower() == 'q':
                break

            target_floor = int(target_floor_input)

            if 0 <= target_floor < building.num_floors:
                # 4. Update game state
                # Move elevator
                print(f"Elevator moving from {elevator.floor} to {target_floor}...")
                elevator.floor = target_floor

                # Pick up passengers
                passengers_to_board = []
                for passenger in building.waiting_passengers[elevator.floor]:
                    if len(elevator.passengers) < elevator.capacity:
                        passengers_to_board.append(passenger)
                
                for passenger in passengers_to_board:
                    building.waiting_passengers[elevator.floor].remove(passenger)
                    elevator.passengers.append(passenger)
                    print(f"Passenger from floor {passenger.start_floor} boarded the elevator and is going to floor {passenger.destination_floor}.")

                # Drop off passengers
                passengers_to_disembark = []
                for passenger in elevator.passengers:
                    if passenger.destination_floor == elevator.floor:
                        passengers_to_disembark.append(passenger)

                for passenger in passengers_to_disembark:
                    elevator.passengers.remove(passenger)
                    building.score += 10 # Points for successful transport
                    building.passengers_transported += 1
                    building.total_wait_time += passenger.wait_time
                    print(f"Passenger for floor {passenger.destination_floor} has disembarked.")

                # Update wait times
                for floor_passengers in building.waiting_passengers:
                    for passenger in floor_passengers:
                        passenger.wait_time += 1
                
                for passenger in elevator.passengers:
                    passenger.wait_time += 1

            else:
                print(f"Invalid floor. Please enter a number between 0 and {building.num_floors - 1}.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        # 5. Check for win/loss conditions
        if building.passengers_transported > 0:
            avg_wait_time = building.total_wait_time / building.passengers_transported
            if avg_wait_time > 15:
                print("\n--- Game Over ---")
                print("Average passenger wait time exceeded 15 turns.")
                break
        
        total_waiting = sum(len(floor) for floor in building.waiting_passengers)
        if total_waiting > 20:
            print("\n--- Game Over ---")
            print("Too many passengers are waiting. The building is overcrowded.")
            break

        if building.score >= 100:
            print("\n--- You Win! ---")
            print(f"You reached a score of {building.score}!")
            break


    print("Thanks for playing!")

if __name__ == "__main__":
    main()
