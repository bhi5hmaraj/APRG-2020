import sys
import heapq
L = list(map(int, input().split()))
N = L[0]
M = L[1]
G = [[] for i in range(N)]
for i in range(M):
    K = list(map(int, input().split()))
    G[K[0]-1].append((K[1],K[2]))
    G[K[1]-1].append((K[0],K[2]))
Sizes = [(sys.maxsize,sys.maxsize) for i in range(N)]
Sizes[0] = (0,sys.maxsize)
def dijkstra():
    Q = [(0,1)]
    while(Q!=[] and Q[0][0]!=sys.maxsize):
        z = heapq.heappop(Q)
        for f in G[z[1]-1]:
            (c,d) = Sizes[f[0]-1]
            if(c > z[0]+f[1]):
                Sizes[f[0]-1] = (z[0]+f[1],c)
                heapq.heappush(Q,(z[0]+f[1],f[0]))
            elif(d > z[0]+f[1] >= c):
                if(c != z[0]+f[1]):
                    Sizes[f[0]-1] = (c,z[0]+f[1])
                    heapq.heappush(Q,(c,f[0]))
                else:
                    if(Sizes[z[1]-1][1] + f[1] < d):
                        Sizes[f[0]-1] = (c,Sizes[z[1]-1][1]+f[1])
                        heapq.heappush(Q,(c,f[0]))
    #print(Sizes)
dijkstra()
print(Sizes[N-1][1])               
