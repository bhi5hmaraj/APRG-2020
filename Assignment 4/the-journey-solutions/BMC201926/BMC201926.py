from queue import PriorityQueue

N, k = map(int, input().split())
time = list(map(int, input().split()))
bustops = []
for i in range(N):
    bustops.append(list(map(int, input().split())))

adj = []                                                                       # This is an array, adj[i] represents neighbours of i and its                                                                                       weight and in which bus-provider list the edge lies.
for i in range(100):
    adj.append([])
for i in range(N):
    for j in bustops[i]:
        for x in bustops[i]:
            if j != x:
                adj[j].append((time[i]*(abs((x-j))), x, i ))

distance = [float('inf') for x in range(100)]
distance[0] = 0

status = [None for x in range(100)]

queue = PriorityQueue()
queue.put((distance[0], 0, status[0]))

while not queue.empty():
    h1 = queue.get()
    p1 = h1[1]
    p2 = status[p1]
    for nbr in adj[p1]:
        a1 = distance[nbr[1]]
        if p2 is None:
            if distance[p1] + nbr[0] < a1:
                distance[nbr[1]] = min(a1, distance[p1] + nbr[0])
                status[nbr[1]] = nbr[2]
                queue.put((distance[nbr[1]], nbr[1]))
        elif p2 == nbr[2]:
            if distance[p1] + nbr[0] < a1:
                distance[nbr[1]] = min(a1, distance[p1] + nbr[0])
                status[nbr[1]] = nbr[2]
                queue.put((distance[nbr[1]], nbr[1]))
        elif p2 != nbr[2]:
            if distance[p1] + nbr[0] + 60 < a1:
                distance[nbr[1]] = min(a1, distance[p1] + nbr[0] + 60)
                status[nbr[1]] = nbr[2]
                queue.put((distance[nbr[1]], nbr[1]))

if distance[k] == float('inf'):
    print("IMPOSSIBLE")
else:
    print(distance[k])
    

