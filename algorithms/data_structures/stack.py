class Stack:
	def __init__(self):
		self.data = []

	def push(self, item):
		self.data.append(item)

	def pop(self):
		if len(self.data) < 1:
			return None
		else:
			return self.data.pop()

	def size(self):
		return len(self.data)

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	item = stack.pop()
	print(item, stack.size())