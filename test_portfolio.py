import portfolio
import pandas as pd
import generate_rule
import trees
import ea
import numpy as np

df = pd.read_csv("Training_data.csv")
df.columns = ["vol1", "close_1", "vol2", "close_2","vol3", "close_3","vol4", "close_4","vol5", "close_5","vol6", "close_6","vol7", "close_7","vol8", "close_8", "vol9", "close_9","vol10", "close_10"]
p = portfolio.Portfolio(df, do_log= True)

def f2(s):
    bool_array = generate_rule.evaluate_tree(s)
    p = portfolio.Portfolio(df, do_log=True)
    
    bool_df = pd.DataFrame(bool_array)
    print(bool_df.head())
    for j in range(1, len(bool_array[0])):
        for k in range(1,10):
            if bool_df[j][k] != bool_df[j-1][k]:
                if bool_df[j][k]:
                    p.buy(k+1, 5)
                else:
                    p.sell(k+1, 5)    
        
    if p.evaluate() == 10000:
        return 5000            
                    
    return p.evaluate()

def f(s):
    bool_array = generate_rule.evaluate_tree(s)
    p = portfolio.Portfolio(df, do_log=True)
    
    bool_array = np.array(bool_array).transpose()
    print(len(bool_array))
    print(bool_array.shape)
    for j in range(1, len(bool_array[0])):
        for k in range(1,10):
            if bool_array[j][k] != bool_array[j-1][k]:
                if bool_array[j][k]:
                    p.buy(k+1, 5)
                else:
                    p.sell(k+1, 5)    
        
    if p.evaluate() == 10000:
        return 5000            
                    
    return p.evaluate()

['or', ['<', ['min5'], ['min50']], ['increase', ['max10'], ['min15']]]

root = trees.Node('or')
root.left = trees.Node("<")
root.right = trees.Node("increase")
root.left.left = trees.Node("min5")
root.left.right = trees.Node("avg5")
root.right.left = trees.Node("max5")
root.right.right = trees.Node("avg5")

print(generate_rule.get_subtree(root))
print(f2(root))