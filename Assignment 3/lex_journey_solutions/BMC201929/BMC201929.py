from collections import deque

class vertex:
    def __init__(self, i):
        self.i = i
        self.neighbours = []

class graph:
    def __init__(self):
        self.vertices = []

[n, e] = input().split()
n = int(n)
e = int(e)

mygraph = graph()
explored = []
for i in range(0, n):
    explored.append(0)
    v_i = vertex(i)
    mygraph.vertices.append(v_i)

[start, end] = input().split()

edges = {}

for i in range(e):
    [a,x,b] = input().split()
    a = int(a) - 1
    b = int(b) - 1
    
    mygraph.vertices[a].neighbours.append(mygraph.vertices[b])
    mygraph.vertices[b].neighbours.append(mygraph.vertices[a])
    
    edges[(a, b)] = x
    edges[(b, a)] = x


start = int(start) - 1
end = int(end) - 1
path_parent = {}

def bfs(graph, vertex):
    
    queue = deque([vertex])
    
    while queue:
        
        v = queue.popleft()
        #print(v.i)
        explored[v.i] = 1
        
        best_alphabet = 'z'
        path_parent[v.i] = -1
        
        for s in v.neighbours:
            if explored[s.i] == 0:            
                queue.append(s)
            else:
                if ord(edges[(s.i, v.i)]) <= ord(best_alphabet):
                    best_alphabet = edges[(s.i, v.i)]
                    path_parent[v.i] = s.i
                
    return 0

x = mygraph.vertices[start]
y = mygraph.vertices[end]

bfs(mygraph, y)

v = x.i
s = ''
#print(path_parent)
while(path_parent[v] != -1):
    
    s += edges[(v, path_parent[v])]
    v = path_parent[v]

print(s)
