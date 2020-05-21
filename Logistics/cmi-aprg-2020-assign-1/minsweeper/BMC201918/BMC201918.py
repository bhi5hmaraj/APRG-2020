n, m = [int(i) for i in input().split()]
grid = [[0 for j in range(m+2)] for i in range(n+2)]
l = [input() for i in range(n)]
for r in range(1,n+1):
    for c in range(1,m+1):
        if l[r-1][c-1] == '*':
            grid[r - 1][c - 1] += 1
            grid[r - 1][c    ] += 1
            grid[r - 1][c + 1] += 1
            grid[r    ][c - 1] += 1
            grid[r    ][c + 1] += 1
            grid[r + 1][c - 1] += 1
            grid[r + 1][c    ] += 1
            grid[r + 1][c + 1] += 1

for r in range(1,n+1):
    for c in range(1,m+1):
        if l[r-1][c-1] == '*':
            grid[r][c] = '*'

for i in range(1,n+1):
    for j in range(1,m+1):
        print(grid[i][j],end = "")
    print("\n", end="")

