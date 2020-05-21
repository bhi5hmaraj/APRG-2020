from queue import PriorityQueue
infty = 1e16
nstop = 101
n, k = [int(i) for i in input().split()]
v = (n*nstop)-1
tl = [int(i) for i in input().split()]
stops = [False]*(n)
for i in range(n):
    stops[i] = [int(j) for j in input().split()]
adjl = [[] for i in range(v+1)]
ecost = {}
for i in range(n):
    z = len(stops[i])
    if (z == 1):
        continue
    else:
        for y in range(z-1):
            u = stops[i][y]
            w = stops[i][y+1]
            c = tl[i]
            ui = (nstop*i)+u
            vi = (nstop*i)+w
            adjl[ui].append(vi)
            adjl[vi].append(ui)
            ecost[(ui, vi)] = c*(w-u)
            ecost[(vi, ui)] = c*(w-u)
for u in range(nstop):
    for i in range(n):
        for j in range(n):
            if (i != j):
                ui = (nstop*i) + u
                uj = (nstop*j) + u
                adjl[ui].append(uj)
                ecost[(ui, uj)] = 60

def dstra(x): 
    cost = [infty]*(v+1)
    isdisc = [False]*(v+1)
    prev = [None]*(v+1)
    dq = PriorityQueue()
    dq.put((0,x))
    while (dq.empty() == False):
        (c,u) = dq.get()
        if (isdisc[u]):
            continue
        isdisc[u] = True
        cost[u] = c
        ec = c
        for w in adjl[u]:
            cw = ec + ecost[(u,w)]
            if (cw < cost[w]):
                dq.put((cw, w))
                prev[w] = u
    return (cost, isdisc, prev)

finalcost = [None]*n
isdiscf = [None]*n
prevf = [None]*n
for i in range(n):
    ui = i*nstop
    finalcost[i], isdiscf[i], prevf[i] = dstra(ui)
minv = infty
for i in range(n):
    for j in range(n):
        minv = min(minv, finalcost[i][(nstop*j)+k])
if (minv == infty):
    print ("IMPOSSIBLE")
else:
    print(minv)
