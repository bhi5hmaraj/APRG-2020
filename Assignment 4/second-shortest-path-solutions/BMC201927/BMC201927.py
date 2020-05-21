import heapq

n, m = map(int, input().split())
##x, y = map(int, input().split())

red = [[] for i in range(n+1)]  # neighbours
alp = {}
coco = 10**10

for i in range(m):
    u, v, w = map(int, input().split())
    if (u, v) not in alp:
        red[u].append(v)
        red[v].append(u)
        alp[(u, v)] = alp[(v, u)] = [w, coco]
    else:
        z, y = alp[(u, v)]
        if w < z:
            alp[(u, v)] = alp[(v, u)] = [w, z]
        elif z < w < y:
            alp[(u, v)] = alp[(v, u)] = [z, w]


def dijkstra(x, y): 
    dist1 = [coco] * (n+1)
    dist2 = [coco] * (n+1)
    dist1[x] = 0
    mark = [False] * (n+1)
    qu = [(0, x)]
    while qu:
        d, v = heapq.heappop(qu)
        for u in red[v]:
            alt = dist1[v] + alp[(v, u)][0]
            if alt < dist1[u]:
                dist2[u] = dist1[u]
                dist1[u] = alt
                heapq.heappush(qu, (dist1[u], u))
            elif dist1[u] < alt < dist2[u]:
                dist2[u] = alt
                heapq.heappush(qu, (dist1[u], u))
            alt = dist1[v] + alp[(v, u)][1]
            if alt < dist2[u]:
                dist2[u] = alt
                heapq.heappush(qu, (dist1[u], u))
            alt = dist2[v] + alp[(v,u)][0]
            if alt < dist2[u]:
                dist2[u] = alt
                heapq.heappush(qu, (dist1[u], u))

    if dist1[y] < coco:
        return dist2[y]
    else:
        return "seriously?"


print(dijkstra(1, n))
