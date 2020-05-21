from math import ceil, log2
from array import array
class MERGE:
    def __init__(self,V):
        self.parent = array('L', list(range(V+1)))
        self.rank = array('L', [0] * (V+1))
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
class MERGER:
    def __init__(self,V):
        self.parent = array('L', list(range(V+1)))
        self.merger = MERGE(V)
    def finalans(self, u, v, p):
        self.merger.merge(u, v)
        self.parent[self.merger.find(u)] = p
    def get(self, u):
        return self.parent[self.merger.find(u)]
n,m=map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]
edges.sort(key=lambda x: x[2], reverse=True)
parent = list(range(n+1))
def root(v):
    while parent[v] != v:
        v = parent[v]
    return v
def KST():
    size={}
    i=0
    MST=[]
    M=[False] * (n+1)
    while i<n-1:
        u, v, w = edges.pop()
        if (not M[u]) and (not M[v]):
            parent[u]=parent[v]
            M[u]=True
            M[v]=True
            size[v]=2
        elif M[u] and (not M[v]):
            M[v]=True
            parent[v]=root(u)
            size[parent[v]]+=1
        elif M[v] and (not M[u]):
            M[u]=True
            parent[u]=root(v)
            size[parent[u]]+=1
        elif root(v)==root(u):
            continue
        else:
            a,b=root(u), root(v)
            if size[a]<size[b]:
                parent[a]=b
                size[b]+=size[a]
            else:
                parent[b]=a
                size[a]+=size[b]
        i+=1
        MST.append((u, v, w))
    return MST
MST=KST()
del edges
del parent
def FCT():
    CS = [0]
    for i in range(1, 2*n):
        CS.append(array('L', [1, 0, 0, 0]))
    parents=MERGER(n)
    for i in range(n+1,2*n):
        u,v,w=MST[i-n-1]
        CS[i][0]=w
        CS[i][1]=parents.get(u)
        CS[i][2]=parents.get(v)
        CS[CS[i][1]][3]=i
        CS[CS[i][2]][3]=i
        parents.finalans(u,v,i)
    return CS
CT = FCT()
del MST
Eulertour=array('L',[0]*(4*n))
Levels=array('L',[0]*(4*n))
Height=array('L',[0]*(2*n))
def DFS():
    current = (2*n-1, 0)
    count = 0
    while current[0] > 0:
        count += 1
        node, level = current
        Eulertour[count] = node
        Levels[count] = level
        if Height[node] == 0: Height[node] = count

        if CT[node][1] != 0 and Height[CT[node][1]] == 0:
            current = (CT[node][1], level+1)
            continue

        if CT[node][2] != 0 and Height[CT[node][2]] == 0:
            current = (CT[node][2], level+1)
            continue

        current = (CT[node][3], level-1)
    
    return count
count = DFS()
def mat():
    N = 2*(2*n-1)
    ceilinglog = ceil(log2(N))
    M = []
    for i in range(N):
        M.append(array('L', [0] * ceilinglog))
    return M
M = mat()
def SPTree(m):
    for i in range(m): M[i][0] = i
    j = 1
    while pow(2, j) <= m:
        i = 0
        power2j = pow(2, j)
        power2j_1 = pow(2, j-1)
        while i + power2j - 1 < m:
            if Levels[M[i][j - 1]] < Levels[M[i + power2j_1][j - 1]]:
                M[i][j] = M[i][j - 1]
            else:
                M[i][j] = M[i + power2j_1][j - 1]
            i += 1
        j += 1
    return None
def integral_log(n):
    integral_log = [0, 0]
    k = 1
    power2k = 2
    while power2k < n:
        integral_log += ([k]*power2k)
        k += 1
        power2k *= 2
    return integral_log
intlog = integral_log(count)
def RMQ(i,j):
    k = intlog[(j-i+1)]
    if Levels[M[i][k]]<=Levels[M[j-pow(2,k)+1][k]]:
        return M[i][k]
    else:
        return M[j-pow(2,k)+1][k]
SPTree(2*(2*n-1))
for i in range(int(input())):
    s,d=map(int, input().split())
    print(CT[Eulertour[RMQ(min(Height[s],Height[d]),max(Height[s],Height[d]))]][0])