inp = list(map(int,input().split()))
N = inp[0]
M = inp[1]
inp1 = list(map(int,input().split()))
X = inp1[0]
Y = inp1[1]
Adj = []
curr_list = []
nextList = [X]
path = []
for k in range (N+1):
    Adj.append([])
for i in range(M):
    (a,b,c) = list(input().split())
    Adj[(int(a))].append(((int(c)),b))
    Adj[(int(c))].append(((int(a)),b))
d = []
for i in range(2):
    d.append([0] * (N+1))
def bfs(n,mar):
    visited = [0] * (N+1)
    Q = []
    d[mar][n] = 0
    Q.append(n)
    l = []
    visited[n]=1
    while (Q != []):
        v = Q.pop(0)
        l.append(v)
        for i in Adj[v]:
            j = i[0]
            k = i[1]
            if (visited[j] == 0):
                visited[j]=1
                d[mar][j] = d[mar][v] + 1
                Q.append(j)
bfs(X,0)
bfs(Y,1)
def rank(n):
    m='z'
    for i in Adj[n]:
        k = i[0]
        if (d[0][k] == d[0][n]+1):
            if (d[0][k]+d[1][k] == d[0][Y]):
                m=min(m,i[1])
    return m

visit = [0]*(N+1)
visit[X]=1
for i in range(d[0][Y]):
    curr_list = nextList
    nextList = []
    temp = []
    l = []
    for t in curr_list:
        if (t != Y):
            l.append(rank(t))
    a = min(l)
    path.append(a)
    for n in curr_list:
        for i in Adj[n]:
            k = i[0]
            if(i[1]!=a):
                continue
            if(visit[k]==1):
                continue
            visit[k]=1
            if (d[0][k] == d[0][n]+1):
                if (d[0][k]+d[1][k] == d[0][Y]) and i[1]==a:
                    nextList.append(i[0])

     
print (''.join(path))