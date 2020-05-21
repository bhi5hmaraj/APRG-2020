from queue import PriorityQueue

n, m = [int(i) for i in input().split()]
adj = [[] for j in range(0, n)]

for i in range(0, m):
    u,v,w = [int(i) for i in input().split()]
    u = u - 1
    v = v - 1
    adj[u].append((w, v))
    adj[v].append((w, u))

booll = [0 for i in range(0, n)]

def getnbs(v):
    l = []
    for (cs, vs) in adj[v]:
        l.append((cs, vs))
        
    return l
            

l = PriorityQueue()
djmap = []
l.put((0, 0))
c = 0
while len(djmap) < 2:
    (cc, cv) = l.get()
    booll[cv] += 1
    if cv == n-1:
        djmap.append(cc)
        djmap = list(dict.fromkeys(djmap))
    
    for (a, b) in getnbs(cv):
        if booll[b] < 2:
            l.put((cc + a, b))



print(djmap[1])



    


        


