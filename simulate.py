import random

def play_game(reveal: int, host: int, player:int, 
              iterations: list, preferences: list) -> list:
    if player == 2:
        return None
    for iteration in range(0, len(iterations)):
        player_choice = preferences[iteration][0]
        revealed_doors = []
        empty_doors = []
        for door in range(0,len(iterations[iteration])):
            if iterations[iteration][door] == 0:
                empty_doors.append(door)

        print(f"-----START ROUND {iteration}-----")
        print(f"Doors are: {iterations[iteration]}")
        print(f"Player's initial choice is {player_choice}")

        for i in range(0, reveal):
            match host:
                case 0:
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
                case 0:
                    preferences[iteration].pop(0)
                    for door in revealed_doors:
                        if door in preferences[iteration]:
                            preferences[iteration].remove(door)
                    print(f"The player changes his decision to {preferences[iteration][0]}...")
                case 1:
                    print(f"The player does not change his decision...")