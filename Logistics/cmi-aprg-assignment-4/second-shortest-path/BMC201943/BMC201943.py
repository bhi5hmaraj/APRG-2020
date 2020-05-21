from queue import PriorityQueue
list_firstLine =  list(map(int,input().split()))
N = list_firstLine[0]
E = list_firstLine[1]

Adj =[ [] for i in range(N+1)]

for i in range(E):
    l = list(map(int,input().split()))
    Adj[l[0]].append((l[2],l[1]))
    Adj[l[1]].append((l[2],l[0]))
dis1 = [10**15 for i in range (N+1)]
disN = [10**15 for i in range (N+1)]

dis1[1] = 0
Q = PriorityQueue()
Q.put((0,1))
while (Q.empty() == False):
    (d,a) = Q.get()
    for (u,b) in Adj[a]:
        if (dis1[b] > dis1[a] + u):
            dis1[b] = dis1[a] +u
            Q.put((dis1[b],b))
            
disN[N] = 0
Q = PriorityQueue()
Q.put((0,N))
while (Q.empty() == False):
    (d,a) = Q.get()
    for (u,b) in Adj[a]:
        if (disN[b] > disN[a] + u):
            disN[b] = disN[a] +u
            Q.put((disN[b],b))            

shortestV = []
for i in range(N+1):
    if (dis1[i] + disN[i] == dis1[N]):
        shortestV.append(i)
    
ans = 10**15    
for i in shortestV:
    for (w,j) in Adj[i]:
        if (dis1[i] +w+ disN[j] != dis1[N]):
            ans = min(ans,w + dis1[i] + disN[j])
print (ans)
