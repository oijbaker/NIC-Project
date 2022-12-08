import numpy as np
import pandas as pd
import generate_rule
import portfolio

def f(s):
    bool_array = generate_rule.evaluate_tree(s)
    p = portfolio.Portfolio(df)
    
    for k in range(0,10):
        if bool_array[k][0]:
            p.buy(k+1, 1)
        for j in range(1,len(bool_array[k])):
            if bool_array[k][j] != bool_array[k][j-1]:
                if bool_array[k][j]:
                    p.buy(k+1, 1)
                else:
                    p.sell(k+1, 1)
            
    return p.evaluate()
    
df = pd.read_csv("Training_data.csv")
df.columns = ["vol1", "close1", "vol2", "close2","vol3", "close3","vol4", "close4","vol5", "close5","vol6", "close6","vol7", "close7","vol8", "close8", "vol9", "close9","vol10", "close10"]

rule = generate_rule.main()
print(f(rule))