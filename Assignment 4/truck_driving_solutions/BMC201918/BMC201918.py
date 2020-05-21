# Problem 1 : Truck Driving
#--------------------------------------------------------
#inputs

n, m = map(int, input().split())
neighborhood = [[] for _ in range(n + 1)]
u: int
v: int
for t in range(m):
    u, v, w = map(int, input().split())
    neighborhood[u].append((v, w))
    neighborhood[v].append((u, w))

q = int(input())
queries = [0]*q
parent = [_ for _ in range(n + 1)]
q_set = [set() for _ in range(n + 1)]

for i in range(q):
    u, v = map(int, input().split())
    if u != v:
        q_set[u].add(i)
        q_set[v].add(i)

#---------------------------------------------------------
# union-find with some modifications

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b, c):
    #precondition: a and b are different components, c is the current weight
    a : int
    b : int
    x : int
    if len(q_set[a]) > len(q_set[b]):
        a, b = b, a
    for x in q_set[a]:
        if x in q_set[b]:
            q_set[b].remove(x)
            queries[x] = c
        else:
            q_set[b].add(x)
    q_set[a].clear()
    parent[a] = b

#----------------------------------------------------------------------------------
# Now Kruskal's Algorithm

edges = []
for u in range(1, n + 1):
    for (v, w) in neighborhood[u]:
        if u < v:
            edges.append((w, u, v))
edges.sort()
e = 0
for (w, u, v) in edges:
    i = find(u)
    j = find(v)
    if i != j:
        e += 1
        union(i, j, w)
    if e == n-1:
        break

#-----------------------------------------------------------------------
# output the answers

for p in queries:
    print(p)

#----------------------------------------------------------------------
# done!