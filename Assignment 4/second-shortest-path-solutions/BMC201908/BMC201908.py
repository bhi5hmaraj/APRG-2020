import heapq

def dijkstra(src):
    Dist = [-1] * N
    Dist[src] = 0
    pair = [(0,src)]
    while pair:
        current_dist,current_vertex = heapq.heappop(pair)
        if current_dist > Dist[current_vertex]:
            continue
        for neighbour in Adj[current_vertex]:
            v = neighbour[0]
            w = neighbour[1]
            foundpathlength = current_dist + w 
            if foundpathlength < Dist[v] or Dist[v] == -1:
                Dist[v] = foundpathlength
                heapq.heappush(pair, (foundpathlength,v))
    return Dist

s = str(input()).split()
(N,M) = (int(s[0]),int(s[1]))
Adj = [[] for i in range(N)]
Edges = []
for i in range(M):
    s = str(input()).split()
    (u,v,w) = (int(s[0]) - 1,int(s[1]) - 1,int(s[2]))
    Edges.append([u,v,w])
    Edges.append([v,u,w])
    Adj[u].append([v,w])
    Adj[v].append([u,w])

(a,b) = (dijkstra(0),dijkstra(N-1))
second_shortestdist = -1
for e in Edges:
    (u,v,w) = (e[0],e[1],e[2])
    cost = a[u] + w + b[v]
    if cost > b[0]:
        if second_shortestdist == -1 or second_shortestdist > cost:
            second_shortestdist = cost
print(second_shortestdist)
