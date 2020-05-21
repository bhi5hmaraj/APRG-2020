
n = int(input())

children = []
parent = []
numChildren = []
lg = []

for i in range(0, n):
    children.append([])
    parent.append(-1)
    numChildren.append(0)
    lg.append(None)

for i in range(0, n-1):
    inUV = list(map(int, input().split()))
    u = inUV[0] - 1
    v = inUV[1] - 1
    children[u].append(v)
    parent[v] = u
    numChildren[u] += 1

root = 0

for i in range(0, n):
    if(numChildren == 0):
        lg[i] = 1
    if(parent[i] == -1):
        root = i

def larG(r):
    if (not lg[r] == None):
        return lg[r]

    g0 = 0
    for i in range(0, numChildren[r]):
        g0 += larG(children[r][i])

    g1 = 1
    for j in range(0, numChildren[r]):
        for i in range(0, numChildren[children[r][j]]):
            g1 += larG(children[children[r][j]][i])

    lg[r] = max(g0, g1)
    return lg[r]

print(larG(root))



