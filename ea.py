import numpy as np
import pandas as pd
import generate_rule
import portfolio
import random
import trees
import matplotlib.pyplot as plt

def f(s):
    bool_array = generate_rule.evaluate_tree(s)
    p = portfolio.Portfolio(df)
    
    
    for k in range(0,10):
        if bool_array[k][0]:
            p.buy(k+1, 5)
        for j in range(1,len(bool_array[k])):
            if bool_array[k][j] != bool_array[k][j-1]:
                if bool_array[k][j]:
                    p.buy(k+1, 5)
                else:
                    p.sell(k+1, 5)
            
    return p.evaluate()



    
df = pd.read_csv("Training_data.csv")
df.columns = ["vol1", "close_1", "vol2", "close_2","vol3", "close_3","vol4", "close_4","vol5", "close_5","vol6", "close_6","vol7", "close_7","vol8", "close_8", "vol9", "close_9","vol10", "close_10"]


def crossover(a,b):
    r = random.choice([0,1,2,3])
    if r == 0:
        a.left, b.left = b.left, a.right
    elif  r== 1:
        a.left, b.right = b.right, a.left
    elif r == 2:
        a.right, b.left = b.left, a.right
    else:
        a.right, b.right = b.right, a.right
    return [a, b]


def mutate(s):
    
    def swap(data):
        if data == 'and':
            return 'or'
        elif data == 'or':
            return 'and'
        elif data == '>':
            return '<'
        elif data == '<':
            return '>'
        else:
            names = ['avg5', 'max5', 'min5','avg10', 'max10', 'min10','avg15', 'max15', 'min15', 'avg25', 'max25', 'min25', 'avg50', 'max50', 'min50', 'close']
            names.remove(data)
            return random.choice(names)
        
    nodes = [s, s.right, s.left, s.right.left, s.right.right, s.left.left, s.left.right]
    node_to_swap = random.choice(nodes)
    node_to_swap.data = swap(node_to_swap.data)
            
    
def generate(p=50):
    pop = []
    for i in range(p):
        pop.append(generate_rule.generate_random_rule())
    return pop


def tournament_selection(pop, t=2):
    winners = []
    for i in range(t):
        t1 = random.choice(pop)
        t2 = random.choice(pop)
        if f(t1) > f(t2):
            winners.append(t1)
        else:
            winners.append(t2)
    return winners[0], winners[1]
    
t1 = generate_rule.generate_random_rule()

 
population = generate(10) 
fitnesses = []
for k in range(10):
    fitness = [f(s) for s in population]
    fitnesses.append(max(fitness))
    a, b = tournament_selection(population)
    print(fitness)
    for c in crossover(a,b):
        mutate(c)
        fit = f(c)
        worst = min(fitness)
        if fit > worst:
            index = fitness.index(worst)
            population[index] = c
            fitness[index] = fit    
    

plt.plot(fitnesses)
plt.show()