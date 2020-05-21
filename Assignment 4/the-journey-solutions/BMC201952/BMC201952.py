from collections import defaultdict
import heapq
graph = defaultdict(dict) 
def createedge(graph,u,v,l): 
    graph[u][v]=l
    graph[v][u]=l
n,k=map(int,input().split())
providertimelist=list(map(int,input().split()))
Vertices,busstoplist=[],[]
for i in range(n):
    busstoplist.append(list(map(int,input().split())))
    for j in busstoplist[i]:
        Vertices.append((i,j))
for (node1,node2) in Vertices:
    for (node3,node4) in Vertices:
        if node1==node3 and node2 < node4:
            createedge(graph,(node1,node2),(node3,node4),(node4-node2)*providertimelist[node1])
        elif node1<node3 and node2==node4:
            createedge(graph,(node1,node2),(node3,node4),60)
def Mydijk(graph,x,y):
    dist={vertex:float('Inf') for vertex in graph}
    dist[x]=0
    pq = [(0,x)]
    while len(pq)>0:
        currdist,currvert=heapq.heappop(pq)
        if currvert==y:
            break
        if currdist > dist[currvert]:
            continue
        for neighbor, weight in graph[currvert].items():
            distance = currdist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist[y] if dist[y]<float('Inf') else -1

possiblejourneycostlist=[]
for i in range(n):
    if busstoplist[i][0]==0:
        for j in range(n):
            if busstoplist[j][-1]>=k:
                if k in busstoplist[j]:
                    possiblejourneycostlist.append(Mydijk(graph,(i,0),(j,k)))
if possiblejourneycostlist:
    print(min(possiblejourneycostlist))
else:
    print('IMPOSSIBLE')
