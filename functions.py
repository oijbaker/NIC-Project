
class Function:
    
    
    def __init__(self, name, number_of_arguments, f):
        self.name = name
        self.n = number_of_arguments
        self.f = f
        
        
    def execute(self, args):
        return self.f(args)