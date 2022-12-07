import functions
from node import Node
from random import choice, random

add = functions.Function("+", 2, lambda x: x[0]+x[1])
subtract = functions.Function("-", 2, lambda x: x[0]-x[1])
multiply = functions.Function("*", 2, lambda x: x[0]*x[1])
divide = functions.Function("/", 2, lambda x: x[0]/x[1])
functions = [add, subtract, multiply]#, divide]
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
        n = 1#random()*10
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
    
    
def get_all_subnodes(root):
    if root.number_of_subnodes == 0:
        return [root]
    
    nodes = [root]
    for child in root.children:
        [nodes.append(node) for node in get_all_subnodes(child)]
        
    return nodes
    
def crossover(tree1, tree2):
    c1 = choice(get_all_subnodes(tree1))
    c2 = choice(get_all_subnodes(tree2))
    p1 = c1.parent
    p2 = c2.parent
    c1.detach()
    c2.detach()
    p1.add(c2)
    p2.add(c1)
    
            
root1 = random_tree(3, None)
root2 = random_tree(3, None)
print(root1.get_subtree())
print(root2.get_subtree())
crossover(root1, root2)

print(root1.get_subtree())
print(root2.get_subtree())