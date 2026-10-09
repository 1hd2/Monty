import random

def generate_iterations(num_iterations:int, iteration_template:list) -> list:
    temp = iteration_template.copy()
    iterations = []
    for i in range(0, num_iterations):
        random.shuffle(temp)
        iterations.append(temp.copy())
    return iterations

def generate_preferences(num_iterations:int, num_doors:int) -> list:
    temp = []
    preferences = []
    for i in range(0, num_doors):
        temp.append(i)
    for i in range(0, num_iterations):
        random.shuffle(temp)
        preferences.append(temp.copy())
    return preferences