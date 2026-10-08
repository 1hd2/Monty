import random

def generate_iterations(num_iterations, iteration_template):
    temp = iteration_template.copy()
    iterations = []
    for i in range(0, num_iterations):
        random.shuffle(temp)
        iterations.append(temp.copy())
    return iterations
