import numpy as np
import pandas as pd
import generate_rule
import portfolio
import random
from trees import Node
import matplotlib.pyplot as plt

# Fitness function
def f(s):
    # Generate a boolean array by evaluating the given tree with the given string
    bool_array = generate_rule.evaluate_tree(s)
    p = portfolio.Portfolio(df, do_log = True)
    
    bool_df = pd.DataFrame(bool_array)
    for j in range(1, len(bool_array[0])):
        for k in range(1,10):
            if bool_df[j][k] != bool_df[j - 1][k]:
                if bool_df[j][k]:
                    p.buy(k + 1, 5)
                else:
                    p.sell(k + 1, 5)    
        
    if p.evaluate() == 10000:
        return 5000            
                   
    return p.evaluate()


df = pd.read_csv("Training_data.csv")
df.columns = ["vol1", "close_1", "vol2", "close_2","vol3", "close_3","vol4", "close_4","vol5", "close_5","vol6", "close_6","vol7", "close_7","vol8", "close_8", "vol9", "close_9","vol10", "close_10"]


# This function is designed for crossover error to avoid using memrory address
def copy_tree(tree):
    # When the current node of the tree is empty, return NULL and end the recursion
    if tree is None:
        return None

    # From Node class to build new tree 
    new_tree = Node(tree.data)
    # Using recursion to traverse the left subtree
    new_tree.left = copy_tree(tree.left)
    # Using recursion to traverse the right subtree
    new_tree.right = copy_tree(tree.right)
    return new_tree


# Crossover function
def crossover(c, d):
    # Copy_tree function rather than assigning values
    a, b = copy_tree(c), copy_tree(d)

    # For crossover, there are 4 cases, use list to set and randomly select it
    r = random.choice([0, 1, 2, 3])
    if r == 0:
        a.left, b.left = b.left, a.right
    elif r == 1:
        a.left, b.right = b.right, a.left
    elif r == 2:
        a.right, b.left = b.left, a.right
    else:
        a.right, b.right = b.right, a.right
    
    # Return 2 objects of tree at a time for the main for loop
    return [a, b]


# Mutation function, default 100% mutation
def mutate(s, m = 1):
    
    def swap(data):
        if data == 'and': return 'or'
        elif data == 'or': return 'and'
        elif data == '>': return '<'
        elif data == '<': return '>'
        else: 
            # The bottom node of the tree
            # This is defualt common rule list for the bottom
            names = ['avg5', 'max5', 'min5','avg10', 'max10', 'min10','avg15', 'max15', 'min15', 'avg25', 'max25', 'min25', 'avg50', 'max50', 'min50', 'close']
            # Del existing rules
            names.remove(data)
            # Return random rule
            return random.choice(names)
        
    mutation_probability = 0.7
    # Cirlcal loop m times to perform m swaps on the input string s  
    for i in range(m):
        mutation_rate = np.random.rand()
        if mutation_rate < mutation_probability:
            # Choose a random node in the tree
            nodes = [s, s.right, s.left, s.right.left, s.right.right, s.left.left, s.left.right]
            node_to_swap = random.choice(nodes)
            # Perform the swap on the chosen node
            node_to_swap.data = swap(node_to_swap.data)
            

# Init population, defualt pop = 500
def generate(p = 500):

    pop = []
    for i in range(p):
        # Generate_random_rule() return a random tree with rule as a pop
        pop.append(generate_rule.generate_random_rule())
    # Return a list with lots of tree roots
    return pop


# Tournament selection function, default size = 2
def tournament_selection(pop, t = 2):

    # Random choose two different number
    pop_selected = random.sample(pop, t)

    # Calculate fitness and decide winner iwth quick sort reverse
    pop_selected.sort(key = lambda i: f(i), reverse = True)

    print(f(pop_selected[0]), f(pop_selected[1]))

    # Return tuple of winners 1st and 2nd
    return pop_selected[0], pop_selected[1]


# The generation loop function, p is population list, n is genetic generations
def run_ea(p, n):
    # Init first population
    population = generate(p)
    # Fitness is this generation fitness value, fitnesses is a list to set average fitness of each generation population
    fitness, fitnesses = [f(s) for s in population], []

    # Start evolving
    for k in range(n):
        
        print("round", k)
        # print(fitness)
        # set this round fitness
        fitnesses.append(np.average(fitness))
        # Selection parents
        a, b = tournament_selection(population)
        for c in crossover(a, b):
            # Mutation
            mutate(c)
            # Record the minium and fitness after mutation
            now_fitness, worst_score = f(c), min(fitness)
            # Compare new fitness with the weakness data
            if f(c) > worst_score:
                # Weakest replacement 
                # Python's garbage collector automatically reclaims the memory space allocated for the tree.
                population[fitness.index(worst_score)] = c
                fitness[fitness.index(worst_score)] = now_fitness

    # return result of fitness list, final population, final fitness of population
    return fitnesses, population, fitness


# invest like 10% of  starting profit into each stock, and then sell at the end
def buy_and_hold():
    p = portfolio.Portfolio(df)
    # Buy and hold strategy
    for k in range(10):
        p.buy_percentage_of_portfolio(k + 1, 10)
      
    p.day += len(df) - 1
    return p.evaluate()


# Init vaule of pop and gene
population_size = 20
generation_times = 50

# Start evolving and get result of fitness list, final population, final fitness of population
fit, pop, fit_pop = run_ea(population_size, generation_times)

print([generate_rule.get_subtree(p) for p in pop])
print(fit_pop)

plt.plot(fit)

# Computational theory buy and hold strategy
v = buy_and_hold()   
plt.plot([v for i in range(generation_times)])

plt.xlabel("genetic generations")
plt.ylabel("fitness")
plt.show()