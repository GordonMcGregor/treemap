import unittest
from Tree import Tree

class TreeTest(unittest.TestCase):

	def setUp(self):
		self.root = Tree()
		self.c1 = Tree(self.root, 1)
		self.c2 = Tree(self.root, 2)
		self.n1 = Tree(self.root)
		self.c3 = Tree(self.n1, 3)
		self.c4 = Tree(self.n1, 4)
		self.n2 = Tree(self.n1)
		self.c5 = Tree(self.n2, 5)
		self.c6 = Tree(self.n2, 6)

	def test_true(self):
		self.assertTrue(True)


	def test_root_size(self):
		self.assertTrue(self.root.get_weight() == 21)


	def test_n2_size(self):
		self.assertTrue(self.n2.get_weight() == 11)


	def test_add_node(self):
		self.n2.get_weight()
		self.c7 = Tree(self.n2, 11)
		self.assertTrue(self.n2.get_weight() == 22)


	def test_add_node(self):
		self.n2.remove_child(self.c5)
		self.assertTrue(self.n2.get_weight() == 6)


	def test_recalc(self):
		self.n2.get_weight()
		self.c7 = Tree(self.n2, 11)
		weight = self.n2.get_weight(recalculate=True)
		self.assertTrue(weight == 22, 'actual weight %d' % weight)


	def test_leaf(self):
		self.assertTrue(self.c6.is_leaf())


	def test_bare_node(self):
		self.n2.remove_child(self.c5)
		self.n2.remove_child(self.c6)
		self.assertTrue(self.n2.is_leaf())


	def test_iter_remove(self):
		to_remove = []
		for node in self.n1:
			to_remove.append(node)

		for node in to_remove:
			self.n1.remove_child(node)
		self.assertTrue(self.n1.is_leaf())


if __name__ == '__main__':
	unittest.main()
