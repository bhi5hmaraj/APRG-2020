from queue import PriorityQueue

N, M = [int(inp) for inp in input().split()]
V = N + 1

neighborhood = [[] for t in range(V)]
for t in range(M):
    u, v, w = [int(inp) for inp in input().split()]
    neighborhood[u].append((v, w))
    neighborhood[v].append((u, w))

dist1 = [-1]*V
distN = [-1]*V


def dijkstra(source, dist):
    pq = PriorityQueue()
    got = [False]*V
    pq.put((0, source))
    dist[source] = 0
    while not pq.empty():
        (d, u) = pq.get()
        while not pq.empty() and got[u]:
            (d, u) = pq.get()
        if got[u]:
            break
        got[u] = True
        for (v, w) in neighborhood[u]:
            if not got[v]:
                if dist[v] == -1 or dist[v] > d + w:
                    dist[v] = d + w
                    pq.put((d + w, v))

dijkstra(1, dist1)
dijkstra(N, distN)
d = dist1[N]
min_yet = -1
for u in range(1, V):
    for (v, w) in neighborhood[u]:
        if dist1[u] != -1 and distN[v] != -1:
            nd = dist1[u] + w + distN[v]
            if nd != d:
                if min_yet == -1 or nd < min_yet:
                    min_yet = nd
print(min_yet)


