n, m = [int(x) for x in input().split(' ')]
p = [-1]*n
s = [set() for i in range(n)]

edge = []
for _ in range(m):
    u, v, w = [int(x) - 1 for x in input().split(' ')]
    edge.append((w + 1, u, v))
edge.sort()

q = int(input())
ans = [-1]*q
for i in range(q):
    u, v = [int(x) - 1 for x in input().split(' ')]
    s[u].add(i)
    s[v].add(i)

def find(v):
    if p[v] < 0:
        return v
    p[v] = find(p[v])
    return p[v]

def combine(u, v, w):
    u = find(u)
    v = find(v)
    if u == v:
        return
    if len(s[u]) < len(s[v]):
        u, v = v, u
    for x in s[v]:
        if x in s[u]:
            ans[x] = w
            s[u].remove(x)
        else:
            s[u].add(x)
    p[v] = u

for (w, u, v) in edge:
    combine(u, v, w)

for i in range(q):
    print(ans[i])