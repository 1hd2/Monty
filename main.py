import argparse

# 1. Define arguments, generate seed
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--doors", type=int, 
                    help="The number of doors in each simulation (default = 3)")
parser.add_argument("-o", "--outcomes", type=int,
                    help="The number of outcomes in each simulation (default = 2)")
parser.parse_args()

print(parser.doors)

# 2. Get parameters (Take command line parameters, return a dict of parameters)


# 3. Setup game (Take a dict, return a list of lists)


# 4. Simulate game (Take a list of lists and a dict, run the game based on dict parameters on each list within list)


# 5. Report game results (print)

