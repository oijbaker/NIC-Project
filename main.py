import functions
from node import Node
from random import choice, random

add = functions.Function("+", 2, lambda x: x[0]+x[1])
subtract = functions.Function("-", 2, lambda x: x[0]-x[1])
multiply = functions.Function("*", 2, lambda x: x[0]*x[1])
divide = functions.Function("/", 2, lambda x: x[0]/x[1])
functions = [add, subtract, multiply, divide]
func_dict = {}
for function in functions:
    func_dict[function.name] = function
    


def f(s):
    if 2 < s < 3:
        return 1
    else:
        return 0


def random_tree(depth, parent):
    
    if depth > 1:
        root_f = choice(functions)
        root = Node(root_f.name, parent, root_f.n)
        for k in range(root_f.n):
            node = random_tree(depth-1, root)     
        return root

    else:
        n = random()*10
        node = Node(str(n), parent, 0)
    
    
    
def evaluate_tree(tree):
    tree_list = tree.get_subtree()
    if tree_list[0] in func_dict:
        f_name = tree_list[0]
        f = func_dict[f_name]
        r = f.execute([evaluate_tree(child) for child in tree.children])
        return r
    else:
        return float(tree_list[0])

            
root = random_tree(100, None)
print(root.get_subtree())
print(evaluate_tree(root))