n, b = [int(x) for x in input().split(' ')]
black_row = [[] for i in range(n)]
x, y = [int(x) for x in input().split(' ')]

for i in range(b):
    x, y = [int(x) for x in input().split(' ')]
    x, y = x - 1, y - 1
    black_row[x].append(y)

blocks = [[] for i in range(n)]
parent = {}
size = {}

for i in range(n):
    black_row[i].append(-1)
    black_row[i].append(n)
    black_row[i].sort()
    for j in range(1, len(black_row[i])):
        l, r = black_row[i][j-1] + 1, black_row[i][j] - 1
        if r - l + 1 > 0:
            blocks[i].append((l, r))
            parent[(i,l,r)] = (i,l,r)
            # print(i, l, r)
            size[(i,l,r)] = 1

def root(v):
    if parent[v] == v:
        return v
    parent[v] = root(parent[v])
    return parent[v]

def combine(u, v):
    u, v = root(u), root(v)
    if u == v:
        return
    if size[u] < size[v]:
        u, v = v, u
    size[u] += size[v]
    parent[v] = u

for row in range(1, n):
    prow = row - 1
    i, j, ni, nj = 0, 0, len(blocks[row]), len(blocks[prow])
    while i < ni and j < nj:
        if blocks[row][i][1] < blocks[prow][j][0]:
            i += 1
        elif blocks[prow][j][1] < blocks[row][i][0]:
            j += 1
        elif blocks[row][i][1] == blocks[prow][j][1]:
            combine((row, blocks[row][i][0], blocks[row][i][1]), (prow, blocks[prow][j][0], blocks[prow][j][1]))
            i += 1
            j += 1
        elif blocks[row][i][1] < blocks[prow][j][1]:
            combine((row, blocks[row][i][0], blocks[row][i][1]), (prow, blocks[prow][j][0], blocks[prow][j][1]))
            i += 1
        else:
            combine((row, blocks[row][i][0], blocks[row][i][1]), (prow, blocks[prow][j][0], blocks[prow][j][1]))
            j += 1

arr = set()
for row in range(0, n):
    for i in range(len(blocks[row])):
        arr.add(root((row, blocks[row][i][0], blocks[row][i][1])))

if len(arr) > 1:
    print('N')
else:
    print('Y')