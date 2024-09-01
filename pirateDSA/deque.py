class Deque:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return len(self.items) == 0

	def add_front(self, item):
		self.items.append(item)

	def add_rear(self, item):
		self.items.insert(0, item)

	def remove_front(self):
		if not self.is_empty():
			return self.items.pop()
		else:
			raise IndexError("remove_front from empty deque")

	def remove_rear(self):
		if not self.is_empty():
			return self.items.pop(0)
		else:
			raise IndexError("remove_rear from empty deque")

	def size(self):
		return len(self.items)

example = Deque()
example.add_front(1)
example.add_front(2)
example.remove_rear()
size = example.size()
print(size)
print(example.items)