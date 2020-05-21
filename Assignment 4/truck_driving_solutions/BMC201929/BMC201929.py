from collections import deque 
from sys import stdin, stdout 


[n ,m] = [int(x) for x in stdin.readline().rstrip().split()]


tree = []
edges = []

for i in range(n):
    tree.append([])

for i in range(m):
    [u, v, w] = [int(x) for x in stdin.readline().rstrip().split()]
    
    edges.append([w, u - 1, v- 1])

par = []

for i in range(n):
    par.append(-1)

def root(x):
    if par[x] < 0:
        return x
    else:
        return root(par[x])

def merge(x, y):
    x = root(x)
    y = root(y)

    if(par[x] < par[y]):
        temp = x
        x = y
        y = temp

    par[y] += par[x]
    par[x] = y

    return


def mst():

    edges.sort()

    for i in range(m):

        edge = edges[i]
        u = edge[1]
        v = edge[2]

        if(root(u) != root(v)):
            merge(u, v)
            tree[v].append([u, edge[0]])
            tree[u].append([v, edge[0]])

    return

mst()

visited = [0]*n
level = [0]*n
parent = [-1]*n
LOGN = 20
ancestor = []
mw = []
for i in range(n):
    ancestor.append([-1]*(LOGN + 1))
    mw.append([0]*(LOGN + 1))
    
def dfs(start):
    
    stack = deque() 
    stack.append(start)
    
    while(len(stack) != 0):
        v = stack.pop()
        visited[v] = 1
        
        for adj in tree[v]:
            if visited[adj[0]] == 0:
                stack.append(adj[0])
                level[adj[0]] = level[v] + 1
                parent[adj[0]] = v
                mw[adj[0]][0] = adj[1]
    
    return 

dfs(0)
    
#print(parent)
def filltable():

    for v in range(n):
        if parent[v] != -1:
            ancestor[v][0] = parent[v]
        
    for i in range(1, LOGN):
        for v in range(n):
            if ancestor[v][i -1] != -1:
                ancestor[v][i] = ancestor[ancestor[v][i -1]][i - 1]
                mw[v][i] = max(mw[v][i - 1], mw[ancestor[v][i - 1]][i - 1])
    return 0

filltable()

def lca1(u, v):
    
    ans = 0
    if level[u] > level[v]:
        temp = u
        u = v
        v = temp
        
    for i in range(LOGN, -1, -1):
        if ancestor[v][i] != -1 and level[ancestor[v][i]] >= level[u]:
            ans = max(ans, mw[v][i])
            v = ancestor[v][i]
            
    if u == v:
        return ans
    
    for i in range(LOGN, - 1, -1):
        if ancestor[u][i] != -1 and ancestor[v][i] != -1 and ancestor[u][i] != ancestor[v][i]:
            ans = max(ans, mw[u][i])
            ans = max(ans, mw[v][i])
            u = ancestor[u][i]
            v = ancestor[v][i]
    
    ans = max(ans, mw[u][0])
    ans = max(ans, mw[v][0])
    return ans
          
[Q] = [int(x) for x in stdin.readline().rstrip().split()]
#print(ancestor)
for i in range(Q):

    [s, d] = [int(x) for x in stdin.readline().rstrip().split()]
    stdout.write(str(lca1(s -1, d - 1))+'\n')

