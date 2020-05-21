from queue import PriorityQueue

N, k = [int(inp) for inp in input().split()]
T = [int(inp) for inp in input().split()]
B = 100
V = B*N + 2
start = V - 2
finish = V - 1
neighborhood = [[] for t in range(V)]
for i in range(N):
    neighborhood[start].append((B * i, 0))
    neighborhood[B * i].append((start, 0))
    neighborhood[finish].append((B * i + k, 0))
    neighborhood[B * i + k].append((finish, 0))

S = [[] for s in range(N)]
for i in range(N):
    S[i] = [int(inp) for inp in input().split()]
    for t in range(len(S[i]) - 1):
        u = S[i][t] + B * i
        v = S[i][t + 1] + B * i
        w = (v - u) * T[i]
        neighborhood[u].append((v, w))
        neighborhood[v].append((u, w))

for i in range(N):
    for j in range(i+1, N):
        p = 0
        q = 0
        while p < len(S[i]) and q < len(S[j]):
            u = S[i][p]
            v = S[j][q]
            if u == v:
                u += B * i
                v += B * j
                neighborhood[u].append((v, 60))
                neighborhood[v].append((u, 60))
                p += 1
                q += 1
            elif u < v:
                p += 1
            else:
                q += 1

dist = [-1]*V

def dijkstra(source):
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


dijkstra(start)
if dist[finish] == -1:
    print("IMPOSSIBLE")
else:
    print(dist[finish])

