from queue import PriorityQueue

INF=10**17
def ssp(graph,wt,x):
    n=len(graph)
    dist=[INF]*n
    q=PriorityQueue()
    dist[x]=0
    q.put((0,x))
    
    while not q.empty():
         d,u=q.get()
         if d>dist[u]:
             continue
        
         for v in graph[u]:
             nd = dist[u]+wt[(u,v)]
             if nd < dist[v]:
                 dist[v]= nd
                 q.put((dist[v],v))
    
    return dist

def run():
    n,m=list(map(int,input().split()))

    graph=[]
    for i in range(n):
        graph.append([])
    
    wt = {}
    inplst=[]
    for i in range(m):
        u,v,w=list(map(int,input().split()))
        u-=1
        v-=1
        inplst.append((u,v,w))
        inplst.append((v,u,w))

        if ((u,v) in wt) or ((v,u) in wt):
            wt[(u,v)]=min(wt[(u,v)],w)
            wt[(v,u)]=min(wt[(v,u)],w)
        else:
            graph[u].append(v)
            graph[v].append(u)
            wt[(u,v)]=w
            wt[(v,u)]=w

    dist1=ssp(graph,wt,0)
    s=dist1[n-1]
    dist2=ssp(graph,wt,n-1)
    l=[]

    for (u,v,w) in inplst:
        l.append(dist1[u]+dist2[v]+w)
    l.sort()

    ans=0
    for x in l:
        if x!=s:
            ans=x
            break
    
    print(ans)
    return

run()

