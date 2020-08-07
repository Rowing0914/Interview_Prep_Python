

class Node:
	def __init__(self, value):
		self.l = None
		self.r = None
		self.v = value


class BinaryTree:
	def __init__(self):
		self.root = None

	def add(self, item):
		if self.root == None:
			self.root = Node(value=item)
		else:
			self._add(item, self.root)

	def _add(self, item, node):
		if item > node.v:
			print("right: ", item)
			if node.r == None:
				node.r = Node(value=item)
			else:
				self._add(item, node.r)
		else:
			print("lefft: ", item)
			if node.l == None:
				node.l = Node(value=item)
			else:
				self._add(item, node.l)

	def printTree(self):
		if self.root == None:
			print("Nothing")
		else:
			self._printTree(self.root)

	def _printTree(self, node):
		if node != None:
			self._printTree(node.l)
			print(str(node.v) + " ")
			self._printTree(node.r)

if __name__ == '__main__':
	tree = BinaryTree()
	tree.add(3)
	tree.add(4)
	tree.add(0)
	tree.add(8)
	tree.add(2)
	tree.printTree()