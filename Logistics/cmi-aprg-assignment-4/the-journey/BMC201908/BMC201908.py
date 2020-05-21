import sys
from queue import PriorityQueue

s = str(input()).split()
No_bus = int(s[0])
dest = int(s[1])

s = str(input()).split()
Time = [int(x) for x in s]

Graph = {}

for i in range(100):
    for j in range(No_bus):
        Graph [(j+1,i)] = []

for j in range(1, No_bus + 1):
    s = str(input()).split()
    node = list(map(int,s))
    
    for m in range(len(node)):
        if m != 0:
            Graph[(j,node[m])].append((j,node[m-1]))
        if m != len(node) - 1:
            Graph[(j,node[m])].append((j,node[m+1]))
            
def dijkstra(src):
    dist = {}
    q = PriorityQueue()
    parent = {src:None}
    for i in range(100):
        for j in range(No_bus):
            if i == src:
                q.put((0,j+1,i))
                dist[(j+1,i)] = 0
            else:
                dist[(j+1,i)]=sys.maxsize
    
    while not q.empty():
        d,p,u=q.get()
        for v in Graph[(p,u)]:
            cost =abs(u-v[1])*Time[p-1] + d
            if cost < dist[v]:
                dist[v] = cost
                q.put((dist[v],v[0],v[1]))
        for l in range(No_bus):
            if p==l+1:
                cost = d
            else:
                cost = d + 60
            if cost < dist[(l+1,u)]:
                dist[(l+1,u)] = cost
                q.put((dist[(l+1,u)],l+1,u))
    return(dist)
val = dijkstra(0)
temp = []
for j in range(No_bus):
    temp.append(val[(j+1,dest)])
min_cost = min(temp)
if min_cost == sys.maxsize:
    print('IMPOSSIBLE')
else:
    print(min_cost)
