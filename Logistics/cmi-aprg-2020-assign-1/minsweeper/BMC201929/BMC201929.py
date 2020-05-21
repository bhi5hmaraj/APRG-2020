n,m = [int(x) for x in input().split()]
matrix = []
for x in range(n):
    a = input()
    matrix.append(a)
newmatrix = []

for x in range(n):
    a = []
    for y in range(m):
        i = 0
        if matrix[x][y] == '*':
            a.append('*')
        else:
            if x > 0 and matrix[x-1][y] == '*':
                i += 1
            if y > 0 and matrix[x][y-1] == '*':
                i += 1
            if x < n - 1 and matrix[x+1][y] == '*':
                i += 1
            if y < m - 1 and matrix[x][y+1] == '*':
                i += 1
            if (x > 0 and y > 0) and matrix[x-1][y-1] == '*':
                i += 1
            if (x < n - 1 and y > 0) and matrix[x+1][y-1] == '*':
                i += 1
            if (y < m - 1 and x > 0) and matrix[x-1][y+1] == '*':
                i += 1
            if (x < n - 1 and y < m - 1) and matrix[x+1][y+1] == '*':
                i += 1
            a.append(i)
    newmatrix.append(a)

for x in range(n):
    for y in range(m):
        print(newmatrix[x][y], end = "")
    print()



