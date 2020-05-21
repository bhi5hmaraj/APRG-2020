from queue import PriorityQueue
infty = 1e16
v,e = [int(i) for i in input().split()]
adjl = [[] for i in range(v+1)]
for i in range(e):
    u,w,c = [int(i) for i in input().split()]
    adjl[u].append((w,c))
    adjl[w].append((u,c))
def dstra(x): 
    cost = [infty]*(v+1)
    isdisc = [False]*(v+1)
    dq = PriorityQueue()
    dq.put((0,x))
    while (dq.empty() == False):
        (c,u) = dq.get()
        if (isdisc[u]):
            continue
        isdisc[u] = True
        cost[u] = c
        ec = c
        for (w,ecw) in adjl[u]:
            cw = ec + ecw
            if (cw < cost[w]):
                dq.put((cw, w))
    return (cost, isdisc)

(sekiro, wolf) = dstra(1)
(kuro, divine) = dstra(v)
setf = set()
def sconn(w):
    return wolf[w] and divine[w]
def mortalblade():
    for w in range(1,v+1):
        if sconn(w):
            tetf = set()
            tetf.add(sekiro[w] + kuro[w])
            for (u, cu) in adjl[w]:
                tetf.add(sekiro[w]+cu+kuro[u])
            for i in tetf:
                setf.add(i)
mortalblade()
pq = PriorityQueue()
for i in setf:
    pq.put(i)
a = pq.get()
b = pq.get()
print(b)


