from trees import Node
import numpy as np
import pandas as pd
from collections import deque
import random
import functions
import random_rules as rr

"""
structure of a rule 

		or 

	>      	  <

avg	 max   max   cp 
 |    |     |     
 50   25    10   

"""
df = pd.read_csv("complete_data.csv").drop("Unnamed: 0",1)

or_ = functions.Function("or", 2, lambda x: (x[0] or x[1]))
and_ = functions.Function("and", 2, lambda x: x[0] and x[1])
functions = [ or_, and_]
func_dict = {}
for function in functions:
	func_dict[function.name] = function



def generate_random_rule():
	# function_array contains funtion that will be used to generate a rule 
	# avg5 means the moving average over 5 days 

	# function_array = ['avg5', 'max5', 'min5','avg10', 'max10', 'min10','avg15', 'max15', 'min15', 'avg25', 'max25', 'min25', 'avg50', 'max50', 'min50', 'close']
	function_array = rr.function_array
	boolean_operators = ['and', 'or']
	relational_operators = ['>', '<'] # for comparisons

	function_idx = []
	boolean_idx = random.randint(0, len(boolean_operators) -1)
	relational_idx = []

	for i in range(2):
		f_idx = random.randint(0, len(function_array)-1)
		r_idx = random.randint(0, len(relational_operators) -1)
		function_idx.append(f_idx)
		relational_idx.append(r_idx)

	# root node should be a boolean operator
	root = Node(boolean_operators[boolean_idx])
	# followed by relational operator
	root.left = Node(relational_operators[relational_idx[0]])
	root.right = Node(relational_operators[relational_idx[1]])

	l0 = Node(random.choice(function_array))
	l1 = Node(random.choice(function_array))
	r0 = Node(random.choice(function_array))
	r1 = Node(random.choice(function_array))
 	
 	# leaf node should be functions 
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

def evaluate(f1, f2, operator, df):
	bool_arr = []
	for i in range(1, 11):
		if operator == '>':
			bool_arr.append(np.where(df[f1 + str('_') + str(i)] > df[f2 + str('_') + str(i)], True, False))
		else:
			bool_arr.append(np.where(df[f1 + str('_') + str(i)] < df[f2 + str('_') + str(i)], True, False))
	return bool_arr


def evaluate_tree(tree):
	# evaluate left sub-tree 
    f1 = tree.left.left.data
    f2 = tree.left.right.data
    operator = tree.left.data
    left = evaluate(f1, f2, operator, df)
    # evaluate right sub-tree 
    f1 = tree.right.left.data
    f2 = tree.right.right.data
    operator = tree.right.data
    right = evaluate(f1, f2, operator, df)
    
    boolean = func_dict[tree.data]
    return [[boolean.execute([left[i][j], right[i][j]]) for j in range(len(left[i]))] for i in range(len(left))]


def main():
	rule = generate_random_rule()


if __name__ == '__main__':
	main()
