class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'
    
    def make_dict(self, some_dictionary, *args):
        for arg in args:
            some_dictionary[arg] = arg.outbound
        return some_dictionary
  
class Graph:
    def __init__(self, root):
        self.root = root
        self.visited = []

    def dfs(self, graph, vertex):
        if vertex not in self.visited:
            print(vertex, end=' ')
            self.visited.append(vertex)
            for neighbor in graph[vertex]:
                self.dfs(graph, neighbor)


#1
a1 = Node('a')
b1 = Node('b')
c1 = Node('c')
d1 = Node('d')

a1.point_to(b1)
b1.point_to(c1)
c1.point_to(d1)
d1.point_to(a1)
b1.point_to(d1)


graph1 = {}
a1.make_dict(graph1, a1, b1, c1, d1)

# graph1 = {
#     a1: a1.outbound,
#     b1: b1.outbound,
#     c1: c1.outbound,
#     d1: d1.outbound
# }

some_g1 = Graph(a1)
some_g1.dfs(graph1, a1)
print(end='\n')


#2
a2 = Node('a')
b2 = Node('b')
c2 = Node('c')

a2.point_to(b2)
b2.point_to(c2)

graph2 = {}
a2.make_dict(graph2, a2, b2, c2)

# graph2 = {
#     a2: a2.outbound,
#     b2: b2.outbound,
#     c2: c2.outbound
# }

some_g2 = Graph(a2)
some_g2.dfs(graph2, a2)
print(end='\n')



#3
a3 = Node('a')
b3 = Node('b')
c3 = Node('c')
d3 = Node('d')
e3 = Node('e')
f3 = Node('f')

a3.point_to(b3)
b3.point_to(c3)
c3.point_to(d3)
d3.point_to(a3)
b3.point_to(d3)
b3.point_to(f3)
c3.point_to(e3)

graph3 = {}
a3.make_dict(graph3, a3, b3, c3, d3, e3, f3)

# graph3 = {
#     a3: a3.outbound,
#     b3: b3.outbound,
#     c3: c3.outbound,
#     d3: d3.outbound,
#     e3: e3.outbound,
#     f3: f3.outbound
# }

some_g3 = Graph(a3)
some_g3.dfs(graph3, a3)
print(end='\n')


#4
a4 = Node('a')
b4 = Node('b')
c4 = Node('c')
d4 = Node('d')
e4 = Node('e')
f4 = Node('f')
g4 = Node('g')
h4 = Node('h')
i4 = Node('i')
k4 = Node('k')

a4.point_to(b4)
b4.point_to(c4)
c4.point_to(d4)
d4.point_to(a4)
b4.point_to(d4)
a4.point_to(e4)
e4.point_to(f4)
e4.point_to(g4)
f4.point_to(i4)
f4.point_to(h4)
g4.point_to(k4)

graph4 = {}
a4.make_dict(graph4, a4, b4, c4, d4, e4, f4, g4, h4, i4, k4)

# graph4 = {
#     a4: a4.outbound,
#     b4: b4.outbound,
#     c4: c4.outbound,
#     d4: d4.outbound,
#     e4: e4.outbound,
#     f4: f4.outbound,
#     g4: g4.outbound,
#     h4: h4.outbound,
#     i4: i4.outbound,
#     k4: k4.outbound
# }

some_g4 = Graph(a4)
some_g4.dfs(graph4, a4)
print(end='\n')