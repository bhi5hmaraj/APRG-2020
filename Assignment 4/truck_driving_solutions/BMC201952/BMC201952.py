from math import ceil, log2
from array import array
class Merge_bifurcation:
    def __init__(self, num):
        self.parent = array('L', list(range(num+1)))
        self.rank = array('L', [0] * (num+1))
    def findit(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.findit(self.parent[u])
        return self.parent[u]
    def mergeit(self, x, y):
        x, y = self.findit(x), self.findit(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
class Helper:
    def __init__(self, num):
        self.parent = array('L', list(range(num+1)))
        self.merger = Merge_bifurcation(num)
    def finalans(self, u, v, p):
        self.merger.mergeit(u, v)
        self.parent[self.merger.findit(u)] = p
    def get(self, u):
        return self.parent[self.merger.findit(u)]
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]
edges.sort(key=lambda x: x[2], reverse=True)
parent = list(range(n+1))
def root(v):
    while parent[v] != v:
        v = parent[v]
    return v
def Kruskal_python():
    sizedict = {}
    edge_count = 0
    minimum_spanning_tree = []
    mark = [False] * (n+1)
    while edge_count < n-1:
        u, v, w = edges.pop()
        if (not mark[u]) and (not mark[v]):
            parent[u] = parent[v]
            mark[u] = True
            mark[v] = True
            sizedict[v] = 2
        elif mark[u] and (not mark[v]):
            mark[v] = True
            parent[v] = root(u)
            sizedict[parent[v]] += 1
        elif mark[v] and (not mark[u]):
            mark[u] = True
            parent[u] = root(v)
            sizedict[parent[u]] += 1
        elif root(v) == root(u):
            continue
        else:
            ru, rv = root(u), root(v)
            if sizedict[ru] < sizedict[rv]:
                parent[ru] = rv
                sizedict[rv] += sizedict[ru]
            else:
                parent[rv] = ru
                sizedict[ru] += sizedict[rv]
        edge_count += 1
        minimum_spanning_tree.append((u, v, w))
    return minimum_spanning_tree
minimum_spanning_tree = Kruskal_python()
del edges
del parent
def make_cartesian_tree():
    cartesianset = [0]
    for i in range(1, 2*n):
        cartesianset.append(array('L', [1, 0, 0, 0]))
    parents = Helper(n)
    for i in range(n+1, 2*n):
        u, v, w = minimum_spanning_tree[i-n-1]
        cartesianset[i][0] = w
        cartesianset[i][1] = parents.get(u)
        cartesianset[i][2] = parents.get(v)
        cartesianset[cartesianset[i][1]][3] = i
        cartesianset[cartesianset[i][2]][3] = i
        parents.finalans(u, v, i)
    return cartesianset
cartesian = make_cartesian_tree()
del minimum_spanning_tree
Eulertour = array('L', [0] * (4*n))
Levels = array('L', [0] * (4*n))
Height = array('L', [0] * (2*n))
def DFS():
    current = (2*n-1, 0)
    count = 0
    while current[0] > 0:
        count += 1
        node, level = current
        Eulertour[count] = node
        Levels[count] = level
        if Height[node] == 0: Height[node] = count

        if cartesian[node][1] != 0 and Height[cartesian[node][1]] == 0:
            current = (cartesian[node][1], level+1)
            continue

        if cartesian[node][2] != 0 and Height[cartesian[node][2]] == 0:
            current = (cartesian[node][2], level+1)
            continue

        current = (cartesian[node][3], level-1)
    
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
def Range_Minimum_Query(i, j):
    k = intlog[(j - i + 1)]
    if Levels[M[i][k]] <= Levels[M[j - pow(2, k) + 1][k]]:
        return M[i][k]
    else:
        return M[j - pow(2, k) + 1][k]
SPTree(2*(2*n-1))
for i in range(int(input())):
    s, d = map(int, input().split())
    print(cartesian[Eulertour[Range_Minimum_Query(min(Height[s],Height[d]), max(Height[s],Height[d]))]][0])    
