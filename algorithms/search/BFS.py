# https://www.geeksforgeeks.org/level-order-tree-traversal/
# solution 1: O(n^2) time complexity

class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.value = val

def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root, i)

def printGivenLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.value)
	elif level > 1:
		printGivenLevel(root.left, level-1)
		printGivenLevel(root.right, level-1)

def height(node):
	if node is None:
		return 0
	else:
		lheight = height(node.left)
		rheight = height(node.right)

		if lheight > rheight:
			return lheight + 1
		else:
			return rheight + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("solution 1")
printLevelOrder(root)

# Solution 2: O(n) time complexity

class Node:
	def __init__(self, val):
		self.right = None
		self.left = None
		self.value = val

def printLevelOrder(root):
	if root is None:
		return

	queue = []

	queue.append(root)

	while len(queue) > 0:
		print(queue[0].value)
		node = queue.pop(0)

		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nSolution 2")
printLevelOrder(root)
