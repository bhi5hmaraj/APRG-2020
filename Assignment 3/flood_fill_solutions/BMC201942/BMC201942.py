from collections import deque


def bfs(i, j, grid):
    queue = deque()
    queue.append([i, j])
    visited = [[False]*(len(grid)) for i in range(len(grid))]
    cellsum = 1
    visited[i][j] = True
    while queue:
        cell = queue.popleft()

        a = cell[0]
        b = cell[1]
        for k in [-1, 1]:
            if 0 <= a+k < n:
                if not visited[a+k][b] and grid[a+k][b]:
                    queue.append([a+k, b])
                    cellsum += 1
                    visited[a+k][b] = True
            if 0 <= b+k < n:
                if not visited[a][b+k] and grid[a][b+k]:
                    queue.append([a, b+k])
                    cellsum += 1
                    visited[a][b+k] = True

    return cellsum


n, b = input().split()
n, b = int(n), int(b)
grid = [[True for i in range(n)] for i in range(n)]
k, l = input().split()
k, l = int(k), int(l)
for i in range(b):
    u, v = input().split()
    u, v = int(u), int(v)
    grid[u-1][v-1] = False
w = 0
for e in range(n):
    for r in range(n):
        if not grid[e][r]:
            w+=1
x = bfs(k-1, l-1, grid)

if x == (n*n) - w:
    print("Y")
else:
    print("N")
