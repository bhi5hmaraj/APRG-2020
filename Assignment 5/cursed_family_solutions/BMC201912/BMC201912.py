from collections import deque
n = int(input())
par = [i for i in range(n+1)]
son = [[] for i in range(n+1)]
dist = [0 for i in range(n+1)]
isdisc = [False for i in range(n+1)]
for i in range(n-1):
    u,w= [int(i) for i in input().split()]
    son[u].append(w)
    par[w] = u
root = 1
while (par[root] != root):
    root = par[root]
def dfs():
    dfsq = deque()
    dfsq.append(root)
    while (dfsq):
        u = dfsq.pop()
        if (isdisc[u] == False):
            isdisc[u] = True
            if (u != root):
                dist[u] = dist[par[u]] + 1
            for w in son[u]:
                if (isdisc[w] == False):
                    dfsq.append(w)
def comp():
    dfs()
    mdist = 0
    for i in range(1, n+1):
        mdist = max(dist[i], mdist)
    depthv = [[] for i in range(mdist+1)]
    for i in range(1, n+1):
        depthv[dist[i]].append(i)
    return (depthv, mdist)
(depthv, mdist) = comp()
dpl = [[0,1] for i in range(n+1)]
for i in range(mdist, -1, -1):
    for u in depthv[i]:
        for v in son[u]:
            dpl[u][0] += max(dpl[v][1], dpl[v][0])
            dpl[u][1] += dpl[v][0]
print(max(dpl[root][0], dpl[root][1]))