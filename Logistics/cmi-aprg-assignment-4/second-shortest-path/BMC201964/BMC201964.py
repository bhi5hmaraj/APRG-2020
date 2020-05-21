from queue import PriorityQueue, Queue

n,m = map(int, input().split())

adj = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]
for i in range(m):
    x,y,w = map(int, input().split())
    adj[x].append([y,w])
    adj[y].append([x,w])

dist1 = []

pq1 = PriorityQueue()
pq1.put([0,1])

for i in range(n+1):
    dist1.append(1000000000)
dist1[1] = 0

while(not pq1.empty()):
    s = pq1.get()
    for v in adj[s[1]]:
        if(dist1[v[0]] > dist1[s[1]] + v[1]):
            dist1[v[0]] = dist1[s[1]] + v[1]
            parent[v[0]] = s[1]
            pq1.put([dist1[v[0]], v[0] ])

dist2 = []

pqn = PriorityQueue()
pqn.put([0,n])

for i in range(n+1):
    dist2.append(1000000000)
dist2[n] = 0

while(not pqn.empty()):
    s = pqn.get()
    for v in adj[s[1]]:
        if(dist2[v[0]] > dist2[s[1]] + v[1]):
            dist2[v[0]] = dist2[s[1]] + v[1]
            pqn.put([dist2[v[0]], v[0] ])

ans = 100000000

for i in range(1,n+1):
    for v in adj[i]:
        if( dist1[i] + dist2[v[0]] + v[1] != dist1[n]):
            ans = min(dist1[i] + dist2[v[0]] + v[1] , ans)

print(ans)










   


