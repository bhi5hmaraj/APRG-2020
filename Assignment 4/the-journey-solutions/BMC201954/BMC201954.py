from queue import PriorityQueue
inf=10**14
def md(x):
    if x>0:
        return x
    else:
        return -x
N,k1=map(int,input().split())
t=list(map(int,input().split()))
adj={}
for i in range(100):
    for j in range(N):
        adj[(j+1,i)]=[]
for i in range(1,N+1):
  d=list(map(int,input().split()))
  for k in range(len(d)):
    if k >0:
      adj[(i,d[k])].append((i,d[k-1]))
    if k<len(d)-1:
      adj[(i,d[k])].append((i,d[k+1]))
def dijk(x):
    path={}
    q=PriorityQueue()
    for i in range(100):
        for j in range(N):
            if i==x:
                q.put((0,j+1,i))
                path[(j+1,i)]=0
            else:
                #q.put((inf,i+1))
                path[(j+1,i)]=inf
    parent={x:None}
    while not q.empty():
        d,p,u=q.get()
        for v in adj[(p,u)]:
            a=md(u-v[1])*t[p-1]+d
            if a<path[v]:
                path[v]=a
                q.put((path[v],v[0],v[1]))
        for l in range(N):
            if p==l+1:
                a=d
            else:
                a=d+60
            if a<path[(l+1,u)]:
                path[(l+1,u)]=a
                q.put((path[(l+1,u)],l+1,u))
    return(path)
d=dijk(0)
a=[]
for i in range(N):
    a.append(d[(i+1,k1)])
r=min(a)
if r==inf:
    print('IMPOSSIBLE')
else:
    print(r)
