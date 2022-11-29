import pandas as pd
import numpy as np
import numpy.random as npr
import portfolio

"""
Going to define a solution as a set of rules, i.e.

s = [f_1, f_2, f_3, f_4,...,f_n]

where each f_i is a fuction taking a field in the dataset and returning a buy or sell weight, e.g. f_1 = if 
"""
    
def f(s, df):
    """ Fitness function:
    
    Run a rule base on (a section of) the dataset and get portfolio value at the end.

    Args:
        s (array): The list to evaluate the fitness of
    """
    return s

def generate_one(df):
    rb = []
    for col_n in range(len(df.columns)):
        col = list(df.columns)[col_n]
        value = npr.choice(df[col])
        greater_than_bool = npr.choice([True, False])
        if greater_than_bool:
            rule = lambda x: x > value
        else:
            rule = lambda x: x < value
        rb.append(rule)
    return rb 

df = pd.read_csv("df_moving_averages.csv").drop("Unnamed: 0", 1)
generate_one(df)
