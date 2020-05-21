
from collections import deque, defaultdict

class Graph:
    def __init__(self, n):
        self.vertices = n
        self.adj = defaultdict(list)
        self.weight = {}
        
    
    def add_e(self, a, l, b):
        self.adj[a].append(b)
        self.adj[b].append(a)
        self.weight[(a,b)] = l
        self.weight[(b,a)] = l
        

    def lex_short_path(self, start, end):

        
        visited = {start: 0}
        queue = deque()
        queue.append(start)
        path = {start: ""}
        while queue:
            vert = queue.popleft()
            if vert == end:
                break
            for v in self.adj[vert]:
                if v not in visited:
                    queue.append(v)
                    path[v] = path[vert] + self.weight[(vert,v)]
                    visited[v] = visited[vert] + 1
                elif visited[v] == visited[vert] + 1:
                    path[v] = min(path[v], path[vert] + self.weight[(vert,v)])
            path[vert] = ""
        return path[end]


a1, b1 = input().split()
a1, b1 = int(a1), int(b1)
graph = Graph(a1)
start, end = map(int, list(input().split()))
for i in range(b1):
    m, l, n = input().split()
    m, n = int(m), int(n)
    graph.add_e(m - 1, l, n - 1)
    
print(graph.lex_short_path(start-1, end-1))