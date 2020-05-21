import heapq

def dijkstra(src):
    distance = [-1] * n
    distance[src] = 0

    pq = [(0,src)]

    while len(pq) > 0:
        dist,u = heapq.heappop(pq)
        if dist > distance[u]:
            continue
        for temp in graph[u]:
            v = temp[0]
            w = temp[1]
            temp_dist = dist + w 
            if temp_dist < distance[v] or distance[v] == -1:
                distance[v] = temp_dist
                heapq.heappush(pq, (temp_dist,v))

    return distance


s = str(input()).split()
n = int(s[0])
m = int(s[1])

graph = [[] for i in range(n)]

edge_set = []

for i in range(m):
    s = str(input()).split()
    u = int(s[0]) - 1
    v = int(s[1]) - 1
    w = int(s[2])
    edge_set.append([u,v,w])
    edge_set.append([v,u,w])
    graph[u].append([v,w])
    graph[v].append([u,w])


dist1 = dijkstra(0)
distn = dijkstra(n-1)

second_shortest_distance = -1

for e in edge_set:
    u = e[0]
    v = e[1]
    w = e[2]
    temp_distance = dist1[u] + w + distn[v]
    if temp_distance > distn[0]:
        if second_shortest_distance == -1 or second_shortest_distance > temp_distance:
            second_shortest_distance = temp_distance

print(second_shortest_distance)

