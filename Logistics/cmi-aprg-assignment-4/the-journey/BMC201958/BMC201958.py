import sys
inf=sys.maxsize
from queue import PriorityQueue
q=PriorityQueue()
cost = {}
adj = {}
minroute = {}
srclist = []
dstlist = []
n,m = map(int,input().split())
l = list(map(int,input().split()))
vertices = [[] for i in range(n)]
for i in range(n):
    l1 = list(map(int,input().split()))
    if l1.count(0) > 0:
        srclist.append((i+1,0))
    if l1.count(m) >0:
        dstlist.append((i+1,m))
    for j in range(len(l1)):
        vertices[i].append((i+1,l1[j]))
#print(vertices)
for i in range(n):
    for j in vertices[i]:
        adj[j]=[]

edgelist= []
for i in range(n):
    l2 = vertices[i]
    for j in range(len(l2)-1):
        adj[l2[j]].append(l2[j+1])
        adj[l2[j+1]].append(l2[j])
        edgelist.append([l2[j],l2[j+1],l[i]*(l2[j+1][1]-l2[j][1])])
l3 = sum(vertices,[])
for i in l3:
    for j in l3:
        if j != i and i[1]==j[1]:
            adj[i].append(j)
for i in edgelist:
    cost[(i[0],i[1])] = i[2]
    cost[(i[1],i[0])] = i[2]
for i in l3:
    for j in l3:
        if j != i and i[1]==j[1]:
           
            cost[(i,j)] = 60
            cost[(j,i)] = 60
           
#print(l3)
def mincost(adj,src,dst):
    minroute = {}
    for i in l3:
        if i == src:
            q.put((0, i))
            minroute[i] = [0,0]
        else:
            minroute[i] = [0,inf]
    while not q.empty():
        w,u=q.get()
        for v in adj[u]:
            a = cost[(u,v)] + w
            if a < minroute[v][1]:
                minroute[v][1] = a
                minroute[v][0] = minroute[u][0] + 1

                q.put((minroute[v][1],v))
            elif a == minroute[v][1] and minroute[v][0] > minroute[u][0] + 1:
                minroute[v][0] = minroute[u][0] + 1
    return(minroute[dst][1])
if len(srclist) == 0:
    print("IMPOSSIBLE")

elif len(dstlist) == 0:
    print("IMPOSSIBLE")

else:
    a=inf
    for i in srclist:
        for j in dstlist:
            a=min([mincost(adj,i,j),a])
    if a==inf:
        print("IMPOSSIBLE")
    else:
        print(a)

