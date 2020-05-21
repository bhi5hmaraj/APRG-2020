inf=10
for i in range(12):
    inf*=10
from queue import PriorityQueue
wgt={}
adj={}

n,m=map(int,(input().split()))
for i in range(n):
    adj[i+1]=[]

for i in range(m):
    a,b,c=map(int,(input().split()))
    if (min([a,b]),max([a,b])) not in wgt:
        wgt[(min([a,b]),max([a,b]))]=[c]
    else:
        wgt[(min([a,b]),max([a,b]))].append(c)
    adj[a].append(b)
    adj[b].append(a)


def dijk(x):
    path={}
    q=PriorityQueue()
    for i in range(n):
        if i+1==x:
            q.put((0,i+1))
            path[i+1]=0
        else:
            #q.put((inf,i+1))
            path[i+1]=inf
    parent={x:None}
    while not q.empty():
        d,u=q.get()
        for v in adj[u]:
            a=min(wgt[(min([u,v]),max([u,v]))])+d
            if a<path[v]:
                path[v]=a
                q.put((path[v],v))
    return(path)
da=dijk(1)

db=dijk(n)
d=[]
for u in range(1,n+1):
    for v in adj[u]:
        for i in wgt[(min([u,v]),max([u,v]))]:
            a=da[u]+db[v]+i
            d.append(a)
#print(d,da,db)
def f(l):
    b=[]
    a=min(l)
    for i in l:
        if i>a:
            b.append(i)
    return(min(b))
print(f(d))
