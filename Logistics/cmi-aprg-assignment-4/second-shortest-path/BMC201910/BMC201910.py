import heapq

def dijkstra(x):
    inf = 9999999999
    cost = [inf]*n
    cost[x]=0

    visited=[(0,x)]
    while visited:
        (dis,u)=heapq.heappop(visited)
        if cost[u] < dis:
            continue
        for edge in Graph[u]:
            v = edge[0]
            w = edge[1]
            edgeDis= dis +w
            if (edgeDis < cost[v]) or (cost[v] == inf):
                cost[v]=edgeDis
                heapq.heappush(visited,(edgeDis,v))
    return(cost)

lss=list(map(int,input().split()))
n=lss[0]
m=lss[1]

Graph= [[] for ks in range(n)]
for jj in range(m):
    ls=list(map(int,input().split()))
    a=ls[0]-1
    b=ls[1]-1
    w=ls[2]
    Graph[a].append([b,w])
    Graph[b].append([a,w])
    
lp1=[]
l1=dijkstra(0)
l2=dijkstra(n-1)
for jk in range(n):
    for es in Graph[jk]:
        lp1.append(l1[jk]+es[1]+l2[es[0]])
        
dijk = l1[n-1]
l = [h for h in lp1 if h!=dijk]
ans=min(l)

print(ans)
#print(dijkstra(n-1))
        
    
    

    
#print(Graph)
#[[[1, 100]], [[0, 100], [3, 200], [2, 250]], [[1, 250], [3, 100]], [[1, 200], [2, 100]]]
#print(dijkstra(0,3))



