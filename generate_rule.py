from trees import Node
import numpy
import pandas 
from collections import deque
import random
import rules

"""
structure of a rule 

		or 
	>      	  <

avg	 50	   	max   30 

The above rule state if moving average over 50 days is greater than closing price buy or sell otherwise
or if max price over 30 days is greater than closing price buy or sell otherwise. 

"""
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
		random_param.append(param)


	root = Node(boolean_operators[boolean_idx])

	root.left = Node(relational_operators[relational_idx[0]])
	root.right = Node(relational_operators[relational_idx[1]])

	root.left.left = Node(function_array[function_idx[0]])
	root.left.right = Node(random_param[0]) 

	root.right.left = Node(function_array[function_idx[1]])
	root.right.right = Node(random_param[1])

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

def main():
	rule = generate_random_rule()
	arr = inorderIterative(rule)
	print(arr)

if __name__ == '__main__':
	main()