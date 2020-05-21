import heapq
in_list = [int(x) for x in input().split()]
numbuses = in_list[0]
stpnums = in_list[1]
timelist = [int(x) for x in input().split()]
neighbours = [[] for i in range(numbuses * 100)]
busstops = [[int(x) for x in input().split()] for i in range(numbuses)]
truckstops = []
num = dict()
for i in range(numbuses):
    for j in range(len(busstops[i]) - 1):
        u, v = 100*i + busstops[i][j], 100*i + busstops[i][j+1]
        neighbours[u].append(v)
        neighbours[v].append(u)
        num[(u, v)] = num[(v, u)] = abs(v-u)*timelist[i]

    for j in range(len(busstops[i])):
        if busstops[i][j] == 0: continue
        u = 100*i + busstops[i][j]
        for k in range(i + 1, numbuses):
            w = 100*k + busstops[i][j]
            if busstops[i][j] in busstops[k]:
                neighbours[u].append(w)
                neighbours[w].append(u)
                num[(u, w)] = num[(w, u)] = 60
    for v in busstops[i]:
        truckstops.append(100*i + v)

def Dijkstra(k):
    time = [float("Inf")] * (501)
    a = []
    for i in range(numbuses):
        visited = [0] * (501)
        time[100*i] = 0
        if 100*i in truckstops:
            heap = [(0, 100*i)]
            heapq.heapify(heap)
            while heap:
                (z, u) = heapq.heappop(heap)
                if visited[u] == 0:
                    visited[u] = 1
                for v in neighbours[u]:
                    if visited[v] == 0 and num[(v, u)] <= time[v] and time[u] + num[(v, u)] <= time[v]:
                        time[v] = time[u] + num[(v, u)]
                        heapq.heappush(heap, (time[v], v))
        for j in range(numbuses):
            if time[100*j + stpnums] != float("Inf"):
                a.append(time[100*j + stpnums])
            else:
                a = a
    if a == []:
        print("IMPOSSIBLE")
    else:
        print(min(a))


Dijkstra(stpnums)

