from queue import PriorityQueue
def dij(s,d):
    Q = PriorityQueue()
    Q.put((0,s))
    d[s] = 0
    while not Q.empty():
        v = Q.get()[1]
        for (l,u) in G[v]:
            dist = d[v] + l
            if dist < d[u]:
                d[u] = dist
                Q.put((d[u],u))

n,m = list(map(int,input().split()))
G = [[] for i in range(n+1)]
for i in range(m):
    u,v,w = list(map(int,input().split()))
    G[u].append((w,v))
    G[v].append((w,u))
d1 = [10**18 for i in range(n+1)]
dn = [10**18 for i in range(n+1)]
dij(1,d1)
dij(n,dn)
ans = 10**18
for v in range(n+1):
    if d1[v]+dn[v] != d1[n]: continue
    for (w,u) in G[v]:
        if w+d1[v]+dn[u] != d1[n]: ans = min(ans,w+d1[v]+dn[u])
print(ans)
