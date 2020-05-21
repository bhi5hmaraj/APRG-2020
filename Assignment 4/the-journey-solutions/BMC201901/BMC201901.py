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

inNK = list(map(int, input().split()))
n = inNK[0]
d = inNK[1]

adlist = []
wts = []
for i in range(0, 500):
    adlist.append([])
    wts.append([])

for i in range(0, n):
    for j in range(i+1, n):
        adlist[i].append(j)
        adlist[j].append(i)
        wts[i].append(0)
        wts[j].append(0)

for k in range(1, 100):
    for i in range(0, n):
        for j in range(i+1, n):
            adlist[n*k + i].append(n*k + j)
            adlist[n*k + j].append(n*k + i)
            wts[n*k + i].append(60)
            wts[n*k + j].append(60)

T = list(map(int, input().split()))

stops = []
for i in range(0, n):
    stops.append([])

for i in range(0, n):
    stops[i] = list(map(int, input().split()))

for k in range(0, n):
    for i in range(0, len(stops[k]) - 1):
        adlist[n*stops[k][i] + k].append(n*stops[k][i+1] + k)
        adlist[n*stops[k][i+1] + k].append(n*stops[k][i] + k)
        wts[n*stops[k][i] + k].append(T[k] * (stops[k][i+1] - stops[k][i]))
        wts[n*stops[k][i+1] + k].append(T[k] * (stops[k][i+1] - stops[k][i]))

s = 0
distance = []
explored = []

for i in range(0, 100*n):
    distance.append(-1)
    explored.append(False)

distance[s] = 0

imp = heap()
imp.insert(s, 0)

while(not imp.isEmpty()):
    t = imp.delMin()
    if(explored[t[0]] == False):
        explored[t[0]] == True
        v = t[0]
        w = t[1]

        for i in range(0, len(adlist[v])):
            if(not distance[adlist[v][i]] == -1):
                if(w + wts[v][i] < distance[adlist[v][i]]):
                    distance[adlist[v][i]] = w + wts[v][i]
                    imp.insert(adlist[v][i], distance[adlist[v][i]])    
            else:
                distance[adlist[v][i]] = w + wts[v][i]
                imp.insert(adlist[v][i], distance[adlist[v][i]])
            

dist = distance[n*d]
for i in range(0, n):
    dist = min(dist, distance[n*d + i])

if(dist == -1):
    print("IMPOSSIBLE")

else:
    print(dist)



    




