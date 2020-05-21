import sys
from queue import Queue
sys.setrecursionlimit(10**6)
n = int(input())
p = [0 for i in range(n+1)]
child = [[] for i in range(n+1)]
r = n
for i in range(n-1):
    u,v = list(map(int,input().split()))
    p[v] = u
    r = u
    child[u].append(v)
level = dict()
depth = [-1 for i in range(n+1)]
while p[r]!=0: r = p[r]
depth[r] = 0
level[0] = [r]
q = Queue()
q.put(r)
while not q.empty():
    v = q.get()
    for u in child[v]: 
        depth[u] = depth[v]+1
        q.put(u)
        if not (depth[u] in level): level[depth[u]] = [u]
        else: level[depth[u]].append(u)
l = max(depth)
sc = [set() for i in range(n+1)]
for i in range(1,n+1):
    for c in child[i]:
        for u in child[c]: sc[i].add(u)

ans = [0 for i in range(n+1)]
for i in range(l,-1,-1):
    for u in level[i]:
        yes,no = 1,0
        for x in sc[u]: yes += ans[x]
        for x in child[u]: no += ans[x]
        ans[u] = max(yes,no)
print(ans[r])