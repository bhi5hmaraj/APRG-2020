n, m = [int(x) for x in input().split()]
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

arr = [input() for i in range(n)]

for x in range(n):
    for y in range(m):
        if arr[x][y] == '*':
            print('*', end = "")
            continue
        cnt = 0
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == '*':
                cnt += 1
        print(cnt, end="")
    print()
