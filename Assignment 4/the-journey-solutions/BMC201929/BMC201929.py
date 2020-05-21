import heapq
[n, k] = input().split()
n = int(n)
k = int(k)
times = input().split()

for i in range(n):
    times[i] = int(times[i])

graph = []   
for i in range(100 * n):
    graph.append([])
    
for i in range(n):
    for j in range(n):
        if i != j:
            for x in range(100):
                graph[(100*i) + x].append(((100*j) + x, 60))

for i in range(n):
    list = input().split()
    l = len(list)
    for j in range(l - 1):
        a = list[j]
        b = list[j + 1]
        a = int(a)
        b = int(b)
        graph[(100*i) + a].append(((100*i) + b , times[i] * (b - a)))
        graph[(100*i) + b].append(((100*i) + a , times[i] * (b - a)))
         

def dijkstra(k):
    dist = [10000000000000001] * 100 * n
    dist[k] = 0
    h = []
    heapq.heappush(h, (0, k))
    while h != []:
        (x, y) = heapq.heappop(h)
        for v in graph[y]:
            if dist[y] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[y] + v[1]
                heapq.heappush(h, (dist[v[0]], v[0]))      
    return dist    
            
            
paths = []

for i in range(n):
    for j in range(n):
        l = dijkstra(100*i)
        paths.append(l[(100*j) + k])
        

m = min(paths)
if m == 10000000000000001 :
    print("IMPOSSIBLE")
else:
    print(m)
