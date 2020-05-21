inf = 10
for i in range(99):
    inf *= 10
from queue import PriorityQueue
q=PriorityQueue()
cost = {}
adj = {}
allcost = {}
n,m = map(int,(input().split()))
for i in range(n):
    adj[i+1] = []
for i in range(m):
    a,b,c = map(int,(input().split()))
    k = min([a,b])
    l = max([a,b])
    if (k, l) in cost:
        cost[(k, l)] = min([c,cost[(k, l)]])
    else:
        cost[(k, l)] = c
    if (k,l) in allcost:
        allcost[(k,l)].append(c)
    else:
        allcost[(k,l)] = [c]
    adj[a].append(b)
    adj[b].append(a)
def mincost(adj,src):
    minroute = {}
    for i in range(n):
        if i+1 == src:
            q.put((0, i+1))
            minroute[i+1] = [0,0]
        else:
            minroute[i+1] = [0,inf]
    while not q.empty():
        w,u=q.get()
        for v in adj[u]:
            a = cost[(min([u,v]),max([u,v]))] + w
            if a < minroute[v][1]:
                minroute[v][1] = a
                minroute[v][0] = minroute[u][0] + 1

                q.put((minroute[v][1],v))
            elif a == minroute[v][1] and minroute[v][0] > minroute[u][0] + 1:
                minroute[v][0] = minroute[u][0] + 1
    return(minroute)
l1=mincost(adj,1)
l2=mincost(adj,n)
costs = []
for u in range(n):
    for v in adj[u+1]:
        for w in allcost[(min([u+1,v]),max([u+1,v]))]:
            costs.append(l1[u+1][1] + l2[v][1] + w)
print(sorted(set(costs))[1])       
