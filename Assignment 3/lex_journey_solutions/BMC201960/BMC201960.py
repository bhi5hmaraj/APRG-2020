l1 = input().split()
N = int(l1[0])
E = int(l1[1])

l2 = input().split()
X = int(l2[0])
Y = int(l2[1])

l = []
for i in range(E):
    l.append(tuple(input().split()))

e = [(int(x), int(y), z) for (x, z, y) in l]

class Vertex:
    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = neighbours

class Graph:
    def __init__(self, vertices, edges, edge_rank):
        self.vertices = vertices
        self.edges = edges
        self.edge_rank = edge_rank
        self.vert_name = [v.name for v in self.vertices]

    def add_vertex(self, v):
        self.vertices.append(Vertex(v, []))
        return self

    def add_edge(self, u, v, c):
        if u in self.vertices and v in self.vertices:
            u.neighbours.append(v)
            v.neighbours.append(u)
            self.edges.append((u.name, v.name))
            self.edge_rank.append(c)
            return self

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        else:
            paths = []
            for node in start.neighbours:
                if node not in path:
                    newpaths = self.find_all_paths(node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
        return paths

v = [i + 1 for i in range(N)]

grp = Graph([], [], [])

for i in v:
    grp.add_vertex(i)

for (x, y, z) in e:
    grp.add_edge(grp.vertices[x - 1], grp.vertices[y - 1], z)

p = grp.find_all_paths(grp.vertices[X - 1], grp.vertices[Y -1])

o = []
for i in range(len(p)):
    k = []
    for j in range(len(p[i])):
        k.append(p[i][j].name)
    o.append(k)

lengths = [len(i) for i in p]
min_length = min(lengths)

q = []
for i in o:
    if len(i) == min_length:
        q.append(i)

a = []
b = []
for i in range(len(q)):
    z = ''
    for j in range(len(q[0]) - 1):
        if (q[i][j], q[i][j + 1]) in grp.edges:
            z += (grp.edge_rank[grp.edges.index((q[i][j], q[i][j + 1]))])
        else:
            z += (grp.edge_rank[grp.edges.index((q[i][j + 1], q[i][j]))])
    b.append(z)
    t = ''.join(sorted(z))
    a.append(t)

r = a
a.sort()

print(b[r.index(a[0])])