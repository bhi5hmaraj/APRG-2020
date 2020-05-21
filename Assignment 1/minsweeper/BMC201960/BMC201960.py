(m, n) = tuple(map(int, input().split()))
my_input = ""
for i in range(m):
    my_input += input() + "\n"

l = list(map(list, my_input.split("\n")))
l.pop(-1)

for i in range(m):
    for j in range(n):
        if l[i][j] == '.':
            l[i][j] = 0
        else:
            l[i][j] = '*'

for i in range(m):
    for j in range(n):
        if l[i][j] == '*':
            if i in range(1, m - 1) and j in range(1, n - 1):
                for (x, y) in [(a, b) for a in [-1, 0, 1] for b in [-1, 0 ,1] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i == 0 and j in range(1, n - 1):
                for (x, y) in [(a, b) for a in [0, 1] for b in [-1, 0 ,1] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i == m - 1 and j in range(1, n - 1):
                for (x, y) in [(a, b) for a in [-1, 0] for b in [-1, 0 ,1] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i in range(1, m - 1) and j == 0:
                for (x, y) in [(a, b) for a in [-1, 0, 1] for b in [0 ,1] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i in range(1, m - 1) and j == n - 1:
                for (x, y) in [(a, b) for a in [-1, 0, 1] for b in [-1, 0] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i == 0 and j == 0:
                for (x, y) in [(a, b) for a in [0, 1] for b in [0 ,1] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i == m - 1 and j == 0:
                for (x, y) in [(a, b) for a in [-1, 0] for b in [0 ,1] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i == 0 and j == n - 1:
                for (x, y) in [(a, b) for a in [0, 1] for b in [-1, 0] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1
            elif i == m - 1 and j == n - 1:
                for (x, y) in [(a, b) for a in [-1, 0] for b in [-1, 0] if not(a == 0 and b == 0)]:
                    if l[i + x][j + y] != '*':
                        l[i + x][j + y] += 1

for i in range(m):
    for j in range(n):
        print(l[i][j], end = '')
    print('\n', end = '')
