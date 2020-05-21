from math import ceil, log2
from array import array


class DisjointSets():
    def __init__(self, num):
        self.parent = array('L', list(range(num+1)))
        self.rank = array('L', [0] * (num+1))

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
        

class ParentInfo():
    def __init__(self, num):
        self.parent = array('L', list(range(num+1)))
        self.ds = DisjointSets(num)

    def set_parent(self, u, v, p):
        self.ds.merge(u, v)
        self.parent[self.ds.find(u)] = p
        self.parent[self.ds.find(v)] = p

    def get(self, u):
        return self.parent[self.ds.find(u)]


n, m = map(int, input().split())
##n, m = 9, 14
edges = [tuple(map(int, input().split())) for i in range(m)]
edges.sort(key=lambda x: x[2], reverse=True)



parent = list(range(n+1))
##edges = [(3,5,14),(1,7,11),(5,4,10),(3,4,9),(1,2,8),(0,7,8),(7,8,7),(2,3,7),(8,6,6),(2,5,4),(0,1,4),(6,5,2),(8,2,2),(7,6,1)]
##edges = list(map(lambda x: (x[0]+1, x[1]+1, x[2]), edges))


def root(v):
    while parent[v] != v:
        v = parent[v]
    return v


def make_MST():
    size = {}
    edge_count = 0
    mst = []
    mark  = [False] * (n+1)
    while edge_count < n-1:
        u, v, w = edges.pop()
        if (not mark[u]) and (not mark[v]):
            parent[u] = parent[v]
            mark[u] = True
            mark[v] = True
            size[v] = 2

        elif mark[u] and (not mark[v]):
            mark[v] = True
            parent[v] = root(u)
            size[parent[v]] += 1

        elif mark[v] and (not mark[u]):
            mark[u] = True
            parent[u] = root(v)
            size[parent[u]] += 1

        elif root(v) == root(u):
            continue

        else:
            ru, rv = root(u), root(v)
            if size[ru] < size[rv]:
                parent[ru] = rv
                size[rv] += size[ru]
            else:
                parent[rv] = ru
                size[ru] += size[rv]

        edge_count += 1
        mst.append((u, v, w))

    return mst

mst = make_MST()
del edges
del parent


def cartesian():
    cart = [0] * (2*n)
    for i in range(1, 2*n):
        cart[i] = array('L', [1, 0, 0, 0])

    parents = ParentInfo(n)

    for i in range(n+1, 2*n):
        u, v, w = mst[i-n-1]
        cart[i][0] = w
        cart[i][1] = parents.get(u)
        cart[i][2] = parents.get(v)

        cart[cart[i][1]][3] = i
        cart[cart[i][2]][3] = i

        parents.set_parent(u, v, i)

    return cart



carte = cartesian()
del mst
Ev = array('L', [0] * (4*n))
L = array('L', [0] * (4*n))
H = array('L', [0] * (2*n))

def create():
    current = (2*n-1, 0)
    counter = 0
    while current[0] > 0:
        counter += 1
        node, level = current
        Ev[counter] = node
        L[counter] = level
        if H[node] == 0: H[node] = counter

        if carte[node][1] != 0 and H[carte[node][1]] == 0:
            current = (carte[node][1], level+1)
            continue


        if carte[node][2] != 0 and H[carte[node][2]] == 0:
            current = (carte[node][2], level+1)
            continue

        current = (carte[node][3], level-1)
    
    return counter


counter = create()

def make_M():
    nV = 2*(2*n-1)
    ceillog = ceil(log2(nV))
    M = []
    for i in range(nV):
        M.append(array('L', [0] * ceillog))
    return M

M = make_M()


def preprocess(N):
    for i in range(N): M[i][0] = i
    j = 1
    while pow(2, j) <= N:
        i = 0
        pow2j = pow(2, j)
        pow2j_1 = pow(2, j-1)
        while i + pow2j - 1 < N:
            if L[M[i][j - 1]] < L[M[i + pow2j_1][j - 1]]:
                M[i][j] = M[i][j - 1]
            else:
                M[i][j] = M[i + pow2j_1][j - 1]
            i += 1
        j += 1
    return None


def make_intlog(xxx):
    intlog = [0,0]
    k = 1
    pow2k = 2
    while pow2k < xxx:
        intlog += ([k]*pow2k)
        k += 1
        pow2k *= 2
    return intlog

intlog = make_intlog(counter)

def RMQ(i, j):
    k = intlog[(j - i + 1)]
    if L[M[i][k]] <= L[M[j - pow(2, k) + 1][k]]:
        return M[i][k]
    else:
        return M[j - pow(2, k) + 1][k]


preprocess(2*(2*n-1))


for temp in range(int(input())):
    s, d = map(int, input().split())
    print(carte[ Ev[ RMQ(min(H[s],H[d]), max(H[s],H[d])) ] ][0])
