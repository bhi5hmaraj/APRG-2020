from collections import deque

n, m = [int(x) for x in input().split(' ')]
x, y = [int(x) for x in input().split(' ')]
g = [[] for i in range(n)]

for i in range(m):
    u, c, v = input().split(' ')
    u, v = int(u), int(v)
    g[u - 1].append((v - 1, c))
    g[v - 1].append((u - 1, c))

x, y = x - 1, y - 1
vis = [False]*n
que = deque([y])
vis[y] = True
dist = [0]*n

while que:
    v = que.popleft()
    for e in g[v]:
        u = e[0]
        if not vis[u]:
            dist[u] = dist[v] + 1
            vis[u] = True
            que.append(u)

min_dist = dist[x]
vec = {x}
for d in range(1, min_dist + 1):
    arr = [set() for i in range(26)]
    for vert in vec:
        for e in g[vert]:
            u = e[0]
            if dist[u] + d == min_dist:
                arr[ord(e[1]) - ord('a')].add(u)

    for i in range(26):
        if len(arr[i]) > 0:
            print(chr(i + ord('a')), end = "")
            vec = arr[i]
            break