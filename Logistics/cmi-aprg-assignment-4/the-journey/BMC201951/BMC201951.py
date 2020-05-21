import sys

from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v): 
        self.graph[u].append(v)
        
        
    def minDistance(self, dist, visited, z): 
        c=0
        min = sys.maxsize
        for v in range(len(z)): 
            if z[v] not in visited: 
                if dist[z[v][0]][z[v][1]]<min:
                    min = dist[z[v][0]][z[v][1]] 
                    min_index = z[v]
                    c=1
          
        if(c==1):
            return min_index      
        else:
            return (-1,-1)
      
    def shortest(self, src, end, sum,N): 
        
        z=[]
        dist = [[sys.maxsize for i in range(100)] for j in range(N)] 
        dist[src[0]][src[1]]=0
        z.append(src)
        visited = {}
  
        for cout in range(sum): 
            u = self.minDistance(dist, visited, z) 
            visited[u] = 1
            if(u==(-1,-1)):
                return -1
            if(u==end):
                break
            for i in self.graph[u]:
                if i not in visited:
                    if dist[i[0]][i[1]] > dist[u[0]][u[1]] + d[(i,u)]:
                        dist[i[0]][i[1]] = dist[u[0]][u[1]] + d[(i,u)]
                        z.append(i)
        return dist[end[0]][end[1]]
        
        
g=Graph()

N,l = map(int,input().split())

T = list(map(int,input().split()))

d={}
O=[]
M=[]
S=[]
sum=0
m=0
for i in range(N):
    P= list(map(int,input().split()))
    S.append(P)
    sum=sum+len(S[i])
    if(S[i][0]==0):
        O.append(i)
    if l in S[i]:
        M.append(i)
    for j in range(len(S[i])-1):
        g.addEdge((i,S[i][j]),(i,S[i][j+1]))
        g.addEdge((i,S[i][j+1]),(i,S[i][j]))
        d[((i,S[i][j]),(i,S[i][j+1]))] = (S[i][j+1]-S[i][j])*T[i]
        d[((i,S[i][j+1]),(i,S[i][j]))] = (S[i][j+1]-S[i][j])*T[i]
        
for i in range(N):
    for j in range(i+1,N):
        for k in range(len(S[i])):
            if S[i][k] in S[j] and S[i][k]!=0:
                g.addEdge((i,S[i][k]),(j,S[i][k]))
                g.addEdge((j,S[i][k]),(i,S[i][k]))
                d[(i,S[i][k]),(j,S[i][k])]=60
                d[(j,S[i][k]),(i,S[i][k])]=60

min=10000
k=0
for i in range(len(O)):
    for j in range(len(M)):
        a=g.shortest((O[i],0),(M[j],l),sum,N)
        if(a==-1):
            continue
        elif(a<min):
            min=a
            k=1

if(k==1):            
    print(min)
else:
    print("IMPOSSIBLE")
