import sys
import heapq
n,m = map(int, input().split())
l = [[] for i in range(n)]
for i in range(m):
    lll = list(map(int, input().split()))
    l[lll[0]-1].append((lll[1],lll[2]))
    l[lll[1]-1].append((lll[0],lll[2]))
sze = [(sys.maxsize,sys.maxsize) for i in range(n)]
sze[0] = (0,999999999999)
q = [(0,1)]
while(q!=[] and q[0][0]!=sys.maxsize):
    z = heapq.heappop(q)
    for f in l[z[1]-1]:
        (c,d) = sze[f[0]-1]
        if(c > z[0]+f[1]):
            sze[f[0]-1] = (z[0]+f[1],c)
            heapq.heappush(q,(z[0]+f[1],f[0]))
        elif(d > z[0]+f[1] >= c):
            if(c != z[0]+f[1]):
                sze[f[0]-1] = (c,z[0]+f[1])
                heapq.heappush(q,(c,f[0]))
            else:
                if(sze[z[1]-1][1] + f[1] < d):
                    sze[f[0]-1] = (c,sze[z[1]-1][1]+f[1])
                    heapq.heappush(q,(c,f[0]))
print(sze[n-1][1])
