import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
import heapq

def find(parent,i):
    if parent[i]==i:
        return(i)
    return find(parent,parent[i])

def union(parent,rank,x,y):
    xroot=find(parent,x)
    yroot=find(parent,y)
    if rank[xroot]<rank[yroot]: 
        parent[xroot] =yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] =xroot
    else:
        parent[yroot]=xroot
        rank[xroot] = rank[xroot] + 1
        
def kruskal(graph):
    i=0
    e=0
    for node in range(n):
        parent.append(node) 
    while e < n -1:
        u,v,w = graph[i]
        i=i+1
        x = u
        while x!= parent[x]:
            x=parent[x]
        y =v
        while y != parent[y]:
            y=parent[y]
        if x!=  y:
            e = e + 1
            if len(Qlist[x])<len(Qlist[y]):
                parent[x]=y
            else:
                parent[y]=x
            if parent[x]==y:
                for a in Qlist[x]:
                    if a in Qlist[y]:
                        ans[a]=w
                        Qlist[y].remove(a)
                    else:
                        Qlist[y].add(a)
            else:
                for a in Qlist[y]:
                    if a in Qlist[x]:
                        ans[a]=w
                        Qlist[x].remove(a)
                    else:
                        Qlist[x].add(a)



lss=list(map(int,input().split()))
n=lss[0]
m=lss[1]
Graph= []
for jj in range(m):
    ls=list(map(int,input().split()))
    a=ls[0]-1
    b=ls[1]-1
    w=ls[2]
    Graph.append([a,b,w])
    Graph.append([b,a,w])
Graph =  sorted(Graph,key=lambda item: item[2])
Q=int(input())
Qlist=[set([]) for ilt in range(n)]
for ik in range(Q):
    lpp=list(map(int,input().split()))
    aa=lpp[0]-1
    bb=lpp[1]-1
    Qlist[aa].add(ik)
    Qlist[bb].add(ik)
    
ans=[0 for ittt in range(Q)]
parent =[]
kruskal(Graph)
for jkl in range(Q):
    print(ans[jkl])
     




