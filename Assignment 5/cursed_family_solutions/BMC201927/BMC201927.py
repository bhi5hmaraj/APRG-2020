n = int(input())

parent = [0] * (n+1)
children = [[] for i in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    parent[v] = u
    children[u].append(v)

parent[0] = n+1
root = parent.index(0)
prev = [root]
levels = []
while prev:
    new = []
    levels.append(prev[:])
    for p in prev:
        new.extend(children[p])
    prev = new[:]


res = [0] * (n+1)
while levels:
    current_level = levels.pop()
    for r in current_level:
        a, b = 1, 0
        for s in children[r]:
            a += res[s][1]
            b += max(res[s])
        res[r] = (a, b)


print(max(res[root]))