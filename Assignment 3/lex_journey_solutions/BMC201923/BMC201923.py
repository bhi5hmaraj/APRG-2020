from queue import Queue

def bfs(u,gr):
    n = len(gr)
    q=Queue()
    q.put(u)
    dist=[-1]*n
    dist[u]=0
    while not q.empty():
        v=q.get()
        
        for w in gr[v]:
            if dist[w]==-1:
                dist[w]=dist[v]+1
                q.put(w)
    return dist

def transform(x,y,graph):
    n=len(graph)
    worthy=[0]*n
    dist = list(map(lambda x,y: x + y,bfs(x,graph),bfs(y,graph)))
    slen = dist[x]
    for v in range(0,n):
        if dist[v]==slen:
            worthy[v]=1

    for i in range(0,n):
        if worthy[i]!=1:
            graph[i]=[]
        
        lp=[]
        for v in graph[i]:
            if worthy[v]==1:
                lp.append(v)
        graph[i]=lp
    return

def solve(x,y,graph,rank):
    transform(x,y,graph)
    dist=bfs(x,graph)
    s=[x]
    n=max(dist)
    ans=""
    for i in range(0,n):
        arr=s
        m='z'
        curlev=dist[arr[0]]
        for u in arr:
            for v in graph[u]:
                if dist[v]==curlev+1:
                    m=min(m,rank[(u,v)])
        out=set()
        for u in arr:
            for v in graph[u]:
                if rank[(u,v)] == m and dist[v] == curlev+1:
                    out.add(v)
        out=list(out)
        s=out
        ans+=m
    
    return ans

def run():
    n,m = list(map(int,input().split()))
    x,y = list(map(int,input().split()))

    x-=1
    y-=1
    graph=[]
    rank={}
    for i in range(0,n):
        graph.append([])

    for z in range(0,m):
        i,r,j=input().split()
        i=int(i)-1
        j=int(j)-1
    
        graph[i].append(j)
        graph[j].append(i)
        rank[(i,j)]=r
        rank[(j,i)]=r

    print(solve(x,y,graph,rank))
    return 0

run()


