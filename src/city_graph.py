from math import sqrt


class City(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return 'City(name=%s, x=%s, y=%s)' % (self.name,self.x, self.y)


class Graph(object):
    def __init__(self, weights):
        self.weights = weights

    def neighbors(self, node):
        entry = self.weights.get(node)
        if entry:
            return entry.keys()
        else:
            return []

    def cost(self, node_a, node_b):
        return self.weights[node_a][node_b]


m = City('Munich', 692094, 5334544)
s = City('Stuttgart', 513440, 5402555)
a = City('Augsburg', 640547, 5359226)
ing = City('Ingolstadt', 678246, 5404342)
ul = City('Ulm', 573098, 5361351)
n = City('Nuernberg', 650508, 5479789)
hd = City('Heidelberg', 476233, 5471836)
hn = City('Heidenheim', 515380, 5443340)
cr = City('Crailsheim', 577568, 5442868)
ka = City('Karlsruhe', 456388, 5428393)

m2ing = 80.1
ing2m = 81.2

m2a = 79.9
a2m = 79.2

a2ul = 86.4
ul2a = 87.9

ul2cr = 113.0
cr2ul = 112.0

ul2s = 92.0
s2ul = 92.5

s2ka = 79.0
ka2s = 78.9

s2hn = 53.5
hn2s = 53.3

ka2hd = 52.9
hd2ka = 53.7

hd2hn = 67.9
hn2hd = 66.5

hn2cr = 75.4
cr2hn = 74.5

cr2n = 96.6
n2cr = 97.9

n2ing = 94.3
ing2n = 94.4

city_graph = Graph({m: {a: m2a, ing: m2ing},
                    a: {m: a2m, ul: a2ul},
                    ing: {m: ing2m, n: ing2n},
                    ul: {a: ul2a, s: ul2s, cr: ul2cr},
                    s: {ul: s2ul, hn: s2hn, ka: s2ka},
                    n: {cr: n2cr, ing: n2ing, s: hn2s},
                    cr: {hn: cr2hn, n: cr2n, ul: cr2ul},
                    hn: {cr: hn2cr, hd: hn2hd, s: hn2s},
                    ka: {s: ka2s, hd: ka2hd},
                    hd: {ka: hd2ka, hn: hd2hn}})


class Heuristic(object):
    def __init__(self, goal):
        self.goal = goal

    def __call__(self, node):
        return sqrt((self.goal.x - node.x)**2 + (self.goal.y - node.y)**2)