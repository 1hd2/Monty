import argparse

# 1. Define arguments, generate seed
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--doors", type=int, default=3, 
                    help="The number of doors in each round (default = 3).")
parser.add_argument("-o", "--outcomes", type=int, default=2,
                    help="The number of outcomes in each round (default = 2).")
parser.add_argument("-r", "--reveal", type=int, default=1,
                    help="The number of doors to be revealed in each round (default = 1).")
parser.add_argument("-g", "--game", type=int, choices=[0,1], default=0, 
                    help='''
                    The behaviour mode of the game host (default=0): \n
                    0 = The host reveals [-r] doors after the player makes a decision, avoiding any winning doors \n
                    1 = The host reveals [-r] doors after the player makes a decision, completely at random 
                    ''')
parser.add_argument("-p", "--player", type=int, choices=[0,1,2], default=0,
                    help='''
                    The behaviour mode of the game player (default=0): \n
                    0 = The player always switches to another door after the host reveals a losing door \n
                    1 = The player never switches to another door \n 
                    2 = The game is played manually 
                    ''')
parser.add_argument("-i", "--iterations", type=int, default=100,
                    help="The number of iterations (rounds) in this simulation (default=100).")
parser.add_argument("-v", "--verbose", action='store_true',
                    help="Activates verbose output mode (default=off).")

args = parser.parse_args()
print(args)
# 2. Get parameters (Take command line parameters, return a dict of parameters)


# 3. Setup game (Take a dict, return a list of lists)


# 4. Simulate game (Take a list of lists and a dict, run the game based on dict parameters on each list within list)


# 5. Report game results (print)

