import heapq

def tree(graph,dist,x,length):
    m=set()
    m1=[(0,x)]
    while m1:
        c=heapq.heappop(m1)
        if c[1] in m:
            continue
        else:
            length[c[1]]=c[0]
        m.add(c[1])
        for i in graph[c[1]]:
            if i not in m:
                heapq.heappush(m1,(dist[(c[1],i)]+c[0],i))
    return(length)

h=[]
n=set()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
length=dict()
graph=dict()
dist1=dict()
dist=dict()
i=100
while i>=0:
    d=100
    dist1[i]=set()
    while d>0:
        length[(i,d)]=999999999
        graph[(i,d)]=set()
        d=d-1
    i=i-1
    
j=1
graph[(0,0)]=set()
while j<=a[0]:
    graph[(0,0)].add((0,j))
    dist[((0,0),(0,j))]=0
    c=list(map(int,input().split()))
    k=heapq.heappop(c)
    dist1[k].add(j)
    while c:
        k1=heapq.heappop(c)
        graph[(k,j)].add((k1,j))
        graph[(k1,j)].add((k,j))
        dist[((k,j),(k1,j))]=b[j-1]*(k1-k)
        dist[((k1,j),(k,j))]=b[j-1]*(k1-k)
        dist1[k1].add(j)
        k=k1
    j=j+1
for i in dist1:
    
    if len(dist1[i])>0:
        for j in dist1[i]:
            if j!=k:
                graph[(i,j)].add((i,k))
                graph[(i,k)].add((i,j))
                dist[((i,k),(i,j))]=60
                dist[((i,j),(i,k))]=60
l=tree(graph,dist,(0,0),length)
k=a[0]
v=10000000000
while k>0:
    if l[(a[1],k)]!=999999999:
        if l[(a[1],k)]<v:
            v=l[(a[1],k)]
        k=k-1
if v==10000000000:
    print("IMPOSSIBLE")
else:
    print(v)
