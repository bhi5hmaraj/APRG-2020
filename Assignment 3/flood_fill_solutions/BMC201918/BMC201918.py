n, b = [int(inp) for inp in input().split()]
u, v = [int(inp)-1 for inp in input().split()]
is_white = [[1 for i in range(n)] for j in range(n)]
for k in range(b):
    x, y = [int(inp)-1 for inp in input().split()]
    is_white[x][y] = 0

flooded = [[0 for i in range(n)] for j in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

back = [(u, v)]
flooded[u][v] = 1
while back:
    front = []
    for (x, y) in back:
        for i in range(4):
            (p, q) = (x + dx[i], y + dy[i])
            if 0 <= p < n and 0 <= q < n:
                if not flooded[p][q] and is_white[p][q]:
                    front.append((p, q))
                    flooded[p][q] = 1
    back = front

ans = 'Y'
for i in range(n):
    for j in range(n):
        if not flooded[i][j] and is_white[i][j]:
            ans = 'N'

print(ans)