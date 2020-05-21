from math import ceil, log2
from array import array
import sys

sys.setrecursionlimit(10 ** 5)


class Node:
    def __init__(self, value_, left_child, right_child, parent_):
        self.left = left_child
        self.right = right_child
        self.parent = parent_
        self.val = value_


class JoinSets:
    def __init__(self, num):
        self.parent = list(range(num + 1))
        self.rank = [0] * (num + 1)

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


class Parenter:
    def __init__(self, num):
        self.parent = list(range(num + 1))
        self.ds = JoinSets(num)

    def set_parent(self, u, v, p):
        self.ds.merge(u, v)
        self.parent[self.ds.find(u)] = p

    def get(self, u):
        return self.parent[self.ds.find(u)]


n, m = map(int, input().split())
connections = [tuple(map(int, input().split())) for i in range(m)]
connections.sort(key=lambda x: x[0], reverse=True)
connections.sort(key=lambda x: x[2], reverse=True)

visited = [False] * (n + 1)
father = list(range(n + 1))


def root(v):
    while father[v] != v:
        v = father[v]
    return v


length = {}
path_length = 0
datas = []
while path_length < n - 1:
    u, v, w = connections.pop()
    if (not visited[u]) and (not visited[v]):
        father[u] = father[v]
        visited[u] = True
        visited[v] = True
        length[v] = 2

    elif visited[u] and (not visited[v]):
        visited[v] = True
        father[v] = root(u)
        length[father[v]] += 1

    elif visited[v] and (not visited[u]):
        visited[u] = True
        father[u] = root(v)
        length[father[u]] += 1

    elif root(v) == root(u):
        continue

    else:
        ru, rv = root(u), root(v)
        if length[ru] < length[rv]:
            father[ru] = rv
            length[rv] += length[ru]
        else:
            father[rv] = ru
            length[ru] += length[rv]

    path_length += 1
    datas.append((u, v, w))

del father
del visited


def cartesian(edges):
    chaos = [0] * (2 * n)
    for i in range(1, 2 * n):
        chaos[i] = Node(1, 0, 0, 0)

    parents = Parenter(n)

    for i in range(n + 1, 2 * n):
        u, v, w = edges[i - n - 1]
        chaos[i].val = w
        chaos[i].left = parents.get(u)
        chaos[i].right = parents.get(v)

        chaos[chaos[i].left].parent = i
        chaos[chaos[i].right].parent = i

        parents.set_parent(u, v, i)

    return chaos


chaotic = cartesian(datas)
A, B, C = array('L', [0] * (4 * n)), array('L', [0] * (4 * n)), array('L', [0] * (4 * n))
scorer = 0


def recursive_dfs(node, level):
    global scorer
    scorer += 1

    A[scorer] = node
    B[scorer] = level
    if C[node] == 0: C[node] = scorer

    if chaotic[node].left != 0:
        recursive_dfs(chaotic[node].left, level + 1)
        scorer += 1
        A[scorer] = node
        B[scorer] = level

    if chaotic[node].right != 0:
        recursive_dfs(chaotic[node].right, level + 1)
        scorer += 1
        A[scorer] = node
        B[scorer] = level

    return None


recursive_dfs(2 * n - 1, 0)
nV = 2 * (2 * n - 1)
M = [0] * nV
for i in range(nV):
    M[i] = array('L', [0] * ceil(log2(nV)))


def preprocess(A, N):
    for i in range(N): M[i][0] = i
    j = 1
    while (1 << j) <= N:
        i = 0
        while i + (1 << j) - 1 < N:
            if A[M[i][j - 1]] < A[M[i + (1 << (j - 1))][j - 1]]:
                M[i][j] = M[i][j - 1]
            else:
                M[i][j] = M[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1
    return None


def RMQ(A, i, j):
    k = int(log2(j - i + 1))
    if A[M[i][k]] <= A[M[j - pow(2, k) + 1][k]]:
        return M[i][k]
    else:
        return M[j - pow(2, k) + 1][k]


def query(i, j):
    return chaotic[A[RMQ(B, min(C[i], C[j]), max(C[i], C[j]))]].val


preprocess(B, 2 * (2 * n - 1))

for temp in range(int(input())):
    s, d = map(int, input().split())
    print(query(s, d))
    