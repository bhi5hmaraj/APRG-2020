class heap:

    def __init__(self):
        self.pq = [None]
        self.size = 0
        self.length = 0

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def exch(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t

    def swim(self, k):
        while(k > 1 and self.pq[int(k/2)][1] > self.pq[k][1]):
            self.exch(int(k/2), k)
            k = int(k/2)

    def sink(self, k):
        while(2*k <= self.size):
            j = 2*k
            if(j < self.size and self.pq[j][1] > self.pq[j+1][1]):
                j += 1
            if(self.pq[k] <= self.pq[j]):
                break
            self.exch(k,j)
            k = j

    def insert (self, v, w):
        self.size += 1
        if(self.size <= self.length):
            self.pq[self.size] = [v, w]
        else:
            self.pq.append([v,w])
            self.length += 1
        self.swim(self.size)

    def delMin(self):
        min = self.pq[1]
        self.exch(1, self.size)
        self.size -= 1
        self.pq[self.size + 1] = None
        self.sink(1)
        return min

inNM = list(map(int, input().split()))
n = inNM[0]
m = inNM[1]

s = 0
d = n - 1

adlist = []
wts = []
edges = []

for i in range(0, n):
    adlist.append([])
    wts.append([])

for i in range(0, m):
    inEdge = list(map(int, input().split()))
    u = inEdge[0] - 1
    v = inEdge[1] - 1
    w = inEdge[2]
    adlist[u].append(v)
    wts[u].append(w)
    adlist[v].append(u)
    wts[v].append(w)    
    edges.append([u, v, w])

distances = []
exploreds = []
distanced = []
exploredd = []

for i in range(0, n):
    distances.append(-1)
    exploreds.append(False)
    distanced.append(-1)
    exploredd.append(False)

distances[s] = 0

imps = heap()
imps.insert(s, 0)

while(not imps.isEmpty()):
    t = imps.delMin()
    if(exploreds[t[0]] == False):
        exploreds[t[0]] == True
        v = t[0]
        w = t[1]

        for i in range(0, len(adlist[v])):
            if(not distances[adlist[v][i]] == -1):
                if(w + wts[v][i] < distances[adlist[v][i]]):
                    distances[adlist[v][i]] = w + wts[v][i]
                    imps.insert(adlist[v][i], distances[adlist[v][i]])    
            else:
                distances[adlist[v][i]] = w + wts[v][i]
                imps.insert(adlist[v][i], distances[adlist[v][i]])

distanced[d] = 0

impd = heap()
impd.insert(d, 0)

while(not impd.isEmpty()):
    t = impd.delMin()
    if(exploredd[t[0]] == False):
        exploredd[t[0]] == True
        v = t[0]
        w = t[1]

        for i in range(0, len(adlist[v])):
            if(not distanced[adlist[v][i]] == -1):
                if(w + wts[v][i] < distanced[adlist[v][i]]):
                    distanced[adlist[v][i]] = w + wts[v][i]
                    impd.insert(adlist[v][i], distanced[adlist[v][i]])    
            else:
                distanced[adlist[v][i]] = w + wts[v][i]
                impd.insert(adlist[v][i], distanced[adlist[v][i]])

minD = distances[d]

inf = float("inf")

SD = inf

for i in range(0, m):
    u = edges[i][0]
    v = edges[i][1]
    w = edges[i][2]

    if(not distances[u] + w + distanced[v] == minD):
        SD = min(distances[u] + w + distanced[v], SD)

    if(not distances[v] + w + distanced[u] == minD):
        SD = min(distances[v] + w + distanced[u], SD)

print(SD)        


