from queue import PriorityQueue
def dij(bus, d):
    Q = PriorityQueue()
    Q.put((0,[0,bus]))
    d[0][bus] = 0
    while not Q.empty():
        [city,b] = Q.get()[1]
        for (w,[c,bs]) in G[city][b]:
            dist = d[city][b] + w
            if dist < d[c][bs]:
                d[c][bs] = dist
                Q.put((d[c][bs],[c,bs]))

#Graph is G[city][bus]
#adjacency list contains neighbours in the form (weight, [city,bus])
n,k = list(map(int,input().split()))
G = [[[] for j in range(n+1)] for i in range(100)]
t = [0] + list(map(int,input().split()))
#print(G[1])
for b in range(1,n+1):
    l = list(map(int,input().split()))
    for v in l: 
        for u in l:
            if not v==u: G[v][b].append((t[b]*abs(v-u),[u,b]))
for city in range(100):
    for bus in range(1,n+1):
        for b in range(1,n+1):
            if not b==bus: G[city][bus].append((60,[city,b]))
d = [[[10**18 for k in range(n+1)] for j in range(100)] for i in range(n+1) ]
for i in range(1,n+1): dij(i,d[i])
ans = 10**18
for i in range(1,n+1): 
    for j in range(1,n+1):
        ans = min(ans, d[i][k][j])
if ans == 10**18: print('IMPOSSIBLE') 
else: print(ans)
