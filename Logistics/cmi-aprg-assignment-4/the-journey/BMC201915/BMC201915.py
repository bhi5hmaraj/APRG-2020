from queue import PriorityQueue

n, k = map(int, input().split())
time = list(map(int, input().split()))
stops = []
for i in range(n):
    stops.append(list(map(int, input().split())))
adj = []
for i in range(100):
    adj.append([])
for i in range(n):
    for j in stops[i]:
        for r in stops[i]:
            if r != j:
                adj[j].append((time[i]*abs(j-r), r, i))
dist = [float("Inf")for i in range(100)]
dist[0] = 0
stat = [None] * 100
queue = PriorityQueue()
queue.put((dist[0], 0, stat[0]))
while not queue.empty() :
    u = queue.get()
    pt = u[1]
    st = stat[pt]
    for nbr in adj[pt]:
        a = dist[nbr[1]]
        if pt is None:
            if dist[pt] + nbr[0] < a:
                dist[nbr[1]] = dist[pt] + nbr[0]
                stat[nbr[1]] = nbr[2]
                queue.put((dist[nbr[1]], nbr[1]))
        elif st == nbr[2]:
            if dist[pt] + nbr[0] < a:
                dist[nbr[1]] = min(a,dist[pt] + nbr[0])
                stat[nbr[1]] = nbr[2]
                queue.put((dist[nbr[1]], nbr[1]))
        elif st != nbr[2]:
            if dist[pt] + nbr[0] + 60 < a:
                dist[nbr[1]] = min(a,dist[pt] + nbr[0] + 60)
                stat[nbr[1]] = nbr[2]
                queue.put((dist[nbr[1]], nbr[1]))
if dist[k] == float("Inf"):
    print("IMPOSSIBLE")
else:
    print(dist[k]-60)
    
