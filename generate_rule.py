from trees import Node
import numpy
import pandas as pd
from collections import deque
import random
import rules
import functions

"""
structure of a rule 

		or 
	>      	  	<

   avg	    50	     max   30 

The above rule state if moving average over 50 days is greater than closing price buy or sell otherwise
or if max price over 30 days is less than closing price buy or sell otherwise. 

"""

def moving_average(stock, days, day):
    return df["moving_average"+str(days)+"_"+str(stock+1)][day]

def max_(stock, days, day):
    return df["max"+str(days)+"_"+str(stock+1)][day]

def min_(stock, days, day):
    return df["min"+str(days)+"_"+str(stock+1)][day]

df = pd.read_csv("complete_data.csv").drop("Unnamed: 0",1)
print(moving_average(3, 50, 2))

add = functions.Function("+", 2, lambda x: x[0]+x[1])
subtract = functions.Function("-", 2, lambda x: x[0]-x[1])
multiply = functions.Function("*", 2, lambda x: x[0]*x[1])
greater = functions.Function(">", 2, lambda x: x[0]>x[1])
or_ = functions.Function("or", 2, lambda x: (x[0] or x[1]))
and_ = functions.Function("and", 2, lambda x: x[0] and x[1])
avg = functions.Function("avg", 0, lambda: rules.moving_average(random.randint(1,50)))
max_ = functions.Function("max", 0, lambda: rules.max_price(random.randint(1,50)))
min_ = functions.Function("min", 0, lambda: rules.min_price(random.randint(1,50)))
functions = [add, subtract, multiply, or_, and_, avg, max_, min_]
func_dict = {}
for function in functions:
	func_dict[function.name] = function
 

def generate_random_rule():
	function_array = ['avg', 'max', 'min']
	boolean_operators = ['and', 'or']
	relational_operators = ['>', '<']

	function_idx = []
	boolean_idx = random.randint(0, len(boolean_operators) -1)
	relational_idx = []
	random_param = []

	for i in range(2):
		f_idx = random.randint(0, len(function_array)-1)
		r_idx = random.randint(0, len(relational_operators) -1)
		param = random.randint(0, 50)
		function_idx.append(f_idx)
		relational_idx.append(r_idx)
		


	root = Node(boolean_operators[boolean_idx])

	root.left = Node(relational_operators[relational_idx[0]])
	root.right = Node(relational_operators[relational_idx[1]])

	l0 = Node(random.choice(function_array))
	l1 = Node(random.choice(function_array))
	r0 = Node(random.choice(function_array))
	r1 = Node(random.choice(function_array))
 
	root.left.add(l0, 'l')
	root.left.add(l1, 'r')
	root.right.add(r0, 'l')
	root.right.add(r1, 'r')

	return root 

def inorderIterative(root):
	stack = deque()
	curr = root
	rule_arr = []
	while stack or curr:
		if curr:
			stack.append(curr)
			curr = curr.left
		else:
			curr = stack.pop()
			rule_arr.append(curr.data)
			curr = curr.right
	return rule_arr

def get_subtree(root):
	
	sub_tree = [root.data]
 
	if root.left != None:
		sub_tree += [get_subtree(root.left)]
		sub_tree += [get_subtree(root.right)]
		
	return sub_tree


def evaluate_tree(tree):
    tree_list = get_subtree(tree)
    if tree_list[0] in func_dict:
        f_name = tree_list[0]
        f = func_dict[f_name]
        r = f.execute([evaluate_tree(child) for child in [tree.left, tree.right]])
        return r
    else:
        return float(tree_list[0])
    

def main():
	rule = generate_random_rule()
	arr = inorderIterative(rule)
	print(arr)
	print(evaluate_tree(rule))

if __name__ == '__main__':
	main()
