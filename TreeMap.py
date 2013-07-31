from Tree import Tree
import pylab
from matplotlib.patches import Rectangle


class TreeMap(object):

	def __init__(self, root):
		self.ax = pylab.subplot(111, aspect='equal')
		pylab.subplots_adjust(left=0, right=1, top=1, bottom=0)
		self.ax.set_xticks([])
		self.ax.set_yticks([])

		self.add_node(root)


	def add_node(self, node, lower=[0,0], upper=[1,1], axis = 0):
		axis = axis % 2
		self.draw_rectangle(lower, upper, node)

		width = upper[axis] - lower[axis]

		for branch in node:
			upper[axis] = lower[axis] + (width * float(branch.get_weight())) / node.get_weight()
			self.add_node(branch, list(lower), list(upper), axis + 1)
			lower[axis] = upper[axis]


	def draw_rectangle(self, lower, upper, node):
		r = Rectangle(lower, upper[0] - lower[0], upper[1]-lower[1], 
			edgecolor='k',
			facecolor = (1, 1, 0))
		self.ax.add_patch(r)
		if node.is_leaf():
			rx, ry = r.get_xy()
			cx = rx + r.get_width()/2.0
			cy = ry + r.get_height()/2.0
			self.ax.annotate(node.get_weight(), (cx, cy), color=(0,0,0), fontsize = 10, ha='center', va='center')
			print node.name, rx, ry, cx, cy


	def show(self):
		pylab.show()

if __name__ == '__main__':

	root = Tree(None, None, 'root')
	c1 = Tree(root, 10, 'c1')
	c2 = Tree(root, 2, 'c2')
	n1 = Tree(root, None, 'n1')
	c3 = Tree(n1, 3, 'c3')
	c4 = Tree(n1, 4, 'c4')
	n2 = Tree(n1, None, 'n2')
	c5 = Tree(n2, 5, 'c5')
	c6 = Tree(n2, 6, 'c6')
	TreeMap(root).show()
