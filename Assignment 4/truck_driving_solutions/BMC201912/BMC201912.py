from collections import deque
V,E = [int(i) for i in input().split()]
logn = 16
dsuarr = [[1,i] for i in range(V+1)]
adjl = [[] for i in range(V+1)]
sparse = [[0 for i in range(logn)] for j in range(V+1)]
mcost = [[0 for i in range(logn)] for j in range(V+1)]
krq = []
for i in range(E):
    u,w,c = [int(i) for i in input().split()]
    krq.append((c, u, w))
krq.sort()
Q = int(input())
l = [[0,0] for i in range(Q)]
for i in range(Q):
    u, v = [int(i) for i in input().split()]
    l[i][0] = u
    l[i][1] = v
def froot(i):
    while dsuarr[i][1] != i:
        i = dsuarr[i][1]
    return i
def union(i, j):
    i = froot(i)
    j = froot(j)
    if (i == j):
        return
    ir = dsuarr[i][0]
    jr = dsuarr[j][0]
    if (ir == jr):
        dsuarr[i][1] = j
        dsuarr[j][0] += ir
    elif (ir > jr):
        dsuarr[j][1] = i
        dsuarr[i][0] += jr
    else:
        dsuarr[i][1] = j
        dsuarr[j][0] += ir
def spar(i, j):
    return (froot(i) == froot(j))
def kruskal():
    for (c, u, v) in krq:
        if (spar(u,v) == False):
            adjl[u].append((v,c))
            adjl[v].append((u,c))
            union(u,v)
kruskal()
dist = [0 for i in range(V+1)]
par = [0 for i in range(V+1)]
parc = [0 for i in range(V+1)]
isdisc = [False for i in range(V+1)]
def dfs():
    dfsq = deque()
    dfsq.append(1)
    while (dfsq):
        u = dfsq.pop()
        if (isdisc[u] == False):
            isdisc[u] = True
            if (u != 1):
                dist[u] = dist[par[u]] + 1
            for (w,c1) in adjl[u]:
                if (isdisc[w] == False):
                    dfsq.append(w)
                    par[w] = u
                    parc[w] = c1
    dist[1] = 0
    par[1] = 1
def precomp():
    sparse[1][0] = 1
    for i in range(2, V+1):
        sparse[i][0] = par[i]
        mcost[i][0] = parc[i]
    for j in range(1, logn):
        for i in range(1, V+1):
            u = sparse[i][j-1]
            sparse[i][j] = sparse[u][j-1]
            mcost[i][j] = max(mcost[u][j-1], mcost[i][j-1])
def mcpath(u, v):
    maxv = 0
    if (u == v):
        return (maxv, v)
    if (dist[v] > dist[u]):
        (v,u) = (u,v)
    delta = dist[u] - dist[v]
    if (delta != 0):
        for i in range(logn):
            if ((delta & (1 <<i)) != 0):
                maxv = max(maxv, mcost[u][i])
                u = sparse[u][i]
    if (u == v):
        return (maxv, v)
    for i in range(logn):
        j = logn - i - 1
        if (sparse[u][j] != sparse[v][j]):
            maxv = max(maxv, mcost[u][j], mcost[v][j])
            u = sparse[u][j]
            v = sparse[v][j]
    maxv = max(maxv, mcost[u][j], mcost[v][j])
    u = sparse[u][j]
    v = sparse[v][j]        
    return (maxv, v)

#(dist, par, parc) = dfs()
dfs()
precomp()
for i in range(Q):
    ans = mcpath(l[i][0], l[i][1])
    print(ans[0])