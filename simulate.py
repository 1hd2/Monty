import random

def play_game(reveal: int, host: int, 
              player:int, doors: list) -> list:
    if player == 0:
        return None
    player_choice = random.randrange(len(doors))
    revealed_doors = {}
    unrevealed_doors = generate_unrevealed(doors)
    empty_doors = {}
    for i in range(len(doors)):
        if doors[i] == 0:
            empty_doors.append(i)

    print(f"Player's initial choice is {player_choice} \n")

    for i in range(0, reveal):
        print(f"Revealed doors: {revealed_doors}")
        print(f"Unrevealed doors: {unrevealed_doors}")
        print(f"Empty doors: {empty_doors} \n")
        match host:
            case 0:
                revealed_door = reveal_losing_door(player_choice, doors, revealed_doors)
                if player_choice in empty_doors:
                    empty_doors.remove(player_choice)
                    revealed_door = random.choice(empty_doors)
                    print(f"Revealing door number {revealed_door}...")
                    revealed_doors.append(revealed_door)
                    empty_doors.append(player_choice)
                else: 
                    revealed_door = random.choice(empty_doors)
                    print(f"Revealing door number {revealed_door}...")
                    revealed_doors.append(revealed_door)
            
            case 1:
                revealed_door = random.rangerange(len(iteration))
                print(f"Revealing door number {revealed_door} at random...")
                revealed_doors.append(revealed_door)
        
        match player:
            case 1:

                print(f"The player changes his decision to ...")
            case 2:
                print(f"The player does not change his decision...")

def generate_unrevealed(doors: list) -> set:
    unrevealed_doors = []
    for i in range(0, len(doors)):
        unrevealed_doors.append(i)
    return unrevealed_doors

def reveal_losing_door(player_choice: int, empty_doors: set, unrevealed_doors: set) -> set:
    available_doors = unrevealed_doors.copy()
    for door_number in available_doors:
        if door_number not in empty_doors:
            available_doors.remove(door_number)