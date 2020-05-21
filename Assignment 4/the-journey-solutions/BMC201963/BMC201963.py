import heapq
def f (x):
    return(x[0] + 99*(x[1]-1))
def shortestpath (l,x,n):
    visited = [0 for i in range(n)]
    h = [[0,x]]
    mydict = {}
    mydict[x] = [0,x]
    heapq.heapify(h)
    visited[f(x)] = 1
    while h != []:
        k = h[0]
        heapq.heappop(h)
        for v in l[k[-1]]:
            if v[0] in l:
                if visited[f(v[0])] == 0:
                    mydict[v[0]] = [v[1]+k[0],v[0]]
                    heapq.heappush(h,mydict[v[0]])
                    visited[f(v[0])] = 1
                else:
                    if v[0] not in mydict:
                        mydict[v[0]] = [v[1]+k[0],v[0]]
                        heapq.heappush(h,mydict[v[0]])
                    else:
                        g = mydict[v[0]][0]
                        p = min(mydict[v[0]][0],v[1]+k[0])
                        if p != g:
                            mydict[v[0]] = [p,v[0]]
                            heapq.heappush(h,mydict[v[0]])
                        elif v[1] + k[0] == g:
                            mydict[v[0]] = [g,v[0]]
    return(mydict)
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = {}
d[(0,0)] = []
for i in range(a[0]):
    l = list(map(int,input().split()))
    for k in range(len(l)):
            if l[k] == 0:
                if d[(0,0)] == []:
                    d[(0,0)] = [((l[k+1],i+1),(l[k+1])*b[i])]
                else:
                    d[(0,0)].append(((l[k+1],i+1),(l[k+1])*b[i]))
            else:
                d[(l[k],i+1)] = [((l[k],x+1),60) for x in range(a[0]) if x != i]
                if k > 0:
                    d[(l[k],i+1)].append(((l[k-1],i+1),(l[k]-l[k-1])*b[i]))
                if k < len(l)-1:
                    d[(l[k],i+1)].append(((l[k+1],i+1),(l[k+1]-l[k])*b[i]))
mydict = shortestpath(d,(0,0),496)
for i in range(5):
    if (a[1],i+1) not in mydict:
        mydict[(a[1],i+1)] = [10**8,"easy problem"]
l = [mydict[(a[1],i+1)] for i in range(5)]
L = [x[0] for x in l]
m = min(L)
if a[1] == 0:
    print(0)
elif m == 10**8:
    print("IMPOSSIBLE")
else:
    print(m)
