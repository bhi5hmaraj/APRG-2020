from collections import defaultdict
class Graph:
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def lar_gat(self, u):
        if self.graph[u] == []:
            A[u-1] = 1
            return 1
        else:
            ans1 = 0
            ans2 = 1
            childs = self.graph[u]
            for i in childs:
                if A[i-1] != 0:
                    ans1+=(A[i-1])
                else:
                    ans1+=(self.lar_gat(i))
            for i in childs:
                for j in self.graph[i]:
                    if A[j-1] != 0:
                        ans2+=(A[j-1])
                    else:
                        ans2+=(self.lar_gat(j))
            A[u-1] = max(ans1, ans2)
            return(max(ans1, ans2))
            
n = int(input())
g = Graph(n+1)
A = [0 for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    g.addEdge(u, v)
ans = 0
for i in range(1, n+1):
    if ans < g.lar_gat(i):
        ans = g.lar_gat(i)
print(ans)