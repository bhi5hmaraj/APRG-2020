import heapq
in_list = [int(x) for x in input().split()]
n = in_list[0]
m = in_list[1]
neighbours = [[] for i in range(n + 1)]
num = dict()
for i in range(m):
    x, y, numbers = input().split()
    x = int(x)
    y = int(y)
    num[(x, y, i)] = int(numbers)
    num[(y, x, i)] = int(numbers)
    neighbours[x].append((y, i))
    neighbours[y].append((x, i))


def Dijkstra(x):
    dist = [float("Inf")] * (n+1)
    dist[x] = 0
    heap = [(0, x)]
    heapq.heapify(heap)
    while heap:
        (z, u) = heapq.heappop(heap)
        for (v, i) in neighbours[u]:
            if num[(u, v, i)] <= dist[v] and dist[u] + num[(u, v, i)] <= dist[v]:
                dist[v] = dist[u] + num[(u, v, i)]
                heapq.heappush(heap, (dist[v], v))
    return dist


def Dijkstra2(_s, _d):
    a = Dijkstra(_s)
    b = Dijkstra(_d)
    dist2 = []
    for x in range(1, n+1):
        for (y, i) in neighbours[x]:
            if a[_d] < a[x] + num[(x, y, i)] + b[y]:
                dist2.append(a[x] + num[(x, y, i)] + b[y])
    print(min(dist2))


Dijkstra2(1, n)
