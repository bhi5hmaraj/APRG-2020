import math

graph = []
parent = []
rank = []
adlist = []
wts = []
levels = []
P = []
Pd = []
queue = []

def find(parent, i):
    if(parent[i] == i): 
        return i 
    return find(parent, parent[i])


def union(parent, rank, x, y): 
    xroot = find(parent, x) 
    yroot = find(parent, y) 
  
    if(rank[xroot] < rank[yroot]): 
        parent[xroot] = yroot 
    elif(rank[xroot] > rank[yroot]): 
        parent[yroot] = xroot 
  
    else: 
        parent[yroot] = xroot 
        rank[xroot] += 1

inNM = list(map(int, input().split()))
n, m = inNM

for i in range(0, m):
    inEdge = list(map(int, input().split()))
    u = inEdge[0]
    v = inEdge[1]
    w = inEdge[2]
    graph.append([u-1, v-1, w])

for i in range(0, n):
    adlist.append([])
    wts.append([])
    levels.append(-1)

for i in range(0, n):
    parent.append(i)
    rank.append(0)

graph =  sorted(graph, key =lambda item: item[2])

# for i in range(0, len(graph)):
#     print(graph[i][0] + 1, graph[i][1] + 1, graph[i][2])

e = 0
V = 0

while(e < n-1):
    u = graph[V][0]
    v = graph[V][1]
    w = graph[V][2]
    V += 1

    x = find(parent, u)
    y = find(parent, v)

    if(not x == y):
        e += 1
        union(parent, rank, x, y)
        # MST.append([u, v, w])
        adlist[u].append(v)
        adlist[v].append(u)
        wts[u].append(w)
        wts[v].append(w)

# for i in range(0, len(MST)):
#     print(MST[i][0] + 1, MST[i][1] + 1, MST[i][2])

for i in range(0, n):
    P.append([-1])
    Pd.append([-1])

for i in range(0, n):
    rank[i] = False

queue.append(0)
rank[0] = True

ctr = 0
while(not len(queue) == ctr):
    s = queue[ctr]
    ctr += 1
    for j in range(0, len(adlist[s])):
        i = adlist[s][j]
        if(rank[i] == False):
            queue.append(i)
            P[i][0] = s
            Pd[i][0] = wts[s][j]
            levels[i] = levels[s] + 1
            rank[i] = True

# for i in range(0, n):
#     print("parent of", i+1, par[i][0]+1, par[i][1])

logn = int(math.log(n, 2)) + 1

for j in range(1, logn):
    for i in range(0, n):
        if(not P[i][j-1] == -1):
            v = P[P[i][j-1]][j-1]
            w = max(Pd[i][j-1], Pd[P[i][j-1]][j-1])
            if(v == -1):
                w = -1
            P[i].append(v)
            Pd[i].append(w)
        else:
            P[i].append(-1)
            Pd[i].append(-1)


# for j in range(0, logn):
#     for i in range(0, n):
#         print("P", i+1, j, P[i][j] + 1, Pd[i][j])

def LCA(u, v):
    if(levels[u] < levels[v]):
        t = u
        u = v
        v = t

    du = Pd[u][0]
    dv = Pd[v][0]


    dist = levels[u] - levels[v]

    while(dist > 0):
        r = int(math.log(dist, 2))
        du = max(du, Pd[u][r])
        u = P[u][r]
        dist -= (1<<r)

    if(u == v):
        return du

    for j in range(logn -1, -1, -1):
        if(not P[u][j] == -1 and not P[u][j] == P[v][j]):
            du = max(du, Pd[u][j])
            dv = max(dv, Pd[v][j])
            u = P[u][j]
            v = P[v][j]

    du = max(du, Pd[u][0])
    dv = max(dv, Pd[v][0])

    return max(du, dv)


Q = int(input())

for q in range(0, Q):
    inSD = list(map(int, input().split()))
    s = inSD[0] - 1
    d = inSD[1] - 1

    print(LCA(s,d))

