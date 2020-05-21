import sys

from collections import defaultdict 
  
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self, u, v): 
        self.graph[u].append(v)
        
    def delEdge(self, u, v):
        c=0
        for i in range(len(self.graph[u])): 
            
            if(c==1):
                self.graph[u][i-1]=self.graph[u][i]
            if (self.graph[u][i]==v): 
                c=1
                
        self.graph[u].pop(-1)

        
    def minDistance(self, dist, a): 
        min = sys.maxsize
        c=0
        for v in a: 
            if dist[v]<min:
                c=1
                min = dist[v] 
                min_index = v
                
        if(c==1):
            return min_index 
        else:
            return -1
    
    def shortest(self, src, end, n): 
        
        dist = [sys.maxsize] * n 
        L = [[] for i in range(n)]
        dist[src] = 0
        visited = {}
        a={}
        a[src]=1
  
        for cout in range(n): 
            u = self.minDistance(dist, a) 
            if(u==-1):
                return (0,[0])
                break
            visited[u] = 1
            a.pop(u)
            if(u==end):
                break
            
            for i in self.graph[u]:
                if i not in visited:
                    for j in range(len(d[(i,u)])):
                        if(dist[i] > dist[u] + d[(i,u)][j]):
                            dist[i] = dist[u] + d[(i,u)][j]
                            L[i].append(u)
                            a[i]=1
                    
        queue=[]
        c=1
        a=end
        queue.append(end)
        queue.append(L[a][-1])
        while(L[a][-1]!=src):
            a=queue[c]
            queue.append(L[a][-1])
            c=c+1
            
        #print(dist[end],queue)           
        return (dist[end],queue)
        
    def secshort(self,n):
        min=sys.maxsize
        (a,b) = self.shortest(0,n-1,n)
        for i in range(len(b)-1):
            for j in self.graph[b[i+1]]:
                for k in range(len(d[(j,b[i+1])])):
                    x = a + (2*d[j,b[i+1]][k])
                    if(x<min):
                        min = x
            if(len(d[(b[i],b[i+1])])==1):
                self.delEdge(b[i],b[i+1])
                self.delEdge(b[i+1],b[i])
                (c,q)=self.shortest(0,n-1,n)
                if(c==a):
                    p = self.secshort(n)
                    if(p<min):
                        min=p
                self.addEdge(b[i],b[i+1])
                self.addEdge(b[i+1],b[i])
                
            else:
                min1=sys.maxsize
                l=0
                for j in range(len(d[(b[i],b[i+1])])):
                    if(d[(b[i],b[i+1])][j]<min1):
                        min1=d[(b[i],b[i+1])][j]
                        l=j
                        
                d[(b[i],b[i+1])].pop(l)
                (c,q)=self.shortest(0,n-1,n)
                if(c==a):
                    p = self.secshort(n)
                    if(p<min):
                        min=p
                    
                d[(b[i],b[i+1])].append(min1)
                
            if(c==0):
                continue
            elif(c>a and c<min):
                min=c
                
            if(min==a+1):
                break
            
        return min
g = Graph()

n,m = map(int,input().split())

d={}
for i in range(m):
    u,v,w = map(int,input().split())
    g.addEdge(u-1,v-1)
    g.addEdge(v-1,u-1)
    if (u-1,v-1) not in d:
        d[(u-1,v-1)]=[w]
        d[(v-1,u-1)]=[w]
    else:
        d[(u-1,v-1)].append(w)
        d[(v-1,u-1)].append(w)

h = g.secshort(n)

print(h)
