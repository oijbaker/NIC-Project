import pandas as pd
import numpy as np
import numpy.random as npr
import portfolio









""" whole file is deprecated is it is a pile of shit """










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
    p = portfolio.Portfolio(df)

    for i, r in df.iterrows():
        for k in range(len(s)):
            # buy?
            """ this is shit in needs changing but it'll work for now """
            val = r[df.columns[k]]
            stock_index = str(df.columns[k])[-1]
            if stock_index == "0":
                stock_index = 10
            if s[k][0](val):
                p.buy(int(stock_index), 1)
            if s[k][1](val):
                p.sell(int(stock_index), 1)
        p.day += 1
    return p.evaluate()

def generate_one(df):
    rb = []
    values = []
    for col_n in range(len(df.columns)):
        bv_sv = []
        col = list(df.columns)[col_n]
        value = npr.choice(df[col])
        greater_than_bool = npr.choice([True, False])
        if greater_than_bool:
            buy_rule = lambda x: x > value
            bv = ">"
        else:
            buy_rule = lambda x: x < value
            bv = "<"
        bv_sv.append(bv+str(value))
        value = npr.choice(df[col])
        greater_than_bool = npr.choice([True, False])
        if greater_than_bool:
            sell_rule = lambda x: x > value
            sv = ">"
        else:
            sell_rule = lambda x: x < value
            sv = "<"
        bv_sv.append(sv+str(value))
        rb.append([buy_rule, sell_rule])
        values.append(bv_sv)
        
    return rb, values 

df = pd.read_csv("df_moving_averages.csv").drop("Unnamed: 0", 1)
rb, values = generate_one(df)
print(f(rb,df))
print(values)