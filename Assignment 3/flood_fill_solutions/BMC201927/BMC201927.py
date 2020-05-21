
n, b = map(int, input().split())
x, y = map(int, input().split())

pool = [[1] * (n+2)] + [[1] + [0] * n + [1] for i in range(n)] + [[1] * (n+2)]

for i in range(b):
    a, b = map(int, input().split())
    pool[a][b] = 1

prev = [(x, y)]
pool[x][y] = 2

while prev:
    new = []
    for p, q in prev:
        neighbours = [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]
        for r, s in neighbours:
            if not pool[r][s]:
                pool[r][s] = 2
                new.append((r, s))
    prev = new[:]

found = [1 for p in pool if 0 in p]
if found:  # there is at least one white pixel left
    print('N')
else:
    print('Y')