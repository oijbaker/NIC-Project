import portfolio
import pandas as pd
import generate_rule
import trees
import ea

df = pd.read_csv("Training_data.csv")
df.columns = ["vol1", "close_1", "vol2", "close_2","vol3", "close_3","vol4", "close_4","vol5", "close_5","vol6", "close_6","vol7", "close_7","vol8", "close_8", "vol9", "close_9","vol10", "close_10"]
p = portfolio.Portfolio(df)


root = trees.Node('and')
root.left = trees.Node(">")
root.right = trees.Node("<")
root.left.left = trees.Node("avg5")
root.left.right = trees.Node("max50")
root.right.left = trees.Node("max25")
root.right.right = trees.Node("min5")

print(generate_rule.get_subtree(root))
print(ea.f(root))