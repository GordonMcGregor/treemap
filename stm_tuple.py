from Tree import Tree as t
import Tree
from Tree import make_tree
from TreeMap import TreeMap

short_map = (((1, 2), 3, ((1, 1), 4, ((32,34,1,2), 1, 1, (1, 2, 4, 5,(2,2,(2,(2,(1,1,1,1,(3,2,12),1)))))))))

x=make_tree(short_map, TreeType = Tree.HueTree)
TreeMap(x).show()
