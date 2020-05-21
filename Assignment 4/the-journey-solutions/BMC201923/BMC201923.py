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
    n,k=list(map(int,input().split()))
    t=list(map(int,input().split()))
    graph=[]
    for i in range(100*n+2):
        graph.append([])
    wt = {}
    
    for i in range(n):
        l=list(map(int,input().split()))
        prev=-1
        for x in l:
            u=i*100+x
            for j in range(n):
                v=j*100+x
                if u==v:
                    continue
                
                graph[u].append(v)
                wt[(u,v)]=60
            if prev!=-1:
                graph[prev].append(u)
                graph[u].append(prev)
                w=(u-prev)*t[i]
                wt[(u,prev)]=w
                wt[(prev,u)]=w
            prev=u
    
    start=100*n
    end=n*100+1
    
    for i in range(n):
        graph[start].append(i*100)
        wt[(start,100*i)]=0
        graph[i*100 + k].append(end)
        wt[(i*100+k,end)]=0
    
    dist=ssp(graph,wt,start)
    ans = dist[end]
    if ans>=INF:
        print("IMPOSSIBLE")
    else:
        print(ans)
    return

run()
        
