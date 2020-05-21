import heapq
import sys

s = str(input()).split()
N = int(s[0])
M = int(s[1])

g = [[] for i in range(N)]

edges = []

for i in range(M):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    weight = int(s[2])
    edges.append([u,v,weight])
    edges.append([v,u,weight])
    g[u].append([v,weight])
    g[v].append([u,weight])


def dijkstra(src):
    distance = [sys.maxsize] * N
    distance[src] = 0

    pair = [(0,src)]

    while pair:
        (dist,u) = (heapq.heappop(pair))
        if dist > distance[u]:
            continue
        for neighbour in g[u]:
            v = neighbour[0]
            weight = neighbour[1]
            cost = dist + weight 
            if cost < distance[v] or distance[v] == sys.maxsize:
                distance[v] = cost
                heapq.heappush(pair, (cost,v))

    return distance


r = dijkstra(0)
s = dijkstra(N-1)

D = sys.maxsize
A = []
for e in edges:
    u = e[0]
    v = e[1]
    w = e[2]
    A.append((r[u],s[v],w))
    A.append((r[v],s[u],w))
    
for a in A:
    if r[N-1] < a[0]+a[1]+a[2] < D:
        D = a[0]+a[1]+a[2]
print(D)

