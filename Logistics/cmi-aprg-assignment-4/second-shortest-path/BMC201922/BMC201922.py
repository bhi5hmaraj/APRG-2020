import heapq
sd = list(map(int, input().split()))
n, m = sd[0], sd[1]
l = [[] for i in range(n)]
for i in range(m):
    qqqq = list(map(int, input().split()))
    x,y = qqqq[0]-1,qqqq[1]-1
    l[x].append((y+1,qqqq[2]))
    l[y].append((x+1,qqqq[2]))
sizee = [(999999999,999999999) for i in range(n)]
sizee[0] = (0,999999999999)
q = [(0,1)]
while(q!=[] and q[0][0]!=999999999):
    z = heapq.heappop(q)
    for f in l[z[1]-1]:
        (c,d) = sizee[f[0]-1]
        if(c > z[0]+f[1]):
            sizee[f[0]-1] = (z[0]+f[1],sizee[f[0]-1][0])
            heapq.heappush(q,(z[0]+f[1],f[0]))
        elif(d > z[0]+f[1] >= sizee[f[0]-1][0]):
            if(c != z[0]+f[1]):
                sizee[f[0]-1] = (c,z[0]+f[1])
                heapq.heappush(q,(c,f[0]))
            else:
                if(sizee[z[1]-1][1] + f[1] < d):
                    sizee[f[0]-1] = (c,sizee[z[1]-1][1]+f[1])
                    heapq.heappush(q,(c,f[0]))
print(sizee[n-1][1])
