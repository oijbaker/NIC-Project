import random

class Node:

	def __init__(self, data):
		self.left = None
		self.right = None 
		self.data = data  
		self.number = random.randint(1,100)


	def replace(self, new):
		new.left = self.left
		new.right = self.right


	def add(self, node, parent):
		if parent == "r":
			self.right = node
		else:
			self.left = node
  
