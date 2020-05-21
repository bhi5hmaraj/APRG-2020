from collections import defaultdict
class Graph:
    def __init__(self,vertices): 
        self.V= vertices  
           
        self.graph = defaultdict(list)  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    def printAllPathsUtil(self, u, d, visited, path):
        visited[u]= True
        path.append(u) 
        if u == d: 
            ans.append(list(path))
        else: 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i, d, visited, path) 

        path.pop() 
        visited[u]= False

    def printAllPaths(self,s, d):
        visited =[False]*(self.V) 
        path = [] 
        self.printAllPathsUtil(s, d,visited, path)
n, m = map(int, input().split())
g = Graph(n+1)
A = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    A[u][v] = w
    A[v][u] = w
    g.addEdge(u, v)
    g.addEdge(v, u)
ans = []
(g.printAllPaths(1, n))
values_ans = []
for i in range(len(ans)):
    path_i = ans[i]
    val = 0
    for j in range(len(path_i) - 1):
        val+=(A[(path_i[j])][(path_i[j+1])])
    values_ans.append(val)
values_ans.sort()
if len(values_ans) == 1:
    print(values_ans[0])
else:
    print(values_ans[1])
