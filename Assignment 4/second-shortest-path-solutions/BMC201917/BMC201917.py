from collections import defaultdict
import heapq
def Dijkstra(graph):
    distances={vertex:float('Inf') for vertex in graph}
    distances[1]=0
    path={}
    pq = [(0,1)]
    while len(pq)>0:
        current_distance,current_vertex=heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor in graph[current_vertex].keys():
            distance = current_distance + min(graph[current_vertex][neighbor])
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    v,d=n,float('Inf')
    while v!=1:
        for neighbor in graph[v]:
            for i in graph[v][neighbor]:
                a = distances[neighbor]+i+distances[n]-distances[v]
                if a<d and a>distances[n]:
                    d=a
        v=path[v]
    print(d)
graph = defaultdict(dict) 
def add_edge(graph,u,v,l): 
    if graph.get(u) and graph[u].get(v):
        graph[u][v]=graph[u][v]+[l,3*l]
        graph[v][u]=graph[v][u]+[l,3*l]
    else:
        graph[u][v]=[l,3*l]
        graph[v][u]=[l,3*l]
n,m=input().split()
n,m=int(n),int(m)
for i in range(m):
    k,l,w=input().split()
    k,l,w=int(k),int(l),int(w)
    add_edge(graph,k,l,w)
Dijkstra(graph)
