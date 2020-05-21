import heapq
import sys
def shortestpath (l,n):
    h = [[0,1]]
    mydict = {}
    mydict[1] = [0,1]
    heapq.heapify(h)
    ssplength = [sys.maxsize for k in range(n)]
    while h != [] and h[0][0] != sys.maxsize:
        k = h[0]
        heapq.heappop(h)
        for v in l[(k[-1]-1)]:
            if v[0] not in mydict:
                mydict[v[0]] = [sys.maxsize,v[0]]
            if ssplength[v[0]-1] > v[1]+k[0]:
                if mydict[v[0]][0] > v[1] + k[0]:
                    c = mydict[v[0]][0]
                    mydict[v[0]][0] = v[1] + k[0]
                    ssplength[v[0]-1] = c
                    heapq.heappush(h,mydict[v[0]])
                elif mydict[v[0]][0] == v[1]+k[0]:
                    if ssplength[k[1]-1] + v[1] < ssplength[v[0]-1]:
                        ssplength[v[0]-1] = ssplength[k[1]-1] + v[1]
                        heapq.heappush(h,mydict[v[0]])
                else:
                    ssplength[v[0]-1] = v[1]+k[0]
                    heapq.heappush(h,mydict[v[0]])
    return(ssplength[-1])
a = list(map(int, input().split()))
l = [[] for i in range(a[0])]
for i in range(a[1]):
    t = list(map(int, input().split()))
    if l[(t[0]-1)] == []:
        l[(t[0]-1)] = [(t[1],t[2])]
    else:
        l[(t[0]-1)].append((t[1],t[2]))
    if l[(t[1]-1)] == []:
        l[(t[1]-1)] = [(t[0],t[2])]
    else:
        l[(t[1]-1)].append((t[0],t[2]))
print(shortestpath(l,a[0]))
