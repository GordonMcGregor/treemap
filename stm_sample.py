from Tree import HueTree as t
from Tree import make_tree
from TreeMap import TreeMap

a = t()
b = t(a)
e = t(b, 1, 'e')
f = t(b, 2, 'f')

c = t(a, 3, 'c')

d = t(a)
g = t(d)
j = t(g, 1, 'j')
k = t(g, 1, 'k')
h = t(d, 4, 'h')
l = t(d)
lprime = t(l, 1, 'l')
m = t(l, 1, 'm')
n = t(l, 1, 'n')
o = t(l, 1, 'o')


TreeMap(a).show()
