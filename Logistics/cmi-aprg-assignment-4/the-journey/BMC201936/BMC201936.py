from collections import defaultdict
import heapq
diag = defaultdict(dict) 
def formedg(diag,one,two,take): 
    diag[one][two]=take
    diag[two][one]=take
A,B=map(int,input().split())
Tlist=list(map(int,input().split()))
corners,busstop=[],[]
for so in range(A):
    busstop.append(list(map(int,input().split())))
    for to in busstop[so]:
        corners.append((so,to))
for (n1,n2) in corners:
    for (n3,n4) in corners:
        if n1==n3 and n2 < n4:
            formedg(diag,(n1,n2),(n3,n4),(n4-n2)*Tlist[n1])
        elif n1<n3 and n2==n4:
            formedg(diag,(n1,n2),(n3,n4),60)
def ssp(diag,x,y):
    length={corner:float('Inf') for corner in diag}
    length[x]=0
    pq = [(0,x)]
    while len(pq)>0:
        D,C=heapq.heappop(pq)
        if C==y:
            break
        if D > length[C]:
            continue
        for N, weight in diag[C].items():
            dist = D + weight
            if dist < length[N]:
                length[N] = dist
                heapq.heappush(pq, (dist, N))
    return length[y] if length[y]<float('Inf') else -1

costoftravel=[]
for so in range(A):
    if busstop[so][0]==0:
        for to in range(A):
            if busstop[to][-1]>=B:
                if B in busstop[to]:
                    costoftravel.append(ssp(diag,(so,0),(to,B)))
if costoftravel:
    print(min(costoftravel))
else:
    print('IMPOSSIBLE')
