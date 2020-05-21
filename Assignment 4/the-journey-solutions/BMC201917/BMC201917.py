from collections import defaultdict
import heapq
def Dijkstra(graph,x,y):
    distances={vertex:float('Inf') for vertex in graph}
    distances[x]=0
    pq = [(0,x)]
    while len(pq)>0:
        current_distance,current_vertex=heapq.heappop(pq)
        if current_vertex==y:
            break
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances[y] if distances[y]<float('Inf') else -1
graph = defaultdict(dict) 
def add_edge(graph,u,v,l): 
    graph[u][v]=l
    graph[v][u]=l
n,k=input().split()
n,k=int(n),int(k)
t=list(map(int,input().split()))
V,l=[],[]
for i in range(n):
    l.append(list(map(int,input().split())))
    for j in l[i]:
        V.append((i,j))
for (p,q) in V:
    for (r,s) in V:
        if p==r and q < s:
            add_edge(graph,(p,q),(r,s),(s-q)*t[p])
        elif p<r and q==s:
            add_edge(graph,(p,q),(r,s),60)
D=[]
for i in range(n):
    if l[i][0]==0:
        for j in range(n):
            if l[j][-1]>=k:
                if k in l[j]:
                    D.append(Dijkstra(graph,(i,0),(j,k)))
if D:
    print(min(D))
else:
    print('IMPOSSIBLE')
