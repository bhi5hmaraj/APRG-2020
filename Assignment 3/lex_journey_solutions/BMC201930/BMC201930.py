from queue import Queue
[N,M] = list(map(int,input().split()))
[X,Y] = list(map(int,input().split()))
G = [[] for i in range(N+1)]
for i in range(M):
    [u,c,v] = input().split()
    (u,v) = (int(u),int(v))
    G[u].append((c,v))
    G[v].append((c,u))
d = [10**7 for i in range(N+1)]
rat = [chr(ord('z')+1) for i in range(N+1)]
d[X] = 0
q = Queue()
q.put(X)
rat[X] = ''
while not q.empty():
    node = q.get()
    for (ch,nbh) in G[node]:
        if d[nbh] > d[node]+1:
            rat[nbh] = rat[node] + ch
            q.put(nbh)
            d[nbh] = d[node] + 1
        else:
            if (d[nbh] == d[node]+1) and (rat[nbh]>rat[node] + ch):
                rat[nbh] = rat[node] + ch
    if node != Y: rat[node] = ''
print(rat[Y])