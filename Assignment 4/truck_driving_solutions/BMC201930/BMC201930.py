import sys
sys.setrecursionlimit(10**6)
n,m = list(map(int, input().split()))
G = []
for i in range(m):
    u,v,w = list(map(int, input().split() ))
    G.append((w,u,v))
G.sort()
s = [set() for i in range(n+1)]
Q = int(input())
q = [0 for i in range(Q)]
for i in range(Q):
    u,v = list(map(int,input().split()))
    s[u].add(i)
    s[v].add(i)

parent = [i for i in range(n+1)]
edges = 0 
ptr = 0

def find(parent,i):
    if parent[i]==i: return i
    return find(parent,parent[i])


while edges < n-1:
    (w,u,v) = G[ptr]
    ptr += 1
    x = find(parent,u)
    y = find(parent,v)
    if x!=y: 
        if len(s[x])<len(s[y]): (x,y) = (y,x)
        edges += 1
        for i in s[y]:
            if i in s[x]: 
                s[x].remove(i)
                q[i] = w
            else: s[x].add(i)
        parent[y] = x
for i in q: print(i)