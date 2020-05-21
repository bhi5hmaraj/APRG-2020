from collections import defaultdict
import heapq
graph = defaultdict(dict) 
def createedge(graph,u,v,l): 
    if graph.get(u) and graph[u].get(v):
        graph[u][v]=graph[u][v]+[l,3*l]
        graph[v][u]=graph[v][u]+[l,3*l]
    else:
        graph[u][v]=[l,3*l]
        graph[v][u]=[l,3*l]
n,m=map(int,input().split())
for i in range(m):
    k,l,w=map(int,input().split())
    createedge(graph,k,l,w)
def Mydijk(graph):
    dist={vertex:float('Inf') for vertex in graph}
    dist[1]=0
    path={}
    pq = [(0,1)]
    while len(pq)>0:
        currdist,currvert=heapq.heappop(pq)
        if currdist > dist[currvert]:
            continue
        for neighbor in graph[currvert].keys():
            distance = currdist + min(graph[currvert][neighbor])
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                path[neighbor] = currvert
                heapq.heappush(pq, (distance, neighbor))
    v,ans=n,float('Inf')
    while v!=1:
        for neighbor in graph[v]:
            for i in graph[v][neighbor]:
                a = dist[neighbor]+i+dist[n]-dist[v]
                if a<ans and a>dist[n]:
                    ans=a
        v=path[v]
    print(ans)

Mydijk(graph)
