import math
N,M = map(int,input().split())
G = [[] for i in range(N)]
ll = []
for i in range(M):
    l = list(map(int,input().split()))
    ll.append((l[2],l[0],l[1]))
    G[l[0]-1].append((l[1],l[2]))
    G[l[1]-1].append((l[0],l[2]))
iminst = [0 for i in range(M)]
edg = sorted(ll,key = lambda x: x[0])
sz = [1 for i in range(N)]
prt = [i+1 for i in range(N)]
def find(s):
    while(prt[s-1] != s):
        prt[s-1] = prt[prt[s-1]-1]
        s = prt[s-1]
    return s
def uni(x,y):
    if(x != y):
        if(sz[x-1] < sz[y-1]):
            temp = x
            x = y
            y = temp
        prt[y-1] = x
        sz[x-1] += sz[y-1]
noe, i = 0, 0
while(noe < N-1):
    (w,u,v) = edg[i]
    uR = find(u)
    vR = find(v)
    if(uR != vR):
        noe += 1
        iminst[i] = 1
        uni(uR,vR)
    i += 1
P = [[-1 for i in range(math.ceil(math.log2(N)))]for j in range(N)]
A = [[0 for i in range(math.ceil(math.log2(N)))]for j in range(N)]
minst = [[] for i in range(N)]
for i in range(M):
    if(iminst[i] == 1):
        K = edg[i]
        minst[K[1]-1].append((K[2],K[0]))
        minst[K[2]-1].append((K[1],K[0]))
        
Level = [1 for i in range(N)]
Visited = [0 for i in range(N)]
pit = [(-1,0) for i in range(N)]

Q = [find(1)]
while(Q):
    z = Q.pop(0)
    Visited[z-1] = 1
    for elem in minst[z-1]:
        if(Visited[elem[0]-1] == 0):
            Level[elem[0]-1] = Level[z-1]+1
            pit[elem[0]-1] = (z,elem[1])
            Q.append(elem[0])
for i in range(N):
    P[i][0] = pit[i][0]
    A[i][0] = pit[i][1]

for j in range(1,math.ceil(math.log2(N))):
    for i in range(N):
        if(P[i][j-1] != -1):
            P[i][j] = P[P[i][j-1]-1][j-1]
            A[i][j] = max(A[i][j-1],A[P[i][j-1]-1][j-1])
def tkz(u,v):
    if(Level[u-1] < Level[v-1]):
        temp = u
        u = v
        v = temp
    utlca = A[u-1][0] 
    vtlca = A[v-1][0]
    levdif = Level[u-1] - Level[v-1]
    while(levdif > 0):
        raise_by = math.floor(math.log2(levdif))
        utlca = max(utlca,A[u-1][raise_by])
        u = P[u-1][raise_by]
        levdif -= (1<<raise_by)
    if (u == v):
        LCA = u
        answer = utlca    
    else:
        k = math.ceil(math.log2(N))-1
        while(k >= 0):
            if(P[u-1][k-1] != -1 and P[u-1][k-1] != P[v-1][k-1]):
                utlca = max(utlca,A[u-1][k-1])
                vtlca = max(vtlca,A[v-1][k-1])
                u = P[u-1][k-1]
                v = P[v-1][k-1]
            k = k-1
        LCA = pit[u-1][0]
        answer = max(utlca,vtlca,A[u-1][0],A[v-1][0])
    print(answer)

q = int(input())
for i in range(q):
    l = list(map(int,input().split()))
    tkz(l[0],l[1])