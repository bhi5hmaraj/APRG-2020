from queue import PriorityQueue

N,M = map(int, input().split())

A = [[] for i in range(N+1)]

for _ in range(M):
    a,b,w = map(int, input().split())
    A[a].append((b,w))
    A[b].append((a,w))

Max = 1000001

vertCost = [Max]*(N+1)

def DJK(s):
    vertCost[s] = 0
    q = PriorityQueue()
    q.put((0,s))
    while not(q.empty()):
        u = q.get()
        for v in A[u[1]]:
            if vertCost[v[0]] > vertCost[u[1]] + v[1]:
                vertCost[v[0]] = vertCost[u[1]] + v[1]
                q.put((vertCost[v[0]],v[0]))

DJK(1)
dist1 = vertCost[0:]

vertCost = []
vertCost = [Max]*(N+1)

DJK(N)
distN = vertCost[0:]

dmin = dist1[N]
d2 = Max

for u in range(1,N+1):
    for v in A[u]:
        x = dist1[u] + v[1] + distN[v[0]]
        if dmin != x :
            d2 = min(d2,x)

print(d2)
