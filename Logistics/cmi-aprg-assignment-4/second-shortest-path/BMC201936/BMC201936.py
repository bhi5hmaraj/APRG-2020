from collections import defaultdict

import heapq
diag = defaultdict(dict) 
def formedg(diag,one,two,take): 
    
    if diag.get(one) and diag[one].get(two):
        diag[one][two]=diag[one][two]+[take,3*take]
        diag[two][one]=diag[two][one]+[take,3*take]
    
    else:
        diag[one][two]=[take,3*take]
        diag[two][one]=[take,3*take]

        
A,B=map(int,input().split())
for i in range(B):
    k,take,w=map(int,input().split())
    formedg(diag,k,take,w)
def ssp(diag):
    length={corner:float('Inf') for corner in diag}
    length[1]=0
    path={}
    pq = [(0,1)]
    while len(pq)>0:
        D,C=heapq.heappop(pq)
        if D > length[C]:
            continue
        for N in diag[C].keys():
            dist = D + min(diag[C][N])
            if dist < length[N]:
                length[N] = dist
                path[N] = C
                heapq.heappush(pq, (dist, N))
    
    two,result=A,float('Inf')
    while two!=1:
        for N in diag[two]:
            for hey in diag[two][N]:
                x = length[N]+hey+length[A]-length[two]
                if x<result and x>length[A]:
                    result=x
        two=path[two]
    print(result)

ssp(diag)
