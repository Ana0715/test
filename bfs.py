from collections import deque

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
        self._root = root

    def dfs(self, graph, vertex, visited_dfs=None):
        if visited_dfs == None:
            self.visited_dfs = set()

        if vertex not in self.visited_dfs:
            print (vertex, end='\n')
            self.visited_dfs.add(vertex)

            for neighbor in graph[vertex]:
                self.dfs(graph, neighbor, self.visited_dfs)

    def bfs(self, graph, vertex_start):
        self.visited_bfs = set()
        self.queue = deque()

        self.queue.append(vertex_start)
        self.visited_bfs.add(vertex_start)

        while self.queue:
            vertex = self.queue.popleft()
            print(vertex, end='\n')

            for neighbor in graph[vertex]:
                if neighbor not in self.visited_bfs:
                    self.queue.append(neighbor)
                    self.visited_bfs.add(neighbor)
        



g_test = Graph(0)

graph_test = {
    0: [1,2,3],
    1: [0,2],
    2: [0,1,4],
    3: [0],
    4: [2]
}
print('dfs:')
g_test.dfs(graph_test, 0)
print('dfs 2:')
g_test.dfs(graph_test, 0)
print('bfs:')
g_test.bfs(graph_test, 0)
print('bfs 2:')
g_test.bfs(graph_test, 0)
print(end='\n')


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

some_g1 = Graph(a1)
print('dfs:')
some_g1.dfs(graph1, a1)
print('bfs:')
some_g1.bfs(graph1, a1)
print(end='\n')


#2
a2 = Node('a')
b2 = Node('b')
c2 = Node('c')

a2.point_to(b2)
b2.point_to(c2)

graph2 = {}
a2.make_dict(graph2, a2, b2, c2)

some_g2 = Graph(a2)
print('dfs:')
some_g2.dfs(graph2, a2)
print('bfs:')
some_g2.bfs(graph2, a2)
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

some_g3 = Graph(a3)
print('dfs:')
some_g3.dfs(graph3, a3)
print('bfs:')
some_g3.bfs(graph3, a3)
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

some_g4 = Graph(a4)
print('dfs:')
some_g4.dfs(graph4, a4)
print('bfs:')
some_g4.bfs(graph4, a4)
print(end='\n')