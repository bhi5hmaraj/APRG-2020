from queue import PriorityQueue, Queue

n,k = map(int, input().split())

adj = [[] for i in range(500)]

Ti = [int(x) for x in input().split()]

for i in range(n):
    lis = [int(x) for x in input().split()]
    for j in range(len(lis)):
        if(j != len(lis)-1):
            adj[lis[j] + 100*i].append([lis[j+1] + 100*i, Ti[i]* (lis[j+1] - lis[j])])
            adj[lis[j+1] + 100*i].append([lis[j] + 100*i, Ti[i]* (lis[j+1] - lis[j])])
        for kk in range(i):
            if(len(adj[lis[j] + 100*kk]) != 0):
                adj[lis[j] + 100*kk].append([lis[j] + 100*i,60])
                adj[lis[j] + 100*i].append([lis[j] + 100*kk,60])

def dijkstra(ss):
    dist1 = []

    pq1 = PriorityQueue()
    pq1.put([0,ss])

    for i in range(500):
        dist1.append(100000000)
    dist1[ss] = 0
    while(not pq1.empty()):
        s = pq1.get()
        for v in adj[s[1]]:
            #print(s[1],v[0])
            if(dist1[v[0]] > dist1[s[1]] + v[1]):
                    dist1[v[0]] = dist1[s[1]] + v[1]
                    pq1.put([dist1[v[0]], v[0]])

    mm = 100000000
    for i in range(n):
        mm = min(mm, dist1[k + i*100])

    return mm


mmm = 100000000

for i in range(n):
    mmm = min(mmm, dijkstra(i*100))

if mmm == 100000000:
    print("IMPOSSIBLE")
else:
    print(mmm)








   


