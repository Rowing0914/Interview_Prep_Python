class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

def in_order_search(node):
	if node:
		in_order_search(node.left)
		print(node.value)
		in_order_search(node.right)

def pre_order_search(node):
	if node:
		print(node.value)
		pre_order_search(node.left)
		pre_order_search(node.right)

def post_order_search(node):
	if node:
		post_order_search(node.left)
		post_order_search(node.right)
		print(node.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nInorder traversal of binary tree")
in_order_search(root)

print("\nPreorder traversal of binary tree")
pre_order_search(root)

print("\nPostorder traversal of binary tree")
post_order_search(root)