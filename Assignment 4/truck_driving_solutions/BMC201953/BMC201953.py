import sys
sys.setrecursionlimit(10**8)

def log2(x):
    k = 1
    curr = -1
    while (k <= x):
        k = k << 1
        curr = curr + 1
    return curr

#taking the graph input
inp = list(input().split())
N = int(inp[0])
M = int(inp[1])

#taking the edges
mh = []
seq = []
for i in range(M):
    inp = list(input().split())
    u = int(inp[0])
    v = int(inp[1])
    w = int(inp[2])
    mh.append((w , u , v))
    seq.append(i)
    
#making the compare function and sorting seq
def compare(s):
    return mh[s][0]
seq.sort(key = compare)

#mst
labels = [-1]
rank = [-1]
tree = [[]]

depth = [-1]

path_max = [[]]
anc = [[]]
max_length = log2(N)

for i in range(N):
    labels.append(i + 1)
    rank.append(0)
    tree.append([])
    depth.append(-1)
    path_max.append([])
    anc.append([])
#my implementation of dsu
def combine(a , b):
    if(rank[a] > rank[b]):
        labels[b] = a
    elif(rank[a] < rank[b]):
        labels[a] = b
    else:
        labels[a] = b
        rank[b] = rank[b] + 1
def findParent(x):
    curr = x
    while(curr != labels[curr]):
        curr = labels[curr]
    return curr
#kruskal
added = 0
for i in range(len(seq)):
    if(added == N - 1):
        break
    edge = mh[seq[i]]
    u = edge[1]
    v = edge[2]
    w = edge[0]
    p1 = findParent(u)
    p2 = findParent(v)
    if(p1 != p2):
        combine(p1 , p2)
        tree[u].append((v , w))
        tree[v].append((u , w))
        added += 1
#root the tree at 1
def dfs(u , p , weight):
    anc[u].append(p)
    path_max[u].append(weight)
    for i in range(1 , max_length + 1):
        anc[u].append(-1)
        path_max[u].append(-1)
        anc[u][i] = anc[anc[u][i - 1]][i - 1]
        path_max[u][i] = max(path_max[u][i - 1] , path_max[anc[u][i - 1]][i - 1])
    for j in range(len(tree[u])):
        v = tree[u][j][0]
        wie = tree[u][j][1]
        if (v != p):
            depth[v] = depth[u] + 1
            dfs(v , u , wie)

def lca(x , y):
    temp1 = -1
    p = x
    q = y
    if(depth[x] < depth[y]):
        p = y
        q = x
    i = max_length
    while(i >= 0):
        if((depth[p] - (1 << i)) >= depth[q]):
            temp1 = max(temp1 , path_max[p][i])
            p = anc[p][i]
        i = i - 1
    if(p == q):
        return temp1
    i = max_length
    while(i >= 0):
        if(anc[p][i] != anc[q][i]):
            temp1 = max(temp1 , path_max[p][i] , path_max[q][i])
            p = anc[p][i]
            q = anc[q][i]
        i = i - 1
    temp1 = max(temp1 , path_max[p][0] , path_max[q][0])
    return temp1   
dfs(1 , 1 , -1)

#taking the queries
Q = int(input())
for i in range(Q):
    inp = list(input().split())
    a = int(inp[0])
    b = int(inp[1])
    if(a == b):
        print(0)
        continue
    print(lca(a , b))