li = list(map(int, input().split()))
n = li[0]
m = li[1]
A = [[] for i in range(n)]
for i in range(m):
    li = list(map(int, input().split()))
    A[(li[0]-1)].append((li[1]-1,li[2]))
    A[(li[1]-1)].append((li[0]-1,li[2]))
def distance(A,n,k):    
    mark = [ 0 for i in range(n)]
    distance = [10000000000 for i in range(n)]
    mark[k] = 1
    distance[k] = 0
    import heapq
    h = []
    heapq.heappush(h, (0,k))
    
    while h != []:
        a = heapq.heappop(h)
        for v in A[a[1]]:
                if distance[a[1]] + v[1] < distance[v[0]]:
                    distance[v[0]] = distance[a[1]] + v[1]
                    heapq.heappush(h, (distance[v[0]], v[0]))
        mark[a[1]] = 1
    return distance
distance1 = distance(A,n,0)
distancen = distance(A,n,n-1)
x = distance1[n-1]
c = 10000000000
"""mark = [ 0 for i in range(n)]
distancen = [1000000 for i in range(n)]
mark[n-1] = 1
distancen[n-1] = 0
import heapq
h = []

for v in A[n-1]:
    distancen[v[0]] = v[1]
    heapq.heappush(h, (distancen[v[0]],v[0]))
    
while h != []:
    a = heapq.heappop(h)
    if mark[a[1]] == 1:
        continue
    for v in A[a[1]]:
            if a[0] + v[1] < distancen[v[0]]:
                distancen[v[0]] = a[0] + v[1]
                heapq.heappush(h, (a[0] + v[1], v[0]))
    mark[a[1]] = 1
while c == x:
    for i in range(n):
        for v in A[i]:
            a = distance1[v[0]] + v[1] + distancen[i]
            if c < a:
                c = a"""
                
for i in range(n):
    for v in A[i]:
        a = distance1[v[0]] + v[1] + distancen[i]
        if  x < a < c:
            c = a
print(c)   
