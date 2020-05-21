import heapq
a= list(map(int,input().split()))
b= list(map(int,input().split()))
Graph=dict()
weights=dict()
stops=dict()
distance=dict()
i=0
while(i<100):
    stops[i]=[]
    j=1
    while(j<=5):
        Graph[(i,j)]=[]
        distance[(i,j)]=987987987987987987
        j=j+1
    i=i+1
Graph[0,0]=[]
j=1
while (j<=a[0]):
    Graph[(0,0)].append((0,j))
    weights[((0,0),(0,j))]=0
    c= list(map(int,input().split()))
    head=heapq.heappop(c)
    stops[head].append(j)
    while c:
        head1= heapq.heappop(c)
        Graph[(head,j)].append((head1,j))
        Graph[(head1,j)].append((head,j))
        weights[((head,j),(head1,j))]=b[j-1]*(head1-head)
        weights[((head1,j),(head,j))]=b[j-1]*(head1-head)
        stops[head1].append(j)
        head=head1
    j=j+1
    
for i in range(0,100):
        if len(stops[i])>0:
            for j in stops[i]:
                for k in stops[i]:
                    if j!=k:
                        Graph[(i,j)].append((i,k))
                        Graph[(i,k)].append((i,j))
                        weights[((i,k),(i,j))]=60
                        weights[((i,j),(i,k))]=60
visited=set()
current=[(0,(0,0))]
while current:
    d=heapq.heappop(current)
    if d[1] in visited:
        continue
    else :
        distance[d[1]]=d[0]
    visited.add(d[1])
    for i in Graph[d[1]]:
        if i not in visited:
            heapq.heappush(current,(weights[(d[1],i)]+d[0],i))
k=a[0]
v=10000000000
while k>0:
    if distance[(a[1],k)]!= 987987987987987987:
        if distance[(a[1],k)]<v:
            v=distance[(a[1],k)]
    k=k-1
if (v==10000000000):
        print("IMPOSSIBLE")
else:
        print(v)    
            



    
    
