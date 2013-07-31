from Tree import Tree as t
from Tree import make_tree
from TreeMap import TreeMap

short_map = (((1, 2), 3, ((1, 1), 4, (1, 1, 1, 1))))

x=make_tree(short_map)
TreeMap(x).show()
