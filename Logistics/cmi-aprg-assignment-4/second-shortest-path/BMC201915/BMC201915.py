import math
n, m = map(int, input().split())
adj = [[[float("inf"),float("inf")] for i in range(n)] for j in range(n)]
for i in range(m):
    x, y, value = map(int, input().split())
    if value < max(adj[x-1][y-1]):
        adj[x-1][y-1].remove(max(adj[x-1][y-1]))
        adj[y-1][x-1].remove(max(adj[y-1][x-1]))
        
        adj[x-1][y-1].append(value)
        adj[y-1][x-1].append(value)
dist = [float("inf")]*n
dist1 = [float("inf")]*n
sptSet = [False]*n
def minDist():
    mins = float("inf")
    min_index = float("inf")
    for v in range(n):
        if dist[v] < mins and sptSet[v] == False:
            mins = dist[v]
            min_index = v
    return min_index
def minDist1():
    mins = float("inf")
    min_index = float("inf")
    for v in range(n):
        if dist1[v] < mins and sptSet[v] == False:
            mins = dist1[v]
            min_index = v
    return min_index
def dikstra():
    dist[0] = 0
    for j in range(n):
        u = minDist()  #minimum value in the priority queue
        sptSet[u] = True
        for v in range(n):
            for k in range(2):
                if sptSet[v] == False and dist[v] > dist[u] + adj[u][v][k]:
                    dist[v] = dist[u] + adj[u][v][k]
def dikstra1():
    dist1[-1] = 0
    for j in range(n):
        u = minDist1()  #minimum value in the priority queue
        sptSet[u] = True
        for v in range(n):
            for k in range(2):
                if sptSet[v] == False and dist1[v] > dist1[u] + adj[u][v][k]:
                    dist1[v] = dist1[u] + adj[u][v][k]
            
dikstra1()
sptSet = [False]*n
dikstra()
d2 = float("inf")
for j in range(n):
        for i in range(n):
            for k in range(2):
                if i != j and (not math.isinf(adj[i][j][k])) and dist[-1] < dist[i] + dist1[j] + adj[i][j][k] < d2:
                    d2 = dist[i] + dist1[j] + adj[i][j][k]
print(d2)
                
