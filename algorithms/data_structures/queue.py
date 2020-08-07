class Quque:
	def __init__(self):
		self.data = []

	def push(self, item):
		self.data.append(item)

	def pop(self):
		if len(self.data) < 1:
			return None
		else:
			return self.data.pop(0)

	def size(self):
		return len(self.data)

if __name__ == '__main__':
	queue = Quque()
	queue.push(1)
	queue.push(2)
	res = queue.pop()
	print(res)