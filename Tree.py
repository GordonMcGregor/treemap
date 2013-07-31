class Tree(object):

	def __init__(self, parent=None, weight=None):
		self.parent = parent
		self.children = []
		self.weight = weight
 		self.changed = False
		if self.parent:
			self.parent.add_child(self)


	def add_child(self, child):
 		self.changed = True
		self.children.append(child)


	def remove_child(self, child):
 		self.changed = True
		self.children.remove(child)


	def get_weight(self, recalculate = False):

		if (recalculate and self.children) or not self.weight or self.changed:
	 		self.weight = 0
	 		self.changed = False
			for child in self.children:
				self.weight += child.get_weight(recalculate)

		return self.weight


	def __iter__(self):
		for child in self.children:
			yield child


	def is_leaf(self):
		return len(self.children) == 0


if __name__ == '__main__':
	root = Tree()
	c1 = Tree(root, 1)
	c2 = Tree(root, 2)
	n1 = Tree(root)
	c3 = Tree(n1, 3)
	c4 = Tree(n1, 4)
	n2 = Tree(n1)
	c5 = Tree(n2, 5)
	c6 = Tree(n2, 6)
