l = input().split()
N = int(l[0])
b = int(l[1])

l2 = input().split()
(h, k) = (int(l2[0]), int(l2[1]))

l3 = ''
for i in range(b):
    l3 += input() + '\n'

grid = [(i + 1, j + 1) for i in range(N) for j in range(N)]

blacks = l3.split('\n')
blacks.pop(-1)
for i in range(b):
    blacks[i] = (int(blacks[i].split()[0]), int(blacks[i].split()[1]))

whites = [i for i in grid if i not in blacks]


class Vertex:
    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = neighbours

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.vert_name = [v.name for v in self.vertices]

    def add_vertex(self, v):
        self.vertices.append(Vertex(v, []))
        return self

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            u.neighbours.append(v)
            v.neighbours.append(u)
            self.edges.append((u,v))
            return self


g = Graph([], [])

for i in whites:
    g.add_vertex(i)

for x in g.vertices:
    for z in g.vertices:
        if (z.name == (x.name[0] + 1, x.name[1]) or z.name == (x.name[0] - 1, x.name[1]) or z.name == (x.name[0], x.name[1] + 1) or z.name == (x.name[0], x.name[1] - 1)) and z not in x.neighbours:
            g.add_edge(x, z)


def dfs(vertex, graph, visited):
    if vertex in graph.vertices:
        visited.append(vertex)
        s = [i for i in vertex.neighbours if i not in visited]
        for n in s:
            dfs(n, graph, visited)
        return visited

vert_name = [v.name for v in g.vertices]
q = vert_name.index((h,k))
vert = g.vertices[q]

p = []
dfs(vert, g, p)

z = [i for i in g.vertices if i in dfs(vert, g, p)]

if z == g.vertices:
    print('Y')
else:
    print('N')