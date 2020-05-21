import heapq
[n, m] = input().split()
n = int(n)
m = int(m)
graph = []

for i in range(n):
    graph.append([])

def printgraph():
    for i in range(n):
        print(graph[i])

for i in range(m):
    [p, q, w] = input().split()
    p = int(p)
    q = int(q)
    w = int(w)
    graph[p-1].append((q-1, w))
    graph[q-1].append((p-1, w))

def dijkstra(k):
    dist = [10000000000001] * n
    dist[k] = 0
    h = []
    heapq.heappush(h, (0, k))
    while h != []:
        (x, y) = heapq.heappop(h)
        for v in graph[y]:
            if dist[y] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[y] + v[1]
                heapq.heappush(h, (dist[v[0]], v[0]))      
    return dist

dist1 = dijkstra(0)
dist2 = dijkstra(n-1)

def secondshortestpath(dist1, dist2, src, dest):
    path = 10000000000001
    bestpath = dist1[n-1]
    for a in range(n):
        for b in graph[a]:
        #if graph[a][b] > 0:
            if dist1[a] + b[1] + dist2[b[0]] > bestpath and dist1[a] + b[1] + dist2[b[0]] < path:
                path = dist1[a] + b[1] + dist2[b[0]]
                

    return path

m = secondshortestpath(dist1, dist2, 0, n-1)
print(m)
