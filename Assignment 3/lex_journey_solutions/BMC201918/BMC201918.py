n, m = [int(inp) for inp in input().split()]
x, y = [int(inp) for inp in input().split()]

neighborhood = [[] for i in range(n + 1)]

for i in range(m):
    inp = input().split()
    a, c, b = int(inp[0]), inp[1], int(inp[2])
    neighborhood[a].append((c, b))
    neighborhood[b].append((c, a))

level_x = [-1] * (n+1)
level_y = [-1] * (n+1)

back = [x]
level_x[x] = 0
while back:
    front = []
    for u in back:
        for (w, v) in neighborhood[u]:
            if level_x[v] == -1:
                level_x[v] = level_x[u] + 1
                front.append(v)
    back = front

back = [y]
level_y[y] = 0
while back:
    front = []
    for u in back:
        for (w, v) in neighborhood[u]:
            if level_y[v] == -1:
                level_y[v] = level_y[u] + 1
                front.append(v)
    back = front

answer = ''
weight = ['~'] * (n+1)
rank = '~'
best_rank = '~'
back = [x]
while back:
    front = []
    for u in back:
        if weight[u] == best_rank:
            dx = level_x[u] + 1
            dy = level_y[u] - 1
            for (w, v) in neighborhood[u]:
                if level_x[v] == dx and level_y[v] == dy:
                    if weight[v] == '~':
                        front.append(v)
                    if w < weight[v]:
                        weight[v] = w
                        rank = min(rank, w)
    best_rank = rank
    if best_rank == '~':
        break
    rank = '~'
    answer += best_rank
    back = front

print(answer)