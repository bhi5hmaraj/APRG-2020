from queue import PriorityQueue

n, k = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]
stopmap = [[0 for j in range(0, 100)] for i in range(0, n)]
adj = {}
kthere = 0 
zerothere = -1

for i in range(0, n):
    l = [int(i) for i in input().split()]
    for j in l:
        adj[100*i + j] = []
        stopmap[i][j] = 1 
        if j == k:
            kthere = 1
            newk = 100*i + k
        if j == 0:
            zerothere = i
    for j in range(0, len(l)):
        if j-1 >= 0:
            adj[100*i + l[j]].append((T[i]*(l[j]-l[j-1]), 100*i + l[j - 1]))
        if j+1 < len(l):
            adj[100*i + l[j]].append((T[i]*(l[j+1]-l[j]), 100*i + l[j + 1]))
    
for i in range(0, n):
    for j in range(0, 100):
        if stopmap[i][j] == 1:
            if j != 0 and j != k:
                for t in range(0, n):
                    if stopmap[t][j] == 1 and t != i:
                        adj[100*i + j].append((60, 100*t + j))
            else:
                for t in range(0, n):
                    if stopmap[t][j] == 1 and t != i:
                        adj[100*i + j].append((0, 100*t + j))

booll = dict.fromkeys(adj.keys())
for j in booll.keys():
    booll[j] = 0



def getnbs(v):
    l = []
    for (cs, vs) in adj[v]:
        l.append((cs, vs))
        
    return l
            

def dijk(v):
    l = PriorityQueue()
    djmap = dict.fromkeys(adj.keys())
    l.put((0, v))
    while not(l.empty()):
        (cc, cv) = l.get()
        if booll[cv] == 0:
            booll[cv] = 1
            djmap[cv] = cc
            for (a, b) in getnbs(cv):
                if booll[b] == 0:
                    l.put((cc + a, b))
    
    return djmap



if kthere == 1 and zerothere != -1:
    d = dijk(100*zerothere)
    print(d[newk])
else:
    print("IMPOSSIBLE")



    


        


