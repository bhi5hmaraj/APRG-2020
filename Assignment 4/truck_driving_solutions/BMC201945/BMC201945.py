import sys
sys.setrecursionlimit(10**6)
import math
from queue import PriorityQueue
l=list(map(int,input().split()))
a=l[0]
b=l[1]
z=[]
adj_list={}
for i in range (l[0]):
  adj_list[i]=[]
for i in range (l[1]):
  x=list(map(int,input().split()))
  z.append((x[2],x[0],x[1]))
x1=[]
a1=int(input())
for i in range (a1):
  y1= list(map(int,input().split()))
  x1.append(y1) 
def findset(x,set1):
  if set1[x]==x:
    return x
  else:
    return findset(set1[x],set1)
def unionset(set1,rank,x1,y1):
   if rank[x1]<rank[y1]:
     set1[x1]=y1
   elif rank[x1]>rank[y1]:
     set1[y1]=x1 
   else:
     set1[y1]=x1
     rank[x1]+=1
def mst(z):
  e=0
  parent=[]
  rank=[]
  q=PriorityQueue()
  for i in z:
    q.put(i)
  for i in range (l[0]+1):
    parent.append(i)
    rank.append(1)  
  while e<l[0]-1:
    p=q.get()
    w=p[0]
    u=p[1]
    v=p[2]
    x=findset(u,parent)
    y=findset(v,parent)
    if x != y:
      e=e+1
      adj_list[u-1].append((v-1,w))
      adj_list[v-1].append((u-1,w))  
      unionset(parent,rank,x,y)
  return (adj_list)   
t=mst(z)
parent=[[] for i in range (l[0])]
path=[[] for i in range (l[0])]
d=[0 for i in range (l[0])]
maxl = (int)(math.log(l[0],2))
def dfs(u,p,w):
    parent[u].append(p)
    path[u].append(w)
    for i in range(1,maxl+1):
        parent[u].append(-1)
        path[u].append(-1)
        if(parent[u][i-1]!=-1):
            parent[u][i] = parent[parent[u][i-1]][i-1]
            path[u][i]=max(path[u][i-1],path[parent[u][i-1]][i-1])
    for i in t[u]:
        if(i[0] != p):
            d[i[0]] = d[u] + 1
            dfs(i[0],u,i[1])
dfs(0,-1,-0)
def lca (x,y):
    a=-1
    p=x
    q=y
    if d[x]<d[y]:
        p=y
        q=x
    b=maxl    
    while b>=0:
        if d[p]-(1<<b)>=d[q]:
            a=max(a,path[p][b])
            p=parent[p][b]
        b -=1
    if p==q:
        return a
    c=maxl
    while c>=0:
        if parent[p][c] != parent[q][c]:
            a=max(a,path[p][c],path[q][c])
            p=parent[p][c]
            q=parent[q][c]
        c -=1
    a=max(a,path[p][0],path[q][0])
    return a
for i in range (len(x1)):
    print(lca(x1[i][0]-1,x1[i][1]-1))