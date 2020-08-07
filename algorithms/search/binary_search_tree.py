# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.value = val

def search(root, key):
	if root is None or root.value == key:
		return root

	if root.value < key:
		return search(root.right, key)

	return search(root.left, key)

root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(search(root, 2) != None)


class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.value = val

def insert(node, key):
	if node:
		if node.value < key:
			if node == None:
				node.right = Node(key)
			else:
				insert(node.right, key)
		elif node.value > key:
			if node.left == None:
				node.left = Node(key)
			else:
				insert(node.left, key)

def in_order_print(node):
	if node:
		in_order_print(node.left)
		print(node.value)
		in_order_print(node.right)

node = Node(10)
insert(node, 2)
in_order_print(node)