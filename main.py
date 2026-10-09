import argparse
import random
from generate import generate_iterations, generate_preferences

# 1. Get parameters
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
parser.add_argument("-s", "--seed", type=str,
                     help="The seed used for randomisation")

args = parser.parse_args()

# 2. Setup game (Generate randomised arrays representing doors)
if args.seed != None:
    random.seed(args.seed)
else:
    random.seed()
iteration_template = []
for i in range(args.outcomes):
    iteration_template.append(i)
while len(iteration_template) < args.doors:
    iteration_template.append(0)


# setup a list with the different types of outcome
# shuffle and append to a list of iterations
print(args)

print(f"generating {args.iterations} iterations of {iteration_template}...")
iterations = generate_iterations(args.iterations, iteration_template)

print(f"generating {args.iterations} preferences...")
preferences = generate_preferences(args.iterations, args.doors)

for i in range(args.iterations):
    print(i, iterations[i], preferences[i])

# 3. Simulate game (For each array, randomise player behaviour, host response, and player response)


# 4. Report game results (print)

