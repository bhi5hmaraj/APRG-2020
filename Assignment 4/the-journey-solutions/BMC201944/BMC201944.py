from queue import PriorityQueue

N,e = map(int, input().split())

routeTime = list(map(int, input().split()))

routes = []
for i in range(N):
    routes.append(list(map(int, input().split())))

l = N*100

A = [[] for i in range(l+2)]

for i in range(N):
    r = routes[i]
    t = routeTime[i]
    y = len(r)
    A[100*i+r[0]].append((100*i+r[1],abs(r[0]-r[1])*t))
    A[100*i+r[-1]].append((100*i+r[-2],abs(r[-1]-r[-2])*t))
    for x in range(1,y-1): # Caution if y = 1
        A[100*i+r[x]].append((100*i+r[x-1],abs(r[x]-r[x-1])*t))
        A[100*i+r[x]].append((100*i+r[x+1],abs(r[x]-r[x+1])*t))

for i in range(l):
    x = i%100
    for j in range(N):
        y = 100*j + x
        if  y != i and len(A[y])>0:
            A[i].append((y,60))

for i in range(N):
    A[l].append((100*i,0))
    A[100*i].append((l,0))
    A[l+1].append((100*i+e,0))
    A[100*i+e].append((l+1,0))

Max = 1000001

vertCost = [Max]*(l+2)

def DJK(s):
    vertCost[s] = 0
    q = PriorityQueue()
    q.put((0,s))
    while not(q.empty()):
        u = q.get()
        for v in A[u[1]]:
            if vertCost[v[0]] > vertCost[u[1]] + v[1]:
                vertCost[v[0]] = vertCost[u[1]] + v[1]
                q.put((vertCost[v[0]],v[0]))


DJK(l)

if vertCost[l+1] == Max:
    print("IMPOSSIBLE")
else:
    print(vertCost[l+1])
