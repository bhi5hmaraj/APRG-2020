from heapq import *
INF = 1<<50

n, m = [int(x) for x in input().split(' ')]
g = [[] for i in range(n)]

for _ in range(m):
    u, v, w = [int(x) for x in input().split(' ')]
    g[u - 1].append((w, v - 1))
    g[v - 1].append((w, u - 1))

dx = [INF]*n
vis = [0]*n
dx[0] = 0
q = [(0, 0)]
while q:
    v = heappop(q)[1]
    if vis[v]:
        continue
    vis[v] = 1
    for (w, u) in g[v]:
        if not vis[u]:
            if dx[u] > dx[v] + w:
                dx[u] = dx[v] + w
                heappush(q, (dx[u], u))

dy = [INF]*n
vis = [0]*n
dy[n - 1] = 0
q = [(0, n - 1)]
while q:
    v = heappop(q)[1]
    if vis[v]:
        continue
    vis[v] = 1
    for (w, u) in g[v]:
        if not vis[u]:
            if dy[u] > dy[v] + w:
                dy[u] = dy[v] + w
                heappush(q, (dy[u], u))

min_dist = dx[n - 1]
ans = INF
for v in range(n):
    for (w, u) in g[v]:
        tmp = dx[v] + dy[u] + w
        if tmp > min_dist:
            ans = min(ans, tmp)

print(ans)
