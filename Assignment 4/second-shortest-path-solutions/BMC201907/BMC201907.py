import sys

from collections import defaultdict 

num_vert, num_edges = map(int, input().split())
d = {}
  
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self, node, neighbour): 
        self.graph[node].append(neighbour)
        self.graph[neighbour].append(node)
        
    def minDistance(self, dist, a): 
        inf_min = sys.maxsize
        flag = 0
        for v in a: 
            if dist[v] < inf_min:
                flag = 1
                inf_min = dist[v] 
                min_pos = v
                
        if(flag == 1):
            return min_pos 
        else:
            return -1
        
        
    def delEdge(self, node, neighbour):
        flag = 0
        
        for i in range(len(self.graph[node])):             
            if(flag == 1):
                self.graph[node][i - 1] = self.graph[node][i]
            if (self.graph[node][i] == neighbour): 
                flag = 1
                
        self.graph[node].pop(-1)

    def dijkstra(self, start, finish, n): 
        
        dist = [sys.maxsize for i in range(n)]
        dist[start] = 0
        
        L = [[] for i in range(n)]

        visited = {}
        
        a = {}
        a[start] = 1
  
        for iter in range(n): 
            vert = self.minDistance(dist, a) 
            
            if(vert == -1):
                return (0,[0])
                break
                
            visited[vert] = 1
            a.pop(vert)
            
            if(vert == finish):
                break
            
            for i in self.graph[vert]:
                if i not in visited:
                    for j in range(len(d[(i, vert)])):
                        if(dist[i] > dist[vert] + d[(i, vert)][j]):
                            dist[i] = dist[vert] + d[(i, vert)][j]
                            L[i].append(vert)
                            a[i] = 1
                    
        myQueue = []
        p = 1
        a = finish
        myQueue.append(finish)
        myQueue.append(L[a][-1])
        while(L[a][-1] != start):
            a = myQueue[p]
            myQueue.append(L[a][-1])
            p = p + 1
                       
        return (dist[finish], myQueue)
        
    def secShortest(self, n):
        inf_min = sys.maxsize
        (a, b) = self.dijkstra(0, n-1, n)
        
        for i in range(len(b) - 1):
            for j in self.graph[b[i + 1]]:
                for k in range(len(d[(j, b[i + 1])])):
                    x = a + (2*d[j, b[i + 1]][k])
                    if(x < inf_min):
                        inf_min = x
                        
            if(len(d[(b[i], b[i + 1])]) == 1):
                self.delEdge(b[i], b[i + 1])
                self.delEdge(b[i + 1], b[i])
                
                (c, q) = self.dijkstra(0, n-1, n)
                
                if(c == a):
                    p = self.secShortest(n)
                    if(p < inf_min):
                        inf_min=p
                        
                self.addEdge(b[i], b[i+1])
                self.addEdge(b[i+1], b[i])
                
            else:
                inf_min_new = sys.maxsize
                l = 0
                for j in range(len(d[(b[i], b[i + 1])])):
                    if(d[(b[i], b[i + 1])][j] < inf_min_new):
                        inf_min_new = d[(b[i], b[i + 1])][j]
                        l = j
                        
                d[(b[i], b[i + 1])].pop(l)
                (c, q)=self.dijkstra(0, n-1, n)
                
                if(c == a):
                    p = self.secShortest(n)
                    if(p < inf_min):
                        inf_min = p
                    
                d[(b[i], b[i+1])].append(inf_min_new)
                
            if(c == 0):
                continue
                
            elif(c > a and c < inf_min):
                inf_min = c
                
            if(inf_min == a+1):
                break
            
        return inf_min

myGraph = Graph()

for i in range(num_edges):
    node, neighbour, weight = map(int,input().split())
    myGraph.addEdge(node - 1, neighbour - 1)
    
    if (node - 1, neighbour - 1) not in d:
        d[(node - 1, neighbour - 1)] = [weight]
        d[(neighbour - 1, node - 1)] = [weight]
    else:
        d[(node - 1, neighbour - 1)].append(weight)
        d[(neighbour - 1, node - 1)].append(weight)

print(myGraph.secShortest(num_vert))
