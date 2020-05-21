from collections import defaultdict as d
from sys import maxsize as max

class my_graph:
    def __init__(self):
        self.gr = d(list)
        
    def add_edge(self,x,w): 
        self.gr[w].append(x)
    
    @staticmethod    
    def min_dist(dist, vis, l): 
        s = 0
        min = max
        for v in range(len(l)): 
            if not(l[v] in vis): 
                if min > dist[l[v][0]][l[v][1]] :
                    min = dist[l[v][0]][l[v][1]] 
                    min_index = l[v]
                    s = 1
          
        if s == 1 :
            return(min_index)    
        else:
            return (-1,-1)
      
    def shortest(self, abc, end, sum,N): 
        z=[]
        dist = [[max for i in range(100)] for j in range(N)] 
        dist[abc[0]][abc[1]]=0
        z.append(abc)
        vis = {}
  
        for i in range(sum): 
            u = my_graph.min_dist(dist, vis, z) 
            vis[u] = 1
            if u == (-1,-1):
                return -1
            if u == end:
                break
            for j in self.gr[u]:
                if j not in vis:
                    if dist[u[0]][u[1]] + d[(j,u)] < dist[j[0]][j[1]]:
                            dist[j[0]][j[1]] = dist[u[0]][u[1]] + d[(j,u)]
                            z.append(j)        
        return dist[end[0]][end[1]]
        
        
g = my_graph()
N,stop = map(int,input().split())
T = list(map(int,input().split()))

d = {}
B = []
C = []
D = []
sum = 0
m=0
for p in range(N):
    P= list(map(int,input().split()))
    D.append(P)
    sum = sum+len(D[p])
    if D[p][0] == 0:
        B.append(p)
    if stop in D[p]:
        C.append(p)
    for j in range(len(D[p])-1):
        d[((p,D[p][j]),(p,D[p][j+1]))] = (D[p][j+1]-D[p][j])*T[p]
        d[((p,D[p][j+1]),(p,D[p][j]))] = (D[p][j+1]-D[p][j])*T[p]        
        g.add_edge((p,D[p][j+1]),(p,D[p][j]))
        g.add_edge((p,D[p][j]),(p,D[p][j+1]))

        
for p in range(N):
    for j in range(p+1,N):
        for k in range(len(D[p])):
            if D[p][k] in D[j] and D[p][k]:
                d[(p,D[p][k]),(j,D[p][k])] = 60
                d[(j,D[p][k]),(p,D[p][k])] = 60                
                g.add_edge((j,D[p][k]),(p,D[p][k]))
                g.add_edge((p,D[p][k]),(j,D[p][k]))


min = 9999
k = 0
for p in range(len(B)):
    for j in range(len(C)):
        a = g.shortest((B[p],0),(C[j],stop),sum,N)
        if a == -1:continue
        elif a < min:
            min=a
            k=1

if k == 1:print(min)
else:print("IMPOSSIBLE")
