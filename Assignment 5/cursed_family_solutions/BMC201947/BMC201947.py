#import collections
#import heapq

    
from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v): 
        #u is the father of v
        self.graph[u].append(v) 
    
    #def root(self,n):
    #    for member in range(n):
    #        if member not in 
    #Visited = {}
    def gather(self,parent,Visited):
        #Visited = {}
        if parent not in self.graph :
            Visited[parent] = 1
            return(1)
        else:
            c1 = 0
            c2 = 1
            for child in self.graph[parent]:
                if child not in Visited:
                    Visited[child] = self.gather(child,Visited)
                c1 = c1 + Visited[child]
                for grandchild in self.graph[child] :
                    if grandchild not in Visited:
                        Visited[grandchild] = self.gather(grandchild ,Visited) 
                    c2 = c2 + Visited[grandchild]
            return(max(c1,c2))

g=Graph()
Visited = {}
n = int(input())
dad = []
for i in range(n):
    dad.append(-1)
for i in range(n-1):
    u,v = map(int,input().split())
    g.addEdge(u-1,v-1)
    dad[v-1] = u-1 
    #g.addEdge(b-1,a-1)

head = dad.index(-1)
ans = g.gather(head,Visited)
print(ans)


