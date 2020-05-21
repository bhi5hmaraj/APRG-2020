import math
import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict 
from queue import PriorityQueue
  

def find(parent, i): 
    if parent[i] == i: 
        return i 
    return find(parent, parent[i]) 
  
def union( parent, rank, x, y): 
    xroot = find(parent, x) 
    yroot = find(parent, y) 
  
    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot 

    else : 
        parent[yroot] = xroot 
        rank[xroot] += 1
  
def KruskalMST(N,g): 
  
    p=defaultdict(list)
    d={}
  
    e = 0 
  
    pq=PriorityQueue()
    for i in g:
        pq.put(i)
    #print(g)
  
    parent = [] 
    rank = [] 
  
    for node in range(N): 
        #print(node)
        parent.append(node) 
        rank.append(0) 
    #print(parent)
      
    while e < N -1 : 
  
        w,u,v = pq.get()
        #print(u,v,w)
        x = find(parent, u) 
        #print(x,"x")
        y = find(parent ,v) 
        #print(y,"y")
    
        if x != y: 
            e = e + 1     
            p[u].append(v)
            p[v].append(u)
            d[(u,v)]=w
            d[(v,u)]=w
            union(parent, rank, x, y)             
  
    return (p,d)
   

        
def dfs(me,mom,weight):
    p[me][0]=mom
    path[me][0]=weight
    for i in range(1,maximum+1): 
        if(p[me][i-1]!=-1):
            p[me][i] = p[p[me][i-1]][i-1]
            if(path[p[me][i-1]][i-1]!=-1):
                path[me][i] = max(path[me][i-1],path[p[me][i-1]][i-1])
    for i in h[me]:
        if(i != mom):
            depth[i] = depth[me] + 1
            dfs(i,me,d[(i,me)])
                
                
def lca(x,y):
    min = -1
    if(depth[x]>depth[y]):
        t=x
        x=y
        y=t
    a=maximum
    while(a>=0):
        if (depth[y])-(1 << a) >= depth[x]:
            min = max(min, path[y][a])
            y = p[y][a]
        a=a-1
    if(x==y):
        print( min)
        return 0
    a=maximum
    while(a>=0):
        if(p[y][a] != p[x][a]):
            min = max(min, path[y][a], path[x][a])
            y=p[y][a]
            x=p[x][a]
        a=a-1
    min = max(min,path[x][0],path[y][0])
    print(min)
    return 0
        
N,M = map(int,input().split())

g={}
for i in range(M):
    (u,v,w)=map(int,input().split())
    g[(w,u-1,v-1)]=1

#print(g)    

h=defaultdict(list)
d={}

(h,d)=KruskalMST(N,g)
#print(a)

maximum = (int)(math.log(N,2))
depth=[0 for i in range(N)]
p=[[-1 for j in range(maximum+1)] for i in range(N)]
path=[[-1 for j in range(maximum+1)] for i in range(N)] 

dfs(0,-1,-1)

Q = (int)(input())

for i in range(Q):
    x,y = map(int,input().split())
    lca(x-1,y-1)
    