from queue import PriorityQueue

N, M = map(int, input().split())
edges = []
for i in range(M):
    edges.append(list(map(int, input().split())))
    
adj = []
for i in range(0, N):
    adj.append([])
for i in edges:
    adj[i[0] - 1].append((i[2], i[1]))
    adj[i[1] - 1].append((i[2], i[0]))
    
distance1 = [float('inf') for x in range(N)]
distance1[0] = 0

queue = PriorityQueue()
queue.put((distance1[0], 1))
while not queue.empty():
    h1 = queue.get()
    p1 = h1[1]
    for nbr in adj[p1 - 1]:
        a1 = distance1[nbr[1] - 1]
        if nbr[0] + distance1[p1-1] < a1:
            distance1[nbr[1]-1] = min(a1, nbr[0] + distance1[p1-1])
            queue.put((distance1[nbr[1]-1], nbr[1]))

a = distance1[N-1] 

distance2 = [float('inf') for x in range(N)]
distance2[N-1] = 0

queue2 = PriorityQueue()
queue2.put((distance2[N-1], N))
while not queue2.empty():
    h1 = queue2.get()
    p1 = h1[1]
    for nbr in adj[p1 - 1]:
        a2 = distance2[nbr[1] - 1]
        if nbr[0] + distance2[p1-1] < a2:
            distance2[nbr[1]-1] = min(a2, nbr[0] + distance2[p1-1])
            queue2.put((distance2[nbr[1]-1], nbr[1]))

distance3 = float('inf')

adj2 = []
for i in edges:
    if 1==1:
        adj2.append((distance1[i[0] - 1],i[2], distance2[i[1] - 1]))
        adj2.append((distance1[i[1] - 1],i[2], distance2[i[0] - 1]))
        
for e in adj2:
    if a < e[0] + e[1] + e[2] < distance3:
        distance3 = e[0] + e[1] + e[2]
    
print(distance3)

    
