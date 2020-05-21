from queue import PriorityQueue


def dijkstra(graph,wt,x):
    
    que=PriorityQueue()
    que.put((0,x))
    dis=[10**17]*len(graph)
    dis[x]=0
    while que.empty()==False:
         d,u=que.get()
         if d<=dis[u]:
             for v in graph[u]:
                 if dis[u]+wt[(u,v)] >= dis[v]:
                     continue
                 nd = dis[u]+wt[(u,v)]
                 que.put((nd,v))
                 dis[v]= nd
    return dis


n,k=input().split()
n=int(n)
k=int(k)

end=n*100+1
start=100*n

t=list(map(int,input().split()))
graph=[]
wt = {}

for i in range(100*n+2):
    graph.append([])

for i in range(n):
    l=list(map(int,input().split()))
    prev=-1
    for x in l:
        for j in range(n):
            v=j*100+x
            u=i*100+x
            if u==v:
                continue
            wt[(u,v)]=60
            graph[u].append(v)
            
        if prev!=-1:
            graph[prev].append(u)
            graph[u].append(prev)
            wt[(u,prev)]=(u-prev)*t[i]
            wt[(prev,u)]=(u-prev)*t[i]
        prev=u


for i in range(n):
    graph[start].append(i*100)
    graph[i*100 + k].append(end)
    wt[(start,100*i)]=0
    wt[(i*100+k,end)]=0

dist=dijkstra(graph,wt,start)

if dist[end]>=10**17:
    print("IMPOSSIBLE")
else:
    print(dist[end])
        


