import sys

from collections import defaultdict 
  
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self, x, y): 
        self.graph[x].append(y)
        
    def delEdge(self, x, y):
        f=0
        for i in range(len(self.graph[x])): 
            
            if(f==1):
                self.graph[x][i-1]=self.graph[x][i]
            if (self.graph[x][i]==y): 
                f=1
                
        self.graph[x].pop(-1)

        
    def minDistance(self, dist, a): 
        m = sys.maxsize
        f=0
        for y in a: 
            if dist[y]<m:
                f=1
                m = dist[y] 
                m_index = y
                
        if(f==1):
            return m_index 
        else:
            return -1
    
    def shortest(self, s, end, n): 
        
        dist = [sys.maxsize] * n 
        L = [[] for i in range(n)]
        dist[s] = 0
        visited = {}
        a={}
        a[s]=1
  
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
        f=1
        a=end
        queue.append(end)
        queue.append(L[a][-1])
        while(L[a][-1]!=s):
            a=queue[f]
            queue.append(L[a][-1])
            f=f+1
                  
        return (dist[end],queue)
        
    def secondshort(self,n):
        m=sys.maxsize
        (x,y) = self.shortest(0,n-1,n)
        for i in range(len(y)-1):
            for j in self.graph[y[i+1]]:
                for k in range(len(d[(j,y[i+1])])):
                    u = x + (2*d[j,y[i+1]][k])
                    if(u<m):
                        m = u
            if(len(d[(y[i],y[i+1])])==1):
                self.delEdge(y[i],y[i+1])
                self.delEdge(y[i+1],y[i])
                (z,q)=self.shortest(0,n-1,n)
                if(z==x):
                    p = self.secondshort(n)
                    if(p<m):
                        m=p
                self.addEdge(y[i],y[i+1])
                self.addEdge(y[i+1],y[i])
                
            else:
                M=sys.maxsize
                l=0
                for j in range(len(d[(y[i],y[i+1])])):
                    if(d[(y[i],y[i+1])][j]<M):
                        M=d[(y[i],y[i+1])][j]
                        l=j
                        
                d[(y[i],y[i+1])].pop(l)
                (z,q)=self.shortest(0,n-1,n)
                if(z==x):
                    p = self.secshort(n)
                    if(p<m):
                        m=p
                    
                d[(y[i],y[i+1])].append(M)
                
            if(z==0):
                continue
            elif(z>x and z<m):
                m=z
                
            if(m==x+1):
                break
            
        return m
G = Graph()

n,m = map(int,input().split())

d={}
for i in range(m):
    x,y,z = map(int,input().split())
    G.addEdge(x-1,y-1)
    G.addEdge(y-1,x-1)
    if (x-1,y-1) not in d:
        d[(x-1,y-1)]=[z]
        d[(y-1,x-1)]=[z]
    else:
        d[(x-1,y-1)].append(z)
        d[(y-1,x-1)].append(z)

g = G.secondshort(n)

print(g)
