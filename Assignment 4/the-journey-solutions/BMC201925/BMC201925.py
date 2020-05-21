from heapq import *
INF = 1<<50
TTIME = 60
NV = 100

n, k = [int(x) for x in input().split(' ')]
t = [int(x) for x in input().split(' ')]
g = [[] for i in range(NV)]

for i in range(n):
    arr = [int(x) for x in input().split(' ')]
    m = len(arr)
    for u in range(m):
        for v in range(u + 1, m):
            g[arr[u]].append(((arr[v] - arr[u])*t[i], arr[v]))
            g[arr[v]].append(((arr[v] - arr[u])*t[i], arr[u]))

# for i in range(NV):
#     if len(g[i]) > 0:
#         for j in g[i]:
#             print(i, j[1], j[0])

d = [INF]*NV
vis = [0]*NV
d[0] = 0
q = [(0, 0)]
while q:
    v = heappop(q)[1]
    if vis[v]:
        continue
    vis[v] = 1
    for (w, u) in g[v]:
        if not vis[u]:
            if d[u] > d[v] + w + TTIME:
                d[u] = d[v] + w + TTIME
                heappush(q, (d[u], u))

if d[k] == INF:
    print("IMPOSSIBLE")
elif k == 0:
    print(0)
else:
    print(d[k] -  60)

