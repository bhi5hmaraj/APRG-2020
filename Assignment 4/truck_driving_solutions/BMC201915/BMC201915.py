import sys
n, m = map(int, input().split())
adj = [[float("inf") for i in range(n)]for j in range(n)]
for i in range(m):
    x, y, value = map(int, input().split())
    adj[x-1][y-1] = value
    adj[y-1][x-1] = value
def minDistance(dist, sptSet): 

        min = float("inf")

        for v in range(n): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
def dijkstra(src, desn): 
  
    dist = [float("inf")] * n 
    dist[src-1] = 0
    sptSet = [False] * n
  
    for cout in range(n): 

        u = minDistance(dist, sptSet) 
  
        sptSet[u] = True
  
     
        for v in range(n): 
            if adj[u][v] > 0 and sptSet[v] == False and dist[v] > max(dist[u], adj[u][v]):
                dist[v] = max(dist[u],adj[u][v])
    print(dist[desn-1])
q = int(input())
for i in range(q):
    s, d = map(int, input().split())
    dijkstra(s, d)
    