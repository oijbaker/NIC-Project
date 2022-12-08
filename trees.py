class Node:

	def __init__(self, data):
		self.left = None
		self.right = None 
		self.data = data  


	def add(self, node, parent):
		if parent == "r":
			self.right = node
		else:
			self.left = node
	
