import portfolio
import pandas as pd
import generate_rule
import trees
import ea
import numpy as np
import generate_rule
import portfolio
import matplotlib.pyplot as plt

def f(s):
    bool_array = generate_rule.evaluate_tree(s)
    p = portfolio.Portfolio(df, do_log=True)
            
    for k in range(0,10):
        if bool_array[k][0]:
            p.buy(k+1, 5)
    for j in range(1, len(bool_array)):
        for k in range(0,10):
            if bool_array[k][j] != bool_array[k][j-1]:
                if bool_array[k][j]:
                    p.buy(k+1, 5)
                else:
                    p.sell(k+1, 5)
                p.day += 1
            
    plt.plot(p.value_list)
    plt.show()
        
    return p.evaluate()

df = pd.read_csv("Training_data.csv")
df.columns = ["vol1", "close_1", "vol2", "close_2","vol3", "close_3","vol4", "close_4","vol5", "close_5","vol6", "close_6","vol7", "close_7","vol8", "close_8", "vol9", "close_9","vol10", "close_10"]
p = portfolio.Portfolio(df)


root = trees.Node('and')
root.left = trees.Node("<")
root.right = trees.Node("<")
root.left.left = trees.Node("avg5")
root.left.right = trees.Node("min15")
root.right.left = trees.Node("avg10")
root.right.right = trees.Node("min10")

print(generate_rule.get_subtree(root))
print(f(root))