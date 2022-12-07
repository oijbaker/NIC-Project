class Node:
    
    
    def __init__(self, name, parent, number_of_subnodes):
        self.name = name
        self.parent = parent
        self.number_of_subnodes = number_of_subnodes
        self.children = []
        
        if self.parent != None:
            self.parent.children.append(self)
        
        
    def get_subtree(self):
        
        sub_tree = [self.name]
        for child in self.children:
            sub_tree += [child.get_subtree()]
            
        return sub_tree
            
    def delete(self):
        
        if self.number_of_subnodes == 0:
            return None

        for child in self.children:
            child.delete()
        self.number_of_subnodes = 0
        
        self.parent.children.delete(self)
        
        
    def add(self, child):

        if len(self.children) <= self.number_of_subnodes:
            self.children.append(child)
       
       
    def detach(self):
        self.parent.children.remove(self)
        self.parent = None